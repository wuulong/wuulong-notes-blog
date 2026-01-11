
import sqlite3
import math

DB_PATH = "events/notes/wuulong-notes-blog/static/walkgis_prj/walkgis.db"

# Xiluo Township Office Coordinates (Approximate based on known location)
XILUO_OFFICE_LAT = 23.7937
XILUO_OFFICE_LON = 120.4571

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius in kilometers
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    
    a = math.sin(delta_phi/2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c

def parse_wkt_point(wkt):
    # Basic WKT Point parser: POINT (lon lat) or POINT(lon lat)
    import re
    match = re.search(r"POINT\s*\(\s*([0-9\.]+)\s+([0-9\.]+)\s*\)", wkt)
    if match:
        return float(match.group(2)), float(match.group(1)) # lat, lon
    return None, None

def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Query all Point features
    cursor.execute("""
        SELECT name, geometry_wkt 
        FROM walking_map_features 
        WHERE geometry_type = 'POINT'
    """)
    
    nearest_dist = float('inf')
    nearest_name = None
    
    results = []
    
    for row in cursor.fetchall():
        name, wkt = row
        lat, lon = parse_wkt_point(wkt)
        
        if lat is None or lon is None:
            continue
            
        dist = haversine(XILUO_OFFICE_LAT, XILUO_OFFICE_LON, lat, lon)
        results.append((name, dist))
        
    results.sort(key=lambda x: x[1])
    
    print(f"Location: 西螺鄉公所 (Lat: {XILUO_OFFICE_LAT}, Lon: {XILUO_OFFICE_LON})")
    print("\nNearest WalkGIS Features:")
    for name, dist in results[:10]:
        print(f" - {name}: {dist:.2f} km")

if __name__ == "__main__":
    main()
