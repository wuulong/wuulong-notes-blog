import os
import sqlite3

BASE_DIR = "events/notes/wuulong-notes-blog/static/walkgis_prj"
FEATURES_DIR = os.path.join(BASE_DIR, "features")
SQL_DIR = os.path.join(BASE_DIR, "sql")
DB_PATH = os.path.join(BASE_DIR, "walkgis.db")
MAP_ID = "2026_daan_dajia_pipeline"
MAP_NAME = "大安大甲溪聯通管工程計畫地圖"

# Approximate Waypoints (Lat, Lon)
# Red Line: 石岡壩 -> 沿河岸 -> 后里
path_red = [
    (24.2797, 120.7691), # 石岡壩
    (24.2820, 120.7600), # 河岸轉折
    (24.2850, 120.7500), # 國道四號附近
    (24.2900, 120.7400), # 續行
    (24.3000, 120.7350), # 轉向后里
    (24.3195, 120.7359)  # 后里第一淨水場
]

# Purple Line: 鯉魚潭水庫 -> 枕頭山 -> 水管橋 -> 后里
path_purple = [
    (24.3415, 120.7819), # 鯉魚潭水庫
    (24.3343, 120.7660), # 枕頭山
    (24.3258, 120.7516), # 大安溪水管橋
    (24.3195, 120.7359)  # 后里第一淨水場
]

# Yellow Line: 后里圳相關
path_yellow = [
    (24.3195, 120.7359), # 后里第一淨水場
    (24.3155, 120.7258), # 鯉魚潭淨水場
    (24.3060, 120.7266)  # 后里圳
]

pipelines = [
    {
        "name": "路徑_大甲溪輸水管",
        "desc": "沿大甲溪左岸鋪設，全長約10.2公里，連接石岡壩與后里第一淨水場。",
        "color": "#FF0000", # Red
        "path": path_red
    },
    {
        "name": "路徑_鯉魚潭第二原水管",
        "desc": "從鯉魚潭水庫出發，穿越枕頭山與大安溪，連接至后里第一淨水場。",
        "color": "#800080", # Purple
        "path": path_purple
    },
    {
        "name": "路徑_后里圳送水管",
        "desc": "連接后里第一淨水場、鯉魚潭淨水場與后里圳的聯絡管線。",
        "color": "#FFFF00", # Yellow
        "path": path_yellow
    }
]

def generate_wkt(path):
    # WKT Format: LINESTRING(lon1 lat1, lon2 lat2, ...)
    coords = ", ".join([f"{p[1]} {p[0]}" for p in path])
    return f"LINESTRING({coords})"

def run():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    order = 20 # Start ordering after point features
    
    for pipe in pipelines:
        feature_id = f"20260101_daan_dajia_pipeline_{pipe['name']}"
        wkt = generate_wkt(pipe['path'])
        
        # 1. Create Markdown
        md_content = f"""---
id: {feature_id}
title: {pipe['name']}
tags: [{MAP_NAME}, 輸水管線]
geometry_type: LineString
color: "{pipe['color']}"
coordinates: {pipe['path']}
---
# {pipe['name'].replace('路徑_', '')}

{pipe['desc']}

## Geometry
WKT: `{wkt}`
"""
        filepath = os.path.join(FEATURES_DIR, f"{feature_id}.md")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(md_content)
        print(f"Generated: {filepath}")

        # 2. Update DB (Feature)
        # Assuming layer_id 1 exists (or we query it)
        cursor.execute("SELECT layer_id FROM layers WHERE layer_type='工程計畫' LIMIT 1")
        layer_row = cursor.fetchone()
        layer_id = layer_row[0] if layer_row else 1
        
        cursor.execute(f"""
            INSERT OR REPLACE INTO walking_map_features 
            (feature_id, name, description, layer_id, geometry_type, geometry_wkt) 
            VALUES (?, ?, ?, ?, 'LineString', ?)
        """, (feature_id, pipe['name'], pipe['desc'], layer_id, wkt))
        
        # 3. Update DB (Relation)
        cursor.execute(f"""
            INSERT OR REPLACE INTO walking_map_relations 
            (map_id, feature_id, display_order) 
            VALUES (?, ?, ?)
        """, (MAP_ID, feature_id, order))
        
        order += 1
        print(f"DB Updated for {pipe['name']}")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    run()
