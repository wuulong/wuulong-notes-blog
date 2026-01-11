
import sqlite3
import math
import os
from osgeo import ogr, gdal, osr

# Config
DB_PATH = "events/notes/wuulong-notes-blog/static/walkgis_prj/walkgis.db"
FEATURES_DIR = "events/notes/wuulong-notes-blog/static/walkgis_prj/features"
# Correct SHP path
SHP_PATH = "/Volumes/D2024/QGIS/projects/流域情報開放地圖/2-流域設施與空間發展/1-構造物介紹及功能說明/DIKEGATE-水門位置圖/dikegate.shp"
MAP_ID = "20260111_zhuoshui_facilities"
# We need to filter for Zhuoshui Basin 
# Looking at ogrinfo output: BASIN_NO (Integer) = 1140 (Danshui), Zhuoshui is 1510.
TARGET_BASIN_NO = 1510

def parse_wkt_point(wkt):
    import re
    match = re.search(r"POINT\s*\(\s*([0-9\.]+)\s+([0-9\.]+)\s*\)", wkt)
    if match:
        return float(match.group(2)), float(match.group(1)) # lat, lon
    return None, None

def get_or_create_layer(cursor, layer_type, description=""):
    cursor.execute("SELECT layer_id FROM layers WHERE layer_type = ?", (layer_type,))
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        cursor.execute("INSERT INTO layers (layer_type, description) VALUES (?, ?)", (layer_type, description))
        return cursor.lastrowid

def main():
    # 1. Load SHP features 
    driver = ogr.GetDriverByName("ESRI Shapefile")
    dataSource = driver.Open(SHP_PATH, 0)
    layer = dataSource.GetLayer()
    
    # Transform to WGS84 
    source_srs = layer.GetSpatialRef()
    target_srs = osr.SpatialReference()
    target_srs.ImportFromEPSG(4326) # WGS84
    target_srs.SetAxisMappingStrategy(osr.OAMS_TRADITIONAL_GIS_ORDER) # Lon, Lat
    transform = osr.CoordinateTransformation(source_srs, target_srs)
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    layer_id = get_or_create_layer(cursor, "濁水溪_水利", "水門與水利設施")
    
    cnt = 0
    print("Importing gates...")
    for feature in layer:
        # Filter by Basin
        basin_no = feature.GetFieldAsInteger("BASIN_NO")
        if basin_no != TARGET_BASIN_NO:
            continue
            
        geom = feature.GetGeometryRef()
        if geom:
            geom.Transform(transform)
            lon = geom.GetX()
            lat = geom.GetY()
            
            # Sanity Check
            if lat > 100 or lon < 50: lat, lon = lon, lat
            
            wkt = f"POINT({lon} {lat})"
            
            name = feature.GetFieldAsString("NAME")
            milage = feature.GetFieldAsString("MILAGE")
            note = feature.GetFieldAsString("NOTE")
            manage_sys = feature.GetFieldAsString("USE") # e.g. 手動/電動
            
            # Smart Naming Logic
            display_name = name
            if name == "水門":
                if milage and milage.strip():
                    if "水門" in milage:
                        display_name = milage
                    else:
                        display_name = f"{milage} 水門"
                else:
                    display_name = f"濁水溪水門_{cnt}"
            
            # Feature ID
            fid = f"{MAP_ID}_gate_{str(cnt).zfill(3)}_{display_name.replace(' ', '_').replace('+', '_' )}"
            
            # Insert DB
            try:
                cursor.execute("""
                    INSERT OR REPLACE INTO walking_map_features 
                    (feature_id, name, description, layer_id, geometry_type, geometry_wkt) 
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (fid, display_name, f"位置: {note}\n操作方式: {manage_sys}", layer_id, "POINT", wkt))
                
                cursor.execute("INSERT OR REPLACE INTO walking_map_relations (map_id, feature_id, display_order) VALUES (?, ?, ?)",
                            (MAP_ID, fid, 2000 + cnt))
                            
                # Create detailed Markdown
                md_content = f"""---
id: {fid}
name: {display_name}
map_id: {MAP_ID}
layer_id: {layer_id}
geometry_wkt: {wkt}
---

## 簡介
這是一座位於濁水溪流域的水利設施。

## 基本資訊
- **名稱**: {display_name}
- **原始名稱**: {name}
- **里程位置**: {milage}
- **操作方式**: {manage_sys}
- **所屬流域**: 濁水溪 (Basin 1510)

## 交通指引
{note}

## 備註
本資料來自水利署公開資料 (DIKEGATE)。
"""
                with open(os.path.join(FEATURES_DIR, f"{fid}.md"), 'w', encoding='utf-8') as f:
                    f.write(md_content)
                    
                cnt += 1
                
            except sqlite3.Error as e:
                print(f"Error inserting {display_name}: {e}")

    conn.commit()
    conn.close()
    print(f"Imported {cnt} gates for Basin {TARGET_BASIN_NO}.")

if __name__ == "__main__":
    main()
