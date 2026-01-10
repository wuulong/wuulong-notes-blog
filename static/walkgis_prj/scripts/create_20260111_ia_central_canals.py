
import json
import os
import sqlite3

# Configuration
MAP_ID = "20260111_ia_central_canals"
MAP_NAME = "農田水利署中區圳路地圖"
INPUT_FILE = "../data/20260111_ia_central_canals_pois.json"
DB_PATH = "../walkgis.db"

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FEATURES_DIR = os.path.join(BASE_DIR, "../features")
MAPS_DIR = os.path.join(BASE_DIR, "../maps")
SQL_DIR = os.path.join(BASE_DIR, "../sql")
DB_FILE = os.path.join(BASE_DIR, DB_PATH)

os.makedirs(FEATURES_DIR, exist_ok=True)
os.makedirs(MAPS_DIR, exist_ok=True)
os.makedirs(SQL_DIR, exist_ok=True)

def safe_name(name):
    # Remove parens and other chars for safe filenames
    return "".join([c if c.isalnum() else "_" for c in name]).strip("_")

def get_or_create_layer(cursor, category):
    # Map category string to Layer Type/Subtype
    # Example format: "水利設施-彰化管理處"
    parts = category.split('-')
    if len(parts) >= 2:
        layer_type = parts[0]
        layer_subtype = parts[1]
    else:
        layer_type = "未分類"
        layer_subtype = category

    cursor.execute("SELECT layer_id FROM layers WHERE layer_type = ? AND layer_subtype = ?", (layer_type, layer_subtype))
    row = cursor.fetchone()
    if row:
        return row[0]
    else:
        cursor.execute("INSERT INTO layers (layer_type, layer_subtype, description) VALUES (?, ?, ?)", 
                       (layer_type, layer_subtype, f"Auto-generated layer for {category}"))
        return cursor.lastrowid

def main():
    with open(os.path.join(BASE_DIR, INPUT_FILE), 'r', encoding='utf-8') as f:
        pois = json.load(f)

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    layer_map = {} 
    features_md_links = []
    sql_statements = []
    
    sql_statements.append("BEGIN TRANSACTION;")
    
    # 1. Map Record
    sql_statements.append(f"""
    INSERT OR REPLACE INTO walking_maps (map_id, name, description, region, created_at) 
    VALUES ('{MAP_ID}', '{MAP_NAME}', '彰化、雲林、南投管理處重要圳路設施', '中台灣', CURRENT_TIMESTAMP);
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
        
        # Layer Logic
        if category not in layer_map:
            layer_map[category] = get_or_create_layer(cursor, category)
        layer_id = layer_map[category]

        # MD Content
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
        
        # SQL Logic
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
        
        sql_statements.append(f"""
        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('{MAP_ID}', '{feature_id}', {idx});
        """)

        # Mermaid
        if category not in categories:
            categories[category] = []
        categories[category].append(safe_n)
        mermaid_graph.append(f"    {safe_n}[\"{poi['name']}\"]")


    # Mermaid Wiring
    for cat, items in categories.items():
        # Clean category name for node ID (remove dash)
        cat_node = safe_name(cat)
        mermaid_graph.append(f"    {cat_node}({cat})")
        for item in items:
            mermaid_graph.append(f"    {cat_node} --> {item}")

    sql_statements.append("COMMIT;")
    
    conn.commit()
    conn.close()

    # 2. Map MD
    map_md_content = f"""---
id: {MAP_ID}
name: {MAP_NAME}
description: 彰化、雲林、南投管理處重要圳路設施
region: 中台灣
cover_image: assets/cover_images/placeholder.jpg
created_at: 2026-01-11
updated_at: 2026-01-11
tags: [水利設施, 圳路, 農田水利署]
---

# {MAP_NAME}

## 地圖結構 (Topology)
```mermaid
{chr(10).join(mermaid_graph)}
```

## 簡介 (Introduction)
本圖資彙整了農業部農田水利署（彰化、雲林、南投管理處）轄區內的重要圳路設施、取水口與相關景點。適合進行水利文化探索與考察。

## 使用者補充筆記 (User Notes)
### 重點觀察
- 彰化：八堡圳水系
- 雲林：濁幹線與水圳綠道
- 南投：埔里與頭社水庫生態

## 🗺️ AI 深度探索 (Deep Research)
如果您擁有 Gemini Advanced 或其他 Deep Research 工具，可以複製以下 Prompt，針對本工程地圖進行深度的文史與美食探索：

```markdown
# Context
一份名為「{MAP_NAME}」的導覽路線，探索中台灣重要的農田水利設施。

# Task
請針對以下景點列表，進行 Deep Research，挖掘背後的「歷史深度」、「生活溫度」與「在地美食」。

**景點列表：**
1. 八堡圳 (台灣最古老埤圳)
2. 斗六大圳
3. 頭社水庫
4. 水圳綠道

# Requirements (請分析以下維度)
1. **歷史與工程脈絡**: 該點在台灣水利/歷史的角色？
2. **在地文化與生態**: 周邊古蹟、廟宇、特殊生態景觀。
3. **順遊景點**: 步行/單車可達的隱藏景點。
4. **必吃在地美食**: 老字號小吃、在地人推薦 (非連鎖)。
```

## 📊 Dynamic View 視覺化
如果您已經產出了 Deep Research Report，接著在 Dynamic View 中，您的 Prompt 策略應該從「獲取資訊」轉向**「結構化與視覺化」**。

1. **生成時間軸 (Timeline View)**
   - Prompt: "基於這份研究報告，請以時間軸視圖呈現各水利設施的建造年代與演變。"
2. **生成比較表格 (Comparison Table View)**
   - Prompt: "請建立一個比較表格，分析不同管理處（彰化/雲林/南投）的灌溉特色與水源差異。"

## 下載與資源 (Resources)
- **[KML 地圖檔下載](./{MAP_ID}.kml)**

## 景點列表 (Features)
{chr(10).join(features_md_links)}
"""

    with open(os.path.join(MAPS_DIR, f"{MAP_ID}.md"), 'w', encoding='utf-8') as f:
        f.write(map_md_content)

    with open(os.path.join(SQL_DIR, f"create_{MAP_ID}.sql"), 'w', encoding='utf-8') as f:
        f.write("\n".join(sql_statements))

    print(f"Generated {len(features_md_links)} features.")
    print(f"Map MD: {os.path.join(MAPS_DIR, f'{MAP_ID}.md')}")

if __name__ == "__main__":
    main()
