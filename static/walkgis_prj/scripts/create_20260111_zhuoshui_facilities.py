
import sqlite3
import json
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(SCRIPT_DIR, "../walkgis.db")
JSON_PATH = os.path.join(SCRIPT_DIR, "../data/20260111_zhuoshui_facilities.json")
FEATURES_DIR = os.path.join(SCRIPT_DIR, "../features")
MAPS_DIR = os.path.join(SCRIPT_DIR, "../maps")

MAP_ID = "20260111_zhuoshui_facilities"
MAP_NAME = "濁水溪及其周邊景點設施地圖"
MAP_DESC = "彙整濁水溪流域之交通、水利、人文與自然景點"

CATEGORIES = {
    "水利": ["圳", "水庫", "堰", "堤", "抽水站", "水門", "大排", "淨水場", "水利"],
    "交通": ["車站", "橋", "鐵道", "交流道", "服務區", "隧道", "路"],
    "人文": ["廟", "宮", "寺", "遺址", "古厝", "國小", "國中", "高中", "大學", "紀念碑", "聚落", "老街"],
    "自然": ["步道", "公園", "山", "溼地", "農場", "風景區", "斷層"],
    "災害": ["監測站", "地層下陷"]
}

def get_layer_id(cursor, layer_type):
    cursor.execute("SELECT layer_id FROM layers WHERE layer_type = ?", (layer_type,))
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        cursor.execute("INSERT INTO layers (layer_type, description) VALUES (?, ?)", (layer_type, "Auto-generated category"))
        return cursor.lastrowid

def classify_feature(name):
    for cat, keywords in CATEGORIES.items():
        for kw in keywords:
            if kw in name:
                return f"濁水溪_{cat}"
    return "濁水溪_其他"

def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 1. Create Map
    cursor.execute("INSERT OR REPLACE INTO walking_maps (map_id, name, description, region, created_at) VALUES (?, ?, ?, ?, DATE('now'))", 
                   (MAP_ID, MAP_NAME, MAP_DESC, "Central Taiwan"))
    
    # 2. Process Features
    if not os.path.exists(JSON_PATH):
        print(f"JSON not found: {JSON_PATH}")
        return

    with open(JSON_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    feature_links = []
    
    print(f"Processing {len(data)} features...")
    
    for idx, item in enumerate(data):
        name = item['name']
        geometry = item['geometry']
        feat_id = f"{MAP_ID}_{str(idx).zfill(3)}_{name.replace(' ', '_').replace('/', '_')}"
        
        # Categorize
        layer_type = classify_feature(name)
        layer_id = get_layer_id(cursor, layer_type)
        
        # Insert Feature
        try:
            cursor.execute("""
                INSERT OR REPLACE INTO walking_map_features 
                (feature_id, name, description, layer_id, geometry_type, geometry_wkt) 
                VALUES (?, ?, ?, ?, ?, ?)
            """, (feat_id, name, item['description'], layer_id, item['type'], geometry))
        except sqlite3.Error as e:
            print(f"Error inserting {name}: {e}")
            continue

        # Link to Map
        cursor.execute("INSERT OR REPLACE INTO walking_map_relations (map_id, feature_id, display_order) VALUES (?, ?, ?)",
                       (MAP_ID, feat_id, idx))
        
        # Create Markdown
        md_content = f"""---
id: {feat_id}
name: {name}
map_id: {MAP_ID}
layer_id: {layer_id}
geometry_wkt: {geometry}
---

## 簡介
{item['description'] if item['description'] else "(待補充詳細資料)"}

## 相關連結
"""
        os.makedirs(FEATURES_DIR, exist_ok=True)
        md_path = os.path.join(FEATURES_DIR, f"{feat_id}.md")
        with open(md_path, 'w', encoding='utf-8') as mf:
            mf.write(md_content)
        
        feature_links.append(f"- [{name}](../features/{feat_id}.md)")

    # 3. Create Map Markdown
    map_md_content = f"""---
id: {MAP_ID}
name: {MAP_NAME}
description: {MAP_DESC}
region: 中台灣
cover_image: assets/cover_images/placeholder.jpg
created_at: 2026-01-11
updated_at: 2026-01-11
tags: [濁水溪, 景點, 設施]
---

# {MAP_NAME}

## 簡介 (Introduction)
{MAP_DESC}。本資料集包含水利、交通、人文、自然等多面向的景點。

## 地圖結構 (Topology)
```mermaid
graph TD
    Map["{MAP_NAME}"]
"""
    # Simply add a note about graph being too large
    map_md_content += """
    Note["(Graph Truncated: Too many features to display in Mermaid)"]
    Map --> Note
```

## 🗺️ AI 深度探索 (Deep Research)
(由於景點眾多，建議針對特定分類進行搜尋)

## 下載與資源 (Resources)
- **[KML 地圖檔下載](./20260111_zhuoshui_facilities.kml)**

## 景點列表 (Features)
""" + "\n".join(feature_links)

    os.makedirs(MAPS_DIR, exist_ok=True)
    with open(os.path.join(MAPS_DIR, f"{MAP_ID}.md"), 'w', encoding='utf-8') as f:
        f.write(map_md_content)

    conn.commit()
    conn.close()
    print("Done!")

if __name__ == "__main__":
    main()
