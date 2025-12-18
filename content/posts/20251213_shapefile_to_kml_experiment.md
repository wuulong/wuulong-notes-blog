---
title: "實驗紀錄：取得河川流域 Shapefile 圖資並轉換為 KML 匯入 Google My Maps"
date: 2025-12-13T13:05:11+08:00
draft: false
series: ["GenAI"]
categories: ["GIS", ]
tags: ["Shapefile", "KML", "Google My Maps", "ogr2ogr", "GDAL", "Open Data", "大甲溪"]
author: "Wuulong"
summary: "本實驗記錄了從政府開放資料平台取得水利署河川流域 Shapefile 資料，並將其中「大甲溪」流域資料篩選後，使用 GDAL/ogr2ogr 工具轉換為 Google My Maps 支援的 KML 格式的完整過程。"
---

## 實驗目的

從政府開放資料平台（水利署）取得河川流域 Shapefile 圖資，篩選出特定流域（大甲溪），並將其轉換為 Google My Maps 支援的 KML 格式，解決 Google My Maps 不支援直接匯入 GeoJSON 的問題，最終成功將圖資匯入地圖中。

## 實驗環境

*   **作業系統**：macOS (Darwin)
*   **專案目錄**：`~/github/bmad-pa`
*   **GenAI 工具**：`gemini cli with gemini-2.5-flash`, `gov_openapi_agent MCP tool` 
*   **工具環境**：Conda 環境 `m2504` (安裝 Fiona, GDAL)
*   **關鍵工具**：`ogr2ogr` (GDAL library)

## 實驗步驟與過程

### 1. 流域圖資的發現與來源
*   **需求發起**：查詢「流域 GIS 的開放資料」，目標是取得台灣河川流域的地理資訊。
*   **資料搜尋**：透過工具搜尋政府開放資料平台，鎖定「河川流域範圍圖」資料集。
*   **取得資料**：下載 `BASIN.zip` 檔案，本地存放路徑為 `events/camping_2026/data/BASIN.zip`。

### 2. 初始嘗試：GeoJSON 轉換遇阻
*   **檔案檢視**：使用 `fio info` 確認 Shapefile (`basin.shp`) 的屬性結構，確認流域名稱欄位為 `BASIN_NAME`。
*   **格式迷思**：
    *   最初嘗試使用 `fio cat` 篩選 `BASIN_NAME='大甲溪'` 並匯出。
    *   嘗試轉為 Google My Maps 常見格式。原本誤以為 Google My Maps 支援 GeoJSON，因此先產生了 `dajiaxi_basin.geojson`。
*   **匯入失敗**：實測並經查證後確認，**Google My Maps 不支援直接匯入 GeoJSON 檔案**，僅支援 KML, KMZ, CSV, XLSX, GPX 等格式。
*   **結論**：必須將資料轉換為 standard **KML** 格式。

### 3. 工具建置：解決 ogr2ogr 環境問題
*   **工具選擇**：轉檔首選工具為 GDAL 套件中的 `ogr2ogr`。
*   **環境除錯**：
    *   初次執行時系統回報 `command not found`。
    *   檢查 Conda 環境 `m2504`，發現尚未安裝 GDAL。
    *   **解決方案**：執行 `conda install -n m2504 gdal -y` 安裝 GDAL 函式庫。安裝後 `ogr2ogr` 指令即無法使用。

### 4. 成功轉換：Shapefile 直轉 KML
*   **執行轉換**：在環境準備好後，使用以下指令直接從原始 Shapefile 篩選出大甲溪流域並轉存為 KML，略過中間的 GeoJSON 步驟以減少轉換誤差。
    ```bash
    conda run -n m2504 ogr2ogr -where "BASIN_NAME='大甲溪'" -f KML \
    dajiaxi_basin.kml \
    raw_data/basin/basin.shp
    ```
    *(註：路徑已簡化示意)*
*   **結果**：成功生成 `dajiaxi_basin.kml`。

### 5. 驗證與歸檔
*   **驗證**：將生成的 `dajiaxi_basin.kml` 上傳至 Google My Maps，圖層成功顯示大甲溪流域範圍。
*   **歸檔**：將最終檔案保存於專案目錄：`events/camping_2026/data/dajiaxi_basin.kml`。

## 實驗結果

成功建立了一套從「政府開放資料 Shapefile」到「Google My Maps KML」的標準作業流程。解決了中間格式不相容與工具環境缺失的問題。

## 學習與反思

1.  **工具驗證重要性**：Google My Maps 對匯入格式的支援有特定限制（不支援 GeoJSON），規劃資料流時應先查證規格，避免走冤枉路。
2.  **環境管理**：GIS 處理工具（如 `ogr2ogr`）通常依賴 C/C++ 底層函式庫 (GDAL)，在 Python/Conda 環境中需特別留意這些二進位依賴是否正確安裝。
3.  **流程優化**：`ogr2ogr` 的 `-where` 參數非常強大，能夠在庫（Database/File）層級直接進行 SQL-like 的篩選，無需將全部資料載入記憶體或轉存中間檔，效率最佳。
