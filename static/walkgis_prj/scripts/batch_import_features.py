import sqlite3
import os
import datetime

# 設定專案根目錄 (相對於腳本執行位置)
PROJECT_ROOT = "events/notes/walkgis_prj"
DB_PATH = f"{PROJECT_ROOT}/walkgis.db"
FEATURES_DIR = f"{PROJECT_ROOT}/features"

# 確保目錄存在
os.makedirs(FEATURES_DIR, exist_ok=True)

# 今天的日期前綴
TODAY = datetime.date.today().strftime("%Y%m%d")

# 景點資料清單 (Source Data)
# 格式: (Short_ID, Name, Lat, Lon, Description, Layer_Subtype)
# Layer_ID 假設: 1=水文/親水(預設), 2=文化/歷史, 3=交通/設施, 4=景觀/休憩
# 這裡先簡化，全部暫時設為 Layer_ID=1，之後可再細分
scenic_spots = [
    ("houli_ranch", "后里馬場", 24.298637, 120.73582, "后豐鐵馬道起點，歷史悠久的馬場。", "景點"),
    ("couple_tree", "夫妻樹", 24.29100, 120.73600, "后豐鐵馬道著名地標，兩棵老樹相依。", "景點"),
    ("tunnel_9", "九號隧道", 24.28950, 120.73663, "舊山線最長隧道，全長1.2公里，夏日涼爽。", "歷史建築"),
    ("old_beam_bridge", "花樑鋼橋", 24.28055, 120.74583, "橫跨大甲溪的壯觀鋼桁架橋，舊山線遺跡。", "歷史建築"),
    ("pukou_station", "朴口車站", 24.27139, 120.74611, "東豐綠廊舊車站遺跡。", "歷史建築"),
    ("fengrong_stele", "豐榮水利碑", 24.27805, 120.76111, "見證葫蘆墩圳歷史的水利紀念碑。", "歷史建築"),
    ("fengyuan_blvd_bike", "豐原大道自行車道", 24.28000, 120.73000, "環繞豐原市區的自行車道系統。", "交通設施"), # 示意座標
    ("kunglaoping", "公老坪", 24.26352, 120.75359, "豐原著名賞夜景與觀景地點。", "景點"),
    ("shigang_dam", "石岡水壩", 24.28138, 120.76916, "大甲溪重要水利設施，921地震地景保留地。", "水利設施"),
    ("shigang_fault", "石岡斷層月台", 24.28222, 120.77000, "見證921地震威力的斷層錯動月台遺跡。", "歷史建築"),
    ("0_dan_platform", "0蛋月台", 24.27636, 120.77798, "舊名零擔月台，現保留火車車廂供拍照。", "景點"),
    ("jiufang_3d", "九房3D彩繪村", 24.27600, 120.77900, "以童話故事為主題的3D彩繪社區。", "景點"),
    ("shigang_visitor", "石岡旅客服務中心", 24.27603, 120.77890, "提供旅遊諮詢，亦是自行車補給站。", "服務設施"),
    ("lovers_bridge", "情人木橋", 24.27100, 120.78500, "遠東最長景觀膠合木橋，跨越食水嵙溪。", "景點"),
    ("tuniu_hakka", "石岡土牛客家文化館", 24.26525, 120.80955, "展示大埔客家文化的重要館舍。", "文化設施"),
    ("meizi_station", "梅子車站", 24.27166, 120.80638, "東豐綠廊懷舊車站之一。", "歷史建築"),
    ("meizi_mango", "梅子百年芒果樹", 24.27555, 120.80444, "樹齡數百年的珍貴老樹，旁有土地公廟。", "自然景觀"),
    ("meizi_iron_bridge", "梅子鐵橋", 24.27200, 120.80600, "跨越東勢與石岡的鐵橋。", "歷史建築"),
    ("dongshi_hakka", "東勢客家文化園區", 24.25769, 120.83200, "由舊東勢車站改建，東豐綠廊終點。", "文化設施"),
    ("camphor_platform", "樟樹平台", 24.29000, 120.73600, "夫妻樹附近的大樟樹休憩平台。", "休憩設施"),
    ("winery", "鐵道之鄉酒莊", 24.27857, 120.74568, "結合鐵道文化與品酒的休閒酒莊。", "商店"),
    ("rongting_grocery", "榮町雜貨店", 24.27860, 120.74570, "充滿懷舊氛圍的柑仔店 (座標參考酒莊附近)。", "商店"),
    ("greenway_junction", "綠廊交接處", 24.28000, 120.74000, "后豐鐵馬道與東豐綠廊的交會點。", "交通設施"), # 示意座標
    ("200_days_ice", "200days冰店", 24.27850, 120.74560, "純白玻璃屋網美冰店 (座標參考朴子街)。", "商店")
]

def generate_markdown(feature_id, name, lat, lon, description, subtype):
    content = f"""---
id: {feature_id}
name: {name}
type: 自行車道景點
subtype: {subtype}
date: {datetime.date.today()}
---

# {name}

**地點**：台中市 (Houfeng/Dongfeng Bike Path)
**座標**：{lon}, {lat}

## 簡介
{description}

## 交通資訊
位於自行車道沿線。
"""
    filename = f"{FEATURES_DIR}/{feature_id}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    return filename

def insert_to_db(feature_id, name, lat, lon, description):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # 幾何 WKT
    geometry_wkt = f"POINT({lon} {lat})"
    
    # Meta Data
    meta_data = f'{{"ref_doc": "features/{feature_id}.md", "generated_by": "batch_import"}}'

    try:
        cursor.execute("""
            INSERT OR REPLACE INTO walking_map_features 
            (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data) 
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (feature_id, name, description, 1, 'Point', geometry_wkt, meta_data))
        conn.commit()
    except Exception as e:
        print(f"Error inserting {name}: {e}")
    finally:
        conn.close()

def main():
    print(f"Starting batch import for {len(scenic_spots)} spots...")
    
    for short_id, name, lat, lon, desc, subtype in scenic_spots:
        feature_id = f"{TODAY}_{short_id}"
        
        # 1. 生成 Markdown
        md_file = generate_markdown(feature_id, name, lat, lon, desc, subtype)
        print(f"Generated: {md_file}")
        
        # 2. 寫入 DB
        insert_to_db(feature_id, name, lat, lon, desc)
        print(f"Inserted to DB: {name}")

    print("Batch import completed successfully!")

if __name__ == "__main__":
    main()
