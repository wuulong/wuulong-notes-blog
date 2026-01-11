
import sqlite3
import math
import os

DB_PATH = "events/notes/wuulong-notes-blog/static/walkgis_prj/walkgis.db"
FEATURES_DIR = "events/notes/wuulong-notes-blog/static/walkgis_prj/features"
DUPLICATION_THRESHOLD_KM = 0.015  # 15 meters

def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    delta_phi, delta_lambda = math.radians(lat2 - lat1), math.radians(lon2 - lon1)
    a = math.sin(delta_phi/2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c

def parse_wkt_point(wkt):
    import re
    match = re.search(r"POINT\s*\(\s*([0-9\.]+)\s+([0-9\.]+)\s*\)", wkt)
    if match:
        return float(match.group(2)), float(match.group(1)) # lat, lon
    return None, None

def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    print("Finding duplicates...")
    
    # 1. Get all features for this map (using JOIN)
    cursor.execute("""
        SELECT f.feature_id, f.name, f.geometry_wkt 
        FROM walking_map_features f
        JOIN walking_map_relations r ON f.feature_id = r.feature_id
        WHERE r.map_id = '20260111_zhuoshui_facilities' 
        AND f.geometry_type = 'POINT'
    """)
    features = []
    for row in cursor.fetchall():
        lat, lon = parse_wkt_point(row[2])
        if lat and lon:
            features.append({'id': row[0], 'name': row[1], 'lat': lat, 'lon': lon})
            
    # 2. Identify duplicates
    to_delete = []
    seen = []
    
    for f in features:
        is_duplicate = False
        for s in seen:
            if f['name'] == s['name']: # Same name
                dist = haversine(f['lat'], f['lon'], s['lat'], s['lon'])
                if dist < DUPLICATION_THRESHOLD_KM:
                    # It's a duplicate! Keep the first one (s), delete this one (f)
                    print(f"Duplicate found: {f['name']} ({f['id']}) is {dist*1000:.1f}m from ({s['id']})")
                    to_delete.append(f['id'])
                    is_duplicate = True
                    break
        
        if not is_duplicate:
            seen.append(f)
            
    print(f"Found {len(to_delete)} duplicates to delete.")
    
    # 3. Delete
    for fid in to_delete:
        cursor.execute("DELETE FROM walking_map_relations WHERE feature_id = ?", (fid,))
        cursor.execute("DELETE FROM walking_map_features WHERE feature_id = ?", (fid,))
        
        md_path = os.path.join(FEATURES_DIR, f"{fid}.md")
        if os.path.exists(md_path):
            try:
                os.remove(md_path)
            except OSError as e:
                print(f"Error removing {md_path}: {e}")
            
    conn.commit()
    conn.close()
    
    print("Cleanup complete.")

if __name__ == "__main__":
    main()
