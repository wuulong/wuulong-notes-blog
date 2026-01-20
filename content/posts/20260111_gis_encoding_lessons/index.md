---
title: "[GIS筆記] SHP 轉檔的亂碼陷阱：從「百年舊堤」案例看編碼偵測的重要性"
date: 2026-01-11
draft: false
tags: [GIS, Python, OGR, GDAL, Encoding, Big5, UTF-8]
categories: ["Project (專案)"]
series: ["WalkGIS"]
---

在將既有的 GIS 開放資料（如 QGIS 專案中的 Shapefile）整合進 WalkGIS 系統時，最常遇到的挑戰往往不是座標轉換，而是**文字編碼（Encoding）**。

最近在處理「濁水溪流域情報地圖」中的「百年舊堤」圖層時，我遇到了一個經典的亂碼案例。這篇文章將紀錄問題的成因、誤判的過程，以及最終的正確解法，作為未來處理 GIS 舊資料的參考。

## 案例背景

我試圖將一份名為 `23座百年舊堤.shp` 的檔案匯入我的 WalkGIS SQLite 資料庫。

### 1. 初次嘗試：預設轉檔的失敗
一開始，我直接將 SHP 轉為 KML/KMZ 進行預覽。結果在 KML 中，所有的堤防名稱都變成了無法辨識的亂碼，如：
> `偌`

這些字並不是常見的「」或亂數，而是顯示為 **PUA (Private Use Area)** 區域的罕見字元。這是一個強烈的訊號，代表**編碼解讀錯誤**。

### 2. 直覺誤判：這一定是 Big5
台灣早期的 GIS 資料（尤其是政府開放資料），絕大多數的 `.dbf` 屬性表都使用 **Big5 (CP950)** 編碼。當看見中文變亂碼時，直覺反應通常是：「啊，這一定是工具用 UTF-8 去讀 Big5 造成的。」

於是我在 Python 腳本中強制指定了編碼：
```python
# 錯誤的嘗試
gdal.SetConfigOption("SHAPE_ENCODING", "CP950")
```

結果出乎意料：**亂碼依然存在**，甚至變成了另一種形式的亂碼。如果您嘗試用各種 Big5/Latin1 交叉解碼都無效，那問題可能比想像中複雜。

## 真相：雙重編碼災難

為了找出真相，我使用 `ogrinfo` 指令進行了雙盲測試（A/B Testing）：

**測試 A：指定 CP950**
```bash
ogrinfo -al -so --config SHAPE_ENCODING CP950 "23座百年舊堤.shp"
> Name (String) = 偌  (亂碼)
```

**測試 B：不指定 (預設/UTF-8)**
```bash
ogrinfo -al -so "23座百年舊堤.shp"
> Name (String) = 勞水坑二號堤防 (正確中文！)
```

### 結論
這份 SHP 檔案雖然是「舊資料」，但其中途可能經過轉檔處理，其 `.dbf` 屬性表**已經被轉換為 UTF-8 編碼**。

當我們自作聰明地強制指定 `CP950` 時，GDAL 會將這些原本正確的 UTF-8 bytes，強行當作 Big5 雙位元組字元來解讀，導致了「將正確的 UTF-8 再次解碼」的**二次亂碼（Mojibake）**。

## 正確的處理流程

處理這類 GIS 資料匯入時，建議遵循以下 SOP：

1.  **先用 ogrinfo 探勘**：在寫程式碼之前，先用 CLI 工具檢查。如果不確定編碼，**不要加 `--config SHAPE_ENCODING` 參數**先跑一次看看。
    ```bash
    ogrinfo -al -so layer.shp | head
    ```
2.  **信任 Default**：現代的 GDAL/OGR 已經很聰明，能自動偵測 `.cpg` 檔案或標準編碼標頭。除非預設讀出來是亂碼，否則不應強制指定編碼。
3.  **Python 實作**：
    在 Python 中使用 OGR 讀取時，保持預設設定通常是最安全的做法。

    ```python
    from osgeo import ogr
    
    # 不需設定 SHAPE_ENCODING，除非確定它是 Big5 且沒被自動偵測到
    driver = ogr.GetDriverByName("ESRI Shapefile")
    dataSource = driver.Open(shp_path, 0)
    layer = dataSource.GetLayer()
    
    for feature in layer:
        # 直接讀取，GDAL 會自動處理 UTF-8
        name = feature.GetFieldAsString("Name")
        print(name)
    ```

## 總結

GIS 資料處理中，「直覺」有時是危險的。看到亂碼就認為是 Big5，反而可能讓你親手毀了原本正確的資料。

透過工具（如 `ogrinfo`）進行客觀驗證，並理解資料的真實狀態，才能避免在編碼的迷宮中繞路。這次的經驗也提醒我們，在自動化腳本中，**編碼偵測**應該是一個動態的過程，而非寫死的參數。

## 參考
- [濁水溪及其周邊景點設施地圖](https://walkgis-544663807110.us-west1.run.app/?map=20260111_zhuoshui_facilities)

---

> **AI 協作聲明**：
> 本文內容由筆者與 AI 助手 Antigravity 共同撰寫。在處理 GIS 舊檔並面臨亂碼問題時，AI 協助進行了雙盲測試的邏輯推演，找出了「誤判 Big5」的根本原因，並提供 Python 與 ogrinfo 的除錯程式碼。
