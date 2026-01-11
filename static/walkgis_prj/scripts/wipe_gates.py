
import os
import sqlite3
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(SCRIPT_DIR, "../walkgis.db")
FEATURES_DIR = os.path.join(SCRIPT_DIR, "../features")
MAP_ID = "20260111_zhuoshui_facilities"

def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    print("Finding '水門' features to delete...")
    
    # Select features to delete
    cursor.execute("""
        SELECT f.feature_id 
        FROM walking_map_features f
        JOIN walking_map_relations r ON f.feature_id = r.feature_id
        WHERE f.name = '水門' 
        AND r.map_id = ?
    """, (MAP_ID,))
    
    fids_to_delete = [row[0] for row in cursor.fetchall()]
    
    print(f"Found {len(fids_to_delete)} features to delete.")
    
    for fid in fids_to_delete:
        # Delete from DB
        cursor.execute("DELETE FROM walking_map_relations WHERE feature_id = ?", (fid,))
        cursor.execute("DELETE FROM walking_map_features WHERE feature_id = ?", (fid,))
        
        # Delete MD
        md_file = os.path.join(FEATURES_DIR, f"{fid}.md")
        if os.path.exists(md_file):
            try:
                os.remove(md_file)
            except:
                pass
                
    conn.commit()
    conn.close()
    print("Deletion complete.")

if __name__ == "__main__":
    main()
