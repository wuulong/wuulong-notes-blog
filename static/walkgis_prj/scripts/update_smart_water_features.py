import os

# Config
BASE_DIR = "../../static/walkgis_prj/features"
SQL_FILE = "../../static/walkgis_prj/sql/insert_smart_water_features.sql"

# Feature Data (ID, Name, Coords, Updated Desc)
FEATURES = [
    {
        "id": "20251229_baileng_intake",
        "name": "白冷圳進水口",
        "coords": [24.2100, 121.0155],
        "desc": "位於天輪發電廠對岸，大甲溪與東卯溪匯流處。這裡是白冷圳的取水源頭，透過地下管線引穿大甲溪底，展現了人定勝天的水利智慧。"
    },
    {
        "id": "20251229_baileng_malipu",
        "name": "白冷圳馬力埔支線",
        "coords": [24.2250, 120.8250],
        "desc": "位於新社馬力埔社區，沿線有著名的彩繪小徑。這條支線不僅灌溉了新社的花海與香菇，更與當地人文景觀深度結合。"
    },
    {
        "id": "20251229_houli_low_head_power",
        "name": "后里圳低落差示範電廠",
        "coords": [24.2980, 120.7350],
        "desc": "全台首座貫流式水輪發電機組，利用后里圳僅 3.6 公尺的落差進行發電。證明了小水力發電在平原灌溉渠道中的巨大潛力。"
    },
    {
        "id": "20251229_zhonghe_gate",
        "name": "忠和中排水截水閘門",
        "coords": [24.2250, 120.5300],
        "desc": "位於龍井區，具備自動化水位監測與控制功能。在防洪與區域排水管理中扮演關鍵角色，是現代化智慧水利的實踐。"
    },
    {
        "id": "20251229_huyan_fuxing",
        "name": "虎眼一圳福興支線",
        "coords": [24.2764, 120.6699],
        "desc": "流經神岡/大雅交界，結合福興生態園區。這裡展現了水利工程與生態保育共存的理念，是觀察水域生態的好去處。"
    },
    {
        "id": "20251229_yuanlin_branch",
        "name": "員林支線",
        "coords": [24.2459, 120.6579],
        "desc": "位於大雅區神林路旁，穿越繁忙的半都會區。見證了農業灌溉渠道如何適應都市化發展，繼續滋潤這片土地。"
    },
    {
        "id": "20251229_taliangou_branch",
        "name": "塔蓮溝支線",
        "coords": [24.2400, 120.6500],
        "desc": "大雅區重要的灌排兼用渠道，近年進行了護岸整治工程，提升了排水效率與安全性。"
    },
    {
        "id": "20251229_huludun_intake",
        "name": "葫蘆墩圳進水口",
        "coords": [24.2790, 120.7448],
        "desc": "位於豐原萬順二街盡頭，是大甲溪水進入台中盆地的第一站。這裡保存了歷史遺跡，也設有現代化的監測設備。"
    }
]

def update_markdown(feature):
    file_path = os.path.join(BASE_DIR, f"{feature['id']}.md")
    
    # Check if file exists
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    # Read content
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update Frontmatter Coordinates
    coord_str = f"coordinate: [{feature['coords'][0]}, {feature['coords'][1]}]"
    if "coordinate:" not in content:
        content = content.replace("tags:", f"{coord_str}\ntags:")
    
    # Update Description (Simple append or replace strategy)
    # We'll regenerate the file content to be safe and clean
    new_content = f"""---
id: {feature['id']}
name: {feature['name']}
type: 水利設施
subtype: 智慧水圳
date: 2025-12-29
{coord_str}
tags: ["智慧水圳玩樂地圖-臺中管理處"]
---

# {feature['name']}

{feature['desc']}

## 基本資訊
*   **座標**: {feature['coords'][0]}, {feature['coords'][1]}
*   **特色**: 智慧監測、生態工法、歷史傳承
"""
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated MD: {feature['id']}")

def generate_sql(features):
    sql_content = "-- Insert Smart Water Features\n"
    # Ensure Layer 3 (or put in 2?) Let's put in Layer 2 (Hydration) but maybe specific subtype
    # We use Layer 2: 水利工程與歷史
    
    sql_content += "INSERT OR REPLACE INTO walking_map_features (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data) VALUES\n"
    
    values = []
    for f in features:
        wkt = f"POINT({f['coords'][1]} {f['coords'][0]})" # Lon Lat
        meta = f'{{"markdown_file": "{f["id"]}.md", "tags": ["智慧水圳"]}}'
        values.append(f"('{f['id']}', '{f['name']}', '{f['desc']}', 2, 'Point', '{wkt}', '{meta}')")
    
    sql_content += ",\n".join(values) + ";"
    
    with open(SQL_FILE, 'w', encoding='utf-8') as f:
        f.write(sql_content)
    print(f"Generated SQL: {SQL_FILE}")

def main():
    # Update Markdowns
    for f in FEATURES:
        update_markdown(f)
    
    # Generate SQL
    generate_sql(FEATURES)

if __name__ == "__main__":
    # Ensure current directory context
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    main()
