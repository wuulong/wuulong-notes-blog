-- 1. Create the Map
INSERT OR REPLACE INTO walking_maps (map_id, name, description, region, cover_image) VALUES
('2025_smart_water_fun_map_taichung', '智慧水圳玩樂地圖-臺中管理處 (Taichung Management Office)', '探索大甲溪流域的智慧水利設施，見證傳統灌溉與現代科技的結合。', '台中市', 'assets/images/smart_water_cover.jpg');

-- 2. Insert Relations (Ordered)
DELETE FROM walking_map_relations WHERE map_id = '2025_smart_water_fun_map_taichung';

INSERT INTO walking_map_relations (map_id, feature_id, display_order, is_highlight, note) VALUES
('2025_smart_water_fun_map_taichung', '20251229_baileng_intake', 1, 1, '白冷圳源頭'),
('2025_smart_water_fun_map_taichung', '20251229_baileng_malipu', 2, 0, '馬力埔支線'),
('2025_smart_water_fun_map_taichung', '20251229_houli_low_head_power', 3, 1, '低落差發電示範'),
('2025_smart_water_fun_map_taichung', '20251229_zhonghe_gate', 4, 0, '忠和中排水閘門'),
('2025_smart_water_fun_map_taichung', '20251229_huyan_fuxing', 5, 0, '虎眼一圳福興支線'),
('2025_smart_water_fun_map_taichung', '20251229_yuanlin_branch', 6, 0, '員林支線'),
('2025_smart_water_fun_map_taichung', '20251229_taliangou_branch', 7, 0, '塔蓮溝支線'),
('2025_smart_water_fun_map_taichung', '20251229_huludun_intake', 8, 1, '葫蘆墩圳進水口');
