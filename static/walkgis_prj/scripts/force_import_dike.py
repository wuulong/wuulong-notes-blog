
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
    # 1. Force Clean up EVERYTHING related to garbled data or old dikes
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    print("Force cleaning all garbled/old dike features...")
    
    # Select IDs to verify what we are deleting
    cursor.execute("""
        SELECT feature_id FROM walking_map_features 
        WHERE name LIKE '百年舊堤%' 
           OR name LIKE '%%' 
           OR feature_id LIKE '%%'
           OR layer_id = (SELECT layer_id FROM layers WHERE layer_type = '百年舊堤')
    """)
    features_to_delete = [row[0] for row in cursor.fetchall()]
    
    for fid in features_to_delete:
        cursor.execute("DELETE FROM walking_map_relations WHERE feature_id = ?", (fid,))
        cursor.execute("DELETE FROM walking_map_features WHERE feature_id = ?", (fid,))
        
        md_path = os.path.join(FEATURES_DIR, f"{fid}.md")
        if os.path.exists(md_path):
            os.remove(md_path)
            print(f"Removed file: {fid}.md")
            
    conn.commit()
    print(f"Deleted {len(features_to_delete)} old/garbled features from DB.")

    # 2. Re-import from SHP with correct ENCODING
    
    # Important: Set CPL_Config option for SHAPE_ENCODING
    gdal.SetConfigOption("SHAPE_ENCODING", "CP950")
    gdal.SetConfigOption("CPL_LOG", "/dev/null") # Silence some logs
    
    driver = ogr.GetDriverByName("ESRI Shapefile")
    dataSource = driver.Open(SHP_PATH, 0)
    
    if dataSource is None:
        print("Could not open SHP file")
        return
        
    layer = dataSource.GetLayer()
    layer_id = get_layer_id(cursor, LAYER_TYPE)
    
    target_srs = osr.SpatialReference()
    target_srs.ImportFromEPSG(4326) # WGS84
    
    idx = 0
    for feature in layer:
        geom = feature.GetGeometryRef()
        source_srs = geom.GetSpatialReference()
        
        if source_srs and not source_srs.IsSame(target_srs):
            transform = osr.CoordinateTransformation(source_srs, target_srs)
            geom.Transform(transform)
            
        wkt = geom.ExportToWkt()
        geom_type = geom.GetGeometryName()
        
        # Get Name - Try multiple fields
        name = "Unknown"
        for field_idx in range(feature.GetFieldCount()):
            fdef = feature.GetFieldDefnRef(field_idx)
            fname = fdef.GetNameRef()
            # print(f"Field {fname}: {feature.GetFieldAsString(field_idx)}")
            if fname.lower() in ['name', 'dike_name', 'name_c', 'rv_name']:
                name = feature.GetFieldAsString(field_idx)
                break
        
        # Fallback if name is still empty or looks like garbage (simple check)
        if not name or name.strip() == "":
             name = feature.GetFieldAsString(0) # Use first field
             
        # Create Feature ID
        feat_id = f"{MAP_ID}_dike_{str(idx).zfill(3)}_{name.replace(' ', '_')}"
        
        # Insert
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
        
    conn.commit()
    conn.close()
    print(f"Successfully re-imported {idx} features from SHP.")

if __name__ == "__main__":
    main()
