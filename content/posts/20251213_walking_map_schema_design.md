---
title: "大甲溪散步地圖：SQLite Schema 設計與 SpatiaLite 應用"
date: 2025-12-14T07:45:00+08:00
categories: ["GIS", "技術筆記"]
series: ["2026台灣河流探索","GenAI"]
tags: ["SQLite", "SpatiaLite", "Schema Design", "QGIS", "Open Data"]
draft: false
ShowToc: true
TocOpen: true
---

# 散步地圖資料庫 Schema 設計與考量

## 導言
本文件旨在闡述為「大甲溪散步地圖」專案設計的 SQLite 資料庫 Schema。此設計旨在平衡資料的結構化、靈活性與地理空間處理能力，以有效支援從網路資料蒐集到現場資料查證，再到最終 GIS 呈現的完整工作流程。

## 整體設計哲學
*   **核心資料結構化**：確保地理特徵的基本資訊（名稱、描述、類型）保持一致性，便於查詢與管理。
*   **非核心資料彈性化**：利用 JSON 格式的 `meta_data` 欄位，提供高度彈性來儲存多樣化且不斷演進的非核心屬性，無需頻繁修改資料庫 Schema。
*   **GIS 原生支援**：透過 SpatiaLite 擴展，直接在資料庫層面支援地理空間資料的儲存、查詢與分析。
*   **圖層正規化管理**：獨立的 `layers` 表格用於管理圖層的分類和 QGIS 呈現樣式，提高資料一致性和維護效率。
*   **AI 協作友好**：結構化且彈性的 Schema 設計，極大地方便 AI 代理進行資料的自動化處理、分析與驗證。

## 社區 GIS 背景資訊與 Layer 分類設計架構

### 社區 GIS 背景資訊
「社區 GIS」強調地理資訊系統在社區層級的應用，旨在支援地方居民參與、資源管理、文化保存、社會服務及永續發展。這類專案的核心在於將多樣化的在地資訊（例如：親水點、交通、設施、風險、文化景點、生態熱點等）以地理空間的形式進行收集、組織、分析與視覺化。其資料分類通常會考量到以下幾個面向：
*   **功能應用**：資料服務於哪種社區需求（如防災、生態教育、文化導覽）。
*   **資料類型**：具體的地理實體是什麼（點、線、面，以及相關屬性）。
*   **使用者視角**：如何讓在地居民和外部使用者最直觀地理解地圖內容。

### Layer 分類設計架構
為呼應社區 GIS 的精神，並支援 QGIS 等工具的靈活呈現，我們特別設計了 `layers` 表格來管理圖層的分類。其核心架構為 `layer_type` (主分類) 與 `layer_subtype` (次分類) 的組合，這種層次化設計有以下優點：

*   **清晰的層次結構**：透過 `layer_type` 劃分大類（如「水文與親水層」、「生態與景觀層」），再由 `layer_subtype` 細分具體內容（如「親水點」、「河床路徑入口」），使得圖層組織邏輯清晰。
*   **支持 QGIS 分類呈現**：`layer_type` 和 `layer_subtype` 欄位可以直接被 QGIS 作為分類符號化 (Categorized Symbology) 的依據，便於為不同類型的地圖元素設定視覺樣式。
*   **易於查詢與篩選**：使用者或 AI 可以根據這些分類欄位，快速篩選出感興趣的地理特徵，例如「查詢所有『用路人與車泊層』中『合法車泊點』的資訊」。
*   **可擴展性**：隨著地圖內容的豐富，可以靈活地增加新的 `layer_type` 或 `layer_subtype` 組合，而無需修改 `walking_map_features` 表格的結構。
*   **與 QGIS QML 整合**：`layers` 表格中的 `qgis_qml` 欄位可以直接儲存對應圖層的完整樣式定義，確保了視覺呈現的標準化和一致性。

## 表格 Schema 設計

### 1. `layers` 表格：圖層定義
此表格用於定義散步地圖中所有的圖層類型，並可關聯 QGIS 的預設呈現樣式。

#### CREATE TABLE Statement
```sql
CREATE TABLE layers (
    layer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    layer_type TEXT NOT NULL,                         -- 主分類 (例如：水文與親水層, 生態與景觀層)
    layer_subtype TEXT,                               -- 次分類 (例如：親水點, 河床路徑入口, 合法車泊點)
    qgis_qml TEXT,                                    -- 儲存 QGIS Style (QML 格式的 XML 字串或片段)，用於定義該圖層的視覺呈現
    description TEXT,                                 -- 該圖層的說明 (Markdown 格式)
    meta_data TEXT,                                   -- JSON 格式的備註資訊 (例如：{"source_url": "...", "last_updated": "..."})
    UNIQUE(layer_type, layer_subtype)                 -- 確保 layer_type 和 layer_subtype 的組合是唯一的
);
```

#### 欄位說明
*   **`layer_id`**: 唯一識別碼，自動遞增。
*   **`layer_type`**: 圖層的主分類，例如「水文與親水層」。
*   **`layer_subtype`**: 圖層的次分類，例如「親水點」。
*   **`qgis_qml`**: 儲存 QGIS 樣式定義的 XML 字串，直接將視覺化設定與圖層關聯。
*   **`description`**: 該圖層的詳細說明，支持 Markdown 格式。
*   **`meta_data`**: 用於儲存與圖層本身相關的額外備註資訊，例如資料來源、更新頻率等。

#### 範例 INSERT 語句 (親水點)
```sql
INSERT INTO layers (layer_type, layer_subtype, qgis_qml, description, meta_data) VALUES
('水文與親水層', '親水點', 
'<qgis version="3.28.3-Firenze" style-type="Point" symbol-name="square_red_marker">...</qgis>', -- 簡化為 ...
'### 親水點\n\n表示大甲溪流域中適合親近水域的地點，如河床路徑入口、戲水區等。\n\n**注意事項**：請特別留意安全資訊和季節性限制。',
'{"default_symbol_type": "marker", "related_activities": ["游泳", "涉水", "釣魚"], "safety_rating_scheme": "1-5星", "created_by": "Wuulong"}'
);
```

### 2. `walking_map_features` 表格：散步地圖特徵
此表格儲存散步地圖上的所有地理特徵（點、線、面），並透過 `layer_id` 關聯到 `layers` 表格。

#### CREATE TABLE Statement
```sql
CREATE TABLE walking_map_features (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,                         -- 特徵名稱 (例如：后里馬場、大甲溪河流線、緩衝區範圍)
    description TEXT,                           -- 特徵簡要描述 (Markdown 格式)
    layer_id INTEGER NOT NULL,                  -- 外鍵，關聯到 layers.layer_id
    geometry_type TEXT NOT NULL,                -- 幾何類型 (例如：Point, LineString, Polygon)
    meta_data TEXT,                             -- JSON 格式的非核心屬性
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP, -- 創建時間
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,  -- 最後更新時間
    FOREIGN KEY (layer_id) REFERENCES layers(layer_id)
);
-- SpatiaLite 幾何欄位會在表格創建後添加
-- SELECT AddGeometryColumn('walking_map_features', 'geom', 4326, 'GEOMETRY', 'XY');
```

#### 欄位說明
*   **`id`**: 唯一識別碼，自動遞增。
*   **`name`**: 地理特徵的名稱，例如「后里馬場」。
*   **`description`**: 該特徵的詳細描述，支持 Markdown 格式。
*   **`layer_id`**: 外鍵，指向 `layers` 表格中的 `layer_id`，建立特徵與圖層定義的關聯。
*   **`geometry_type`**: 明確指定該特徵的幾何類型，例如 `Point`, `LineString`, `Polygon`。
*   **`meta_data`**: 用於儲存該特徵獨有的、非核心的詳細屬性，以 JSON 格式儲存。
*   **`created_at` / `updated_at`**: 時間戳記，追蹤記錄的生命週期。
*   **`geom`**: 由 SpatiaLite 管理的幾何欄位，儲存實際的地理空間資料。

#### 範例 INSERT 語句 (后里馬場點位)
```sql
INSERT INTO walking_map_features (name, description, layer_id, geometry_type, meta_data) VALUES
('后里馬場', 
'### 后里馬場\n\n**地點**：台中市后里區\n\n自行車租借與大甲溪沿線鐵馬道騎乘的絕佳出發點。\n\n**特色**：腹地廣大，適合家庭活動與休憩。',
1, -- 假設 layer_id=1 對應到 '水文與親水層', '親水點' (需從 layers 表中獲取)
'Point',
'{"activities": ["自行車", "野餐", "兒童遊樂"], "facilities": {"廁所": "有", "餐飲": "有", "停車": "有"}, "best_visit_time": "上午"}'
);

-- 插入幾何資料 (範例：經緯度 120.73582, 24.298637)
-- UPDATE walking_map_features SET geom = ST_PointFromText('POINT(120.73582 24.298637)', 4326) WHERE id = (SELECT last_insert_rowid());
```

### 3. `meta_data_templates` 表格：元數據範本
此表格儲存用於指導 `walking_map_features.meta_data` 欄位填寫的 JSON 範本。

#### CREATE TABLE Statement
```sql
CREATE TABLE meta_data_templates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    template_name TEXT NOT NULL UNIQUE,       -- 範本名稱 (例如：親水點通用範本, 合法車泊點範本)
    applies_to_layer_type TEXT NOT NULL,      -- 此範本適用的圖層類型
    applies_to_subtype TEXT,                  -- 此範本適用的子類型
    template_json TEXT NOT NULL,              -- 儲存完整的 JSON 範例字串
    description TEXT                          -- 範本的簡要說明或用途 (Markdown 格式)
);
```

#### 欄位說明
*   **`id`**: 唯一識別碼，自動遞增。
*   **`template_name`**: 範本的名稱。
*   **`applies_to_layer_type`**: 該範本適用於的主圖層分類。
*   **`applies_to_subtype`**: 該範本適用於的次圖層分類。
*   **`template_json`**: 儲存標準的 JSON 結構範例字串。
*   **`description`**: 範本的詳細說明，支持 Markdown 格式。

#### 範例 INSERT 語句 (親水點 meta_data 範本)
```sql
INSERT INTO meta_data_templates (template_name, applies_to_layer_type, applies_to_subtype, template_json, description) VALUES
('親水點通用範本', '水文與親水層', '親水點',
'{"access_condition": {"vehicle_type": [], "road_surface": "", "difficulty": "", "seasonal_access": {"rainy_season": "", "dry_season": ""}}, "water_condition": {"flow_rate_estimate": "", "water_depth_estimate": "", "current_speed": "", "suitable_for_activities": []}, "safety_notes": "", "contact_person": {"name": "", "phone": ""}, "last_checked_date": ""}',
'### 親水點 Meta Data 範本\n\n此範本提供親水點相關的核心元數據結構，包含水文、安全和可達性等資訊，便於統一記錄。'
);
```

---


## SpatiaLite 幾何整合
上述 Schema 設計中，`walking_map_features` 表格的地理空間資料將由 SpatiaLite 進行管理。在創建 `walking_map_features` 表格後，我們將執行以下命令來添加幾何欄位：

```sql
SELECT AddGeometryColumn('walking_map_features', 'geom', 4326, 'GEOMETRY', 'XY');
```
*   `'GEOMETRY'` 類型允許 `walking_map_features` 表格儲存任何幾何類型（點、線、面），提供了極高的靈活性。
*   `4326` 為 WGS84 經緯度座標系統，是地理空間資料的標準。
