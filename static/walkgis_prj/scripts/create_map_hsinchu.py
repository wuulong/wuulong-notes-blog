import os

# Config
BASE_DIR = "../features"
SQL_FILE = "../sql/create_2025_smart_water_fun_map_hsinchu.sql"


MAP_ID = "2025_smart_water_fun_map_hsinchu"
MAP_NAME = "智慧水圳玩樂地圖-新竹管理處"
MAP_DESC = "探索新竹地區的重要水利設施，見證傳統水圳與現代科技的結合。"
MAP_COVER = "assets/images/hsinchu_water_cover.jpg"
TAG = "智慧水圳玩樂地圖-新竹管理處"

FEATURES = [
    {
        "id": "20251230_sancha_pond",
        "name": "三叉埤",
        "coords": [24.7137, 121.1268],
        "desc": "位於橫山鄉，由當地居民人工築堤而成，匯集三座山谷溪流。不僅是百年水利設施，也是橫山村的地理中心與生態熱點。"
    },
    {
        "id": "20251230_tingfu_canal",
        "name": "汀甫圳",
        "coords": [24.8024, 120.9960],
        "desc": "新竹市最長的水圳，始建於清朝，紀念末代圳長何汀甫捐圳予公。沿線流經新竹精華區，是城市中的綠色水脈。"
    },
    {
        "id": "20251230_tingfu_main_canal",
        "name": "汀甫圳幹線",
        "coords": [24.7980, 120.9900], # 近交大博愛校區段
        "desc": "汀甫圳的主幹線，近期進行了景觀改善工程，結合砌卵石護岸與步道，成為市民休閒散步的好去處。"
    },
    {
        "id": "20251230_zhudong_canal_sand_basin",
        "name": "竹東圳 (分水沉沙池)",
        "coords": [24.7203, 121.0436], # 近寶二水庫
        "desc": "竹東圳是新竹重要的導水路，連結上坪溪與寶山水庫。此處的分水沉沙池負責在注入水庫前沉澱泥沙，確保水庫壽命。"
    },
    {
        "id": "20251230_dongxing_old_port_canal_circle",
        "name": "東興舊港圳圓環",
        "coords": [24.7715, 121.0664],
        "desc": "獨特的「水利雙圓環」，利用圓環分水汴將水源公平分配至東興圳與舊港圳，展現了日治時期的分水智慧。"
    },
    {
        "id": "20251230_jietou_main_canal",
        "name": "街頭圳幹線",
        "coords": [24.7170, 121.1210],
        "desc": "位於橫山鄉的重要灌溉渠道，滋潤了田寮村的農田，也是當地農村風貌的重要組成部分。"
    },
    {
        "id": "20251230_longen_canal",
        "name": "隆恩圳 (東大路旁)",
        "coords": [24.7985, 121.0163],
        "desc": "台灣三大古圳之一，已有300年歷史。在東大路段展現了古老水圳如何流經現代都市，並被賦予新的親水機能。"
    },
    {
        "id": "20251230_maoerding_branch_3",
        "name": "貓兒錠幹線3支線",
        "coords": [24.8320, 121.1120], # 概略位置
        "desc": "位於竹北鳳岡地區，服務當地的水稻田。這條支線體現了竹北平原區發達的灌溉網絡。"
    }
]

def create_markdown(f):
    content = f"""---
id: {f['id']}
name: {f['name']}
type: 水利設施
subtype: 智慧水圳
date: 2025-12-30
coordinate: [{f['coords'][0]}, {f['coords'][1]}]
tags: ["{TAG}"]
---

# {f['name']}

{f['desc']}

## 基本資訊
*   **座標**: {f['coords'][0]}, {f['coords'][1]}
*   **特色**: 歷史水利、生態工法、分水智慧
"""
    filepath = os.path.join(BASE_DIR, f"{f['id']}.md")
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Created MD: {filepath}")

def create_sql(features):
    sql = f"""-- Create Map: {MAP_NAME}
INSERT OR REPLACE INTO walking_maps (map_id, name, description, region, cover_image) 
VALUES ('{MAP_ID}', '{MAP_NAME}', '{MAP_DESC}', '新竹縣市', '{MAP_COVER}');

-- Create Features & Relation
DELETE FROM walking_map_relations WHERE map_id = '{MAP_ID}';
"""
    
    for idx, f in enumerate(features):
        wkt = f"POINT({f['coords'][1]} {f['coords'][0]})" # Lon Lat
        meta = f'{{"markdown_file": "{f["id"]}.md", "tags": ["{TAG}"]}}'
        
        # Insert Feature
        sql += f"""
INSERT OR REPLACE INTO walking_map_features (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data)
VALUES ('{f['id']}', '{f['name']}', '{f['desc']}', 2, 'Point', '{wkt}', '{meta}');

-- Insert Relation
INSERT INTO walking_map_relations (map_id, feature_id, display_order, is_highlight, note)
VALUES ('{MAP_ID}', '{f['id']}', {idx+1}, {1 if idx < 3 else 0}, '{f['name']}');
"""

    with open(SQL_FILE, 'w', encoding='utf-8') as file:
        file.write(sql)
    print(f"Created SQL: {SQL_FILE}")

def main():
    if not os.path.exists(BASE_DIR):
        os.makedirs(BASE_DIR)
        
    for f in FEATURES:
        create_markdown(f)
        
    create_sql(FEATURES)

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    main()
