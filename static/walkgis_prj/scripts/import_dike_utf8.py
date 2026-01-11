
import os
import sqlite3
from osgeo import ogr, osr, gdal

# Paths
SHP_PATH = "/Volumes/D2024/QGIS/projects/流域情報開放地圖/0A_流域/0A04_濁水溪流域/濁水溪調適計畫/百年舊堤/23座百年舊堤.shp"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(SCRIPT_DIR, "../walkgis.db")
FEATURES_DIR = os.path.join(SCRIPT_DIR, "../features")
MAP_ID = "20260111_zhuoshui_facilities"
LAYER_TYPE = "百年舊堤"

def get_layer_id(cursor, layer_type):
    cursor.execute("SELECT layer_id FROM layers WHERE layer_type = ?", (layer_type,))
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        cursor.execute("INSERT INTO layers (layer_type, description) VALUES (?, ?)", (layer_type, "Imported from SHP"))
        return cursor.lastrowid

def main():
    # 1. Open SHP - DO NOT SET CP950/BIG5 CONFIG.
    # The ogrinfo test showed that default encoding (UTF-8 or auto-detect) worked, while CP950 returned Mojibake.
    # This implies the SHP file's DBF is actually UTF-8 encoded despite standard practices.
    
    # gdal.SetConfigOption("SHAPE_ENCODING", "") # Clear it
    
    driver = ogr.GetDriverByName("ESRI Shapefile")
    dataSource = driver.Open(SHP_PATH, 0)
    
    if dataSource is None:
        print("Could not open SHP file")
        return
        
    layer = dataSource.GetLayer()
    
    # 2. Connect to DB
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    layer_id = get_layer_id(cursor, LAYER_TYPE)
    
    target_srs = osr.SpatialReference()
    target_srs.ImportFromEPSG(4326) # WGS84
    
    print(f"Reading {layer.GetFeatureCount()} features (Default Encoding)...")
    
    idx = 0
    for feature in layer:
        geom = feature.GetGeometryRef()
        if geom is None:
            continue
            
        source_srs = geom.GetSpatialReference()
        if source_srs and not source_srs.IsSame(target_srs):
            transform = osr.CoordinateTransformation(source_srs, target_srs)
            geom.Transform(transform)
            
        wkt = geom.ExportToWkt()
        geom_type = geom.GetGeometryName()
        
        # Get Name
        name_field_idx = feature.GetFieldIndex("Name")
        if name_field_idx != -1:
            name = feature.GetFieldAsString(name_field_idx)
        else:
            name = feature.GetFieldAsString(0)
            
        # Create Feature ID
        feat_id = f"{MAP_ID}_dike_{str(idx).zfill(3)}_{name.replace(' ', '_')}"
        
        # Insert
        try:
            cursor.execute("""
                INSERT OR REPLACE INTO walking_map_features 
                (feature_id, name, description, layer_id, geometry_type, geometry_wkt) 
                VALUES (?, ?, ?, ?, ?, ?)
            """, (feat_id, name, "來自濁水溪百年舊堤 SHP 原始資料", layer_id, geom_type, wkt))
            
            cursor.execute("INSERT OR REPLACE INTO walking_map_relations (map_id, feature_id, display_order) VALUES (?, ?, ?)",
                        (MAP_ID, feat_id, 900 + idx))

            # Markdown
            md_content = f"""---
id: {feat_id}
name: {name}
map_id: {MAP_ID}
layer_id: {layer_id}
geometry_wkt: {wkt}
---

## 簡介
這是濁水溪流域中重要的百年歷史舊堤防：{name}。

## 相關連結
"""
            with open(os.path.join(FEATURES_DIR, f"{feat_id}.md"), 'w', encoding='utf-8') as mf:
                mf.write(md_content)
            idx += 1
            
        except sqlite3.Error as e:
            print(f"DB Error for {name}: {e}")
            
    conn.commit()
    conn.close()
    print(f"Successfully imported {idx} features.")

if __name__ == "__main__":
    main()
