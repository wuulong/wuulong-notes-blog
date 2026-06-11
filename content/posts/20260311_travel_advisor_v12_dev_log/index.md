---
title: "[哈爸筆記] 讓 AI 擁有地理動向的靈魂：智慧行車導遊兩日開發實錄"
date: 2026-03-11T09:10:00+08:00
categories:
  - GIS & Mapping (地理資訊與地圖)
  - GenAI (生成式 AI)
  - Productivity & KM (生產力與知識管理)
  - Travel & Geography (旅行與地理)
series: ["智慧導遊"]
tags:
  - GIS
  - Gemini
  - Open Data
draft: false
---
最近兩天，我跟我的 AI 夥伴 (Antigravity) 泡在 `Travel-Advisor-HUD` 這個專案裡。目標很單純：**讓我的行車助理不再只是「唸出路名」，而是像個真正懂我的「私人導遊」。**

在兩天的密集對話中，我們經歷了幾次關鍵的「卡關」與「破繭而出」，這幾個點我覺得是開發地理感知型 AI (Geographic AI) 最迷人的地方。

### 🚀 什麼是 Travel Advisor HUD？

這是一個跨裝置的行車助理系統：由 Mac 負責背景運算與大腦邏輯，iPad 則作為沈浸式視覺看板 (HUD)。它能感知你的位置、速度與航向，並結合你過去在 WalkGIS 筆記中的內容，由 Gemini 生成具備人文厚度的即時導覽。

---

### 🧩 關鍵卡關與突破

#### 1. 沉重的 Geopandas 與「資料主權」的執念
一開始，我們想用 Python 的 Geopandas 來處理鄉鎮邊界 (SHP) 的空間對位。但在路測邏輯中，Geopandas 顯得過於笨重，且我有一個堅持：**「資料主權」**。

我不想為了讓 AI 讀數據，就把我珍貴的 `walkgis.db` (私有筆記) 或內政部的圖資檔案搬來搬去、轉檔轉去。
*   **突破點**：我們轉向了 **SpatiaLite (SQLite 的空間外掛)**。
*   **心得**：透過 `ATTACH DATABASE` 直接掛載原始 DB，並用 `VirtualShape` 虛擬映射 SHP 檔案。資料「原地不動」，但查詢卻是極速的 SQL 指令。這讓「資料主權」與「運算效能」在這一層完美的對位了。

#### 2. 從「歡迎」到「盤點」的內容層次
原先的導覽很死板：進入新縣市就唸一段 Wiki 簡介。但開車的人真正需要的是：「這裡有沒有我以前記過的東西？」
*   **卡關**：AI 雖然強筆強大，但如果你不給它具體的「本地上下文」，它只會說些漂亮但空泛的廢話。
*   **突破點**：**「行政區點位盤點 (Township Inventory)」機制**。
*   **心得**：在跨越邊界的瞬間，系統自動在背景先發動一次空間點名，把該鄉鎮內所有關於我的私有筆記 POI 抓出來，做成摘要餵給 Gemini。當 AI 說出：「歡迎來到橫山，這裡有您之前筆記過的內灣車站喔...」時，那種「它真的懂我」的導覽感才算真正建立。

#### 3. Hammerspoon 的定時器與動態設定
Hammerspoon 雖然穩定，但預設的定時器是靜態的。如果我在開車中想調整檢查頻率（比如從 5 分鐘改成 1 分鐘），以往我得停下車，打開 Mac、改代碼、Reload Config。
*   **卡關**：駕駛中「Reload」是一個高風險且降體驗的舉動。
*   **突破點**：**「60秒脈動 (Base Tick)」機制**。
*   **心得**：我們重構了 Lua 定時器。讓它每一分鐘像「心跳」一樣跳動，跳動時再去讀取我的 iPad HUD 修改後的 `config.json`。這讓我可以直接在 iPad 上點一下設定，助理的報位節奏就瞬間改變，實現了真正的動態配置。

#### 4. 小螢幕的視覺困局
在 iPad 上，當 AI 真的寫出一篇長達千字的人文深度導覽時，我的精緻琉璃介面竟然「爆了」—— 資訊被切掉，看不到底部的儲存按鈕。
*   **突破點**：彈性佈局與 **Rolling History (歷史回溯)**。
*   **心得**：除了修正 CSS 捲動，最關鍵的是我們實作了「導覽歷史」。開車時聽不清楚、或是想回頭看剛才經過的地方，點開 `📜 History` 就能看最近 20 筆的完整故事。這解決了語音「聽過即逝」的痛點。

---

### 🔮 結語：AI 導覽的靈魂在於「對位」

這兩天的經驗告訴我，智慧助理的強大，不在於它會寫程式，而在於它能把**「枯燥的 GPS 座標」**與**「溫暖的私有記憶」**精準對位。

當我們把所有的資料源隱藏在一個「統一彙整層」下面時，AI 就不再只是工具，而是一個隨時能在正確的地點、唸出正確筆記的數位領主管家。

---

### AI 協作宣告 (AI Collaboration Disclosure)
> ![AI Generated](https://img.shields.io/badge/Content-AI%20Assisted-8A2BE2?style=flat-square&logo=google-gemini&logoColor=white) 
> ![Human Reviewed](https://img.shields.io/badge/Review-Human%20Verified-green?style=flat-square)
>
> **本文內容由 AI 協作生成**：
> 1.  **素材來源**：Travel-Advisor-HUD 專案實作紀錄與開發對話。
> 2.  **文章生成**：Antigravity 協助提煉關鍵卡關點並轉化為部落格敘事。
> 3.  **文章落地**：Antigravity 協助遵循 [hugo-content-wizard] 技能規範進行發布。
