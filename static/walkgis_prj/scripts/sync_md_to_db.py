import sqlite3
import os
import json
import re

# 設定路徑
BASE_PATH = "."
PROJECT_ROOT = f"{BASE_PATH}/events/notes/wuulong-notes-blog/static/walkgis_prj"
DB_PATH = f"{PROJECT_ROOT}/walkgis.db"
FEATURES_DIR = f"{PROJECT_ROOT}/features"

def sync_md_to_db():
    if not os.path.exists(DB_PATH):
        print("Database not found.")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 找出所有行政區劃的檔案
    enriched_files = [f for f in os.listdir(FEATURES_DIR) if f.startswith(('TOWN_', 'COUNTY_')) and f.endswith('.md')]

    for filename in enriched_files:
        feature_id = filename.replace('.md', '')
        file_path = os.path.join(FEATURES_DIR, filename)
        
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        # 移除 Frontmatter
        body = re.sub(r'^---.*?---\s*', '', content, flags=re.DOTALL)
        
        # 取得標題後的第一段作為描述 (限制長度以免 DB 過大)
        lines = [l.strip() for l in body.split('\n') if l.strip()]
        if len(lines) > 1:
            # 假設第一行是 # Title
            desc = lines[1] if not lines[1].startswith('#') else lines[2]
            # 截取前 200 字
            desc = (desc[:200] + '...') if len(desc) > 200 else desc
        else:
            desc = "已厚化內容，請查看詳細文件。"

        try:
            cursor.execute("UPDATE walking_map_features SET description = ? WHERE feature_id = ?", (desc, feature_id))
            print(f"Synced {feature_id} description to DB.")
        except Exception as e:
            print(f"Error syncing {feature_id}: {e}")

    conn.commit()
    conn.close()
    print("Sync completed!")

if __name__ == "__main__":
    sync_md_to_db()
