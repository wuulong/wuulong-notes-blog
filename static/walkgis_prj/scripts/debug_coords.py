
import sqlite3
import math
import os
from osgeo import ogr, gdal, osr

DB_PATH = "events/notes/wuulong-notes-blog/static/walkgis_prj/walkgis.db"
SHP_PATH = "/Volumes/D2024/QGIS/projects/流域情報開放地圖/2-流域設施與空間發展/1-構造物介紹及功能說明/DIKEGATE-水門位置圖/dikegate.shp"

def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT name, geometry_wkt FROM walking_map_features WHERE name = '水門' LIMIT 1")
    row = cursor.fetchone()
    if row:
        print(f"DB Sample: {row}")
    
    driver = ogr.GetDriverByName("ESRI Shapefile")
    dataSource = driver.Open(SHP_PATH, 0)
    layer = dataSource.GetLayer()
    
    # Check SRS
    print(f"SHP SRS: {layer.GetSpatialRef()}")
    
    feature = layer.GetNextFeature()
    geom = feature.GetGeometryRef()
    print(f"SHP Sample Raw: {geom.ExportToWkt()}")
    
    source_srs = layer.GetSpatialRef()
    target_srs = osr.SpatialReference()
    target_srs.ImportFromEPSG(4326)
    
    if source_srs.IsSame(target_srs):
        print("SRS is same")
    else:
        print("SRS is different, transform needed")
        transform = osr.CoordinateTransformation(source_srs, target_srs)
        geom.Transform(transform)
        print(f"SHP Sample Transformed: {geom.ExportToWkt()}")

if __name__ == "__main__":
    main()
