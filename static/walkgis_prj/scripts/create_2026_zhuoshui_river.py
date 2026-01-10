
import json
import os
import sqlite3

# Configuration
MAP_ID = "2026_zhuoshui_river"
MAP_NAME = "濁水溪流域百科全書式探索"
INPUT_FILE = "../data/2026_zhuoshui_river_pois.json"
DB_PATH = "../walkgis.db"

# Paths (Relative to script location)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FEATURES_DIR = os.path.join(BASE_DIR, "../features")
MAPS_DIR = os.path.join(BASE_DIR, "../maps")
SQL_DIR = os.path.join(BASE_DIR, "../sql")
DB_FILE = os.path.join(BASE_DIR, DB_PATH)

os.makedirs(FEATURES_DIR, exist_ok=True)
os.makedirs(MAPS_DIR, exist_ok=True)
os.makedirs(SQL_DIR, exist_ok=True)

def safe_name(name):
    return "".join([c if c.isalnum() else "_" for c in name]).strip("_")

def get_or_create_layer(cursor, category):
    """
    Maps category to a specific layer_type/subtype and returns layer_id.
    """
    # Simple mapping logic
    layer_type = "未分類"
    layer_subtype = category
    
    if "自然地景" in category:
        layer_type = "自然地景"
        layer_subtype = category.replace("自然地景-", "")
    elif "水利設施" in category:
        layer_type = "水利設施"
        layer_subtype = category.replace("水利設施-", "")
    elif "交通設施" in category:
        layer_type = "交通設施"
        layer_subtype = category.replace("交通設施-", "")
    elif "人文史蹟" in category:
        layer_type = "人文史蹟"
        layer_subtype = category.replace("人文史蹟-", "")
    elif "災害" in category:
        layer_type = "災害與環境"
        layer_subtype = "一般"

    # Check existence
    cursor.execute("SELECT layer_id FROM layers WHERE layer_type = ? AND layer_subtype = ?", (layer_type, layer_subtype))
    row = cursor.fetchone()
    if row:
        return row[0]
    else:
        # Create
        cursor.execute("INSERT INTO layers (layer_type, layer_subtype, description) VALUES (?, ?, ?)", 
                       (layer_type, layer_subtype, f"Auto-generated layer for {category}"))
        return cursor.lastrowid

def main():
    with open(os.path.join(BASE_DIR, INPUT_FILE), 'r', encoding='utf-8') as f:
        pois = json.load(f)

    # Dictionary to cache layer IDs
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    layer_map = {} # category -> layer_id

    features_md_links = []
    sql_statements = []
    
    sql_statements.append("BEGIN TRANSACTION;")
    
    # 1. Upsert Map (walking_maps)
    # Using INSERT OR REPLACE. Note: Schema uses 'map_id', 'name', 'description', 'created_at'.
    sql_statements.append(f"""
    INSERT OR REPLACE INTO walking_maps (map_id, name, description, region, created_at) 
    VALUES ('{MAP_ID}', '{MAP_NAME}', '從上游到出海口的完整流域探索', '濁水溪流域', CURRENT_TIMESTAMP);
    """)

    mermaid_graph = ["graph TD"]
    categories = {}

    for idx, poi in enumerate(pois):
        if not poi.get('found', False):
            print(f"Skipping {poi['name']} (Not Found)")
            continue

        safe_n = safe_name(poi['name'])
        feature_id = f"{MAP_ID}_{idx:02d}_{safe_n}"
        category = poi.get('category', 'Uncategorized')
        
        # Get Layer ID
        if category not in layer_map:
            layer_map[category] = get_or_create_layer(cursor, category)
        layer_id = layer_map[category]

        # Prepare MD Content
        md_content = f"""---
id: {feature_id}
name: {poi['name']}
description: {category} - {poi.get('address', '')}
geometry:
  type: Point
  coordinates: [{poi['lon']}, {poi['lat']}]
properties:
  category: {category}
  rating: {poi.get('rating', '')}
  place_id: {poi.get('place_id', '')}
---

# {poi['name']}

- **類別**: {category}
- **地址**: {poi.get('address', 'N/A')}
- **評分**: {poi.get('rating', 'N/A')}

## 簡介
(待補充詳細資料)

## 相關連結
- [Google Maps](https://www.google.com/maps/search/?api=1&query={poi['lat']},{poi['lon']}&query_place_id={poi.get('place_id', '')})
"""
        
        with open(os.path.join(FEATURES_DIR, f"{feature_id}.md"), 'w', encoding='utf-8') as f:
            f.write(md_content)
        
        features_md_links.append(f"- [{poi['name']}](../features/{feature_id}.md)")
        
        # Generate SQL for walking_map_features
        # WKT: POINT(120.123 23.456)
        wkt = f"POINT({poi['lon']} {poi['lat']})"
        clean_desc = f"{category} - {poi.get('address', '')}".replace("'", "''")
        meta_json = json.dumps({
            "category": category,
            "rating": poi.get('rating', ''),
            "place_id": poi.get('place_id', '')
        }, ensure_ascii=False).replace("'", "''")

        sql_statements.append(f"""
        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('{feature_id}', '{poi['name']}', '{clean_desc}', {layer_id}, 'Point', '{wkt}', '{meta_json}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        """)
        
        # walking_map_relations
        sql_statements.append(f"""
        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('{MAP_ID}', '{feature_id}', {idx});
        """)

        if category not in categories:
            categories[category] = []
            
        mermaid_graph.append(f"    {safe_n}[\"{poi['name']}\"]")
        # Store for simple alphabetical sort or similar later if needed, 
        # but here we just list nodes.
        # Linking logic:
        # Link category node to item
        cat_safe = safe_name(category)
        categories[category].append(safe_n)

    # Mermaid wiring
    for cat, items in categories.items():
        cat_safe = safe_name(cat)
        mermaid_graph.append(f"    {cat_safe}({cat})")
        for item in items:
            mermaid_graph.append(f"    {cat_safe} --> {item}")

    sql_statements.append("COMMIT;")
    
    # Commit any new layers created
    conn.commit()
    conn.close()

    # 2. Generate Map MD
    map_md_content = f"""---
id: {MAP_ID}
name: {MAP_NAME}
description: 濁水溪流域自然、人文、水利、交通與災害維度探索
---

# {MAP_NAME}

## 地圖結構
```mermaid
{chr(10).join(mermaid_graph)}
```

## 景點列表
{chr(10).join(features_md_links)}
"""

    with open(os.path.join(MAPS_DIR, f"{MAP_ID}.md"), 'w', encoding='utf-8') as f:
        f.write(map_md_content)

    # 3. Write SQL Script
    with open(os.path.join(SQL_DIR, f"create_{MAP_ID}.sql"), 'w', encoding='utf-8') as f:
        f.write("\n".join(sql_statements))

    print(f"Generated {len(features_md_links)} features.")
    print(f"Map MD: {os.path.join(MAPS_DIR, f'{MAP_ID}.md')}")
    print(f"SQL Script: {os.path.join(SQL_DIR, f'create_{MAP_ID}.sql')}")

if __name__ == "__main__":
    main()
