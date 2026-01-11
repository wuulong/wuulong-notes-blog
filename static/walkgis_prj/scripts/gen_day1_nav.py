
import sqlite3
import urllib.parse
import re

DB_PATH = "events/notes/wuulong-notes-blog/static/walkgis_prj/walkgis.db"
MAP_ID = "20260111_zhuoshui_facilities"

TARGET_NAMES = [
    "鷺鷥生態景觀公園",
    "麥寮港",
    "拱範宮",
    "詔安客家文化園區"
]

ORDERED_NAMES = [
    "鷺鷥生態景觀公園",
    "麥寮港",
    "拱範宮",
    "詔安客家文化園區"
]

def parse_wkt_point(wkt):
    match = re.search(r"POINT\s*\(\s*([0-9\.]+)\s+([0-9\.]+)\s*\)", wkt)
    if match:
        lon = float(match.group(1))
        lat = float(match.group(2))
        return lat, lon
    return None, None

def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT f.name, f.geometry_wkt 
        FROM walking_map_features f
        JOIN walking_map_relations r ON f.feature_id = r.feature_id
        WHERE r.map_id = ?
    """, (MAP_ID,))
    
    found_coords = {} 
    
    for row in cursor.fetchall():
        name = row[0]
        wkt = row[1]
        
        for target in TARGET_NAMES:
            if target in name: 
                lat, lon = parse_wkt_point(wkt)
                if lat:
                    if target not in found_coords:
                        found_coords[target] = (lat, lon)
                    elif name == target:
                        found_coords[target] = (lat, lon)
    
    waypoints = []
    print("Found coordinates:")
    for name in ORDERED_NAMES:
        if name in found_coords:
            lat, lon = found_coords[name]
            waypoints.append(f"{lat},{lon}")
            print(f" - {name}: {lat}, {lon}")
        else:
            print(f" - {name}: NOT FOUND in DB")
            waypoints.append(urllib.parse.quote(name))

    if waypoints:
        url = "https://www.google.com/maps/dir/" + "/".join(waypoints)
        print("\nGoogle Maps Link:")
        print(url)
    else:
        print("No waypoints found.")

if __name__ == "__main__":
    main()
