---
title: "WalkGIS 2.0 願景：打造去中心化的地理資訊協議 (Protocol)"
date: 2026-01-01T06:20:00+08:00
draft: false
categories: ["Project (專案)"]
series: ["WalkGIS"]
tags: ["Decentralized", "Protocol", "Community", "GitHub Pages", "Data Sovereignty"]
summary: "如果不只是我在做地圖，而是每個人都能擁有自己的地理資料庫？本文提出 WalkGIS 的下一步計畫：將其從單一網站昇華為一種類似 Podcast 的去中心化協議，讓每個人都能成為地圖創作者，並透過開放市集共享成果。"
---

在 [WalkGIS App 架構解密](/posts/20251230_walkgis_app_architecture/) 一文中，我們驗證了「Serverless + SQLite Browser」技術的可行性。但這只是一小步。

昨天與夥伴的一場激盪，讓我們看見了更大的可能性：**如果 WalkGIS 不只是一個網站，而是一套協議 (Protocol) 呢？**

![WALKGIS2.0藍圖與願景](WALKGIS2.0藍圖與願景.png)

## 核心概念：地理資訊的 Podcast 化

目前的地理資訊平台（如 Google Maps, AllTrails）大多是中心化的：你的資料存在他們的伺服器上，呈現方式由他們決定。

我們想像中的 WalkGIS 生態系，更像是 **Podcast** 或 **RSS** 的運作模式：

*   **WalkGIS Data Node (資料節點)** = **Podcast 節目源 (RSS Feed)**
    *   這是由**你**擁有的 GitHub Repo。
    *   也就是你的個人地圖資料庫。你想做「京都拉麵地圖」還是「自家附近的秘密小徑」，完全由你決定。資料主權在你手上。
*   **WalkGIS Core Viewer (通用瀏覽器)** = **Podcast 播放器 (如 Apple Podcast)**
    *   這是一個通用的前端 App (Web Viewer)。
    *   它不儲存資料，它只負責「播放」（渲染）你提供的資料來源 URL。
*   **WalkGIS Market (地圖市集)** = **Podcast 目錄**
    *   一個彙整中心，讓大家發現有趣的個人地圖節點，並訂閱收看。

## 架構實作：三部曲計畫

為了達成這個「去中心化地圖市集」的願景，我們規劃了三個階段的推進計畫：

### 1. 前端 App 升級：多重來源切換 (Multi-Source Support)
目前的 WalkGIS App 只能讀取我個人的資料。未來的 2.0 版本將加入「資料來源選擇器」：
*   **介面升級**：使用者可以在 App 中輸入任意的 GitHub Pages URL（例如 `https://yourname.github.io/my-map/`）。
*   **動態載入**：App 會即時切換指向，載入對方的 `walkgis.db` 與 Markdown 內容。這意味著，同一個 App 可以瀏覽全世界成千上萬個不同的個人地圖庫。

### 2. 打造「地圖新手包」 (Starter Template Kit)
為了降低參與門檻，我們不能要求每個人都從頭架設資料庫。
我們將釋出一個 **GitHub Template Repo**，裡面包含：
*   **預設結構**：已經建好的 `walkgis.db` 空殼與目錄架構。
*   **AI 代理人任務 (`.agent/tasks/`)**：這是最強大的武器。你不需要懂 SQL 或寫程式，只要呼叫我們寫好的 AI Agent Task，給它一個地點清單，它就會自動幫你搜尋、建檔、寫入資料庫。

這就像是我們提供了「微波料理包」，你只需要有微波爐 (GitHub Pages) 和一點點創意 (地點清單)，就能端出一盤好菜。

### 3. 文件與指引 (The "How-to")
最後，我們將建立完整的「5 分鐘建站教學」，教導非技術背景的使用者：
1.  Fork Template
2.  呼叫 Agent 生成地圖
3.  開啟 GitHub Pages
4.  將網址貼回 WalkGIS Viewer 分享給全世界

## 結語：讓地圖回歸個人

我們相信，最精彩的地理資訊往往掌握在在地人手中。透過這個協議化、去中心化的架構，WalkGIS 希望能賦權給每一個人，讓大家不僅是地圖的使用者，更是地圖的創造者。

這是一個將「個人足跡」連結成「集體記憶」的實驗，邀請你一起加入。

---
### 🤖 AI 協作宣告
*   **本文內容**: 由人類作者口述願景，Antigravity 協助整理與撰寫。
*   **架構發想**: 文中的 Podcast 類比與三部曲實作計畫，源自於人機協作過程中的架構分析建議。
