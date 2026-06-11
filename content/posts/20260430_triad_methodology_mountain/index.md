---
title: "山脈水文探索的三柱架構：邏輯、證據與實踐的數位循環"
date: 2026-04-30T11:00:00+08:00
categories:
  - Agentic AI (代理程式 AI)
  - Methodology (方法論)
  - Productivity & KM (生產力與知識管理)
  - River Exploration (河流探索)
series: ["2026台灣河流探索"]
tags:
  - Antigravity
featured_image: "featured.png"
description: "如何管理一本書、一個資料庫與一段實地走訪的關係？本篇介紹我們在山脈水文專案中實踐的『三柱架構』，以及如何透過 AI 代理人的技能體系實現複雜地理分析的自動化。"
---
# 山脈水文探索的三柱架構：邏輯、證據與實踐的數位循環

在處理像「台灣山脈水文」這樣複雜的主題時，我們往往會陷入資料碎片化的困境：筆記在 Markdown 裡、數據在 Excel 裡、心得在部落格裡，彼此互不相連。

為了打破這個僵局，我們在 `bmad-pa` 專案中實踐了一套名為 **「三柱架構 (Triad Methodology)」** 的知識工程方法。

## 1. 何謂三柱架構？

這套架構將知識產出分為三個互為支撐的支柱：

*   **邏輯柱 (Logic - The Book)**：這是專案的「大腦」。它負責定義理論架構（如越嶺效率理論）、撰寫書本章節。它是定性的、引導性的。
*   **證據柱 (Evidence - The Database)**：這是專案的「肌肉」。它負責儲存結構化數據（如能高古道的 2533 個點位、海拔、坡度）。它是定量的、可驗證的。
*   **實踐柱 (Practice - The Log)**：這是專案的「足跡」。它包含 POC 實證報告、哈爸筆記遊記。它是動態的、與現實對接的。

**核心紀律**：任何邏輯上的修正，都必須在資料庫中找到證據；而實踐中的發現，則會回頭修正邏輯與數據結構。

## 2. AI 代理人的技能賦能 (Skill-based AI)

在這次能高古道的分析中，我們之所以能快速破解 DTM 下載攔截與座標對合，歸功於我們將專業知識「技能化」：

- **`dtm-acquisition-navigator`**：封裝了政府開放資料的爬取邏輯與非標準 DTM 格式的解析智慧。
- **`qgis-project-architect`**：實現了「軟體定義地圖 (SDM)」，讓 AI 能直接產出配置好渲染規則的 QGIS 專案。
- **`triad-methodology-architect`**：負責維護三柱之間的連結，確保 `BUILD_LOG.md` 紀錄了每一個關鍵決策。

## 3. 軟體定義地圖 (Software Defined Map)

我們在專案中推動「數據與地圖分離」的紀律：
- **YAML/SQLite 是唯一的數據源**。
- **VRT (Virtual Table) 是空間視角**。
- **QGIS 專案只是一個「樣式注入器」**。

這種做法讓我們能實現「注入 -> 渲染 -> 清空」的自動化流程。地圖不再是死板的圖檔，而是可以用程式碼生成的「動態論證」。

## 4. 結語：建立可進化的知識體系

透過這套方法論，我們正在建立的不是一個靜態的 Atlas，而是一個 **「會呼吸的知識系統」**。每一個新流域的加入，都在強化這三根支柱。

> **AI 協作聲明**：本方法論由 Antigravity 助手協作設計，落實了從知識建模到工具鏈自動化的完整閉環。

---
*本方法論的具體實作細節，請參考專案： [mountain-hydrology-atlas (GitHub)](https://github.com/wuulong/mountain-hydrology-atlas)*
