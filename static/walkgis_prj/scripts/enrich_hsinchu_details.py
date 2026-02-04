import os

# 設定路徑
BASE_PATH = "/Users/wuulong/github/bmad-pa"
FEATURES_DIR = f"{BASE_PATH}/events/notes/wuulong-notes-blog/static/walkgis_prj/features"

hsinchu_data = {
    "COUNTY_10018_新竹市.md": {
        "title": "新竹市 (Hsinchu City)",
        "intro": "古稱「竹塹」，是台灣高科技產業重鎮，素有「風城」之稱。擁有深厚的歷史底蘊（如 1718 年開墾紀錄）與領先全球的新竹科學園區。",
        "highlights": [
            "**三大傳統產業**: 米粉、摃丸、玻璃（因強風與高品質矽砂資源而發達）。",
            "**文化地標**: 新竹火車站（國定古蹟）、都城隍廟（全台地位最高）。",
            "**地理景觀**: 背山面海，擁有頭前溪沖積平原與獨特的畚箕地形。"
        ],
        "food": [
            "**新竹米粉**: 咬勁十足，適合炒或煮湯。",
            "**新竹摃丸**: 口感Q彈，以純豬肉手工搥打聞名。",
            "**水蒸蛋糕**: 傳統工法製作，口感綿密不油膩。"
        ],
        "culture": ["玻璃工藝博物館", "新竹市美術館", "眷村博物館"],
        "market": ["東門市場", "中央市場", "竹蓮市場"]
    },
    "TOWN_10018010_新竹市東區.md": {
        "title": "新竹市東區",
        "intro": "新竹都會區的核心精華區，集結了歷史古蹟、頂尖大學（清大、交大）以及高科技搖籃「新竹科學園區」。",
        "highlights": [
            "**新竹科學園區**: 台灣半導體產業基地，帶動地區高度都市化與高所得人口。",
            "**新竹公園與動物園**: 全台原址最老的動物園與規模最大的都會公園。",
            "**購物中心**: 遠東巨城 (Big City) 及新竹火車站周邊商圈。"
        ],
        "food": [
            "**原夜市鴨肉麵**: 新竹代表性鴨肉美食，湯頭濃育。",
            "**東門文昌雞飯**: 東門圓環旁的超人氣排隊名店。",
            "**阿婆早餐麵店**: 以超大份量蛋餅與川味炒手麵聞名新竹高中學子。"
        ],
        "culture": [
            "**新竹市玻璃工藝博物館**: 結合歷史建築與在地產業特色的藝文空間。",
            "**下竹町 (南大路警察宿舍)**: 修復後的日式宿舍，現為文創新據點。",
            "**241藝術空間**: 位於社福大樓內，主打科技與現代藝術結合。"
        ],
        "market": [
            "**東門市場**: 百年市場活化典範，夜晚轉變為創意美食匯聚地。",
            "**竹蓮市場**: 擁有冷氣與現代化設備，是在地人的民生核心。"
        ]
    },
    "TOWN_10018020_新竹市北區.md": {
        "title": "新竹市北區",
        "intro": "新竹市行政中心所在地，擁有清代淡水廳城的舊城區遺風，並擁有壯闊的十七公里海岸線。",
        "highlights": [
            "**都城隍廟**: 建於 1748 年，是新竹最重要的信仰中心與美食集散地。",
            "**南寮漁港**: 擁有地中海風格建築，是 17 公里海岸線自行車道的起點。",
            "**北門大街**: 保留清末民初古建築（進士第、鄭氏家廟），歷史氣息濃厚。"
        ],
        "food": [
            "**黑貓包**: 北門街百年老店，內餡紮實多汁。",
            "**郭家潤餅**: 城隍廟旁料多實在的高人氣傳統點心。"
        ],
        "culture": [
            "**新竹市眷村博物館**: 全台首座眷村博物館，展示濃厚的移民文化生活史。",
            "**消防博物館**: 原為新竹市消防局，現展示古董消防車與防火知識。",
            "**影像博物館 (有樂館)**: 融合古蹟與演藝空間，是台灣首座有冷氣的戲院。"
        ],
        "market": [
            "**中央市場**: 位居核心商圈，內藏多種老饕級的古早味熟食。",
            "**北門市場**: 結合文青風格與傳統買賣的特色空間。",
            "**波光市集**: 南寮漁港旁的設計感露天市集，觀賞夕陽的好去處。"
        ]
    },
    "TOWN_10018030_新竹市香山區.md": {
        "title": "新竹市香山區",
        "intro": "以自然生態、濕地景觀與傳統工業轉型為特色，是新竹市的後花園。",
        "highlights": [
            "**香山濕地**: 北台灣最大濕地生態保護區，招潮蟹與彈塗魚豐富。",
            "**豎琴橋**: 十七公里海岸線上著名的絕美夕陽攝影點。",
            "**青青草原**: 擁有北台灣最長的磨石子溜滑梯，親子休閒首選。"
        ],
        "food": [
            "**鷹王肉圓**: 隱藏在空軍基地旁的排隊肉圓，紅糟內餡香氣足。",
            "**老街碗粿**: 香山老街一甲子的傳統美味，米香濃郁。"
        ],
        "culture": [
            "**老鍋米粉博物館**: 體驗米粉製作工法，了解在地食農文化。",
            "**春池綠能玻璃觀光工廠**: 見證廢玻璃回收轉化為藝術品的環保工藝。",
            "**香山濕地海洋保育教育中心**: 提供跨領域的自然生態導覽與教育。"
        ],
        "market": [
            "**香山傳統市場 (大庄商圈)**: 在地居民採買新鮮食材與品嚐平價小吃的地方。"
        ]
    }
}

def enrich_files():
    for filename, info in hsinchu_data.items():
        file_path = os.path.join(FEATURES_DIR, filename)
        if not os.path.exists(file_path):
            print(f"Skipping {filename}: File not found.")
            continue
            
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            
        # 尋找 Frontmatter 結束位置 (第二個 ---)
        count = 0
        fm_end_idx = 0
        for i, line in enumerate(lines):
            if line.strip() == "---":
                count += 1
            if count == 2:
                fm_end_idx = i
                break
        
        frontmatter = lines[:fm_end_idx + 1]
        
        # 組合新內容
        content = [
            f"\n# {info['title']}\n\n",
            f"{info['intro']}\n\n",
            "## Highlight 亮點\n\n",
            "\n".join([f"- {h}" for h in info['highlights']]) + "\n\n",
            "## 🖼️ 文藝展館 (Culture & Arts)\n\n",
            "\n".join([f"- {c}" for c in info['culture']]) + "\n\n",
            "## 🛒 傳統市場 (Traditional Markets)\n\n",
            "\n".join([f"- {m}" for m in info['market']]) + "\n\n",
            "## 🥢 在地美食 (Local Food)\n\n",
            "\n".join([f"- {f}" for f in info['food']]) + "\n\n"
        ]
        
        # 如果是縣市，保留原本的鄉鎮列表內容
        towns_list = []
        in_towns_section = False
        for line in lines[fm_end_idx + 1:]:
            if "## 所轄鄉鎮" in line:
                in_towns_section = True
            if in_towns_section:
                towns_list.append(line)
        
        final_content = frontmatter + content + towns_list
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(final_content)
        print(f"Enriched: {filename}")
        
        # 如果是縣市，保留原本的鄉鎮列表內容
        towns_list = []
        in_towns_section = False
        for line in lines[fm_end_idx + 1:]:
            if "## 所轄鄉鎮" in line:
                in_towns_section = True
            if in_towns_section:
                towns_list.append(line)
        
        final_content = frontmatter + content + towns_list
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(final_content)
        print(f"Enriched: {filename}")

if __name__ == "__main__":
    enrich_files()
