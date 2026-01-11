
import os
import sqlite3

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(SCRIPT_DIR, "../walkgis.db")
FEATURES_DIR = os.path.join(SCRIPT_DIR, "../features")

def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    print("Deleting features with IDs matching garbled patterns from KMZ import...")
    
    # These IDs look like '20260111_zhuoshui_facilities_377_鞎僕'
    # The common pattern is they came from the original JSON import where names were garbage.
    # We can detect them by checking if the ID contains non-standard characters or just by the index range if known.
    # But safer to check for PUA characters in the ID itself.
    
    cursor.execute("SELECT feature_id FROM walking_map_features")
    all_fids = [row[0] for row in cursor.fetchall()]
    
    deleted_count = 0
    for fid in all_fids:
        # Check for PUA characters in the FID string
        is_garbage = False
        for char in fid:
            if 0xE000 <= ord(char) <= 0xF8FF:
                is_garbage = True
                break
        
        if is_garbage:
            cursor.execute("DELETE FROM walking_map_relations WHERE feature_id = ?", (fid,))
            cursor.execute("DELETE FROM walking_map_features WHERE feature_id = ?", (fid,))
            
            md_path = os.path.join(FEATURES_DIR, f"{fid}.md")
            if os.path.exists(md_path):
                os.remove(md_path)
            deleted_count += 1
            
    conn.commit()
    conn.close()
    print(f"Deleted {deleted_count} garbled features.")

if __name__ == "__main__":
    main()
