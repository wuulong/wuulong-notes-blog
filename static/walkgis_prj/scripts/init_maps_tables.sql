-- 4. walking_maps 表格：地圖/路線集合
CREATE TABLE IF NOT EXISTS walking_maps (
    map_id TEXT PRIMARY KEY,        -- 唯一 ID (e.g., '2025_houfeng_bikeway')
    name TEXT NOT NULL,             -- 名稱 (e.g., '后豐鐵馬道精華遊')
    description TEXT,               -- 描述
    cover_image TEXT,               -- 封面圖路徑 (assets/...)
    region TEXT,                    -- 地區 (e.g., '台中/后里')
    meta_data TEXT,                 -- JSON (含 key: "routes" 存放 Mermaid 語法定義的路徑)
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 5. walking_map_relations 表格：地圖與特徵的關聯 (N:M)
CREATE TABLE IF NOT EXISTS walking_map_relations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    map_id TEXT NOT NULL,           -- FK -> walking_maps.map_id
    feature_id TEXT NOT NULL,       -- FK -> walking_map_features.feature_id
    display_order INTEGER,          -- UI 列表顯示順序 (可為 NULL)
    is_highlight BOOLEAN DEFAULT 0, -- 是否為重點標註
    note TEXT,                      -- 自訂註解
    FOREIGN KEY (map_id) REFERENCES walking_maps(map_id),
    FOREIGN KEY (feature_id) REFERENCES walking_map_features(feature_id),
    UNIQUE(map_id, feature_id)      -- 防止重複加入
);
