import sqlite3
import json

# 設定路徑
BASE_PATH = "/Users/wuulong/github/bmad-pa"
PROJECT_ROOT = f"{BASE_PATH}/events/notes/wuulong-notes-blog/static/walkgis_prj"
DB_PATH = f"{PROJECT_ROOT}/walkgis.db"

def create_taiwan_admin_map():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # 使用全台性的名稱與代號
    map_id = "taiwan_admin_enrichment"
    map_name = "台灣行政區富化管理地圖"
    
    # 建立地圖定義
    map_meta = json.dumps({
        "description": "全台灣行政區（縣市與鄉鎮）的富化進度與深度地誌管理地圖。",
        "routes": {
            "hsinchu": "graph TD; COUNTY_10018_新竹市 --> TOWN_10018010_新竹市東區; COUNTY_10018_新竹市 --> TOWN_10018020_新竹市北區; COUNTY_10018_新竹市 --> TOWN_10018030_新竹市香山區;"
        }
    }, ensure_ascii=False)
    
    cursor.execute("INSERT OR REPLACE INTO walking_maps (map_id, name, meta_data) VALUES (?, ?, ?)", 
                   (map_id, map_name, map_meta))
    
    # 目前僅加入新竹市的特徵進行檢查
    enriched_features = [
        "COUNTY_10018_新竹市",
        "TOWN_10018010_新竹市東區",
        "TOWN_10018020_新竹市北區",
        "TOWN_10018030_新竹市香山區"
    ]
    
    # 清除舊關聯
    cursor.execute("DELETE FROM walking_map_relations WHERE map_id = ?", (map_id,))
    
    for i, fid in enumerate(enriched_features):
        cursor.execute("INSERT INTO walking_map_relations (map_id, feature_id, display_order) VALUES (?, ?, ?)",
                       (map_id, fid, i + 1))
        
    conn.commit()
    conn.close()
    print(f"Map '{map_id}' ('{map_name}') table updated. Currently linked with Hsinchu features.")

if __name__ == "__main__":
    create_taiwan_admin_map()
