import sqlite3
import json

DB_PATH = "events/notes/walkgis_prj/walkgis.db"
MAP_ID = "2025_houfeng_dongfeng_loop"

# 完整的拓樸路徑 Mermaid 定義
mermaid_graph = """graph LR;
    %% 子圖：后豐鐵馬道
    subgraph Houfeng ["后豐鐵馬道 (4.5km)"]
        direction TB
        H1(1. 后里馬場) --> HA(樟樹平台);
        HA --> H2(2. 夫妻樹);
        H2 --> H3(3. 九號隧道);
        H3 --> H4(4. 花樑鋼橋);
        H4 --> HB(鐵道之鄉酒莊);
        HB -.-> HC(榮町雜貨店);
    end

    %% 子圖：東豐綠廊 (前段)
    subgraph Dongfeng_Start ["東豐綠廊-起點段"]
        D7(7. 豐原大道) --> Junction{綠廊交接處};
        HB --> Junction;
        Junction --> D5(5. 朴口車站);
        D5 --> HE(200days冰店);
        HE --> D6(6. 豐榮水利碑);
    end

    %% 子圖：石岡精華段
    subgraph Shigang ["石岡精華段"]
        D6 --> D9(9. 石岡水壩);
        D9 -.-> D10(10. 石岡斷層月台);
        D9 --> D11(11. 0蛋月台);
        D11 --> D12(12. 九房3D彩繪村);
        D12 --> D13(13. 石岡旅服中心);
        D13 --> D14(14. 情人木橋);
        D14 -.-> D15(15. 土牛客家館);
    end

    %% 子圖：東勢段
    subgraph Dongshi ["東勢終點段"]
        D14 --> D16(16. 梅子車站);
        D16 --> D17(17. 梅子百年芒果樹);
        D17 --> D18(18. 梅子鐵橋);
        D18 --> D19(19. 東勢客家園區);
    end

    %% 周邊景點
    D8(8. 公老坪) -.-> D7;

    %% 樣式設定
    classDef spot fill:#fff,stroke:#333,stroke-width:2px;
    classDef highlight fill:#fcf,stroke:#f00,stroke-width:2px;
    class H1,H3,H4,D9,D11,D19 highlight;
    class Junction fill:#ff9,stroke:#333,stroke-width:2px,shape:rhombus;
"""

def update_map_metadata():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        # 1. 讀取現有 Meta Data
        cursor.execute("SELECT meta_data FROM walking_maps WHERE map_id = ?", (MAP_ID,))
        row = cursor.fetchone()
        
        if not row:
            print("Map not found!")
            return

        current_metadata = json.loads(row[0])
        
        # 2. 更新 Routes
        current_metadata["routes"]["main_route"] = mermaid_graph
        
        # 3. 寫回 DB
        cursor.execute("UPDATE walking_maps SET meta_data = ? WHERE map_id = ?", 
                       (json.dumps(current_metadata, ensure_ascii=False), MAP_ID))
        
        conn.commit()
        print(f"Map '{MAP_ID}' updated with detailed Mermaid route.")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    update_map_metadata()
