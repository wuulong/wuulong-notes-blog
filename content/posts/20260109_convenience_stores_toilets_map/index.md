---
title: "WalkGIS 實戰：如何製作「有廁所的便利商店」地圖 (Google My Maps + ATAK)"
date: 2026-01-09
description: "為了河流探索的補給需求，利用 OpenStreetMap 開放資料與 Python 腳本，篩選出全台「有廁所」的便利商店，並成功匯入 Google My Maps 與 ATAK 進行離線導航。"
tags: ["WalkGIS", "ATAK", "OpenStreetMap", "Python", "Google My Maps", "GIS"]
categories: ["Project (專案)"]
series: [WalkGIS]
params:
  ShowToc: true
  TocOpen: true
---

在規劃「2026 台灣河流探索」的過程中，除了路線本身的挑戰，最實際的問題往往是：「哪裡可以補給？」以及更重要的——「哪裡有廁所？」。

雖然 Google Maps 很強大，但要一眼在地圖上看出「哪一家超商有廁所」並不容易。於是，我決定自己動手做一張專屬的地圖，並將其整合到我的主力導航工具 **Google My Maps** 與 **ATAK** 中。

## 🚀 任務目標

1.  取得全台灣便利商店的資料。
2.  篩選出標記為「有廁所」的店家。
3.  製作成 Google My Maps 可以吃的 KML 檔。
4.  打包成 ATAK 可以用的 Data Package。

## 🛠️ Step 1: 資料來源 - OpenStreetMap (OSM)

相較於政府資料只有地址，OpenStreetMap (OSM) 社群維護的資料包含了更多屬性（如廁所、ATM、品牌）。我使用 **Overpass API** 來抓取資料。

### Python 抓取腳本 (核心邏輯)

我們不需要下載整個台灣的圖資，只需針對 `shop=convenience` 進行查詢：

```python
overpass_query = """
[out:json][timeout:60];
area["name:en"="Taiwan"]->.searchArea;
(
  node["shop"="convenience"](area.searchArea);
  way["shop"="convenience"](area.searchArea);
);
out center;
"""
```

這段腳本會抓下全台約 13,000+ 筆超商資料。

## 🧹 Step 2: 現實的殘酷 - 資料篩選

抓下來後，我原本期待能有滿滿的廁所清單，結果進行統計後發現：

*   **Total Stores**: 13,000+
*   **Toilets = Yes**: ~550
*   **Toilets = No**: ~150
*   **Toilets = Unknown**: 12,000+

顯然 OSM 上關於廁所的標記還很不普及（填寫率不到 5%）。但換個角度想，這 **550 間** 是經過熱心網友確認「一定有」廁所的精華名單，對於急需的人來說，這就是最可靠的綠洲。

於是，我用 Python 只保留 `toilets` 屬性為 `yes` 或 `customer` 的節點。

## 🗺️ Step 3: 進軍 Google My Maps

原本想直接匯入 GeoJSON，但立刻撞牆：
1.  Google My Maps 不支援 GeoJSON。
2.  檔案大小限制 5MB (原始檔即便是篩選後轉 KML 有時也會因為描述欄位太多而過大)。

解決方案是轉成 **KML** 格式，並精簡 `description` 欄位的 HTML 內容，只保留必要資訊（店名、品牌）。

```python
# 簡化的 KML 轉換邏輯
kml = ET.Element('kml', xmlns='http://www.opengis.net/kml/2.2')
# ... (建立 Placemark 與 Point 的過程) ...
tree.write('taiwan_convenience_stores_with_toilets.kml')
```

匯入成功後，地圖上出現了這 500 多個珍貴的藍點！

## 📱 Step 4: 戰術地圖 ATAK 整合

對於戶外探索，離線地圖 ATAK 是我的首選。ATAK 需要特定的 **Data Package** 格式（一個包含 `MANIFEST.xml` 的 ZIP 檔）。

我寫了一個腳本自動生成這個包：
1.  產生 `MANIFEST.xml`，指定 UID 與檔案類型。
2.  將剛做好的 KML 與 Manifest 壓成 ZIP。

```python
manifest_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<MPoZIP>
    <Manifest>
        <UID>{package_uid}</UID>
        <Name>Taiwan Convenience Stores with Toilets</Name>
        <Content>
            <Item><name>{kml_file}</name><type>kml</type></Item>
        </Content>
    </Manifest>
</MPoZIP>'''
```

將生成的 `zip` 檔傳到手機，ATAK 秒匯入而且完美顯示。

## 📝 結語

這次實戰驗證了 **Open Data + Python Automation** 的強大之處。雖然目前廁所資料的覆蓋率還不夠高，但這套流程建立起來後，未來想要製作「飲水機地圖」、「AED 地圖」或「露營點地圖」，也就是改改查詢條件的事了。

這正是 **WalkGIS 2.0** 的核心精神：**用數據導引腳步，用技術解決旅途中的真實問題。**
