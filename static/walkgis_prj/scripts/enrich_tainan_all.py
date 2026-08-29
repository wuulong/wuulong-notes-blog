import os
import sqlite3
import json
import datetime

# 路徑設定
BASE_PATH = "."
PROJECT_ROOT = f"{BASE_PATH}/events/notes/wuulong-notes-blog/static/walkgis_prj"
FEATURES_DIR = f"{PROJECT_ROOT}/features"
DB_PATH = f"{PROJECT_ROOT}/walkgis.db"

# 內容字典 (部分示範，可持續擴充)
ENRICHMENT_DATA = {
    "臺南市中西區": {
        "highlights": {
            "歷史": "台南歷史核心，為昔日府城所在地，古蹟密度全台最高。",
            "地理": "位於台南市中心，全台最小行政區，曾是五條港商貿中心。"
        },
        "culture": ["赤崁樓", "台南孔廟", "國立台灣文學館", "林百貨", "神農街"],
        "markets": ["永樂市場", "水仙宮市場", "西市場 (大菜市)"],
        "food": ["牛肉湯", "鱔魚意麵", "鹹粥", "碗粿", "春捲"]
    },
    "臺南市安平區": {
        "highlights": {
            "歷史": "台灣最早開發之地，大航海時代的熱蘭遮城，見證荷、鄭、清歷史。",
            "地理": "位於鹽水溪出海口，擁有安平港與獨特的潟湖地貌。"
        },
        "culture": ["安平古堡", "安平樹屋", "德記洋行", "億載金城", "安平漁人碼頭"],
        "markets": ["安平傳統市場"],
        "food": ["蝦捲", "安平豆花", "蜜餞", "蝦餅", "蚵嗲"]
    },
    "臺南市南區": {
        "highlights": {
            "歷史": "清代稱為「南門外」，擁有全台首學孔廟之外的重要郊區與鹽業地景。",
            "地理": "西臨台灣海峽，擁有黃金海岸及水交社文化園區。"
        },
        "culture": ["水交社文化園區", "黃金海岸", "藍晒圖文創園區"],
        "markets": ["金華市場", "利南市場"],
        "food": ["鹽埕牛肉湯", "老店乾麵", "黃金海岸海鮮"]
    },
    "臺南市北區": {
        "highlights": {
            "歷史": "古稱「鎮北坊」，是府城北方的門戶，擁有多座百年名剎。",
            "地理": "位於市區北部，與永康、安南區相鄰，擁有台南公園。"
        },
        "culture": ["新營太子宮 (分靈)", "大觀音亭", "開基玉皇宮", "台南公園"],
        "markets": ["鴨母寮市場", "和緯市場", "小北觀光夜市"],
        "food": ["葡吉麵包", "松村燻之味", "鴨母寮炭火麵"]
    },
    "臺南市東區": {
        "highlights": {
            "歷史": "日治時期起發展為文教區，擁有成功大學帶動的學術氣息。",
            "地理": "台南市中心東側，地勢略高，發展為高級住宅與商業區。"
        },
        "culture": ["成功大學建築群", "台南文化中心", "巴克禮紀念公園"],
        "markets": ["大東夜市", "復興市場", "崇德市場"],
        "food": ["成大周邊小吃", "勝利早點", "咖啡店聚落"]
    },
    "臺南市安南區": {
        "highlights": {
            "歷史": "古為台江內海，清代因泥沙淤積形成的「海埔新生地」。",
            "地理": "台南面積第二大區，擁有台江國家公園與四草濕地生態。"
        },
        "culture": ["國立臺灣歷史博物館", "正統鹿耳門聖母廟", "四草綠色隧道"],
        "markets": ["本淵寮公有零售市場"],
        "food": ["土魠魚羹", "鮮蚵料理", "在地海鮮"]
    },
    "臺南市永康區": {
        "highlights": {
            "歷史": "早期為平埔族居住地，戰後發展為南台灣重要的工業與居住中心。",
            "地理": "台南市人口最多之區，交通樞紐，與舊市區高度整合。"
        },
        "culture": ["永康總圖館", "永康火車站 (永保安康)"],
        "markets": ["永康公有市場", "尚青市場"],
        "food": ["永康牛肉湯", "三崁店美食", "在地早點"]
    },
    "臺南市七股區": {
        "highlights": {
            "歷史": "以製鹽產業聞名，後轉型為生態旅遊與養殖漁業重鎮。",
            "地理": "位於台南最西端，擁有全台最大的潟湖「七股潟湖」。"
        },
        "culture": ["七股鹽山", "台灣鹽博物館", "黑面琵鷺保護區"],
        "markets": ["七股零售市場"],
        "food": ["鮮蚵料理", "虱目魚粥", "鹹水吳郭魚"]
    },
     "臺南市北門區": {
        "highlights": {
            "歷史": "昔日鹽業重鎮，歷史悠久的南鯤鯓代天府所在地。",
            "地理": "位於北台南海岸線，擁有著名的井仔腳瓦盤鹽田。"
        },
        "culture": ["南鯤鯓代天府", "井仔腳瓦盤鹽田", "水晶教堂"],
        "markets": ["北門零售市場"],
        "food": ["無刺虱目魚", "鹽滷豆花", "海產小吃"]
    },
    "臺南市新營區": {
        "highlights": {
            "歷史": "曾為台南縣治所在地，是溪北地區的政治與經濟中心。",
            "地理": "位於台南北部平原地帶，與後壁、下營接壤。"
        },
        "culture": ["新營文化中心", "天鵝湖公園", "糖鐵五分車"],
        "markets": ["新營第一市場"],
        "food": ["新營豆菜麵", "豆花", "鴨肉羹"]
    },
    "臺南市鹽水區": {
        "highlights": {
            "歷史": "「一府二鹿三艋舺四月津」，曾是重要商港，月津港文化深厚。",
            "地理": "位於台南北端，以每年的鹽水蜂炮聞名全球。"
        },
        "culture": ["月津港園區", "鹽水武廟", "八角樓"],
        "markets": ["鹽水觀光美食城"],
        "food": ["鹽水意麵", "豬頭飯", "雞肉飯"]
    },
    "臺南市麻豆區": {
        "highlights": {
            "歷史": "古為平埔族麻豆社，以產文旦聞名，是溪南重鎮。",
            "地理": "位於台南中心平原地帶，曾有麻豆港對外貿易。"
        },
        "culture": ["總爺藝文中心", "麻豆代天府 (十八地獄)"],
        "markets": ["麻豆公有市場"],
        "food": ["麻豆碗粿", "鱔魚意麵", "當歸鴨"]
    }
}

def update_status(conn, feature_id, status):
    cursor = conn.cursor()
    cursor.execute("SELECT meta_data FROM walking_map_features WHERE feature_id = ?", (feature_id,))
    row = cursor.fetchone()
    if row:
        meta = json.loads(row[0]) if row[0] else {}
        meta['enrichment_status'] = status
        cursor.execute("UPDATE walking_map_features SET meta_data = ? WHERE feature_id = ?", 
                       (json.dumps(meta, ensure_ascii=False), feature_id))

def enrich_file(feature_id, name):
    content_data = ENRICHMENT_DATA.get(name)
    if not content_data:
        # 預設內容 (如果沒有寫在上面的字典裡)
        content_data = {
            "highlights": {
                "歷史": f"{name}的歷史發展與在地故事。",
                "地理": f"{name}的地理位置與環境色。"
            },
            "culture": [f"{name}特色景點"],
            "markets": [f"{name}傳統市場"],
            "food": [f"{name}在地美食"]
        }

    file_path = os.path.join(FEATURES_DIR, f"{feature_id}.md")
    if not os.path.exists(file_path):
        print(f"Skipping {name}: file not found")
        return False

    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # 尋找插入點 (通常在 # {名稱} 之後)
    new_lines = []
    header_found = False
    for line in lines:
        new_lines.append(line)
        if f"# {name}" in line and not header_found:
            header_found = True
            ext_content = f"\n## Highlight 亮點\n"
            ext_content += f"- **歷史**: {content_data['highlights']['歷史']}\n"
            ext_content += f"- **地理**: {content_data['highlights']['地理']}\n\n"
            
            ext_content += "## 🖼️ 文藝展館 (Culture & Arts)\n"
            for item in content_data['culture']:
                ext_content += f"- {item}\n"
            ext_content += "\n"
            
            ext_content += "## 🛒 傳統市場 (Traditional Markets)\n"
            for item in content_data['markets']:
                ext_content += f"- {item}\n"
            ext_content += "\n"
            
            ext_content += "## 🥢 在地美食 (Local Food)\n"
            for item in content_data['food']:
                ext_content += f"- {item}\n"
            
            new_lines.append(ext_content)

    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(new_lines)
    return True

def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # 取得台南所有鄉鎮
    cursor.execute("SELECT feature_id, name FROM walking_map_features WHERE feature_id LIKE 'TOWN_67000%'")
    rows = cursor.fetchall()

    for fid, name in rows:
        print(f"Enriching {name} ({fid})...")
        if enrich_file(fid, name):
            update_status(conn, fid, "AI_ENRICHED")
    
    conn.commit()
    conn.close()
    print("Tainan districts enrichment complete.")

if __name__ == "__main__":
    main()
