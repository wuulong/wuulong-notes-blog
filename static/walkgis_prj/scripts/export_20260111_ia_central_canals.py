
import sqlite3
import re
import os

# Config
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(SCRIPT_DIR, "../walkgis.db")
MAP_ID = "20260111_ia_central_canals"
MAP_NAME = "農田水利署中區圳路地圖"
OUTPUT_KML = os.path.join(SCRIPT_DIR, f"../maps/{MAP_ID}.kml")

def parse_wkt_point(wkt):
    match = re.search(r"POINT\s*\(\s*([0-9\.]+)\s+([0-9\.]+)\s*\)", wkt)
    if match:
        lon = float(match.group(1))
        lat = float(match.group(2))
        return lat, lon 
    return None, None

def create_kml(features):
    kml_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
  <Document>
    <name>{MAP_NAME}</name>
    <description>彰化、雲林、南投管理處重要圳路設施</description>
"""
    for f in features:
        name = f['name']
        lat, lon = f['coords']
        desc = f['feature_desc']
        
        kml_content += f"""
    <Placemark>
      <name>{name}</name>
      <description>{desc}</description>
      <Point>
        <coordinates>{lon},{lat},0</coordinates>
      </Point>
    </Placemark>"""

    kml_content += """
  </Document>
</kml>"""
    return kml_content

def create_google_maps_link(features):
    base_url = "https://www.google.com/maps/dir/"
    waypoints = []
    
    # Limit to first 20 points
    for f in features[:20]:
        lat, lon = f['coords']
        waypoints.append(f"{lat},{lon}")
        
    full_url = base_url + "/".join(waypoints)
    return full_url

def main():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        query = """
        SELECT f.name, f.description, f.geometry_wkt
        FROM walking_map_features f
        JOIN walking_map_relations r ON f.feature_id = r.feature_id
        WHERE r.map_id = ?
        ORDER BY r.display_order ASC
        """
        
        cursor.execute(query, (MAP_ID,))
        rows = cursor.fetchall()
        
        features = []
        for row in rows:
            lat, lon = parse_wkt_point(row[2])
            if lat and lon:
                features.append({
                    'name': row[0],
                    'feature_desc': row[1],
                    'coords': (lat, lon)
                })
        
        if not features:
            print(f"No features found for map: {MAP_ID}")
            return

        # 1. KML
        kml_data = create_kml(features)
        with open(OUTPUT_KML, "w", encoding="utf-8") as f:
            f.write(kml_data)
        print(f"KML file created at: {OUTPUT_KML}")

        # 2. Google Maps Link
        nav_link = create_google_maps_link(features)
        print("\n=== Google Maps Navigation Link ===")
        print(nav_link)
        print("===================================")

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    main()
