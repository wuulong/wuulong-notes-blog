import sqlite3
import os
import datetime
import fiona
from shapely.geometry import shape
from shapely import simplify
import json

# 設定專案路徑
BASE_PATH = "/Users/wuulong/github/bmad-pa"
PROJECT_ROOT = f"{BASE_PATH}/events/notes/wuulong-notes-blog/static/walkgis_prj"
DB_PATH = f"{PROJECT_ROOT}/walkgis.db"
FEATURES_DIR = f"{PROJECT_ROOT}/features"
TOWN_SHP = f"{BASE_PATH}/events/notes/data/流域情報開放地圖/00_基本圖資/TOWN_MOI/TOWN_MOI_1080617.shp"
COUNTY_SHP = f"{BASE_PATH}/events/notes/data/流域情報開放地圖/00_基本圖資/7442-直轄市、縣市界線(TWD97經緯度)/COUNTY_MOI.shp"

# 確保目錄存在
os.makedirs(FEATURES_DIR, exist_ok=True)

# 日期
TODAY = "20260204"

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

def create_md(feature_id, name, type_str, subtype, description, towns_list=None):
    towns_content = ""
    if towns_list:
        towns_content = "\n## 所轄鄉鎮\n\n" + "\n".join([f"- [{t_name}](?map=20260204_taiwan_hierarchy&feature={t_id})" for t_name, t_id in towns_list])
    
    content = f"""---
id: {feature_id}
name: {name}
type: {type_str}
subtype: {subtype}
date: {datetime.date.today()}
---

# {name}

{description}
{towns_content}
"""
    with open(f"{FEATURES_DIR}/{feature_id}.md", "w", encoding="utf-8") as f:
        f.write(content)

def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    map_id = f"{TODAY}_taiwan_hierarchy"
    map_name = "台灣行政區劃層次地圖"
    map_meta = json.dumps({
        "description": "包含縣市與鄉鎮兩層次的行政區劃地圖。",
        "routes": {}
    }, ensure_ascii=False)
    cursor.execute("INSERT OR REPLACE INTO walking_maps (map_id, name, meta_data) VALUES (?, ?, ?)", 
                   (map_id, map_name, map_meta))

    county_to_towns = {}
    
    # 1. 處理鄉鎮
    print("Processing towns...")
    order = 1
    with fiona.open(TOWN_SHP, encoding='utf-8') as src:
        total = len(src)
        for i, feat in enumerate(src):
            p = feat['properties']
            c_name = p['COUNTYNAME']
            t_name = p['TOWNNAME']
            t_code = p['TOWNCODE']
            
            # 代號格式: TOWN_鄉鎮代號_縣市名稱鄉鎮名稱
            feature_id = f"TOWN_{t_code}_{c_name}{t_name}"
            
            if c_name not in county_to_towns:
                county_to_towns[c_name] = []
            county_to_towns[c_name].append((t_name, feature_id))
            
            # 幾何
            geom = simplify(shape(feat['geometry']), tolerance=0.0005)
            
            name = f"{c_name}{t_name}"
            desc = f"{c_name}的{t_name}。"
            
            insert_feature(conn, feature_id, name, desc, geom.geom_type, geom.wkt, subtype="鄉鎮市區")
            link_to_map(conn, map_id, feature_id, order)
            create_md(feature_id, name, "行政區劃", "鄉鎮市區", desc)
            
            if i % 50 == 0: print(f"Town Progress: {i}/{total}")
            order += 1
            
    # 2. 處理縣市
    print("Processing counties...")
    with fiona.open(COUNTY_SHP, encoding='utf-8') as src:
        total = len(src)
        for i, feat in enumerate(src):
            p = feat['properties']
            c_name = p['COUNTYNAME']
            c_code = p['COUNTYCODE']
            
            # 代號格式: COUNTY_縣市代號_縣市名稱
            feature_id = f"COUNTY_{c_code}_{c_name}"
            
            # 幾何
            geom = simplify(shape(feat['geometry']), tolerance=0.001) # 縣市範圍大，簡化程度可略高
            
            name = c_name
            desc = f"台灣的{c_name}。"
            towns = county_to_towns.get(c_name, [])
            
            insert_feature(conn, feature_id, name, desc, geom.geom_type, geom.wkt, subtype="縣市")
            link_to_map(conn, map_id, feature_id, order)
            create_md(feature_id, name, "行政區劃", "縣市", desc, towns_list=towns)
            
            if i % 5 == 0: print(f"County Progress: {i}/{total}")
            order += 1

    conn.commit()
    conn.close()
    print("All done!")

if __name__ == "__main__":
    main()
