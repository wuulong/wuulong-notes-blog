import sqlite3
import os
import datetime
import fiona
from shapely.geometry import shape, mapping
from shapely import simplify
import json

# 設定專案路徑
BASE_PATH = "."
PROJECT_ROOT = f"{BASE_PATH}/events/notes/wuulong-notes-blog/static/walkgis_prj"
DB_PATH = f"{PROJECT_ROOT}/walkgis.db"
FEATURES_DIR = f"{PROJECT_ROOT}/features"
SHP_PATH = f"{BASE_PATH}/events/notes/data/流域情報開放地圖/00_基本圖資/TOWN_MOI/TOWN_MOI_1080617.shp"

# 確保目錄存在
os.makedirs(FEATURES_DIR, exist_ok=True)

# 今天的日期前綴
TODAY = "20260204"

def init_map(conn):
    cursor = conn.cursor()
    map_id = f"{TODAY}_taiwan_towns"
    name = "全台鄉鎮市區地圖"
    meta_data = json.dumps({
        "description": "包含台灣所有鄉鎮市區範圍及新竹市熱門景點的地圖。",
        "routes": {
            "main": "graph TD; \n    A[全台鄉鎮] --> B[新竹市景點];"
        }
    }, ensure_ascii=False)
    
    cursor.execute("INSERT OR REPLACE INTO walking_maps (map_id, name, meta_data) VALUES (?, ?, ?)", 
                   (map_id, name, meta_data))
    conn.commit()
    return map_id

def insert_feature(conn, feature_id, name, description, geometry_type, geometry_wkt, layer_id=1, subtype=""):
    cursor = conn.cursor()
    meta_data = json.dumps({
        "ref_doc": f"features/{feature_id}.md",
        "subtype": subtype,
        "date": str(datetime.date.today())
    }, ensure_ascii=False)
    
    cursor.execute("""
        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data) 
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data))
    
def link_to_map(conn, map_id, feature_id, order):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR REPLACE INTO walking_map_relations (map_id, feature_id, display_order)
        VALUES (?, ?, ?)
    """, (map_id, feature_id, order))

def create_md(feature_id, name, type_str, subtype, description, coords_str, extra=""):
    content = f"""---
id: {feature_id}
name: {name}
type: {type_str}
subtype: {subtype}
date: {datetime.date.today()}
---

# {name}

{description}

{extra}
"""
    with open(f"{FEATURES_DIR}/{feature_id}.md", "w", encoding="utf-8") as f:
        f.write(content)

def process_towns(conn, map_id):
    print("Processing towns from SHP...")
    order = 1
    with fiona.open(SHP_PATH) as src:
        total = len(src)
        for i, feat in enumerate(src):
            props = feat['properties']
            county = props['COUNTYNAME']
            town = props['TOWNNAME']
            town_code = props['TOWNCODE']
            feature_id = f"{TODAY}_town_{town_code}"
            
            # 幾何處理
            geom = shape(feat['geometry'])
            # 簡化幾何以節省尺寸 (度為單位，0.0001 約 11公尺)
            simplified_geom = simplify(geom, tolerance=0.0005)
            wkt = simplified_geom.wkt
            
            name = f"{county}{town}"
            desc = f"台灣{county}的{town}。"
            
            # 寫入 DB
            insert_feature(conn, feature_id, name, desc, simplified_geom.geom_type, wkt, subtype="行政區")
            link_to_map(conn, map_id, feature_id, order)
            
            # 寫入 MD
            create_md(feature_id, name, "行政區劃", "鄉鎮市區", desc, "")
            
            if i % 50 == 0:
                print(f"Progress: {i}/{total}")
            order += 1
    conn.commit()
    return order

hsinchu_pois = [
    {"name": "新竹市立動物園", "dist": "東區", "lat": 24.800194, "lon": 120.979500, "desc": "全台原址現存最老的動物園。"},
    {"name": "新竹公園", "dist": "東區", "lat": 24.800974, "lon": 120.977323, "desc": "新竹市中心最大公園，內有動物園、玻工館。"},
    {"name": "青草湖", "dist": "東區", "lat": 24.774733, "lon": 120.971147, "desc": "新竹著名景湖，適合散步遊憩。"},
    {"name": "十八尖山", "dist": "東區", "lat": 24.794861, "lon": 120.986722, "desc": "新竹市民的陽明山，健行聖地。"},
    {"name": "新竹城隍廟", "dist": "北區", "lat": 24.80449, "lon": 120.96588, "desc": "新竹信仰中心，周邊小吃林立。"},
    {"name": "南寮漁港", "dist": "北區", "lat": 24.84694, "lon": 120.92250, "desc": "十七公里海岸線起點，地中海風情。"},
    {"name": "魚鱗天梯", "dist": "北區", "lat": 24.852572, "lon": 120.924282, "desc": "網美打卡聖地，消波塊的新詮釋。"},
    {"name": "香山濕地賞蟹步道", "dist": "香山區", "lat": 24.789129, "lon": 120.920216, "desc": "近距離觀察濕地生態。"},
    {"name": "香山豎琴橋", "dist": "香山區", "lat": 24.807096, "lon": 120.929851, "desc": "絕美夕陽與攝影聖地。"},
    {"name": "青青草原", "dist": "香山區", "lat": 24.76352, "lon": 120.92359, "desc": "超長溜滑梯，親子踏青好去處。"}
]

def process_hsinchu_pois(conn, map_id, start_order):
    print("Adding Hsinchu POIs...")
    for i, poi in enumerate(hsinchu_pois):
        feature_id = f"{TODAY}_poi_hsinchu_{i:02d}"
        wkt = f"POINT({poi['lon']} {poi['lat']})"
        name = poi['name']
        desc = poi['desc']
        
        insert_feature(conn, feature_id, name, desc, "Point", wkt, layer_id=2, subtype="景點")
        link_to_map(conn, map_id, feature_id, start_order + i)
        create_md(feature_id, name, "熱門景點", poi['dist'], desc, wkt)
    conn.commit()

def main():
    conn = sqlite3.connect(DB_PATH)
    try:
        map_id = init_map(conn)
        last_order = process_towns(conn, map_id)
        process_hsinchu_pois(conn, map_id, last_order)
        print("Success!")
    finally:
        conn.close()

if __name__ == "__main__":
    main()
