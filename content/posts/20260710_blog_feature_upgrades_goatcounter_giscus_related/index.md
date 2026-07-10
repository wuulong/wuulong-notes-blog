---
title: "網站大改造！利用「網頁發想選型 + Antigravity 精準落地」為部落格裝上計數器、留言與相關文章"
date: 2026-07-10T20:30:00+08:00
draft: false
categories:
  - Agentic AI (代理程式 AI)
  - Automation & Workflows (自動化與工作流程)
  - Methodology (方法論)
  - Personal AI Empowerment (個人 AI 賦能)
  - Productivity & KM (生產力與知識管理)
  - Software Engineering (軟體工程)
series:
  - "哈爸筆記網站"
tags:
  - Antigravity
cover:
  image: "cover.jpg"
  alt: "Blog Optimization Hub showing visitor charts, comments and related posts nodes"
  relative: true
---
一個靜態部落格（如我的「哈爸筆記」）在初期可以非常純粹，但隨著內容越來越多、讀者互動與流量統計的需求逐漸浮現，我們往往需要引入三個基礎建設：
1. **計數器/流量分析**：了解哪些文章比較受歡迎。
2. **留言系統**：與讀者互動、搜集反饋。
3. **相關文章推薦**：將零散的筆記串聯成知識網。

我今天成功地為我的 Hugo (PaperMod 主題) 部落格一次裝上了這三個功能。這次的改造過程，我再次驗證了我的 **「雙核人機協作方法論」**：**先在網頁版 AI 中選型發想、整理成結構化 AIQA，再交給地端 Agentic AI (Antigravity) 進行無摩擦代碼落地。** 

整個流程極度流暢，以下是我的實戰紀錄與思維分享：

---

## 🧭 階段 1：網頁端選型發想，AIQA 結構化落庫

我沒有一開始就讓地端 Agent 在程式碼庫裡盲目摸索。相反地，我先在網頁版的 AI (Gemini Web UI) 輸入我的需求，請它針對我的部落格架構給出改善建議，並進行「工具選型」：

### 📈 1. 流量分析選型：GoatCounter
* **痛點**：不希望傳統計數器破壞網頁美觀，且必須保護讀者隱私，同時希望過濾掉自己 localhost 開發時的流量。
* **決定**：選用 **GoatCounter**。它是隱私友善且極簡的 Telemetry 系統，讀者在前端完全看不見任何計數貼紙，只有作者能登入專屬後台看統計。而且它預設會忽略 localhost 流量。

### 💬 2. 留言系統選型：Giscus
* **痛點**：靜態網站如果用免登入留言板，很容易被垃圾廣告機器人（Spam Bots）轟炸，但自己維護資料庫又太重。
* **決定**：選用 **Giscus**。它利用 GitHub Discussions 的 API 作為後端。因為讀者留言必須登入 GitHub 帳號授權，這道「物理防線」直接將 99% 的網軍與廣告機器人擋在門外，且留言資料儲存在 GitHub 倉庫中，零維護成本。

### 📖 3. 延伸閱讀選型：Hugo Related Content
* **決定**：直接採用 Hugo 內建的 **Related Content** 機制。不需要載入額外的 JS 套件，Hugo 在靜態編譯時會自動透過圖論演算法，依據文章的 `tags`、`categories` 與 `date` 權重計算出相似度，靜態寫死在 HTML 中，速度極快。

我們將這些討論過程、以及網頁端 AI 幫我生成好的 script 模板與 TOML/YAML 設定，以標準的 **AIQA** 格式記錄下來，存入本地的知識庫中。

---

## ⚙️ 階段 2：Antigravity 地端接手，精準且無摩擦地落地

有了網頁端收斂出來的「明確規格」與「程式碼片段」後，我把這個關鍵 QA 直接丟給地端的 **Antigravity**。

因為指令極度明確、沒有混沌的雜訊，Antigravity 發揮了它「有手、有代碼操作能力」的特點，迅速在我的 Workspace 內完成了以下優雅的修改：

### 1. 埋入 GoatCounter 腳本
Antigravity 讀取了 `PaperMod` 主題的結構，沒有去修改 themes 目錄（避免主題更新時被覆蓋），而是非常聰明地在覆寫目錄中建立了 [extend_head.html](file:///layouts/partials/extend_head.html)，將 GoatCounter 的無形追蹤 script 寫入，完美實現全站自動載入。

### 2. 配置 Giscus 留言板
它同樣在 global layouts 目錄下建立了 [comments.html](file:///layouts/partials/comments.html)，嵌入 Giscus 的配置腳本，並修改了 [hugo.yml](file:///hugo.yml) 的 params，在全站全域啟用 `comments: true`。

### 3. 設定 Related Content 演算法與 UI 樣式
* **YAML 語法轉換**：因為網頁端產出的是 TOML 格式設定，Antigravity 自動將其轉譯為 `hugo.yml` 專用的 YAML 語法，設定了 tags (權重 100)、categories (權重 80) 與 date (權重 10) 的比對特徵。
* **客製化單篇文章 Layout**：它拷貝了主題的 `single.html` 到 [layouts/_default/single.html](file:///layouts/_default/single.html) 進行覆寫，在文章 footer 與留言板之間，插入了「延伸閱讀」的 HTML。為了適配網站的深色/淺色模式，它使用 PaperMod 的 CSS 變數（如 `var(--primary)`）進行樣式設計，並貼心地使用 `with` 語法包覆，當找不到相關文章時自動隱藏該區塊，維持視覺整潔。

---

## 🎯 實戰總結：發散與落地的完美分工

這次部落格的三大功能改造，從開始討論到全部寫入 commit 僅花了幾分鐘，而且沒有遇到任何 Bug 或編譯中斷。

這證明了 **「Web AI 腦袋發想選型 + Local Agent 雙手代碼實體化」** 的威力：
* **網頁端 (Web UI)**：適合做寬頻的、發散的、有噪聲的探索。在網頁端跟 AI 辯論選型，完全不用擔心污染本地代碼庫，更不怕 context 膨脹帶來的高昂 token 費用。
* **地端 (Antigravity)**：適合做窄頻的、高精準度的、需要實際讀寫檔案與執行環境檢測的工作。我們將網頁端收斂後的 AIQA 當作「合約」，交給 Antigravity 精準按圖施工。

這套方法讓我成功省下了大量無意義的 Debug 時間，將精力真正聚焦在網站的內容與功能設計上。

---

> **哈爸心得**：
> 不要指望一個 Agent 可以從你的混沌念頭中，直接無中生有生出完美的複雜系統。人類的職責是作為「選型決策者」與「過濾器」。在網頁端 AI 把想法梳理乾淨，記錄成 AIQA 後再呼叫地端 Agent 來執行，這才是最省錢、最流暢，也最符合工程美學的 AI 協作姿勢！

---

> **AI 協作聲明**：
> 本文由筆者提供原始網站功能改版心得與實戰流程，由 AI 助手 Antigravity 彙整架構與修辭。結合了靜態網站建置實務與哈爸筆記的敘事風格，展現人機協作下的個人 AI 應用成果。
