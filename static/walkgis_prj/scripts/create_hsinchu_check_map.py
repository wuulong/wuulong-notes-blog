import sqlite3
import json

# 設定路徑
BASE_PATH = "/Users/wuulong/github/bmad-pa"
PROJECT_ROOT = f"{BASE_PATH}/events/notes/wuulong-notes-blog/static/walkgis_prj"
DB_PATH = f"{PROJECT_ROOT}/walkgis.db"

def create_hsinchu_map():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    map_id = "20260204_hsinchu_enrichment_check"
    map_name = "新竹市富化檢查地圖"
    
    # 建立地圖定義
    map_meta = json.dumps({
        "description": "專門用於檢查新竹市及其行政區富化進度的地標地圖。",
        "routes": {
            "hsinchu": "graph LR; COUNTY_10018_新竹市 --> TOWN_10018010_新竹市東區; COUNTY_10018_新竹市 --> TOWN_10018020_新竹市北區; COUNTY_10018_新竹市 --> TOWN_10018030_新竹市香山區;"
        }
    }, ensure_ascii=False)
    
    cursor.execute("INSERT OR REPLACE INTO walking_maps (map_id, name, meta_data) VALUES (?, ?, ?)", 
                   (map_id, map_name, map_meta))
    
    # 關聯新竹市及其行政區
    hsinchu_features = [
        "COUNTY_10018_新竹市",
        "TOWN_10018010_新竹市東區",
        "TOWN_10018020_新竹市北區",
        "TOWN_10018030_新竹市香山區"
    ]
    
    # 先清除舊關聯
    cursor.execute("DELETE FROM walking_map_relations WHERE map_id = ?", (map_id,))
    
    for i, fid in enumerate(hsinchu_features):
        cursor.execute("INSERT INTO walking_map_relations (map_id, feature_id, display_order) VALUES (?, ?, ?)",
                       (map_id, fid, i + 1))
        
    conn.commit()
    conn.close()
    print(f"Map {map_id} created and linked with Hsinchu features.")

if __name__ == "__main__":
    create_hsinchu_map()
