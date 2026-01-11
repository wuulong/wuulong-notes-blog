
import sqlite3
import math
import os
from osgeo import ogr, gdal, osr

# Config
DB_PATH = "events/notes/wuulong-notes-blog/static/walkgis_prj/walkgis.db"
FEATURES_DIR = "events/notes/wuulong-notes-blog/static/walkgis_prj/features"
SHP_PATH = "/Volumes/D2024/QGIS/projects/流域情報開放地圖/2-流域設施與空間發展/1-構造物介紹及功能說明/DIKEGATE-水門位置圖/dikegate.shp"
MAP_ID = "20260111_zhuoshui_facilities"
MATCH_DISTANCE_THRESHOLD_KM = 0.05 # 50 meters tolerance

def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    delta_phi, delta_lambda = math.radians(lat2 - lat1), math.radians(lon2 - lon1)
    a = math.sin(delta_phi/2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c

def parse_wkt_point(wkt):
    # DB WKT is POINT(120.8... 23.7...) i.e. POINT(LON LAT)
    import re
    match = re.search(r"POINT\s*\(\s*([0-9\.]+)\s+([0-9\.]+)\s*\)", wkt)
    if match:
        return float(match.group(2)), float(match.group(1)) # lat, lon
    return None, None

def main():
    # 1. Load SHP features (into memory for fast lookup)
    driver = ogr.GetDriverByName("ESRI Shapefile")
    dataSource = driver.Open(SHP_PATH, 0)
    layer = dataSource.GetLayer()
    
    # Transform to WGS84 for distance comparison
    source_srs = layer.GetSpatialRef()
    target_srs = osr.SpatialReference()
    target_srs.ImportFromEPSG(4326) # WGS84
    # Set Mapping Strategy to ensure Lon, Lat order (Traditional GIS)
    target_srs.SetAxisMappingStrategy(osr.OAMS_TRADITIONAL_GIS_ORDER)
    
    transform = osr.CoordinateTransformation(source_srs, target_srs)
    
    shp_gates = []
    print("Loading SHP data...")
    for feature in layer:
        geom = feature.GetGeometryRef()
        if geom:
            geom.Transform(transform)
            # With OAMS_TRADITIONAL_GIS_ORDER, X should be Lon, Y should be Lat
            lon = geom.GetX()
            lat = geom.GetY()
            
            # Sanity Check for Taiwan (Lat 22-25, Lon 120-122)
            if lat > 100 or lon < 50:
                # Swap if needed (just in case)
                lat, lon = lon, lat
            
            name = feature.GetFieldAsString("NAME")
            milage = feature.GetFieldAsString("MILAGE")
            note = feature.GetFieldAsString("NOTE")
            
            # Construct meaningful name
            new_name = name
            if name == "水門" and milage and milage.strip() != "":
                if "水門" not in milage:
                    new_name = f"{milage} 水門"
                else:
                    new_name = milage
            
            shp_gates.append({
                'name': name,
                'new_name': new_name,
                'lat': lat,
                'lon': lon,
                'note': note
            })
            
    print(f"Loaded {len(shp_gates)} gates from SHP.")

    # 2. Iterate DB features named "水門"
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    query = """
        SELECT f.feature_id, f.name, f.geometry_wkt 
        FROM walking_map_features f
        JOIN walking_map_relations r ON f.feature_id = r.feature_id
        WHERE f.name = '水門' 
        AND r.map_id = ?
    """
    cursor.execute(query, (MAP_ID,))
    db_features = cursor.fetchall()
    
    print(f"Found {len(db_features)} '水門' features in DB to update.")
    
    updates = 0
    for fid, name, wkt in db_features:
        lat, lon = parse_wkt_point(wkt)
        if not lat: continue
        
        # Find closest SHP gate
        nearest_gate = None
        min_dist = float('inf')
        
        for gate in shp_gates:
            dist = haversine(lat, lon, gate['lat'], gate['lon'])
            if dist < min_dist:
                min_dist = dist
                nearest_gate = gate
        
        if nearest_gate and min_dist < MATCH_DISTANCE_THRESHOLD_KM:
            # Match found!
            new_name = nearest_gate['new_name']
            note = nearest_gate['note']
            
            print(f"Updating {fid}: {name} -> {new_name} (Dist: {min_dist*1000:.1f}m)")
            
            # Update DB
            cursor.execute("UPDATE walking_map_features SET name = ?, description = ? WHERE feature_id = ?", 
                           (new_name, f"位置: {note}\n(原始資料 note 欄位)", fid))
            
            # Update Markdown File
            try:
                md_path = os.path.join(FEATURES_DIR, f"{fid}.md")
                if os.path.exists(md_path):
                    with open(md_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                    # Replace Name in frontmatter
                    # Be careful with regex
                    import re
                    # Replace only the first occurrence of name:
                    content = re.sub(r"^name: .*$", f"name: {new_name}", content, count=1, flags=re.MULTILINE)
                    
                    # Append Note
                    if "## 交通指引" not in content:
                        if "## 簡介" in content:
                            content = content.replace("## 簡介", f"## 簡介\n\n(位置資訊: {note})\n")
                        else:
                            content += f"\n\n## 相關資訊\n{note}"
                        
                    with open(md_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                        
                updates += 1
            except Exception as e:
                print(f"Error updating file for {fid}: {e}")

        else:
            print(f"No match for {fid} (Nearest: {min_dist*1000:.1f}m)")

    conn.commit()
    conn.close()
    print(f"Updated {updates} features.")

if __name__ == "__main__":
    main()
