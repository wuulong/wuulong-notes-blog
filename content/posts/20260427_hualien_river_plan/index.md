---
title: "AI 代理與河流探索：花蓮溪流域計畫的建構實踐與 GIS 踩坑筆記"
date: 2026-04-27
tags: ["AI Agent", "GIS", "花蓮溪", "WalkGIS", "開發心得"]
categories: ["技術隨筆"]
author: "Antigravity/哈爸"
---

# 從混亂到標準：花蓮溪計畫的建構經驗分享

在建構「花蓮溪流域探索計畫」的過程中，我們不只是在畫地圖，更是在進行一場 AI 協作的高難度操演。這篇文章紀錄了如何將原始的 GIS 圖資，透過代理人技能（River Exploration Skill）轉化為可導航、具備文史脈絡的數位資產。

## 🛠 技術核心：三位一體架構
這次實作再次驗證了 WalkGIS 專案的「三位一體」存儲原則：
- **Maps (地圖定義)**：存於 `maps/` 目錄，透過 Mermaid 邏輯圖建立流域的骨架。
- **Features (點位描述)**：存於 `features/`，扁平化管理 9 個核心景點（馬太鞍、銅門等）。
- **Data (空間實體)**：存於 `data/`，包含整合後的 KML。

## ⚠️ 那些讓我們「卡住」的 GIS 陷阱
在開發過程中，我們遇到了幾個關鍵技術瓶頸，也同步修復並升級了 AI 技能手冊 (SOP S2.0)：

### 1. 編碼的幽靈：BIG5 vs UTF-8
官方的 `RIVERL.shp` (中央管河川水系) 依然保留著 BIG5 編碼的歷史痕跡。在 AI 自動萃取時若未指定編碼，會導致全台河名亂碼。
> **心得**：在 Python 或 GDAL 處理時，強制鎖定 `SHAPE_ENCODING=BIG5` 是實踐河流探索的第一步。

### 2. 幾何碎片化與清單爆炸
初始導出的 KML 檔案在 Google My Maps 中會出現數百條「花蓮溪」的碎片，導致左側清單無法閱讀。
> **解決方案**：必須執行 `dissolve(by='RV_NAME')` 將幾何圖形物理合併。這讓我們從「滿目的碎片」回歸到「一條完整的大河」。

### 3. 色彩代碼的 AABBGGRR 格式
KML 並非使用常見的 RGB，而是反過來的 ABGR。我們將主流定義為 `ff0000ff` (紅色)，確保在任何底圖上都能一眼鎖定主流位置。

## 📍 定位：從模糊搜尋到 API 定錨
以前我們依賴網頁搜尋，這次我們全面強制使用 **Google Maps API**。
透過 Place ID 的注入，我們能確保「米棧古道」與「箭瑛大橋」的座標精度達到公尺級，這對日後在現場使用 ATAK 導航至關重要。

## 🌏 成果展現
目前這套流程已經被封裝進 `river-exploration` 技能中。透過這套自動化路徑，我們成功產出了：
- [互動地圖 (Google My Maps)](https://www.google.com/maps/d/edit?mid=1FjTWECjGJk5U7GCOCfi2I5pb4AeeOxI&usp=sharing)
- [WalkGIS 地圖主檔](https://walkgis-544663807110.us-west1.run.app/?node=official&map=20260427_hualien_river_exploration)

## 💡 結語：AI 代理的進化
這次的經驗分享不只是為了記錄工具的使用，更是為了優化 AI 代理人的「認知連續性」。透過修正技能手冊，下一回進行「卑南溪」或「淡水河」計畫時，AI 將不再迷失在編碼與路徑中，實現真正的「軟體定義地景」。

---
*本文紀錄於 2026-04-27 花蓮溪計畫任務 [T260427-HHH03] 結案之際。*
