# WalkGIS 專案資源庫 (WalkGIS Project Resources)

歡迎來到 **WalkGIS** 專案的資料與自動化核心。本目錄包含了所有用於生成 [WalkGIS 部落格](https://wuulong.github.io/wuulong-notes-blog/) 上互動地圖與歷史敘事的原始數據、資料庫架構、自動化腳本以及地圖定義檔。

## 📂 專案結構 (Project Structure)

*   **`features/`**: 地圖的原子單位。每個 Markdown 檔案代表一個景點 (POI)，包含元數據（座標、標籤）與豐富的描述內容。
*   **`maps/`**: 地圖定義檔。
    *   `.md` 檔案: 包含地圖元數據以及使用 Mermaid.js 繪製的路線流程圖。
    *   `.kml` 檔案: 匯出的地理空間資料，可直接匯入 Google My Maps 與 Google Earth。
*   **`sql/`**: 資料庫管理。
    *   包含用於初始化架構、插入景點資料以及定義地圖關聯的 SQL 腳本。
*   **`scripts/`**: 自動化工具。
    *   Python 腳本：用於生成 KML 檔案與 Google Maps 導航連結。
    *   Shell 腳本：用於批次處理任務。
    *   `gen_notebooklm_context.sh`：將地圖資料打包成 AI 敘事可用的上下文檔案 (供 NotebookLM 使用)。
*   **`tasks/`**: Agentic AI 任務定義檔。
    *   `create-walkgis-map-from-list.md`：AI 代理人的藍圖，能自動從一份簡單的地點清單，完成搜尋、Markdown 生成、資料庫注入到 KML 匯出的全流程。
*   **`walkgis.db`**: SQLite 資料庫，作為所有地圖數據的單一事實來源 (Single Source of Truth)。

## 🚀 核心工作流 (Key Workflows)

### 1. 建立新地圖 (Agentic Way)
這是擴充本專案最強大的方式，使用 `tasks/` 中的定義檔：
1.  提供一份地點清單給 AI 代理人。
2.  執行任務 `create-walkgis-map-from-list.md`。
3.  代理人將自動完成網路搜尋、檔案建立、SQL 注入以及 KML 匯出。

### 2. 手動匯出 (Manual Export)
若要將特定地圖匯出為 KML：
```bash
python3 scripts/export_map_{map_id}.py
```

### 3. AI 內容生成 (AI Content Generation)
若要建立 Google NotebookLM 專用的上下文檔案：
```bash
./scripts/gen_notebooklm_context.sh {map_id}
```

## 🔗 相關文章 (Related Articles)

*   [WalkGIS V0.1發布：專案理念與技術基石](/posts/20251229_walkgis_v0_1_release/)
*   [WalkGIS 自動化之路：打造「地圖生成工廠」](/posts/20251230_walkgis_automation_task/)
*   [實戰案例：大甲溪溯源與智慧水圳地圖](/posts/20251229_walkgis_case_study/)

---
*Created by [Wuulong](https://github.com/wuulong) & [Antigravity](https://google.com)*
