---
title: "打破部門孤島：開放開源《台灣農漁畜開放數據全景圖鑑》與大一統資料引擎 tw-agro-db"
date: 2026-08-20T13:30:00+08:00
draft: false
categories:
  - "GenAI (生成式 AI)"
  - "Agentic AI (代理程式 AI)"
  - "System Engineering (系統工程)"
  - "Software Engineering (軟體工程)"
series:
  - "架構推動"
tags:
  - "tw-agro-db"
  - "SQLite"
  - "GraphRAG"
  - "OpenData"
  - "FTS5"
  - "Python"
cover:
  image: "cover.webp"
  alt: "台灣農漁畜開放數據全景圖鑑"
  relative: true
---

在推動 AI 落地與數據架構的過程中，我們常常遇到一個很真實的痛點：**「資料明明都在開放平台上，但要拿來做決策或餵給 AI 時，卻像是在拼一幅散落在十幾個不同政府門戶的拼圖。」**

以臺灣的農業生態為例，農糧署拍賣行情、藥毒所農藥許可證、TFDA 食品農檢 MRL 預警、有機資材名冊、漁業署水產交易與水質監測、畜產會毛豬拍賣、動物用藥殘留、氣象署農業氣象站、環境部土壤水質重金屬，乃至於聯合國 FAO 的國際農學詞庫（AGROVOC）——這些資料分別隸屬於不同的單位，採用不同的 API 格式、不同的日期標籤（例如民國年 vs. ISO 日期），甚至連產品名稱都沒有標準化。

為了解決這個問題，我正式開放開源了 **`tw-agro-db` (台灣農業開放大數據引擎)** 以及配套的專書 **《台灣農漁畜開放數據全景圖鑑：從產地行情到食安防禦的資料體系》**。

---

## 💡 這不是另一個 API 封裝，而是「大一統知識體系」

`tw-agro-db` 的核心哲學並不是去寫幾十個爬蟲或 API 包裝函式，而是**將碎片化的開放數據熔煉為單一可攜帶的 SQLite 知識大腦 (`agro.db`)**。

這意味著不論是農民、產銷班、食安稽查人員，還是正在開發大語言模型 (LLM Agent) 的工程師，都不再需要處理網路斷線、API 頻率限制或格式不一致的問題。只要擁有一個幾十 MB 到幾百 MB 的單一 SQLite 檔案，就能在本地端實現**毫秒級的跨域穿透查詢**。

---

## 🎯 4 大 Pillar 與 12 大垂直 DB 的完整融合

在 `tw-agro-db` 的架構中，我們將全台開放數據解耦並重構成四大領域 Pillar，共涵蓋 12 個垂直數據庫：

1. **🌾 Pillar 1: 農糧資材 (Crop & Fertilizer)**
   - `A10` 農糧批發交易行情 DB（引入跨市場 $CV = \frac{\sigma}{\mu}$ 價格離散模型）
   - `A11` 農藥許可證與安全採收期 DB（9,993 筆藥證與 PHI 等待期分級）
   - `A12` 農檢 MRL 殘留抽驗預警 DB（$MRLRatio$ 超標預警模型）
   - `A13` 有機友善農場認證名冊 DB
   - `A14` 農糧資材與肥料登記證 DB（$NPK\_Total$ 養分算式與有機審定評等）

2. **🐟 Pillar 2: 水產養殖 (Fishery & Aquaculture)**
   - `A20` 水產產品與市場行情 DB（管道符 `│` 描述解析器與 80% 在地標籤）
   - `A21` 水質與寒害監測 DB（水溫 $<15^\circ\text{C}$ 寒害與溶氧缺氧 Alert）

3. **🐖 Pillar 3: 畜牧食安 (Livestock & Vet Drug)**
   - `A30` 毛豬批發交易行情 DB（無槓民國年 `1150819` 自動轉 ISO 日期）
   - `A31` 動物用藥殘留管制 DB（針對國定禁藥實施 $MRL = 0.0\text{ ppm}$ 零容忍即時攔截）

4. **🌤️ Pillar 4: 氣象環境與國際標準 (Environment & LOD)**
   - `A40` 農業氣象站歷史觀測 DB（2,527 點觀測微氣候序列）
   - `A41` 土壤與水質環境安全 DB（重金屬 $PollutionRatio \ge 1.0$ 高風險區域預警）
   - `A50` FAO AGROVOC 國際農學詞庫 DB（40,097 概念，將在地台規名詞對接國際 LOD）

---

## 👑 A00 Master Hub：事前融合防禦網與 GraphRAG

在 12 大垂直 DB 之上，我們建立了 **`A00 Master Hub` (母大腦中樞)**。它不只是將資料放到同一個 SQLite 裡，而是在資料入庫的瞬間，透過背景計算引擎發動 **5 大事前融合防衛網 (Safety Meshes)**：

- 🛡️ **農藥採收期預警網**：跨 `A10+A11+A12`，自動碰撞農藥許可證與採收等待期，標註高風險用藥。
- 🥩 **毛豬禁藥零容忍防禦網**：跨 `A30+A31`，對合拍賣市場與 TFDA 禁用藥物清單，0.01 秒完成食安攔截。
- 🌿 **有機農場資材合規網**：跨 `A10+A13+A14`，自動比對審定合格之有機肥料資材。
- ⚠️ **區域農地重金屬風險網**：跨 `A41`，計算重金屬污染比率，避免高風險農地誤種食用作物。
- 🌐 **FAO 國際本體對合網**：將台灣在地作物（如椰子）對接至聯合國 FAO AGROVOC 的國際概念（`c_1784`）。

此外，A00 母大腦更內建了 **346 筆 GraphRAG 實體圖譜網 (`a00_graph_triples`)** 與 **18,725 筆全域 FTS5 全文倒排 (`fts_agro_global`)**。這為下一代 Agentic AI 提供了 **100% 具備物理數據出處、零幻覺 (Zero-Hallucination)** 的接地 (Grounding) 基礎。

---

## 📦 完全開源與全本專書手冊釋出

為了讓這套大一統資料體系能真正賦能給產官學研各界，我們將所有的程式碼、CLI 工具、SQLite Schema、測試資料集與完整專書全部開源：

* **GitHub 開源倉庫**：[https://github.com/wuulong/tw-agro-db](https://github.com/wuulong/tw-agro-db)
* **全本專書手冊**：[FULL_BOOK_TAIWAN_AGRO_DB.md (32 章大一統全景圖鑑)](https://github.com/wuulong/tw-agro-db/blob/main/book/FULL_BOOK_TAIWAN_AGRO_DB.md)
* **全景簡報下載**：[台灣農漁畜開放資料全景圖鑑.pdf](https://drive.google.com/open?id=1RTKDG1PxhUDOq6IYolOsIbf5UodbdiF9&usp=drive_copy)

透過 `tw-agro-db`，我們希望展現的是：**當我們用系統工程與大一統架構去梳理開放數據時，資料不再只是靜止的二進位檔案，而是能跨域穿透、即時防禦並驅動智慧決策的強大資產！**

> **AI 協作聲明**：
> 本文由筆者提供架構觀念與釋出心法，由 AI 助手 Antigravity 彙整編撰與文字修辭。展現人機協作下推動台灣開放數據與 Agentic AI 架構的成果。
