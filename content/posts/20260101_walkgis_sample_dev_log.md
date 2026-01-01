---
title: "WalkGIS 實戰紀錄：自己坑自己踩，我如何用從 walkgis-template 做出一份「清大夜市散步地圖」"
date: 2026-01-01T15:15:00+08:00
draft: false
categories: ["Project (專案)"]
series: ["WalkGIS"]
tags: ["AI Agent", "Automation", "Data Governance", "GitHub Pages", "NotebookLM"]
summary: "這不是一篇理論文，而是一次真實的踩坑紀錄。本文記錄了我如何使用 WalkGIS Template，配合 AI Agent 的自動化任務，從零打造一份包含 16 個景點、具備 GPS 定位與詳細介紹的「清大夜市美食地圖」。文中包含基礎設施架設、AI 內容協作到最終資料治理的完整流程。"
---

在發布了 [WalkGIS 2.0 願景](/posts/20260101_walkgis_2_0_vision/) 後，為了驗證這套「去中心化地圖協議」是否真的如想像中好用，我決定親自下場測試。

我的目標很簡單：製作一份 **「2026 清大夜市散步與美食地圖」**。

## 🛠 Phase 1: 基礎設施架設 (Infrastructure)

### 1. 正確的起手式：Fork Template
一開始我嘗試手動建立 Repo 再複製檔案，發現非常容易出錯且耗時。
**最佳實踐**：直接 Fork `walkgis-template` 到你的目標 Repo (例如 `walkgis-sample`)。這是最快且最乾淨的做法。

### 2. 重要設定：開啟 GitHub Pages
這是最容易被遺忘的步驟。Fork 完之後，必須手動去開啟 Pages 功能，否則網站不會上線。
**操作步驟**：
1.  進入 Repo 的 **Settings** -> **Pages**。
2.  在 **Build and deployment** 下，Source 選擇 **"Deploy from a branch"**。
3.  Branch 選擇 **"main"** 並儲存。
4.  等待約 1-2 分鐘，看到頂部出現綠色勾勾與網址，才算成功。

### 3. 開啟 GitHub Pages 與 `.nojekyll` 的坑
當我把檔案推上去後，興沖沖地用 WalkGIS App 連線，卻發現一片空白。
經過 Debug 後發現，預設的 Jekyll 處理機制會忽略以 `_` (底線) 開頭的資料夾或特定檔案。
**解決方案**：在專案根目錄新增一個空的 `.nojekyll` 檔案。這告訴 GitHub Pages：「請原封不動地提供所有靜態檔案」，藥到病除。

## 🤖 Phase 2: 自動化內容生成 (Automation)

這裡就是展現 Agentic AI 強大的地方。我不需要手動去 Google Maps 查 16 個景點的座標，也不用自己寫 SQL。

### 0. 準備清單
首先，我請 AI 搜尋網路上關於「清大夜市」的推薦美食清單，快速整理出一份包含 16 個店家的目標列表。

### 1. 任務執行 (Task Execution)
我使用 BMad Agent 載入了 `.agent/tasks/create-walkgis-map-from-list.md` 任務，並給了它一個簡單的指令：
`run create-walkgis-map-from-list`

### 2. AI 做了什麼？ (One-Shot Scripting)
AI 自動撰寫了一個 Python 腳本 (`create_260101_tsing_hua_night_market.py`)，一口氣完成了：
*   **資料搜集**：自動搜尋這 16 個地點的地址、營業時間與特色。
*   **檔案生成**：產出 16 個 Feature Markdown 檔 + 1 個 Map Markdown 檔。
*   **資料庫注入**：自動生成 SQL 並寫入 `walkgis.db`。

這原本需要我花 2-3 小時的手工剪貼，AI 在 5 分鐘內就搞定了。

### 3. 多格式產出與視覺化
除了地圖，AI 還順便產出了：
*   **Context for NotebookLM**: 把所有景點資料打包成一個文本，方便餵給 NotebookLM 做後續創作。
*   **Google Nav Link**: 直接生成一條串連所有店家的導航連結，這在實地探訪時非常實用。

**Pro Tip：如何用 AI 生成地圖封面圖？**
預設生成的 map 在列表上沒有封面圖，不太美觀。我的做法是：
1.  在 WalkGIS Viewer 中點擊「Magic Generator」按鈕，取得 "Context for NotebookLM"。
2.  將此內容貼到 Google NotebookLM，請求它為這個散步路線生成一張「摘要圖」或「意象圖」。
3.  下載該圖片，放入 `assets/images/`。
4.  請 Agent 更新 `walkgis.db` 中的該筆 map 紀錄，指向這張新圖片。
這樣，您的地圖在市場列表中就會有一張漂亮的縮圖了！

## 📍 Phase 3: GPS 精準化與內容豐富化

初版生成後，我發現 GPS 位置有較大偏差，因為 AI 預設是使用模糊推估的方式。
雖然使用 Google Maps API 是最快的正規解法，但需要申請 API Key 且可能產生費用。

**我的解法：讓 Agent 當苦力（但有技巧）**
我指示 antigravity Agent 使用瀏覽器工具，一個一個去 Google Maps 網頁查詢真實座標。這雖然比 API 慢，但它是「最基礎也最省錢」的正確解法。

不過這過程充滿血淚。
直接讓 Agent 連續開瀏覽器查詢對記憶體消耗極大，甚至曾經跑到電腦當機重開，導致前面還沒存檔的查詢結果付諸流水。
**痛苦的教訓：必須分批處理 (Batch Processing)。**
我後來改為「每查詢 3-5 個地點就請 Agent 更新一次 Markdown 並存檔」，雖然繁瑣，但這才確保了任務在記憶體不爆掉的情況下順利跑完。

## ⚖️ Phase 4: 資料治理 (Data Governance)

測試過程發現資料似乎不同步：**Single Source of Truth** 的重要性浮現。

### 1. 發現與同步問題
在生成過程中，我發現資料庫 (`walkgis.db`) 與 Markdown 檔案 (`features/*.md`) 的座標數據出現了不一致。有些座標只存在 DB 裡，有些 MD 檔還是空的。

### 2. 自動化同步方案
為了解決這個問題，我們開發了 `scripts/sync_coords.py` 腳本：
*   **以 DB 為準**：SQLite 內的 WKT 資料被視為絕對真理。
*   **回寫 MD**：腳本自動讀取 DB，並將座標以 `coordinate: [lat, lon]` 的標準格式回寫到所有 Markdown 檔案中。

這建立了一個健康的資料維護循環：**DB 用於精確運算，Markdown 用於內容呈現與人類閱讀，兩者透過腳本保持同步。**

## 💡 實戰回饋：給 Template 的優化建議(To-Do)

經過這次實測 (Dogfooding)，我認為 `walkgis-template` 未來版本應該進行以下改進，讓後來者更順暢：

1.  **預設內建 `.nojekyll`**：不要讓使用者再踩一次 GitHub Pages 404 的坑。
2.  **提供標準 Markdown Formatter**：在 Prompt 或工具中規範統一的 Markdown 格式，減少後續資料清洗的負擔。
3.  **內附「自製指引文件」**：將本次 Agent 的操作流程（包含查詢 GPS 的分批技巧）寫成標準 SOP，讓使用者能按圖索驥。

## 🚀 成果展示

最終，這份地圖已經上線並收錄在 WalkGIS 市場中：
*   **地圖網址**: [WalkGIS Viewer](https://walkgis-544663807110.us-west1.run.app/)
*   **原始碼**: [清大夜市散步地圖 repo](https://wuulong.github.io/walkgis-sample)
    - 這個連結就是要輸入 viewer 的內容

這次實戰證明了 WalkGIS Template 加上 AI Agent，確實能讓一個沒有 GIS 背景的人，未來能在在半小時內（我這次用了兩個小時）打造出專業且具備深度內容的散步地圖。

---
### 🤖 AI 協作宣告
*   **本文內容**: 由人類作者提供實戰歷程與經驗總結，Antigravity 協助整理撰寫。
*   **技術實作**: 文中提及的自動化腳本、資料庫同步邏輯以及 Troubleshooting (如 .nojekyll) 皆為人機協作解決之成果。
