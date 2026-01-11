
import zipfile
import os
import json
from xml.dom import minidom

KMZ_PATH = "/Users/wuulong/github/bmad-pa/events/notes/data/濁水溪景點設施.kmz"
OUTPUT_JSON = "/Users/wuulong/github/bmad-pa/events/notes/wuulong-notes-blog/static/walkgis_prj/data/20260111_zhuoshui_facilities.json"

def parse_kml(kml_content):
    dom = minidom.parseString(kml_content)
    placemarks = dom.getElementsByTagName("Placemark")
    features = []
    
    for pm in placemarks:
        name_node = pm.getElementsByTagName("name")
        name = name_node[0].firstChild.data if name_node and name_node[0].firstChild else "Unnamed"
        
        desc_node = pm.getElementsByTagName("description")
        desc = desc_node[0].firstChild.data if desc_node and desc_node[0].firstChild else ""
        
        # Check for Point
        point = pm.getElementsByTagName("Point")
        line = pm.getElementsByTagName("LineString")
        
        geometry = None
        geo_type = None
        
        if point:
            coords = point[0].getElementsByTagName("coordinates")[0].firstChild.data.strip()
            # KML is lon,lat,alt. WKT is POINT(lon lat)
            lon, lat, *alt = coords.split(',')
            geometry = f"POINT({lon} {lat})"
            geo_type = "POINT"
        elif line:
            coords_str = line[0].getElementsByTagName("coordinates")[0].firstChild.data.strip()
            # specific processing for lines if needed, but WalkGIS DB mainly uses Points for features currently or WKT.
            # Convert KML coords "lon,lat,alt lon,lat,alt" to WKT "LINESTRING(lon lat, lon lat)"
            pairs = coords_str.split()
            wkt_pairs = []
            for p in pairs:
                parts = p.split(',')
                wkt_pairs.append(f"{parts[0]} {parts[1]}")
            geometry = f"LINESTRING({', '.join(wkt_pairs)})"
            geo_type = "LINESTRING"
            
        if geometry:
            features.append({
                "name": name,
                "description": desc,
                "geometry": geometry,
                "type": geo_type
            })
            
    return features

def main():
    if not os.path.exists(KMZ_PATH):
        print(f"File not found: {KMZ_PATH}")
        return

    try:
        with zipfile.ZipFile(KMZ_PATH, 'r') as z:
            # Find the .kml file inside
            kml_filename = [n for n in z.namelist() if n.endswith('.kml')][0]
            with z.open(kml_filename) as f:
                kml_content = f.read()
                data = parse_kml(kml_content)
                
                # Ensure output directory exists
                os.makedirs(os.path.dirname(OUTPUT_JSON), exist_ok=True)
                
                with open(OUTPUT_JSON, 'w', encoding='utf-8') as json_file:
                    json.dump(data, json_file, indent=2, ensure_ascii=False)
                
                print(f"Successfully extracted {len(data)} features to {OUTPUT_JSON}")
                
    except Exception as e:
        print(f"Error processing KMZ: {e}")

if __name__ == "__main__":
    main()
