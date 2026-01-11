
import os
import sqlite3

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(SCRIPT_DIR, "../walkgis.db")
FEATURES_DIR = os.path.join(SCRIPT_DIR, "../features")

def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    print("WARNING: Deleting ALL '百年舊堤' related features...")
    
    # 1. Identify features to delete
    # Match by layer_id OR by name pattern to catch everything
    cursor.execute("""
        SELECT feature_id FROM walking_map_features 
        WHERE layer_id = (SELECT layer_id FROM layers WHERE layer_type = '百年舊堤')
           OR name LIKE '百年舊堤%'
           OR name LIKE '%%' -- Catch remaining mojibake
    """)
    features_to_delete = [row[0] for row in cursor.fetchall()]
    
    print(f"Found {len(features_to_delete)} features to delete.")
    
    # 2. Delete from DB
    for fid in features_to_delete:
        cursor.execute("DELETE FROM walking_map_relations WHERE feature_id = ?", (fid,))
        cursor.execute("DELETE FROM walking_map_features WHERE feature_id = ?", (fid,))
        
        # 3. Delete MD file
        md_path = os.path.join(FEATURES_DIR, f"{fid}.md")
        if os.path.exists(md_path):
            os.remove(md_path)
            print(f"Deleted MD: {fid}.md")
            
    conn.commit()
    conn.close()
    print("Cleanup complete.")

if __name__ == "__main__":
    main()
