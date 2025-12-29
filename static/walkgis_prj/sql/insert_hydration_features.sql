-- Ensure Layer 2 exists
INSERT OR IGNORE INTO layers (layer_id, layer_type, layer_subtype, description) 
VALUES (2, '水利工程與歷史', '水利設施', '大甲溪流域的重要水利工程，包含水庫、攔河堰與灌溉水圳');

-- Insert Hydration Features with Real Coordinates
INSERT OR REPLACE INTO walking_map_features (feature_id, name, description, layer_id, geometry_type, geometry_wkt) VALUES
('20251229_baileng_canal', '白冷圳', '翻山越嶺的生命之水', 2, 'Point', 'POINT(120.8299 24.1680)'),
('20251229_dongshi_main_canal', '東勢本圳', '滋潤東勢山城的百年水脈', 2, 'Point', 'POINT(120.8650 24.1950)'),
('20251229_huludun_canal', '葫蘆墩圳', '台中盆地的農業之母', 2, 'Point', 'POINT(120.7448 24.2790)'),
('20251229_techi_reservoir', '德基水庫', '台灣最高的雙曲線薄型拱壩', 2, 'Point', 'POINT(121.1652 24.2541)'),
('20251229_qingshan_dam', '青山壩', '深藏幽谷的地下電廠樞紐', 2, 'Point', 'POINT(121.1602 24.2530)'),
('20251229_guguan_dam', '谷關壩', '中橫公路上的水力地標', 2, 'Point', 'POINT(121.0761 24.2333)'),
('20251229_tianlun_dam', '天輪壩', '白冷社區的水利心臟', 2, 'Point', 'POINT(121.0150 24.2105)'),
('20251229_maan_dam', '馬鞍壩', '友善生態的綠色水壩', 2, 'Point', 'POINT(120.9133 24.1844)');
