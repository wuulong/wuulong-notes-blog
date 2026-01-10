
import sqlite3
import os
import glob

# Config
OLD_PREFIX = "2026_zhuoshui_river"
NEW_PREFIX = "20260111_zhuoshui_river"
# Map ID is also likely changing if the prefix was the Map ID
OLD_MAP_ID = "2026_zhuoshui_river"
NEW_MAP_ID = "20260111_zhuoshui_river"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FEATURES_DIR = os.path.join(BASE_DIR, "../features")
MAPS_DIR = os.path.join(BASE_DIR, "../maps")
DB_PATH = os.path.join(BASE_DIR, "../walkgis.db")

def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    print(f"Migrating from {OLD_PREFIX} to {NEW_PREFIX}...")

    # 1. Update Walking Maps Table
    print("Updating Map ID in DB...")
    cursor.execute("UPDATE walking_maps SET map_id = ? WHERE map_id = ?", (NEW_MAP_ID, OLD_MAP_ID))
    
    # 2. Update Feature IDs in DB (walking_map_features)
    print("Updating Feature IDs in DB...")
    # Select all features with old prefix
    cursor.execute("SELECT feature_id, name FROM walking_map_features WHERE feature_id LIKE ?", (f"{OLD_PREFIX}%",))
    rows = cursor.fetchall()

    files_moved = 0
    
    for row in rows:
        old_fid = row[0]
        name = row[1]
        new_fid = old_fid.replace(OLD_PREFIX, NEW_PREFIX, 1)
        
        # Update Features table
        cursor.execute("UPDATE walking_map_features SET feature_id = ? WHERE feature_id = ?", (new_fid, old_fid))
        
        # Update Relations table
        cursor.execute("UPDATE walking_map_relations SET map_id = ?, feature_id = ? WHERE map_id = ? AND feature_id = ?", 
                       (NEW_MAP_ID, new_fid, OLD_MAP_ID, old_fid))

        # Rename MD File
        old_path = os.path.join(FEATURES_DIR, f"{old_fid}.md")
        new_path = os.path.join(FEATURES_DIR, f"{new_fid}.md")
        
        if os.path.exists(old_path):
            # Update content (ID in frontmatter)
            with open(old_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = content.replace(f"id: {old_fid}", f"id: {new_fid}")
            
            with open(new_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
                
            os.remove(old_path)
            files_moved += 1
            print(f"Moved: {old_fid} -> {new_fid}")
        else:
            print(f"Warning: File not found {old_path}")

    # 3. Rename Map File
    old_map_file = os.path.join(MAPS_DIR, f"{OLD_MAP_ID}.md")
    new_map_file = os.path.join(MAPS_DIR, f"{NEW_MAP_ID}.md")
    
    if os.path.exists(old_map_file):
        with open(old_map_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Update map ID and links
        content = content.replace(f"id: {OLD_MAP_ID}", f"id: {NEW_MAP_ID}")
        content = content.replace(f"../features/{OLD_PREFIX}", f"../features/{NEW_PREFIX}")
        
        with open(new_map_file, 'w', encoding='utf-8') as f:
            f.write(content)
        os.remove(old_map_file)
        print(f"Updated Map MD: {NEW_MAP_ID}.md")
    
    conn.commit()
    conn.close()
    print(f"Done. {files_moved} feature files renamed.")

if __name__ == "__main__":
    main()
