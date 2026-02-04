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

MAP_ID = "taiwan_admin_enrichment"

def get_enriched_list(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT feature_id FROM walking_map_features WHERE json_extract(meta_data, '$.enrichment_status') != 'DEFAULT'")
    return [row[0] for row in cursor.fetchall()]

def insert_feature(conn, feature_id, name, description, geometry_type, geometry_wkt, subtype, is_enriched):
    if is_enriched:
        print(f"Skipping DB update for enriched POI: {feature_id}")
        return

    cursor = conn.cursor()
    meta_data = json.dumps({
        "ref_doc": f"features/{feature_id}.md",
        "subtype": subtype,
        "date": str(datetime.date.today()),
        "enrichment_status": "DEFAULT"
    }, ensure_ascii=False)
    
    cursor.execute("""
        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data) 
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (feature_id, name, description, 1, geometry_type, geometry_wkt, meta_data))
    
def link_to_map(conn, map_id, feature_id, order):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR REPLACE INTO walking_map_relations (map_id, feature_id, display_order)
        VALUES (?, ?, ?)
    """, (map_id, feature_id, order))

def create_md(feature_id, name, type_str, subtype, description, is_enriched, towns_list=None):
    if is_enriched:
        print(f"Skipping MD generation for enriched POI: {feature_id}")
        return

    towns_content = ""
    if towns_list:
        towns_content = "\n## 所轄鄉鎮\n\n" + "\n".join([f"- [{t_name}](?map={MAP_ID}&feature={t_id})" for t_name, t_id in towns_list])
    
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
    enriched_ids = get_enriched_list(conn)
    print(f"Enriched POIs found: {enriched_ids}")

    # 1. 先獲取鄉鎮清單，建立縣市對應關係
    print("Pre-scanning towns for hierarchy...")
    county_to_towns = {}
    town_data = []
    with fiona.open(TOWN_SHP, encoding='utf-8') as src:
        for feat in src:
            p = feat['properties']
            c_name = p['COUNTYNAME']
            t_name = p['TOWNNAME']
            t_code = p['TOWNCODE']
            feature_id = f"TOWN_{t_code}_{c_name}{t_name}"
            
            if c_name not in county_to_towns:
                county_to_towns[c_name] = []
            county_to_towns[c_name].append((t_name, feature_id))
            town_data.append((feature_id, c_name, t_name, feat))

    # 2. 處理鄉鎮
    print("Inserting towns...")
    order = 1
    for feature_id, c_name, t_name, feat in town_data:
        is_enriched = feature_id in enriched_ids
        name = f"{c_name}{t_name}"
        desc = f"{c_name}的{t_name}。"
        
        # 幾何簡化
        geom = simplify(shape(feat['geometry']), tolerance=0.0005)
        
        insert_feature(conn, feature_id, name, desc, geom.geom_type, geom.wkt, "鄉鎮市區", is_enriched)
        link_to_map(conn, MAP_ID, feature_id, order)
        create_md(feature_id, name, "行政區劃", "鄉鎮市區", desc, is_enriched)
        order += 1

    # 3. 處理縣市
    print("Inserting counties...")
    with fiona.open(COUNTY_SHP, encoding='utf-8') as src:
        for feat in src:
            p = feat['properties']
            c_name = p['COUNTYNAME']
            c_code = p['COUNTYCODE']
            feature_id = f"COUNTY_{c_code}_{c_name}"
            is_enriched = feature_id in enriched_ids
            
            # 幾何簡化
            geom = simplify(shape(feat['geometry']), tolerance=0.001)
            
            name = c_name
            desc = f"台灣的{c_name}。"
            towns = county_to_towns.get(c_name, [])
            
            insert_feature(conn, feature_id, name, desc, geom.geom_type, geom.wkt, "縣市", is_enriched)
            link_to_map(conn, MAP_ID, feature_id, order)
            create_md(feature_id, name, "行政區劃", "縣市", desc, is_enriched, towns_list=towns)
            order += 1

    conn.commit()
    conn.close()
    print("Full island administrative initialization complete.")

if __name__ == "__main__":
    main()
