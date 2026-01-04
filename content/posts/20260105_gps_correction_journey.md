---
title: "WalkGIS 資料治理實戰：從「差不多準」到「精確定位」的 GPS 校正之旅"
date: 2026-01-05T07:20:00+08:00
draft: false
categories: ["Project (專案)"]
series: ["WalkGIS"]
tags: ["Google Maps API", "Python", "Data Governance", "GIS", "Automation"]
summary: "在 WalkGIS 2.0 的開發過程中，我發現早期的地圖資料存在嚴重的 GPS 誤差。本文記錄了如何利用 Google Maps API 進行批次自動化校正，並解決了「台灣中心點」歸零問題、路徑檔被誤改以及資料一致性維護的技術挑戰。"
---

在推動 WalkGIS 2.0 的過程中，最關鍵的基礎建設就是**資料準確性**。

早期建立地圖時，為了求快，很多點位是依賴 LLM (大語言模型) 的模糊知識，或是手動在地圖上點大概位置。結果今天心血來潮一驗證，發現誤差驚人。

## 😱 發現問題：誤差高達 3 公里

我寫了一個簡單的腳本，比對 WalkGIS 資料庫中的座標與 Google Maps API 查詢到的座標。結果出來讓我冷汗直流：

*   **大安溪水管橋**：誤差 3.5 公里（定位到后里市區去了）。
*   **鯉魚潭國小**：誤差 2.5 公里（Google 找不到遷校後的點）。
*   **后里圳電廠**：誤差 2.1 公里。

這對於一個強調「走讀」的地圖服務來說，是不可接受的。如果使用者照著這個座標走，大概會迷路在荒郊野外。

## 🛠️ 第一階段：暴力自動化 (The Naive Approach)

既然 Google Maps 比較準，那就全部用 Google 的資料覆蓋吧！

我寫了 `update_features_gps.py`，把所有 features 丟給 Google Geocoding API，然後強制更新 Markdown 檔案與 SQLite 資料庫。

**結果發生了兩個災難：**

1.  **路徑變成了點**：原本是 LineString 的輸水管路徑，因为 API 回傳了一個中心點座標，腳本就無腦地把資料庫裡的幾何形狀從「線」改成了「點」。導致地圖上的管線瞬間消失，變成一個圖釘。
2.  **台灣中心點黑洞**：對於「綠廊交接處」、「200days冰店」這種 Google 認不得的名稱，Google API 回傳了預設的「台灣中心點 (23.9, 120.9)」。結果地圖上好幾個點都瞬移到了南投深山裡。

## 🔧 第二階段：精細化治理 (Refined Governance)

痛定思痛，我調整了策略：

1.  **型別保護 (Type Safety)**：修改腳本，加入 `geometry_type` 檢查。只有當目標是 `POINT` 時才允許更新，絕對不動 `LINESTRING`。
2.  **還原路徑**：重新執行路徑生成腳本，把被破壞的管線資料救回來。
3.  **人工介入 (Human-in-the-loop)**：
    *   對於自動化校正後誤差仍極大的點，或是被丟到台灣中心的點，列出清單。
    *   使用 `search_web` 工具手動查找正確座標。
    *   編寫 `manual_update_features.py` 針對這 7 個頑固份子進行精確打擊。

## 📝 技術收穫：Markdown 與 DB 的雙向綁定

這次也順便解決了一個長期痛點：資料一致性。
WalkGIS 採取「Markdown 為主，DB 為輔」的架構。但在更新座標時，很容易發生 DB 改了但 MD 沒改的情況。

這次我寫了 `standardize_features_frontmatter.py`，強制統一所有 Markdown 的 Frontmatter 格式：
```yaml
coordinate: [24.250556, 120.730371]
```
確保每一份檔案都具備機器可讀的標準座標欄位，這讓未來的維護變得輕鬆許多。

## 結語

精準的地圖資料沒有捷徑。AI 可以幫我們完成 90% 的工作，但剩下那 10% 的誤差，往往決定了產品的成敗。這套「自動掃描 -> 類型過濾 -> 人工校正」的流程，將成為 WalkGIS 未來處理新地圖的標準 SOP。

---
### 🤖 AI 協作宣告
*   **本文內容**: 由人類作者提供核心經驗與觀察，Antigravity 協助架構文章、潤飾文字並生成技術細節描述。
*   **技術實作**: 文中提及的 GPS 校正腳本 (`update_features_gps.py`, `manual_update_features.py`) 均由 Antigravity 根據人類指令編寫與除錯。
