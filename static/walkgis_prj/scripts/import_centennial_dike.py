
import os
import sqlite3
import shutil
from osgeo import ogr, osr

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
    if not os.path.exists(SHP_PATH):
        print(f"SHP file not found: {SHP_PATH}")
        return

    # 1. Open SHP with OGR
    # OGR usually handles encoding from .cpg or assumes system encoding.
    # To force Big5, we might rely on the .cpg file existing (it does).
    # If not, we can set SHAPE_ENCODING config option.
    
    # Force encoding just in case
    # gdal.SetConfigOption("SHAPE_ENCODING", "BIG5") or "CP950"
    from osgeo import gdal
    gdal.SetConfigOption("SHAPE_ENCODING", "CP950")
    
    driver = ogr.GetDriverByName("ESRI Shapefile")
    dataSource = driver.Open(SHP_PATH, 0) # 0 means read-only
    
    if dataSource is None:
        print("Could not open SHP file")
        return
        
    layer = dataSource.GetLayer()
    print(f"Reading {layer.GetFeatureCount()} features from SHP...")
    
    # 2. Connect to DB
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # 3. Clean up old "Garbage" or "Temp" features for this Map + Layer
    # Logic: Find features in this map that look like "百年舊堤_路段_%" OR were the old garbled ones.
    # Actually, simpler to verify which features to delete.
    # Let's delete anything with layer_id matching "百年舊堤" (if I create a specific layer for them)
    # OR we can just delete features where name LIKE '百年舊堤_路段_%'
    
    print("Cleaning up temporary features...")
    cursor.execute("SELECT feature_id FROM walking_map_features WHERE name LIKE '百年舊堤_路段_%'")
    old_fids = [row[0] for row in cursor.fetchall()]
    
    for fid in old_fids:
        # Delete from relations
        cursor.execute("DELETE FROM walking_map_relations WHERE feature_id = ?", (fid,))
        # Delete from features
        cursor.execute("DELETE FROM walking_map_features WHERE feature_id = ?", (fid,))
        # Delete markdown file
        md_path = os.path.join(FEATURES_DIR, f"{fid}.md")
        if os.path.exists(md_path):
            os.remove(md_path)
            
    print(f"Deleted {len(old_fids)} temporary features.")
    
    # 4. Insert new features
    layer_id = get_layer_id(cursor, LAYER_TYPE)
    
    # Spatial Reference transformation if needed
    source_srs = layer.GetSpatialRef()
    target_srs = osr.SpatialReference()
    target_srs.ImportFromEPSG(4326) # WGS84
    
    transform = None
    if source_srs and not source_srs.IsSame(target_srs):
        transform = osr.CoordinateTransformation(source_srs, target_srs)
        
    feature_def = layer.GetLayerDefn()
    # Find Name field (Name? NAME? name?)
    name_field_idx = -1
    for i in range(feature_def.GetFieldCount()):
        fdef = feature_def.GetFieldDefn(i)
        fname = fdef.GetNameRef()
        if fname.lower() in ['name', 'rv_name', 'dike_name', 'name_c']:
            name_field_idx = i
            break
            
    # If no obvious name field, we'll list fields to debug, but assume first field for now or "Id"
    if name_field_idx == -1:
        print("Could not find Name field. Using Field 0.")
        name_field_idx = 0
        
    idx = 0
    for feature in layer:
        geom = feature.GetGeometryRef()
        if transform:
            geom.Transform(transform)
            
        wkt = geom.ExportToWkt()
        geom_type = geom.GetGeometryName()
        
        # Get Name
        try:
            raw_name = feature.GetFieldAsString(name_field_idx)
            # OGR should have handled decoding if we set SHAPE_ENCODING
            name = raw_name
        except:
            name = f"百年舊堤_{idx}"
            
        feat_id = f"{MAP_ID}_dike_{str(idx).zfill(3)}_{name.replace(' ', '_')}"
        
        # Insert Feature
        try:
            cursor.execute("""
                INSERT OR REPLACE INTO walking_map_features 
                (feature_id, name, description, layer_id, geometry_type, geometry_wkt) 
                VALUES (?, ?, ?, ?, ?, ?)
            """, (feat_id, name, "來自濁水溪百年舊堤 SHP 原始資料", layer_id, geom_type, wkt))
        except sqlite3.Error as e:
            print(f"Error inserting {name}: {e}")
            continue
            
        # Link to Map
        cursor.execute("INSERT OR REPLACE INTO walking_map_relations (map_id, feature_id, display_order) VALUES (?, ?, ?)",
                       (MAP_ID, feat_id, 900 + idx)) # Put them at the end or specific order
                       
        # Create Markdown
        md_content = f"""---
id: {feat_id}
name: {name}
map_id: {MAP_ID}
layer_id: {layer_id}
geometry_wkt: {wkt}
---

## 簡介
這是濁水溪流域中重要的百年歷史舊堤防。

## 相關連結
"""
        with open(os.path.join(FEATURES_DIR, f"{feat_id}.md"), 'w', encoding='utf-8') as mf:
            mf.write(md_content)
            
        idx += 1
        
    conn.commit()
    conn.close()
    print(f"Imported {idx} features from SHP.")

if __name__ == "__main__":
    main()
