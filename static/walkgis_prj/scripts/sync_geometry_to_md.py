import sqlite3
import os
import re
from shapely.wkt import loads

# 設定路徑
BASE_PATH = "/Users/wuulong/github/bmad-pa"
PROJECT_ROOT = f"{BASE_PATH}/events/notes/wuulong-notes-blog/static/walkgis_prj"
DB_PATH = f"{PROJECT_ROOT}/walkgis.db"
FEATURES_DIR = f"{PROJECT_ROOT}/features"

def sync_geometry():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # 取得全台行政區的 POI 幾何資訊
    cursor.execute("SELECT feature_id, geometry_wkt FROM walking_map_features WHERE feature_id LIKE 'COUNTY_%' OR feature_id LIKE 'TOWN_%'")
    rows = cursor.fetchall()
    
    for fid, wkt in rows:
        filepath = os.path.join(FEATURES_DIR, f"{fid}.md")
        if not os.path.exists(filepath):
            print(f"File not found: {filepath}")
            continue
            
        # 計算中心點 (Centroid) 用於地圖定位
        try:
            geom = loads(wkt)
            centroid = geom.centroid
            coord_str = f"[{centroid.y}, {centroid.x}]" # [Lat, Lon]
        except Exception as e:
            print(f"Error processing WKT for {fid}: {e}")
            continue
            
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
            
        # 更新 Frontmatter
        new_lines = []
        in_frontmatter = False
        frontmatter_end = 0
        has_coord = False
        has_wkt = False
        
        for i, line in enumerate(lines):
            if line.strip() == "---":
                if not in_frontmatter:
                    in_frontmatter = True
                else:
                    # 結束前插入缺少的欄位
                    if not has_coord:
                        new_lines.append(f"coordinate: {coord_str}\n")
                    if not has_wkt:
                        new_lines.append(f"geometry_wkt: {wkt}\n")
                    in_frontmatter = False
            
            if in_frontmatter:
                if line.startswith("coordinate:"):
                    line = f"coordinate: {coord_str}\n"
                    has_coord = True
                if line.startswith("geometry_wkt:"):
                    line = f"geometry_wkt: {wkt}\n"
                    has_wkt = True
            
            new_lines.append(line)

        with open(filepath, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
        print(f"Updated geometry for {fid}")

    conn.close()

if __name__ == "__main__":
    sync_geometry()
