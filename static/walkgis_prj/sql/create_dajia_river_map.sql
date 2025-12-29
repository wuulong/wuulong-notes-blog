-- 1. Create the Map
INSERT OR REPLACE INTO walking_maps (map_id, name, description, region, cover_image) VALUES
('2025_dajia_river_tour', '大甲溪水利溯源之旅', '沿著台8線一路向上，探索台灣最重要河流的水利工程史詩，從百年水圳到巍峨高壩。', '台中/和平', 'assets/images/dajia_river_cover.jpg');

-- 2. Insert Relations (Ordered)
-- Clean up old relations if any
DELETE FROM walking_map_relations WHERE map_id = '2025_dajia_river_tour';

INSERT INTO walking_map_relations (map_id, feature_id, display_order, is_highlight, note) VALUES
('2025_dajia_river_tour', '20251229_huludun_canal', 1, 0, '起點：平原農業的命脈'),
('2025_dajia_river_tour', '20251229_shigang_dam', 2, 1, '斷層遺跡與水資源樞紐'),
('2025_dajia_river_tour', '20251229_dongshi_main_canal', 3, 0, '東勢山城的生命水'),
('2025_dajia_river_tour', '20251229_maan_dam', 4, 1, '生態魚道觀察點'),
('2025_dajia_river_tour', '20251229_baileng_canal', 5, 1, '必看倒虹吸管工程奇蹟'),
('2025_dajia_river_tour', '20251229_tianlun_dam', 6, 0, '休息站：吃白冷肉包看水壩'),
('2025_dajia_river_tour', '20251229_guguan_dam', 7, 0, '谷關溫泉區'),
('2025_dajia_river_tour', '20251229_qingshan_dam', 8, 0, '深山峽谷中的電力心臟'),
('2025_dajia_river_tour', '20251229_techi_reservoir', 9, 1, '終點：台灣最高的雙曲線拱壩');
