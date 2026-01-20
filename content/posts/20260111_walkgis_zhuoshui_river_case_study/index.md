---
title: "實作筆記：從 Deep Research 到 WalkGIS 自動地圖生成 - 以濁水溪流域為例"
date: 2026-01-11
draft: false
tags: [AI, WalkGIS, Deep Research, Python, Automation, GIS]
categories: ["Project (專案)"]
series: ["WalkGIS"]
---

# 引言：打造「百科全書式」的流域地圖

一直以來，我對於製作「有深度」的地圖充滿熱情。一張好的地圖，不應該只是標記與導航，它應該能承載歷史的厚度、文化的溫度，以及地理空間的邏輯。

這次，我以台灣的母親河——**濁水溪**為範圍，嘗試進行了一次「百科全書式」的探索與實作。我的目標是將這條河流從合歡山源頭到麥寮出海口，涵蓋**自然地景、水利設施、人文史蹟、交通設施、災害環境**五大維度的知識，轉化為可互動、可導航的數位資產。

這篇文章記錄了我如何利用 AI Agent 與自動化腳本，將大量且發散的研究資料，快速收斂為 WalkGIS 系統中的標準化地圖。

# 實作流程解析

我的工作流主要分為三個階段：**Deep Research (發散)** -> **結構化萃取 (收斂)** -> **自動化生成 (Agent Task)**。

## 階段一：Deep Research 與維度定義

首先，我並不是直接開始畫地圖，而是先進行研究。我定義了濁水溪流域的五個觀察維度：

1.  **自然 (Nature)**: 包含源頭的合歡山、地質敏感的金門峒斷崖、以及河口的濕地生態。
2.  **水利 (Water Infrastructure)**: 這是濁水溪的靈魂。從上游的霧社水庫、武界壩，中游的集集攔河堰，到下游滋養彰雲平原的八堡圳與濁幹線。
3.  **人文 (Culture/History)**: 包含原住民部落（曲冰、武界）、客家文化（詔安）、以及漢人聚落（西螺、北斗）。
4.  **交通 (Transport)**: 見證歷史的西螺大橋、集集車站，以及現代的國道橋樑。
5.  **災害 (Disaster/Env)**: 誠實面對環境課題，如車籠埔斷層保存園區、地層下陷區。

我利用 AI 工具（如 Gemini）針對這些維度進行深度搜尋，挖掘出最具代表性的關鍵字與地點。

## 階段二：萃取清單 (The List)

研究之後，我將這些發散的資訊收斂為一份結構化的**景點清單 (List of Locations)**。這份清單不需要包含座標或詳細敘述，只需要準確的「名稱」與「分類」。

例如：
- 水利：八堡一圳、林內分水工
- 交通：西螺大橋、溪州大橋
- 人文：林先生廟、麥寮拱範宮

這份清單，就是餵給 AI Agent 的「種子」。

## 階段三：Run Task - 自動化生成的魔法

這一步是效率爆發的關鍵。我定義了一個名為 `create-walkgis-map-from-list` 的 Agent Task，讓 AI 代理人幫我完成那些繁瑣的 GIS 建置工作。

我只需要輸入指令：
> "幫我建立一張『濁水溪流域百科全書地圖』，清單如下..."

接下來，Agent 自動執行了以下 pipeline：

1.  **POI Research (搜尋)**: 自動呼叫 Google Places API，針對清單中的地點搜尋經緯度、地址與 Place ID。
2.  **Data Cleaning (修正)**: 當遇到同名地點（如「水圳綠道」搜到嘉義而非雲林段）時，透過 Python 腳本進行校正。
3.  **Content Enrichment (豐富化)**: 這是 V3 版本的新功能！Agent 不再只產生空白的 Markdown，而是會去搜尋每個地點的**歷史緣起、特色故事、基本資訊**，並填寫進檔案中。
    *   *結果：原本只有名字的「八堡圳」檔案，現在包含了施世榜、林先生的傳說以及跑水節的由來。*
4.  **Database Injection (建檔)**: 自動將地圖 (Map)、圖層 (Layer)、圖徵 (Feature) 的關聯寫入 SQLite 資料庫 (WalkGIS DB)，並建立 WKT 幾何資料。
5.  **Visual Enhancement (視覺化)**:
    *   **Mermaid 圖表**: 自動生成地圖的拓樸結構圖。
    *   **AI 封面圖**: 使用 Nano Banana (Image Gen) 根據「濁水溪、水利、稻田」等關鍵字，生成一張風格化的封面圖。
6.  **Artifacts Export (產出)**:
    *   **KML**: 供 Google Earth / Maps 使用。
    *   **NotebookLM Context**: 產生一份整合所有知識的長文本 Markdown，讓我可以直接丟進 NotebookLM 進行 RAG (檢索增強生成) 問答。

# 成果與反思

透過這個流程，我在極短的時間內，就從「一個想法」變成了一個「完整的 GIS 專案」。

產出的成果包含：
- 一個包含 48+ 個關鍵景點的 WalkGIS 資料庫。
- 數十篇內容豐富的景點 Markdown 筆記。
- 一張可導航的 KML 地圖。
- 一份可以跟 AI 對話的濁水溪知識庫。

**這就是 AI Agent 賦能地理研究的威力。** 它並沒有取代研究者對地點的篩選與品味（第一階段），但它接原本最耗時的資料查找、格式轉換與建檔工作（第三階段）完全自動化了。讓我們能更專注於發掘土地背後的故事。


## 資源
- [WalkGIS:濁水溪流域百科全書式探索](https://walkgis-544663807110.us-west1.run.app/?map=20260111_zhuoshui_river)


- [濁水溪流域百科全書式探索 google doc](https://docs.google.com/document/d/1CH_I3Te7Bx_fHAUe0iV8zWVrJKB0BbNCI3aNiM9maYA/edit?usp=sharing)

---

> **AI 協作聲明**：
> 本文內容由筆者與 AI 助手 Antigravity 共同撰寫。從 Deep Research 的維度發想、資料搜集，到 Python 自動化腳本的除錯與優化，AI 在其中扮演了關鍵的執行角色，協助將複雜的流域資訊轉化為結構化的 WalkGIS 地圖。
