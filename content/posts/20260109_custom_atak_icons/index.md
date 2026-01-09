---
title: "WalkGIS 實戰：為 ATAK 打造專屬的「河川探索」戰術圖示包"
date: 2026-01-09
description: "如何使用 Python 強大的繪圖庫，不依賴網路素材，自動生成高辨識度、風格統一的中文單字圖示，並打包成 ATAK 專用的 Data Package，讓戶外探索地圖一目瞭然。"
tags: ["WalkGIS", "ATAK", "Python", "GIS", "Visualization"]
categories: ["Project (專案)"]
series: [WalkGIS]
params:
  ShowToc: true
  TocOpen: true
---

在 [上一篇](/posts/20260109_convenience_stores_toilets_map/) 我們搞定了「有廁所的便利商店」地圖資料。然而，當我們真正走入濁水溪或曾文溪的荒野時，地圖上需要的資訊遠不止這些。

我們需要知道哪裡有**攔沙壩 (Weir)** 可以觀察水流，哪裡有 **吊橋 (Suspension Bridge)** 可以跨越峽谷，哪裡有 **土地公廟 (Earth God Temple)** 可以補給休息。

ATAK 內建的軍規符號太過複雜且抽象，網路上抓的圖示又風格不一。於是，我決定自己動手做一套**「WalkGIS 河川探索專用圖示包」**。

## 🎯 設計理念：直覺至上

在地圖上（尤其是戶外強光下的手機螢幕），**辨識度**是第一要務。經過幾次嘗試（從下載 icon 到失敗的 fallback），我發現最有效的方法竟然最簡單：

**「直接把字寫在圓圈裡。」**

*   看圖示猜半天這是廟還是房子？不如直接寫個**「廟」**。
*   這是水壩還是水管？直接寫個**「壩」**。

我將需求分為四大類色系，建立了一套視覺語言：

*   💚 **生存 (Survival) - 綠色**：廁、店 (雜貨)、水 (水源)、車 (車宿點)
*   💙 **水利 (Hydro) - 藍色**：壩、橋、閘 (水門)、生 (生態點)、景 (觀景)
*   🧡 **人文 (Culture) - 橙/棕**：廟 (土地公)、跡 (遺跡)、訊 (解說牌)、村 (部落)
*   ❤️ **危險 (Danger) - 紅色**：危

## 🛠️ 技術實作：Python `Pillow` 自動繪圖

我寫了一個 Python 腳本 (`generate_chinese_icons.py`)，完全不依賴外部圖片素材，直接用程式碼「畫」出這些圖示。

### 核心邏輯

1.  **定義設定檔**：用一個 List 管理所有圖示的名稱、顯示文字與顏色。
2.  **字體偵測**：自動抓取 macOS 系統內的 `PingFang.ttc` 或 `STHeiti` 中文字體。
3.  **畫布生成**：
    *   建立 64x64 的透明底圖。
    *   畫一個實心圓圈（帶白邊），顏色由設定檔決定。
    *   將中文字置中寫在圓圈上。
4.  **ATAK 打包**：生成 `iconset.xml` 並將所有 PNG 壓成 ZIP 檔。

### 程式碼與成果

```python
# 部分程式碼片段
def create_text_icon(item):
    # ... 畫圓與寫字 ...
    draw.ellipse([4, 4, 60, 60], fill=item['color'], outline='white', width=3)
    draw.text((x, y), item['label'], font=font, fill='white')
    # ... 存檔 ...
```

執行後，我得到了一個 `River_Exploration_Icons_Text.zip`。

- [下載點](River_Exploration_Icons_Text.zip)

## 📱 實際應用

將 ZIP 檔傳入手機，在 ATAK 中選擇 **Import** -> **Icon Set**。
瞬間，我的圖針選單裡多了一組整齊劃一的戰術圖示。

現在，當我在地圖上標記一個點時，不再是只有單調的紅點，而是一個個清晰的**「橋」、「廟」、「壩」**。這不僅讓地圖畫面更清爽，也讓我在現場做決策時（例如：前面還有多遠才有「水」？）更加迅速。

這就是 **WalkGIS** 的精神：**用程式解決問題，讓數據服務探險。**
