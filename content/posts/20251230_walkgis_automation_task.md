---
title: "WalkGIS 自動化之路：打造「地圖生成代理人」與新竹水圳實戰"
date: 2025-12-30T06:00:00+08:00
draft: false
categories: ["Project (專案)"]
series: ["WalkGIS"]
tags: ["Task Design", "Python", "Feedback Loop", "Hsinchu"]
summary: "記錄如何將地圖製作流程封裝成可重複執行的 Agent Task，並以「新竹智慧水圳地圖」進行壓力測試與迭代修正的過程。"
---

在上一篇 [WalkGIS 實戰案例](/posts/20251229_walkgis_case_study/) 中，我們雖然成功建立了台中大甲溪與智慧水圳地圖，但過程仍包含許多「人工介入」：手動下指令搜尋座標、手動修復 SQL、手動執行腳本。

對於一名追求效率的開發者來說，重複兩次是偶然，重複三次就是模式。是時候把這個模式封裝成一個自動化的 **Task** 了。

## 1. 定義任務 (The Task Definition)

我建立了一個新的任務檔案 `.agent/tasks/create-walkgis-map-from-list.md`，試圖將地圖製作流程標準化。

這個任務的輸入非常簡單，只有兩樣東西：
1.  **地圖名稱** (例如：智慧水圳玩樂地圖-新竹管理處)
2.  **景點清單** (一串純文字的地名)

而任務的職責則包山包海：
*   🔍 **Research**: 自動上網搜尋每個點的 GPS 座標與歷史簡介。
*   📝 **Content**: 生成每個景點的 Markdown 檔案。
*   💾 **Database**: 生成 SQL 並寫入 SQLite (Features + Map + Relations)。
*   🤖 **AI Context**: 打包資料給 NotebookLM。
*   🗺️ **Visualization**: 產出 KML 與 Google Maps 導航連結。

## 2. 實戰測試：新竹智慧水圳 (The Test Run)

為了驗證這個 Task，我找來了「農田水利署新竹管理處」的 8 個景點清單，包括三叉埤、汀甫圳、隆恩圳等。

啟動任務指令：
```bash
run task create-walkgis-map-from-list.md
```

Agent 開始運作，分批搜尋座標、撰寫 Python 腳本來生成檔案。一切看起來都很美好...直到報錯出現。

## 3. 踩坑與回饋 (The Feedback Loop)

在執行過程中，我遇到了兩個主要問題：

### 問題一：漏掉的主角
我的 Python 腳本產生了所有的 Feature Markdown 和 SQL，卻獨獨忘了產生 **Map Markdown** 本身。導致後續的 NotebookLM 生成腳本 (`gen_notebooklm_context.sh`) 找不到地圖檔而崩潰。

### 問題二：相對路徑的陷阱
腳本中寫死了 `../../static/walkgis_prj/sql` 這樣的相對路徑。當 Agent 在不同目錄下執行指令時，這些路徑立刻失效，導致 `FileNotFoundError`。

## 4. 迭代修正 (Refinement)

這就是 Agentic Workflow 最迷人的地方：**失敗是為了優化流程**。我沒有手動修復檔案就草草了事，而是回頭修改了 Task 定義文件：

1.  **強制 Map MD 生成**：在 Task 中明確規定 Python 腳本必須同時生成 `maps/{map_id}.md`，並包含 Frontmatter 與 Mermaid 圖表。
2.  **路徑最佳實踐**：在 Task 中規範 Python 腳本必須使用 `__file__` 來定位自身位置，確保相對路徑永遠正確：
    ```python
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    SQL_FILE = os.path.join(SCRIPT_DIR, "../sql/create_map.sql")
    ```
3.  **搜尋分批策略**：明確定義搜尋批次大小，避免一次塞太多景點導致 Prompt 爆炸。

## 5. 最終成果

修正 Task 後，我們順利產出了 **[智慧水圳玩樂地圖-新竹管理處](https://www.google.com/maps/dir/24.7137,121.1268/24.8024,120.996/24.798,120.99/24.7203,121.0436/24.7715,121.0664/24.717,121.121/24.7985,121.0163/24.832,121.112)** 的所有資產：

*   ✅ **地圖檔案**: [2025_smart_water_fun_map_hsinchu.md](/wuulong-notes-blog/walkgis_prj/maps/2025_smart_water_fun_map_hsinchu.md)
*   ✅ **KML 圖資**: [2025_smart_water_fun_map_hsinchu.kml](/wuulong-notes-blog/walkgis_prj/maps/2025_smart_water_fun_map_hsinchu.kml)
*   ✅ **AI 素材包**: [walkgis_2025_smart_water_fun_map_hsinchu_notebooklm.md](/wuulong-notes-blog/walkgis_prj/walkgis_2025_smart_water_fun_map_hsinchu_notebooklm.md)
*   ✅ **資料庫 SQL**: [create_2025_smart_water_fun_map_hsinchu.sql](/wuulong-notes-blog/walkgis_prj/sql/create_2025_smart_water_fun_map_hsinchu.sql)

現在，WalkGIS 擁有了一個強健的「地圖生成工廠」。只要給我一個清單，我給你全世界（的地圖）。

---

### 🤖 AI 協作心得
本次任務展示了 "Prompt Engineering" 到 "Task Engineering" 的轉變。我們不再只是下指令，而是編寫「指令的程式碼 (Task Definition)」，並透過測試案例來除錯這個程式碼。這才是與 AI 協作的高級型態。

## 附錄：自動化任務定義 (Appendix: Task Definition)

以下是我們經過迭代後，最終定版的 Task 定義檔，您可以下載並參考使用：
[create-walkgis-map-from-list.md](/wuulong-notes-blog/walkgis_prj/tasks/create-walkgis-map-from-list.md)

---
### 🤖 AI 協作宣告
*   **本文內容**: 由人類作者規劃，Antigravity 協助撰寫。
*   **自動化設計**: 文中提及的 Task 與 Python 腳本邏輯由 AI 建議並實作，經人類驗證後定版。


