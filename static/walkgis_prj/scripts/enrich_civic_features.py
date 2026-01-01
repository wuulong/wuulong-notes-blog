import os

BASE_DIR = "events/notes/wuulong-notes-blog/static/walkgis_prj/features"
MAP_NAME = "大安大甲溪聯通管工程計畫地圖"

features = {
    "20260101_daan_dajia_pipeline_后里泰安國小.md": {
        "title": "后里泰安國小",
        "lat": 24.3213,
        "lon": 120.7486,
        "content": """# 后里泰安國小

位於泰安鐵道文化園區旁，是本計畫重要的**環境教育合作夥伴**。

## 公民參與實績
*   **水資源環教活動**：2025年3月，全校百餘名師生參與了由中區水資源分署舉辦的活動。學生透過有獎徵答，深入認識了「大安大甲溪聯通管」對穩定台中供水的意義。
*   **社區連結**：學校作為社區核心，協助將艱澀的工程知識轉化為淺顯易懂的環教課程，連結了工程與在地生活。"""
    },
    "20260101_daan_dajia_pipeline_苗栗鯉魚潭國小.md": {
        "title": "苗栗鯉魚潭國小",
        "lat": 24.3418,
        "lon": 120.7766,
        "content": """# 苗栗鯉魚潭國小

座落於鯉魚潭水庫旁，是推動水資源與生態教育的**示範基地**。

## 環境教育聯盟
*   **看見台灣**：加入「看見．齊柏林基金會」校園環境教育計畫，引導學生以鳥瞰視角守護家鄉水資源。
*   **水庫環教**：積極參與中區水資分署推動的鯉魚潭水庫環教課程，利用地利之便，將水庫變成最生動的自然教室。"""
    },
    "20260101_daan_dajia_pipeline_經濟部水利署中區水資源分署.md": {
        "title": "經濟部水利署中區水資源分署",
        "lat": 24.0489,
        "lon": 120.6925,
        "content": """# 經濟部水利署中區水資源分署

本計畫的執行機關，更是推動**公民參與**與**公私協力**的核心推手。

## 公民溝通
*   **教育推廣**：主動走入校園（如后里泰安國小、鯉魚潭國小），舉辦水資源環境教育，向下扎根。
*   **地方共好**：在推動重大工程（如聯通管計畫）的同時，積極與地方里民溝通，感謝地方支持，並致力於降低工程對社區的影響，展現了公共工程與在地共存的努力。"""
    }
}

for filename, data in features.items():
    filepath = os.path.join(BASE_DIR, filename)
    if os.path.exists(filepath):
        file_content = f"""---
id: {filename.replace('.md', '')}
title: {data['title']}
tags: [{MAP_NAME}, 水利設施]
coordinate: [{data['lat']}, {data['lon']}]
---
{data['content']}

## 地理資訊
*   緯度: {data['lat']}
*   經度: {data['lon']}
"""
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(file_content)
        print(f"Civic Enriched: {filepath}")
    else:
        print(f"Skipping: {filepath}")
