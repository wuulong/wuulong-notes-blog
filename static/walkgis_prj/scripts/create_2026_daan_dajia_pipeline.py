import os
import sqlite3
import datetime

# --- Configuration ---
MAP_ID = "2026_daan_dajia_pipeline"
MAP_NAME = "大安大甲溪聯通管工程計畫地圖"
MAP_DESC = "展示大甲溪輸水管工程與鯉魚潭第二原水管工程的關鍵設施與路徑。"
MAP_REGION = "台中/苗栗"
COVER_IMAGE = "assets/images/打造你的專屬地圖.png" # Default, user can update later

# Base Directory (relative to script location)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PRJ_DIR = os.path.dirname(BASE_DIR)
FEATURES_DIR = os.path.join(PRJ_DIR, "features")
MAPS_DIR = os.path.join(PRJ_DIR, "maps")
SQL_DIR = os.path.join(PRJ_DIR, "sql")
DB_PATH = os.path.join(PRJ_DIR, "walkgis.db")

# Locations Data (Name, Lat, Lon, Description)
LOCATIONS = [
    ("石岡壩", 24.2797, 120.7691, "大甲溪輸水管工程的起點，提供民生與灌溉用水的重要攔河堰。"),
    ("鯉魚潭水庫", 24.3415, 120.7819, "鯉魚潭第二原水管工程的起點，擁有全台唯一的鋸齒堰溢洪道。"),
    ("豐原淨水場", 24.2694, 120.7303, "負責大台中地區供水，是大甲溪輸水管的終點之一。"),
    ("后里第一淨水場", 24.3195, 120.7359, "新建工程，提升大台中地區供水穩定性，連接兩大輸水系統。"),
    ("鯉魚潭淨水場", 24.3155, 120.7258, "供應大台中地區民生用水的重要淨水場。"),
    ("經濟部水利署中區水資源分署", 24.0489, 120.6925, "計畫執行機關，負責中部地區水資源調配與管理。"),
    ("后里泰安國小", 24.3213, 120.7486, "位於泰安鐵道文化園區旁，曾舉辦水資源環境教育活動。"),
    ("苗栗鯉魚潭國小", 24.3418, 120.7766, "位於鯉魚潭水庫旁，致力於藝術與環境教育。"),
    ("枕頭山 (苗栗)", 24.3343, 120.7660, "工程包含隧道穿越此山，是連接水庫與大安溪的關鍵路徑。"),
    ("大安溪水管橋 (后里圳水橋)", 24.3258, 120.7516, "日治時期建成的拱形水橋，是大安溪上的水利地標。"),
    ("后里圳 (示範電廠)", 24.3060, 120.7266, "日治時期重要水利工程，設有低落差示範電廠。")
]

def generate_feature_md(feature_id, name, desc, lat, lon):
    content = f"""---
id: {feature_id}
title: {name}
tags: [{MAP_NAME}, 水利設施]
coordinate: [{lat}, {lon}]
---
# {name}

{desc}

## 地理資訊
*   緯度: {lat}
*   經度: {lon}
"""
    filepath = os.path.join(FEATURES_DIR, f"{feature_id}.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated Feature: {filepath}")

def generate_map_md(map_id, name, locations):
    # Create Mermaid Graph
    graph = "graph TD;\n"
    # Logic: Reservoir -> Tunnel/Bridge -> Plant
    graph += "    A[鯉魚潭水庫] --> B[枕頭山];\n"
    graph += "    B --> C[大安溪水管橋];\n"
    graph += "    C --> D[后里第一淨水場];\n"
    graph += "    E[石岡壩] --> F[豐原淨水場];\n"
    
    links = ""
    for loc in locations:
        fid = f"{map_id}_{loc[0]}"
        links += f"- [{loc[0]}](../features/{fid}.md)\n"

    content = f"""---
title: {name}
date: {datetime.date.today()}
description: {MAP_DESC}
---
{graph}

# {name}

{MAP_DESC}

## 景點列表
{links}
"""
    filepath = os.path.join(MAPS_DIR, f"{map_id}.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated Map: {filepath}")

def generate_sql(map_id, locations):
    sql_content = ""
    
    # Insert Map
    sql_content += f"INSERT OR REPLACE INTO walking_maps (map_id, name, description, region, cover_image) VALUES ('{MAP_ID}', '{MAP_NAME}', '{MAP_DESC}', '{MAP_REGION}', '{COVER_IMAGE}');\n"
    
    # Insert Layer (Ensure it exists)
    sql_content += f"INSERT OR IGNORE INTO layers (layer_type, layer_subtype, description) VALUES ('工程計畫', '水利設施', '大安大甲溪聯通管計畫設施');\n"
    
    # Insert Features and Relations
    order = 1
    for loc in locations:
        name = loc[0]
        desc = loc[3]
        lat = loc[1]
        lon = loc[2]
        fid = f"{map_id}_{name}"
        wkt = f"POINT({lon} {lat})"
        
        # Feature
        sql_content += f"INSERT OR REPLACE INTO walking_map_features (feature_id, name, description, layer_id, geometry_type, geometry_wkt) VALUES ('{fid}', '{name}', '{desc}', (SELECT layer_id FROM layers WHERE layer_type='工程計畫' LIMIT 1), 'Point', '{wkt}');\n"
        
        # Relation
        sql_content += f"INSERT OR REPLACE INTO walking_map_relations (map_id, feature_id, display_order) VALUES ('{MAP_ID}', '{fid}', {order});\n"
        order += 1
        
    filepath = os.path.join(SQL_DIR, f"create_{map_id}.sql")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(sql_content)
    print(f"Generated SQL: {filepath}")
    return filepath

def execute_sql(sql_file):
    print(f"Executing SQL: {sql_file} on {DB_PATH}")
    # Read sql content
    with open(sql_file, 'r', encoding='utf-8') as f:
        sql_script = f.read()
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.executescript(sql_script)
    conn.commit()
    conn.close()
    print("Database Updated.")

# --- Main Execution ---
if __name__ == "__main__":
    if not os.path.exists(FEATURES_DIR): os.makedirs(FEATURES_DIR)
    if not os.path.exists(MAPS_DIR): os.makedirs(MAPS_DIR)
    if not os.path.exists(SQL_DIR): os.makedirs(SQL_DIR)

    # 1. Generate Features
    for loc in LOCATIONS:
        fid = f"{MAP_ID}_{loc[0]}"
        generate_feature_md(fid, loc[0], loc[3], loc[1], loc[2])

    # 2. Generate Map
    generate_map_md(MAP_ID, MAP_NAME, LOCATIONS)

    # 3. Generate and Run SQL
    sql_file = generate_sql(MAP_ID, LOCATIONS)
    execute_sql(sql_file)

    print("\nNext Steps:")
    print(f"1. Run: sh static/walkgis_prj/scripts/gen_notebooklm_context.sh {MAP_ID}")
    print(f"2. Use NotebookLM to generate a cover image and update DB.")
