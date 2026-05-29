import sqlite3
import json
import os

PROJECT_ROOT = "events/notes/wuulong-notes-blog/static/walkgis_prj"
DB_PATH = f"{PROJECT_ROOT}/walkgis.db"

def update_db():
    if not os.path.exists(DB_PATH):
        print(f"Error: Database not found at {DB_PATH}")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 1. 更新或插入 20260324_liwu_river 的 walking_maps
    map_id = "20260324_liwu_river"
    map_name = "立霧溪探索計畫：橫跨太魯閣大理石峽谷的生命之刃"
    
    mermaid_route = """graph TD
    A[立霧溪出海口: 新城] --> B[砂卡礑溪: 碧藍之謎]
    B --> C[布洛灣: 台地聚落]
    C --> D[燕子口: 河流下切實證]
    D --> E[錐麓大斷崖: 1914 歷史防線]
    E --> F[九曲洞: 大理石心臟]
    F --> G[天祥: 支流匯流點/宿營]
    G --> H[中橫雲霧帶: 洛韶/碧綠神木]
    H --> I[合歡群峰: 立霧溪源頭]
    I --> J[武嶺: 脊樑分水嶺 3275m]
    J --> K[西半部回程: 清境/霧社溪]
    K --> L[眉溪天險: 人止關]
    L --> M[烏溪谷地: 埔里/返家]"""

    map_metadata = {
        "difficulty": "Hard",
        "estimated_time": "5 days",
        "routes": {
            "main_route": mermaid_route
        },
        "description": "立霧溪流域五天深度探索計畫，橫跨大理石峽谷與脊樑分水嶺的生命之刃。"
    }

    cursor.execute("""
        INSERT OR REPLACE INTO walking_maps (map_id, name, meta_data)
        VALUES (?, ?, ?)
    """, (map_id, map_name, json.dumps(map_metadata, ensure_ascii=False)))
    print(f"Updated map: {map_id}")

    # 2. 插入兩個新點位至 walking_map_features
    # WKT 格式 POINT(lon lat)
    features_to_add = [
        (
            "20260324_liwu_12_wuling",
            "武嶺分水嶺",
            "海拔 3275 公尺的中央山脈主脊分水嶺，立霧溪與濁水溪搶水戰爭的動態核心。",
            "POINT(121.272118 24.137456)",
            {
                "ref_doc": "features/20260324_liwu_12_wuling.md",
                "coordinate": [24.137456, 121.272118],
                "address": "546台灣南投縣仁愛鄉武嶺",
                "type": "attraction",
                "river": "立霧溪"
            }
        ),
        (
            "20260324_liwu_13_renzhipass",
            "人止關",
            "眉溪（烏溪支流）劇烈切穿厚層硬質砂岩形成的近垂直峽谷，清代原漢隘勇線與歷史防禦天險。",
            "POINT(121.1039 23.9961)",
            {
                "ref_doc": "features/20260324_liwu_13_renzhipass.md",
                "coordinate": [23.9961, 121.1039],
                "address": "546台灣南投縣仁愛鄉人止關",
                "type": "historical",
                "river": "眉溪"
            }
        )
    ]

    for f_id, f_name, f_desc, f_wkt, f_meta in features_to_add:
        # Layer ID = 1 (水文與親水層)
        cursor.execute("""
            INSERT OR REPLACE INTO walking_map_features 
            (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (f_id, f_name, f_desc, 1, "Point", f_wkt, json.dumps(f_meta, ensure_ascii=False)))
        print(f"Updated feature: {f_name}")

        # 3. 建立 relations 關聯 (如果尚未關聯)
        # 查詢目前最大的 display_order
        cursor.execute("SELECT MAX(display_order) FROM walking_map_relations WHERE map_id = ?", (map_id,))
        max_order = cursor.fetchone()[0]
        next_order = (max_order + 1) if max_order is not None else 1

        cursor.execute("""
            SELECT 1 FROM walking_map_relations WHERE map_id = ? AND feature_id = ?
        """, (map_id, f_id))
        if not cursor.fetchone():
            cursor.execute("""
                INSERT INTO walking_map_relations (map_id, feature_id, display_order, is_highlight)
                VALUES (?, ?, ?, ?)
            """, (map_id, f_id, next_order, 1))
            print(f"Associated {f_name} with map {map_id} at order {next_order}")

    conn.commit()
    conn.close()
    print("Database sync completed successfully!")

if __name__ == "__main__":
    update_db()
