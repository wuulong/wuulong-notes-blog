-- Create Map: 智慧水圳玩樂地圖-新竹管理處
INSERT OR REPLACE INTO walking_maps (map_id, name, description, region, cover_image) 
VALUES ('2025_smart_water_fun_map_hsinchu', '智慧水圳玩樂地圖-新竹管理處', '探索新竹地區的重要水利設施，見證傳統水圳與現代科技的結合。', '新竹縣市', 'assets/images/hsinchu_water_cover.jpg');

-- Create Features & Relation
DELETE FROM walking_map_relations WHERE map_id = '2025_smart_water_fun_map_hsinchu';

INSERT OR REPLACE INTO walking_map_features (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data)
VALUES ('20251230_sancha_pond', '三叉埤', '位於橫山鄉，由當地居民人工築堤而成，匯集三座山谷溪流。不僅是百年水利設施，也是橫山村的地理中心與生態熱點。', 2, 'Point', 'POINT(121.1268 24.7137)', '{"markdown_file": "20251230_sancha_pond.md", "tags": ["智慧水圳玩樂地圖-新竹管理處"]}');

-- Insert Relation
INSERT INTO walking_map_relations (map_id, feature_id, display_order, is_highlight, note)
VALUES ('2025_smart_water_fun_map_hsinchu', '20251230_sancha_pond', 1, 1, '三叉埤');

INSERT OR REPLACE INTO walking_map_features (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data)
VALUES ('20251230_tingfu_canal', '汀甫圳', '新竹市最長的水圳，始建於清朝，紀念末代圳長何汀甫捐圳予公。沿線流經新竹精華區，是城市中的綠色水脈。', 2, 'Point', 'POINT(120.996 24.8024)', '{"markdown_file": "20251230_tingfu_canal.md", "tags": ["智慧水圳玩樂地圖-新竹管理處"]}');

-- Insert Relation
INSERT INTO walking_map_relations (map_id, feature_id, display_order, is_highlight, note)
VALUES ('2025_smart_water_fun_map_hsinchu', '20251230_tingfu_canal', 2, 1, '汀甫圳');

INSERT OR REPLACE INTO walking_map_features (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data)
VALUES ('20251230_tingfu_main_canal', '汀甫圳幹線', '汀甫圳的主幹線，近期進行了景觀改善工程，結合砌卵石護岸與步道，成為市民休閒散步的好去處。', 2, 'Point', 'POINT(120.99 24.798)', '{"markdown_file": "20251230_tingfu_main_canal.md", "tags": ["智慧水圳玩樂地圖-新竹管理處"]}');

-- Insert Relation
INSERT INTO walking_map_relations (map_id, feature_id, display_order, is_highlight, note)
VALUES ('2025_smart_water_fun_map_hsinchu', '20251230_tingfu_main_canal', 3, 1, '汀甫圳幹線');

INSERT OR REPLACE INTO walking_map_features (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data)
VALUES ('20251230_zhudong_canal_sand_basin', '竹東圳 (分水沉沙池)', '竹東圳是新竹重要的導水路，連結上坪溪與寶山水庫。此處的分水沉沙池負責在注入水庫前沉澱泥沙，確保水庫壽命。', 2, 'Point', 'POINT(121.0436 24.7203)', '{"markdown_file": "20251230_zhudong_canal_sand_basin.md", "tags": ["智慧水圳玩樂地圖-新竹管理處"]}');

-- Insert Relation
INSERT INTO walking_map_relations (map_id, feature_id, display_order, is_highlight, note)
VALUES ('2025_smart_water_fun_map_hsinchu', '20251230_zhudong_canal_sand_basin', 4, 0, '竹東圳 (分水沉沙池)');

INSERT OR REPLACE INTO walking_map_features (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data)
VALUES ('20251230_dongxing_old_port_canal_circle', '東興舊港圳圓環', '獨特的「水利雙圓環」，利用圓環分水汴將水源公平分配至東興圳與舊港圳，展現了日治時期的分水智慧。', 2, 'Point', 'POINT(121.0664 24.7715)', '{"markdown_file": "20251230_dongxing_old_port_canal_circle.md", "tags": ["智慧水圳玩樂地圖-新竹管理處"]}');

-- Insert Relation
INSERT INTO walking_map_relations (map_id, feature_id, display_order, is_highlight, note)
VALUES ('2025_smart_water_fun_map_hsinchu', '20251230_dongxing_old_port_canal_circle', 5, 0, '東興舊港圳圓環');

INSERT OR REPLACE INTO walking_map_features (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data)
VALUES ('20251230_jietou_main_canal', '街頭圳幹線', '位於橫山鄉的重要灌溉渠道，滋潤了田寮村的農田，也是當地農村風貌的重要組成部分。', 2, 'Point', 'POINT(121.121 24.717)', '{"markdown_file": "20251230_jietou_main_canal.md", "tags": ["智慧水圳玩樂地圖-新竹管理處"]}');

-- Insert Relation
INSERT INTO walking_map_relations (map_id, feature_id, display_order, is_highlight, note)
VALUES ('2025_smart_water_fun_map_hsinchu', '20251230_jietou_main_canal', 6, 0, '街頭圳幹線');

INSERT OR REPLACE INTO walking_map_features (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data)
VALUES ('20251230_longen_canal', '隆恩圳 (東大路旁)', '台灣三大古圳之一，已有300年歷史。在東大路段展現了古老水圳如何流經現代都市，並被賦予新的親水機能。', 2, 'Point', 'POINT(121.0163 24.7985)', '{"markdown_file": "20251230_longen_canal.md", "tags": ["智慧水圳玩樂地圖-新竹管理處"]}');

-- Insert Relation
INSERT INTO walking_map_relations (map_id, feature_id, display_order, is_highlight, note)
VALUES ('2025_smart_water_fun_map_hsinchu', '20251230_longen_canal', 7, 0, '隆恩圳 (東大路旁)');

INSERT OR REPLACE INTO walking_map_features (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data)
VALUES ('20251230_maoerding_branch_3', '貓兒錠幹線3支線', '位於竹北鳳岡地區，服務當地的水稻田。這條支線體現了竹北平原區發達的灌溉網絡。', 2, 'Point', 'POINT(121.112 24.832)', '{"markdown_file": "20251230_maoerding_branch_3.md", "tags": ["智慧水圳玩樂地圖-新竹管理處"]}');

-- Insert Relation
INSERT INTO walking_map_relations (map_id, feature_id, display_order, is_highlight, note)
VALUES ('2025_smart_water_fun_map_hsinchu', '20251230_maoerding_branch_3', 8, 0, '貓兒錠幹線3支線');
