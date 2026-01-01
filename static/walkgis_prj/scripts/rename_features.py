import os
import sqlite3
import re

# Config
BASE_DIR = "events/notes/wuulong-notes-blog/static/walkgis_prj"
FEATURES_DIR = os.path.join(BASE_DIR, "features")
MAPS_DIR = os.path.join(BASE_DIR, "maps")
DB_PATH = os.path.join(BASE_DIR, "walkgis.db")
OLD_PREFIX = "2026_daan_dajia_pipeline_"
NEW_PREFIX = "20260101_daan_dajia_pipeline_"

def rename_features():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Get all files matching the old prefix
    files = [f for f in os.listdir(FEATURES_DIR) if f.startswith(OLD_PREFIX) and f.endswith(".md")]
    
    renamed_map = {} # old_id -> new_id

    for filename in files:
        old_path = os.path.join(FEATURES_DIR, filename)
        new_filename = filename.replace(OLD_PREFIX, NEW_PREFIX)
        new_path = os.path.join(FEATURES_DIR, new_filename)
        
        # 1. Rename File
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} -> {new_filename}")
        
        old_id = filename.replace(".md", "")
        new_id = new_filename.replace(".md", "")
        renamed_map[old_id] = new_id

        # 2. Update Content (Frontmatter ID)
        with open(new_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        new_content = content.replace(f"id: {old_id}", f"id: {new_id}")
        
        with open(new_path, "w", encoding="utf-8") as f:
            f.write(new_content)

    # 3. Update Database
    for old_id, new_id in renamed_map.items():
        # Update features table
        cursor.execute("UPDATE walking_map_features SET feature_id = ? WHERE feature_id = ?", (new_id, old_id))
        # Update relations table
        cursor.execute("UPDATE walking_map_relations SET feature_id = ? WHERE feature_id = ?", (new_id, old_id))
        print(f"DB Updated: {old_id} -> {new_id}")

    conn.commit()
    conn.close()
    return renamed_map

def update_map_file(renamed_map):
    # Only one map file for this task
    map_file = "2026_daan_dajia_pipeline.md"
    map_path = os.path.join(MAPS_DIR, map_file)
    
    if os.path.exists(map_path):
        with open(map_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        for old_id, new_id in renamed_map.items():
            # Update links: ../features/old_id.md -> ../features/new_id.md
            content = content.replace(f"{old_id}.md", f"{new_id}.md")
            
        with open(map_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated Map Links in: {map_path}")
    else:
        print("Map file not found, skipping link update.")

if __name__ == "__main__":
    renamed_map = rename_features()
    update_map_file(renamed_map)
