# WalkGIS Project (V0.1.0)
> 專為 Agentic AI 設計的輕量級 GIS 資料庫與協作系統。

![Version](https://img.shields.io/badge/version-0.1.0-blue)


## 專案簡介
這是「全台散步地圖」的核心資料專案。此目錄作為 GIS 資料的「單一來源 (Single Source of Truth)」，包含 SQLite 資料庫與原始靜態資源。

## 目錄結構

*   **`walkgis.db`**: 核心資料庫 (SQLite + WKT Geometry)。儲存所有圖層、景點資訊與元數據。
*   **`assets/`**: 靜態資源庫。
    *   `images/`: 存放探訪時拍攝的原始照片。
    *   `docs/`: 存放 GPX 軌跡檔、PDF 參考文件等。
*   **`features/`**: 存放結構化的景點介紹文件 (Reference Markdown)。
    *   命名規則：`{YYYYMMDD}_{簡短英文ID}.md` (例如：`20251212_houli.md`)。
    *   此 ID 亦作為資料庫中該 Feature 的唯一識別參考。
*   **`scripts/`**: 工具腳本。
    *   `init_db.sql`: 資料庫初始化腳本。

## 協作工作流 (Workflow)

### 1. 資料探勘與記錄 (Data Entry)
*   將照片存入 `assets/images/`。
*   建立 Feature 文件於 `features/`，例如 `features/20251212_houli.md`。
*   利用 Agent 將景點資訊寫入 `walkgis.db`，其中：
    *   `meta_data` 欄位應包含 `{"feature_id": "20251212_houli", "ref_doc": "features/20251212_houli.md", ...}`。
    *   圖片路徑使用相對路徑 (e.g., `assets/images/photo.jpg`)。

### 2. 內容發布 (Content Publishing)
當需要在 Blog (`wuulong-notes-blog`) 撰寫遊記時：
1.  從 `walkgis.db` 查詢相關景點資訊作為素材。
2.  將所需的圖片從 `assets/images/` **複製** 到 Blog 的 `static/images/` 目錄。
3.  在 Markdown 文章中引用 Blog 的圖片路徑。

---
**注意**：此資料夾應視為獨立專案進行版控與備份。
