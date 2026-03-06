---
title: "地底下的台灣：如何用 AI 打造『全台考古遺址』知識 Master Registry"
date: 2026-03-06T10:00:00+08:00
draft: false
tags: ['WalkGIS', 'HGIS', 'AI', '考古', '曾文溪', 'Taiwan History Atlas']
categories: ['Project (專案)']
series: ["台灣史探索"]
description: "HGIS 系列第八篇：探討如何整合文資局與中研院多方數據，建立全台 2,563 處遺址的 Master Registry，並運用 AI Agent 進行 Layer 1 至 Layer 2 的知識建模與血緣追蹤。"
---

在之前的 HGIS 系列中，我們主要處理的是「紙上的歷史」——透過方志與古籍還原清代的社會空間。然而，要真正觸摸到「台灣主體性」最深層的脈絡，我們必須將目光投向更長的時間尺度：**考古遺址**。

如果說《臺灣通史》記載的是數百年的族群演進，那麼埋藏在台南平原地底下的「文化層」，則是長達數千年的地景變遷證詞。

今天，我正式在 [Taiwan History Atlas](https://github.com/wuulong/taiwan-history-atlas) 專案中發布了 **v260306.1 更新**，核心重點就在於建構一套具備「血緣追蹤」能力的 **考古遺址 Master Registry (主註冊表)**。

---

## 🏛️ 為什麼我們需要 Master Registry？

在處理全台遺址資料時，最頭痛的不是「沒資料」，而是「資料太多且碎片化」。文資局有「法定遺址」、中研院有「普查遺址」、地方政府還有「疑似遺址」。

要在 AI 輔助下進行科學分析，我們不能只是貼貼補補，必須建立一個 **Master Registry**：
1.  **資料對齊**：解決同一個遺址在不同單位有不同名字 or 座標微差的問題。
2.  **層級化建模**：將原始資料 (L0) 轉化為帶有語義標籤的實體 (L1)，再整合進知識中樞 (L2)。
3.  **血緣追蹤 (Source Origin)**：每一筆數據都能回溯到是哪個單位的原始點位，確保「證據力」。

目前這套系統已成功整合了 **2,563 處** 遺址，成為我們 HGIS 引擎中最堅實的核心數據庫。

---

## 🛠️ 核心腳本與工作流 (Scripts Toolkit)

在 `taiwan-history-atlas` 儲存庫中，我們透過以下工具實現了這一流程：

### 1. Layer 1：實體萃取與特徵標記
利用 `scripts/extract_entities.py`，AI 會自動掃描原始 Open Data 文本，提取出：
- **文化年代**：從大坌坑、蔦松到金屬器時代。
- **遺址等級**：Rank 1（國定）到 Rank 4（疑似）。
- **特徵標籤**：貝塚、石器、多層疊壓等。

### 2. Layer 2：跨庫遷移與合成
使用 `scripts/atlas_migrator.py`，將分散在各區域的實體統一遷移至 `data/history_atlas.db`。這個過程不只是搬家，更是在進行「去重 (De-duplication)」與「血緣標註」。

---

## 🤖 不只是資料：外掛式 AI Skill (HGIS Architect)

這是我最想分享的概念：本專案不只是一個 Repo，它更是一套 **「外掛式 AI 技能 (AI Skill)」**。

在 `skill/SKILL.md` 中，我封裝了 `hgis-atlas-architect v2.0` 藍圖。當你將此儲存庫交給具備代理能力 (Agentic AI) 的 AI 助理（如 Claude, Gemini, Antigravity 等），它能自動：
1.  讀取 `history_atlas.db` 並理解遺址的分佈規律。
2.  根據你輸入的座標，自動判斷該處在史前時代可能的地貌與文化背景。
3.  利用儲存庫中的腳本，重新為新的區域建立 HGIS 知識模型。

這是從「給 AI 魚吃」轉向「給 AI 釣竿」的實踐。

---

## 🔜 下一步：超越物理地表的分析

有了這 2,560 多個遺址點位作為「感測器」，我們接下來要做的，是透過 AI 進行 **Layer 4：空間拓樸分析**。

我們將計算這些地點與河道的距離、海拔高度，並推導出三千年來，曾文溪流域的住民是如何在海退人進的過程中，寫下他們的生存史詩。

這部分的深度報告與工具，我已經同步更新在專案文檔中，歡迎大家前往探索：
👉 [Taiwan History Atlas (GitHub)](https://github.com/wuulong/taiwan-history-atlas)

---
*本文由 AI 助理與哈爸透過 [bmad-pa](https://github.com/wuulong/bmad-pa) 指令集共同協作，運用大數據與地理分析技術產製。*
---
*哈爸筆記 - HGIS 系列持續更新中*
