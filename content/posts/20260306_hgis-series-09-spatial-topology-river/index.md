---
title: "空間拓樸：尋找遺址與河的『生存甜蜜點』"
date: 2026-03-06T11:00:00+08:00
draft: false
tags:
  - AI
  - AI Agent
  - GIS
  - GitHub
  - HGIS
  - WalkGIS
  - 哈爸筆記
  - 曾文溪
  - 河流探索
  - 知識管理
categories:
  - Agentic AI (代理程式 AI)
  - GIS & Mapping (地理資訊與地圖)
  - History & Culture (歷史與文化)
  - Productivity & KM (生產力與知識管理)
  - River Exploration (河流探索)
  - Software Engineering (軟體工程)
series: ["台灣史探索"]
description: "HGIS 系列第九篇：跳脫傳統圖資限制，運用 Layer 4 空間拓樸技術，計算全台 2,249 個遺址與流域河道的距離規律，解讀史前先民在曾文溪流域的選址智慧。"
basins:
  - 曾文溪

---
當我們在地圖上標註了全台兩千五百多個考古遺址後，下一個問題是：**「為什麼他們要住在這？」**

在傳統的 HGIS 中，我們習慣去找「古地圖」。但面對三千年前的遺址，世界地圖還是一片空白。這時，我們必須切換思維，引入 **Layer 4：空間拓樸分析 (Spatial Topology)**。

---

## 📐 什麼是 Layer 4？跳脫物理地表的「相對關係」

如果說 L1 是點位，L2 是知識，那麼 **Layer 4** 就是「點與環境的交互作用」。

我不想只是知道遺址在哪裡，我想知道它與「生存資源」——特別是**河流**的幾何關係。在曾文溪流域，河道會擺盪、海岸線會進退，但人類對於「取水與避災」的空間邏輯往往是恆定的。

透過 `scripts/poc_l4_tributary_clustering.py` 這個對合引擎，我們讓 2,249 個遺址自動去尋找它們對應的主流與支流，計算出精確的「離水距離」。

---

## 📊 數據發現：離水 2.5 公里的生存密碼

透過分析，我們在曾文溪流域發現了一個驚人的統計規律：

*   **濱海初始期**：離水最近距離平均約 **2,700 公尺**。
*   **長期定居點**：離水最近距離平均約 **2,200 公尺**。

這是一個 **「生存甜蜜點」**。
在那個沒有堤防的年代，住得太近（如 1km 內）會面臨曾文溪猛烈氾濫的改道威脅；住得太遠又取水不便。
這 **2.5 公里的緩衝帶**，正是史前先民在沒有現代水利工程的情況下，利用地形與距離「換取安全」的生存智慧。

---

## 🛠️ 核心工具：空間特徵標記 (Feature Extractor)

為了實現這種規模的運算，我在儲存庫中提供了一個關鍵腳本：
- **`scripts/feature_extractor.py`**：它不只記錄座標，更會透過幾何運算為每個點位打上「空間標籤」。例如：是否位於「河流樞紐」、屬於哪個「次流域」、以及其「離水梯度」。

這樣的設計，讓 AI Agent 在解讀資料時，不再只是讀到一串數字，而是讀到一個 **「人類與環境博弈的空間邏輯」**。

---

## 🤖 AI Skill 的深度應用

這項分析成果已整合進我們的 **[HGIS Architect AI Skill](https://github.com/wuulong/taiwan-history-atlas/blob/main/skill/SKILL.md)**。

目前的 AI 助理不再只是會翻翻方志摘要，當你開啟此 Skill 並指向一個座標時，它能調用 L4 的拓樸數據告訴你：「這個位置雖然現在離曾文溪很遠，但在三千年前，它正好位於主要支流的交會口，是一個戰略性的交通節點。」

這就是我們如何將「數據」轉化為「專業洞察」的過程。

---

## 🔗 探索開源成果
你可以直接下載我們的 `history_atlas.db`，或是閱讀最新的分析報告：
👉 [曾文溪流域聚落時空移轉深度分析報告](https://github.com/wuulong/taiwan-history-atlas/blob/main/docs/settlement_shift_report.md)
👉 [Taiwan History Atlas (GitHub)](https://github.com/wuulong/taiwan-history-atlas)

---
*本文由 AI 助理與哈爸透過 [bmad-pa](https://github.com/wuulong/bmad-pa) 指令集共同協作，透過 L4 空間拓樸引擎分析產製。*
---
*哈爸筆記 - 尋找史前時空的幾何秩序*
