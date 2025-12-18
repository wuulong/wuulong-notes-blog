---
title: "實驗紀錄：使用 GDAL 進行大甲溪流域 1km 緩衝區萃取與合併"
date: 2025-12-13T14:57:15+08:00
draft: false
categories: ["GIS", "Data Experiment"]
tags: ["GDAL", "ogr2ogr", "KML", "Buffer", "ST_Union", "Big5", "大甲溪"]
author: "Wuulong"
summary: "本實驗使用 GDAL/ogr2ogr 工具，從中央管河川區域 Shapefile 中萃取大甲溪河流範圍，解決 Big5 編碼篩選問題，進行 1 公里緩衝分析 (Buffer)，並透過 SQL ST_Union 合併多個圖層特徵，最終產出 KML 檔案。"
---

## 實驗目的

目標是從「流域情報開放地圖的中央管河川區域」Shapefile (`RIVERL.shp`) 中，精確萃取「大甲溪」的河流範圍線。針對這些河流線進行 **1 公里緩衝 (Buffer)** 擴展，最後將分散的緩衝區特徵 (Features) **合併 (Dissolve/Union)** 為單一幾何圖形，並輸出為 KML 格式以便於 Google My Maps 使用。

## 實驗環境

*   **作業系統**：macOS (Darwin)
*   **專案目錄**：`~/github/bmad-pa`
*   **工具環境**：Conda 環境 `m2504` (安裝 Fiona, GDAL)
*   **資料來源**：`RIVERL-中央管河川區域/RIVERL.shp` (Big5 編碼)
*   **GenAI 工具**：`gemini cli with gemini-2.5-flash`, `gov_openapi_agent MCP tool` 

## 實驗步驟與過程

### 1. 資料探勘：確認屬性與編碼
*   **檢查工具**：使用 `fio info` 檢視 Shapefile。
*   **關鍵發現**：
    *   幾何類型：`LineString` (線性河川)。
    *   座標系統：`EPSG:3826` (TWD97 / TM2 zone 121)，單位為公尺，這對緩衝區計算非常有利（無需投影轉換即可直接設定公尺距離）。
    *   **編碼陷阱**：資料集的文字編碼為 `Big5`。這意味著在命令列工具中若不指定編碼，將無法正確篩選中文流域名稱。

### 2. 第一階段：篩選與緩衝 (Buffer)
*   **操作目標**：選出「大甲溪」並向外擴張 1000 公尺。
*   **技術挑戰**：需同時處理 Big5 編碼與幾何計算。
*   **解決方案**：
    *   設定環境變數 `SHAPE_ENCODING=Big5` 讓 `ogr2ogr` 能讀懂屬性表。
    *   利用 SQLite Dialect 的 `ST_Buffer` 函數進行幾何運算。
*   **執行指令**：
    ```bash
    export SHAPE_ENCODING=Big5
    ogr2ogr -where "RV_NAME='大甲溪'" -f KML \
    dajiaxi_river_1km_buffer.kml \
    RIVERL.shp \
    -dialect sqlite -sql "SELECT ST_Buffer(geometry, 1000) AS geometry, RV_NAME FROM RIVERL WHERE RV_NAME='大甲溪'"
    ```
*   **結果**：生成 `dajiaxi_river_1km_buffer.kml`，但內部包含 8 個分散的 Polygons。

### 3. 第二階段：特徵合併 (Union/Dissolve)
*   **操作目標**：將分散的 8 個 Polygon 合併成一個完整的範圍。
*   **技術挑戰**：
    *   嘗試 `ogr2ogr -union` 參數無效（版本不支援或參數誤用）。
    *   改用 SQL `ST_Union` 時遇到語法錯誤，因為輸入的 KML 圖層名稱可能與 SQL 關鍵字衝突。
*   **解決方案**：
    *   使用 `ST_Union` 函數聚合幾何圖形。
    *   在 SQL 中對來源圖層名稱（KML 預設常為 `SELECT` 或檔名）進行跳脫引用。
*   **執行指令**：
    ```bash
    ogr2ogr -f KML \
    dajiaxi_river_1km_buffer_dissolved.kml \
    dajiaxi_river_1km_buffer.kml \
    -dialect sqlite -sql "SELECT ST_Union(geometry) AS geometry, '大甲溪' AS RV_NAME FROM \"SELECT\""
    ```
    *(註：輸入 KML 的圖層名稱在此例中被識別為 `SELECT`，因此 SQL 中需寫為 `"SELECT"`)*

## 實驗結果

成功產出 `dajiaxi_river_1km_buffer_dissolved.kml`。該檔案包含了一個單一、連續且帶有 1 公里緩衝區的大甲溪河流範圍，完美適用於後續的地理分析或地圖展示。

## 學習與反思

1.  **編碼敏感度**：處理台灣早期或政府開放資料時，`Big5` 編碼是常客。在使用 `ogr2ogr` 等國際開源工具時，務必透過 `SHAPE_ENCODING` 環境變數或 `--config` 參數明確宣告。
2.  **SQL Dialect 強大性**：`ogr2ogr` 的 `-dialect sqlite` 非常強大，讓使用者能在轉檔過程中直接呼叫 SpatiaLite 的強大幾何函數（如 `ST_Buffer`, `ST_Union`），省去了將資料匯入資料庫再匯出的繁瑣步驟。
3.  **特殊字元處理**：當圖層名稱不幸撞名 SQL 關鍵字（如 `SELECT`）時，精準的引號使用（Quoting）是解決 Syntax Error 的關鍵。
