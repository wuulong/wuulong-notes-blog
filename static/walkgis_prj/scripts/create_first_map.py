import sqlite3
import json

DB_PATH = "events/notes/walkgis_prj/walkgis.db"
MAP_ID = "2025_houfeng_dongfeng_loop"
MAP_NAME = "后豐鐵馬道 & 東豐綠廊精華遊"

# 1. 定義地圖 Metadata (含 Mermaid Route)
map_metadata = {
    "difficulty": "Easy",
    "total_distance": "18km",
    "estimated_time": "3-4 hours",
    "routes": {
        "main_route": """graph LR;
    Start(后里馬場) --> A(九號隧道);
    A --> B(花樑鋼橋);
    B --> C(石岡水壩);
    C --> D(0蛋月台);
    D --> E(九房3D彩繪村);
    E --> F(情人木橋);
    F --> G(東勢客家文化園區);
    style Start fill:#f9f,stroke:#333;"""
    }
}

def create_map():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        # 1. 插入 Map
        print(f"Creating Map: {MAP_ID}...")
        cursor.execute("""
            INSERT OR REPLACE INTO walking_maps (map_id, name, description, region, meta_data)
            VALUES (?, ?, ?, ?, ?)
        """, (
            MAP_ID, 
            MAP_NAME, 
            "一次體驗舊山線鐵道風情與大甲溪與綠色隧道的完美單車路線。",
            "台中/后里/豐原/石岡/東勢",
            json.dumps(map_metadata, ensure_ascii=False)
        ))

        # 2. 查詢所有 Features (我們剛匯入的那些)
        # 假設都是今天匯入的，feature_id 開頭為 2025
        cursor.execute("SELECT feature_id, name FROM walking_map_features WHERE feature_id LIKE '2025%'")
        rows = cursor.fetchall()

        # 3. 建立關聯 (Relations)
        relation_count = 0
        for idx, (feature_id, name) in enumerate(rows):
            # 簡單給個顯示順序 10, 20, 30...
            display_order = (idx + 1) * 10
            
            # 判斷是否高亮 (簡單邏輯：名字裡有'馬場','水壩','客家'就算重點)
            is_highlight = 1 if any(k in name for k in ['馬場', '水壩', '隧道', '鋼橋', '客家']) else 0

            cursor.execute("""
                INSERT OR REPLACE INTO walking_map_relations (map_id, feature_id, display_order, is_highlight)
                VALUES (?, ?, ?, ?)
            """, (MAP_ID, feature_id, display_order, is_highlight))
            relation_count += 1
        
        conn.commit()
        print(f"Map created successfully with {relation_count} relations!")

    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    create_map()
