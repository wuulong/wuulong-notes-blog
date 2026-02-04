import sqlite3
import os
import datetime
import json

# 路徑設定
BASE_PATH = "/Users/wuulong/github/bmad-pa"
PROJECT_ROOT = f"{BASE_PATH}/events/notes/wuulong-notes-blog/static/walkgis_prj"
DB_PATH = f"{PROJECT_ROOT}/walkgis.db"
MAP_FILE = f"{PROJECT_ROOT}/maps/taiwan_admin_enrichment.md"

def generate_mermaid():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT feature_id, name FROM walking_map_features WHERE feature_id LIKE 'COUNTY_%'")
    counties = {row[1]: row[0] for row in cursor.fetchall()}
    conn.close()

    # 定義分組
    six_cities = ["臺北市", "新北市", "桃園市", "臺中市", "臺南市", "高雄市"]
    islands = ["金門縣", "連江縣", "澎湖縣"]
    others = [c for c in counties.keys() if c not in six_cities and c not in islands]

    mermaid = "```mermaid\ngraph TD\n"
    mermaid += "    ROOT[鄉鎮導航] --> SIX[六都]\n"
    mermaid += "    ROOT --> MAIN[一般縣市]\n"
    mermaid += "    ROOT --> ISL[離島地區]\n\n"

    for name in six_cities:
        if name in counties:
            safe_id = counties[name].split('_')[1]
            mermaid += f"    SIX --> {safe_id}({name})\n"
            mermaid += f"    click {safe_id} \"?map=taiwan_admin_enrichment&feature={counties[name]}\"\n"

    for name in sorted(others):
        if name in counties:
            safe_id = counties[name].split('_')[1]
            mermaid += f"    MAIN --> {safe_id}({name})\n"
            mermaid += f"    click {safe_id} \"?map=taiwan_admin_enrichment&feature={counties[name]}\"\n"

    for name in islands:
        if name in counties:
            safe_id = counties[name].split('_')[1]
            mermaid += f"    ISL --> {safe_id}({name})\n"
            mermaid += f"    click {safe_id} \"?map=taiwan_admin_enrichment&feature={counties[name]}\"\n"

    mermaid += "```"
    return mermaid

def generate_status_table():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT feature_id, name, json_extract(meta_data, '$.enrichment_status') as status 
        FROM walking_map_features 
        WHERE feature_id LIKE 'COUNTY_%' 
        ORDER BY 
            CASE WHEN status = 'DEEP_RESEARCHED' THEN 1 
                 WHEN status = 'AI_ENRICHED' THEN 2 
                 ELSE 3 END, 
            name ASC
    """)
    counties = cursor.fetchall()

    table = "| 縣市 | 狀態 | 鄉鎮進度 |\n| :--- | :--- | :--- |\n"
    
    for fid, name, status in counties:
        county_prefix = fid.split('_')[1]
        cursor.execute("""
            SELECT 
                COUNT(*) as total,
                SUM(CASE WHEN json_extract(meta_data, '$.enrichment_status') != 'DEFAULT' AND json_extract(meta_data, '$.enrichment_status') IS NOT NULL THEN 1 ELSE 0 END) as enriched
            FROM walking_map_features 
            WHERE feature_id LIKE ?""", (f'TOWN_{county_prefix}%',))
        total, enriched = cursor.fetchone()
        
        status_label = f"`{status}`" if status else "`DEFAULT`"
        link_name = f"[{name}](?map=taiwan_admin_enrichment&feature={fid})"
        table += f"| {link_name} | {status_label} | {enriched}/{total} |\n"
    
    conn.close()
    return table

def update_map_file():
    mermaid_content = generate_mermaid()
    status_table = generate_status_table()
    today = datetime.date.today()
    
    content = f"""---
map_id: taiwan_admin_enrichment
name: 鄉鎮導航
region: 台灣
date: {today}
---

# 鄉鎮導航

本提圖旨在管理全台灣所有縣市與鄉鎮的「內容富化 (Enrichment)」進度。

## 📊 富化現況總覽 (Enrichment Roadmap)

{status_table}

## 🗺️ 鄉鎮導航 (Mermaid 導覽)

{mermaid_content}

## 📌 富化進度說明
- **DEFAULT**: 初始匯入 (已完成全台框架與幾何邊界)
- **AI_ENRICHED**: 標準 AI 搜尋厚化 (已初步建立亮點、市場、美食資訊)
- **DEEP_RESEARCHED**: 深度研究整合 (已整合文史研究、產業脈絡之長篇內容)
- **VERIFIED**: 人工完成校驗 (最終確認內容無誤)
"""
    with open(MAP_FILE, "w", encoding="utf-8") as f:
        f.write(content)
    print("Map navigation and status table updated.")

if __name__ == "__main__":
    update_map_file()
