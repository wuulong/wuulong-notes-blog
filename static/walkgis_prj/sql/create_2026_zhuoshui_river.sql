BEGIN TRANSACTION;

    INSERT OR REPLACE INTO walking_maps (map_id, name, description, region, created_at) 
    VALUES ('2026_zhuoshui_river', '濁水溪流域百科全書式探索', '從上游到出海口的完整流域探索', '濁水溪流域', CURRENT_TIMESTAMP);
    

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('2026_zhuoshui_river_00_合歡山武嶺牌樓', '合歡山武嶺牌樓', '自然地景-源頭與山岳 - 546台灣南投縣仁愛鄉仁和路170號', 4, 'Point', 'POINT(121.275739 24.1371281)', '{"category": "自然地景-源頭與山岳", "rating": 4.8, "place_id": "ChIJte6zETiTaDQRA6gtQKdhV8k"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('2026_zhuoshui_river', '2026_zhuoshui_river_00_合歡山武嶺牌樓', 0);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('2026_zhuoshui_river_01_合歡山主峰步道', '合歡山主峰步道', '自然地景-源頭與山岳 - 546台灣南投縣仁愛鄉', 4, 'Point', 'POINT(121.2716627 24.1336539)', '{"category": "自然地景-源頭與山岳", "rating": 4.8, "place_id": "ChIJX4XFDjeTaDQRO0JqI8_K8-w"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('2026_zhuoshui_river', '2026_zhuoshui_river_01_合歡山主峰步道', 1);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('2026_zhuoshui_river_02_合歡山東峰', '合歡山東峰', '自然地景-源頭與山岳 - 546台灣南投縣仁愛鄉合歡山東峰', 4, 'Point', 'POINT(121.280984 24.1353636)', '{"category": "自然地景-源頭與山岳", "rating": 4.8, "place_id": "ChIJM3uNWz-TaDQRp2uAKgGlyPw"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('2026_zhuoshui_river', '2026_zhuoshui_river_02_合歡山東峰', 2);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('2026_zhuoshui_river_03_集集大山', '集集大山', '自然地景-源頭與山岳 - 552台灣南投縣集集鎮集集大山', 4, 'Point', 'POINT(120.838294 23.854553)', '{"category": "自然地景-源頭與山岳", "rating": 4.2, "place_id": "ChIJHxKWH8YraTQRDGfF3YiI8tA"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('2026_zhuoshui_river', '2026_zhuoshui_river_03_集集大山', 3);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('2026_zhuoshui_river_04_瑞龍瀑布園區', '瑞龍瀑布園區', '自然地景-水文/濕地 - 557台灣南投縣竹山鎮坪頂路', 5, 'Point', 'POINT(120.6888271 23.6646837)', '{"category": "自然地景-水文/濕地", "rating": 4.1, "place_id": "ChIJewwDrJTPbjQRhWvZK4iOzT8"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('2026_zhuoshui_river', '2026_zhuoshui_river_04_瑞龍瀑布園區', 4);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('2026_zhuoshui_river_05_日月潭', '日月潭', '自然地景-水文/濕地 - 555台灣南投縣魚池鄉日月潭', 5, 'Point', 'POINT(120.9159131 23.8573342)', '{"category": "自然地景-水文/濕地", "rating": 4.6, "place_id": "ChIJBQDuduDVaDQRKKUSU_2mF-w"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('2026_zhuoshui_river', '2026_zhuoshui_river_05_日月潭', 5);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('2026_zhuoshui_river_06_新草嶺潭觀景臺_受災小攤', '新草嶺潭觀景臺（受災小攤）', '自然地景-水文/濕地 - 646台灣雲林縣古坑鄉', 5, 'Point', 'POINT(120.683197 23.5806866)', '{"category": "自然地景-水文/濕地", "rating": 3.8, "place_id": "ChIJj_0E9pPEbjQRXpsZC65g8k0"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('2026_zhuoshui_river', '2026_zhuoshui_river_06_新草嶺潭觀景臺_受災小攤', 6);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('2026_zhuoshui_river_07_濁水溪出海口生態基地', '濁水溪出海口生態基地', '自然地景-水文/濕地 - 638台灣雲林縣麥寮鄉', 5, 'Point', 'POINT(120.244146 23.821301)', '{"category": "自然地景-水文/濕地", "rating": 4.2, "place_id": "ChIJPf_4Q-2pbjQRPk9qLK55-Hw"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('2026_zhuoshui_river', '2026_zhuoshui_river_07_濁水溪出海口生態基地', 7);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('2026_zhuoshui_river_08_雙龍瀑布', '雙龍瀑布', '自然地景-水文/濕地 - 556台灣南投縣信義鄉', 5, 'Point', 'POINT(120.9504481 23.7767852)', '{"category": "自然地景-水文/濕地", "rating": 4.4, "place_id": "ChIJWSKndtvUaDQRnRoVvZzGDFI"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('2026_zhuoshui_river', '2026_zhuoshui_river_08_雙龍瀑布', 8);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('2026_zhuoshui_river_09_金門峒斷崖', '金門峒斷崖', '自然地景-地質 - 556台灣南投縣信義鄉金門峒斷崖', 6, 'Point', 'POINT(120.98931 23.502296)', '{"category": "自然地景-地質", "rating": 0, "place_id": "ChIJyxniIAIkbzQRNTR-SSehG3w"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('2026_zhuoshui_river', '2026_zhuoshui_river_09_金門峒斷崖', 9);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('2026_zhuoshui_river_10_濁水溪', '濁水溪', '自然地景-地質 - 527台灣彰化縣大城鄉濁水溪', 6, 'Point', 'POINT(120.2838041 23.8273796)', '{"category": "自然地景-地質", "rating": 4.1, "place_id": "ChIJoSHnuyWsbjQR_FwJs2mzKA8"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('2026_zhuoshui_river', '2026_zhuoshui_river_10_濁水溪', 10);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('2026_zhuoshui_river_11_武界壩', '武界壩', '水利設施-壩堰 - 546台灣南投縣仁愛鄉武界壩', 7, 'Point', 'POINT(121.057222 23.915)', '{"category": "水利設施-壩堰", "rating": 0, "place_id": "ChIJnT4aEqLaaDQR4PtUmAvUbTw"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('2026_zhuoshui_river', '2026_zhuoshui_river_11_武界壩', 11);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('2026_zhuoshui_river_12_霧社水庫', '霧社水庫', '水利設施-壩堰 - 546台灣南投縣仁愛鄉霧社水庫', 7, 'Point', 'POINT(121.1352393 23.9991367)', '{"category": "水利設施-壩堰", "rating": 4.3, "place_id": "ChIJk6sRD5jDaDQRmPKE5kETOQQ"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('2026_zhuoshui_river', '2026_zhuoshui_river_12_霧社水庫', 12);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('2026_zhuoshui_river_13_集集攔河堰', '集集攔河堰', '水利設施-壩堰 - 552台灣南投縣集集鎮林尾里攔河路2號', 7, 'Point', 'POINT(120.7633291 23.818335)', '{"category": "水利設施-壩堰", "rating": 4.1, "place_id": "ChIJPfLmHdwsaTQRpIxw-3U8zkM"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('2026_zhuoshui_river', '2026_zhuoshui_river_13_集集攔河堰', 13);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('2026_zhuoshui_river_14_八堡二圳取水口', '八堡二圳取水口', '水利設施-圳路 - 530台灣彰化縣二水鄉', 8, 'Point', 'POINT(120.6450621 23.7995881)', '{"category": "水利設施-圳路", "rating": 4.9, "place_id": "ChIJ72RKCADNbjQRZLNW6xc5-jI"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('2026_zhuoshui_river', '2026_zhuoshui_river_14_八堡二圳取水口', 14);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('2026_zhuoshui_river_15_莿仔埤圳第一放水路', '莿仔埤圳第一放水路', '水利設施-圳路 - 524台灣彰化縣溪州鄉莿仔埤圳第一放水路', 8, 'Point', 'POINT(120.5610401 23.8220779)', '{"category": "水利設施-圳路", "rating": 5, "place_id": "ChIJ8SSVtOjKbjQRThZrkEQNz4E"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('2026_zhuoshui_river', '2026_zhuoshui_river_15_莿仔埤圳第一放水路', 15);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('2026_zhuoshui_river_16_斗六大圳', '斗六大圳', '水利設施-圳路 - 台灣雲林縣斗六大圳', 8, 'Point', 'POINT(120.6007312 23.7110601)', '{"category": "水利設施-圳路", "rating": 3.9, "place_id": "ChIJ7YnoSCfJbjQRSUXXQjYH9eM"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('2026_zhuoshui_river', '2026_zhuoshui_river_16_斗六大圳', 16);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('2026_zhuoshui_river_17_石山引水道入口處', '石山引水道入口處', '水利設施-圳路 - 556台灣南投縣信義鄉阿里山公路', 8, 'Point', 'POINT(120.8459194 23.4732996)', '{"category": "水利設施-圳路", "rating": 4.5, "place_id": "ChIJWV50vk3ebjQR0F4Tx0RRme4"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('2026_zhuoshui_river', '2026_zhuoshui_river_17_石山引水道入口處', 17);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('2026_zhuoshui_river_18_台電大觀發電廠_大觀G_S', '台電大觀發電廠(大觀G/S)', '水利設施-電廠 - 553台灣南投縣水里鄉明潭巷73號', 9, 'Point', 'POINT(120.869621 23.854427)', '{"category": "水利設施-電廠", "rating": 4.4, "place_id": "ChIJW1V4LCMqaTQRRKJ7BkoAKt8"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('2026_zhuoshui_river', '2026_zhuoshui_river_18_台電大觀發電廠_大觀G_S', 18);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('2026_zhuoshui_river_19_西螺大橋', '西螺大橋', '交通設施-橋樑 - 台灣西螺大橋', 10, 'Point', 'POINT(120.461058 23.8138002)', '{"category": "交通設施-橋樑", "rating": 0, "place_id": "ChIJrZs43EK0bjQRK3XsEqYto-Y"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('2026_zhuoshui_river', '2026_zhuoshui_river_19_西螺大橋', 19);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('2026_zhuoshui_river_20_溪州大橋_新西螺大橋', '溪州大橋(新西螺大橋)', '交通設施-橋樑 - 648台灣彰化縣西螺鎮縱貫公路附近號', 10, 'Point', 'POINT(120.4716127 23.7978137)', '{"category": "交通設施-橋樑", "rating": 4.4, "place_id": "ChIJ2V6lk0W0bjQRElvWwUfrWqY"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('2026_zhuoshui_river', '2026_zhuoshui_river_20_溪州大橋_新西螺大橋', 20);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('2026_zhuoshui_river_21_自強大橋', '自強大橋', '交通設施-橋樑 - 台灣自強大橋', 10, 'Point', 'POINT(120.398178 23.829617)', '{"category": "交通設施-橋樑", "rating": 0, "place_id": "ChIJC7CXtrGzbjQRsK1dFD3wx8U"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('2026_zhuoshui_river', '2026_zhuoshui_river_21_自強大橋', 21);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('2026_zhuoshui_river_22_中沙大橋', '中沙大橋', '交通設施-橋樑 - 524台灣彰化縣溪州鄉中山高速公路', 10, 'Point', 'POINT(120.4841178 23.8076469)', '{"category": "交通設施-橋樑", "rating": 5, "place_id": "ChIJ0cNrFb61bjQRBcIp9fl3Z_U"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('2026_zhuoshui_river', '2026_zhuoshui_river_22_中沙大橋', 22);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('2026_zhuoshui_river_23_西濱大橋', '西濱大橋', '交通設施-橋樑 - 527台灣彰化縣大城鄉台61線', 10, 'Point', 'POINT(120.2890934 23.8304674)', '{"category": "交通設施-橋樑", "rating": 3.8, "place_id": "ChIJY74SHiCtbjQRd3qtso9LKFE"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('2026_zhuoshui_river', '2026_zhuoshui_river_23_西濱大橋', 23);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('2026_zhuoshui_river_24_553南投縣水里鄉龍神橋', '553南投縣水里鄉龍神橋', '交通設施-橋樑 - 553台灣南投縣水里鄉龍神橋', 10, 'Point', 'POINT(120.8695967 23.7789311)', '{"category": "交通設施-橋樑", "rating": 0, "place_id": "ChIJWZE2KDXVbjQRBKiqeDU-m-Y"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('2026_zhuoshui_river', '2026_zhuoshui_river_24_553南投縣水里鄉龍神橋', 24);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('2026_zhuoshui_river_25_雙龍七彩吊橋', '雙龍七彩吊橋', '交通設施-橋樑 - 556台灣南投縣信義鄉光復巷', 10, 'Point', 'POINT(120.9498198 23.7806637)', '{"category": "交通設施-橋樑", "rating": 4.4, "place_id": "ChIJ0zNzrODUaDQRhEHNBuJR4DE"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('2026_zhuoshui_river', '2026_zhuoshui_river_25_雙龍七彩吊橋', 25);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('2026_zhuoshui_river_26_名竹大橋', '名竹大橋', '交通設施-橋樑 - 557台灣南投縣竹山鎮名竹大橋', 10, 'Point', 'POINT(120.7068136 23.816025)', '{"category": "交通設施-橋樑", "rating": 3.8, "place_id": "ChIJSXpvodozaTQRRDmRR9GGs2o"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('2026_zhuoshui_river', '2026_zhuoshui_river_26_名竹大橋', 26);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('2026_zhuoshui_river_27_孫海橋與丹大吊橋遺構', '孫海橋與丹大吊橋遺構', '交通設施-橋樑 - 台灣南投縣信義鄉556', 10, 'Point', 'POINT(121.0117452 23.7871899)', '{"category": "交通設施-橋樑", "rating": 4.3, "place_id": "ChIJLbldPAvTaDQRq0nT1wJXT6w"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('2026_zhuoshui_river', '2026_zhuoshui_river_27_孫海橋與丹大吊橋遺構', 27);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('2026_zhuoshui_river_28_北港溪糯米石橋', '北港溪糯米石橋', '交通設施-橋樑 - 544台灣南投縣國姓鄉國姓路', 10, 'Point', 'POINT(120.9065125 24.0585088)', '{"category": "交通設施-橋樑", "rating": 4.2, "place_id": "ChIJ1UzfOm7faDQRBS1tixG_oCk"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('2026_zhuoshui_river', '2026_zhuoshui_river_28_北港溪糯米石橋', 28);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('2026_zhuoshui_river_29_集集車站', '集集車站', '交通設施-車站 - 552台灣南投縣集集鎮', 11, 'Point', 'POINT(120.78489 23.826451)', '{"category": "交通設施-車站", "rating": 4.1, "place_id": "ChIJUZEbvJMsaTQRKCCSuiKnaDU"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('2026_zhuoshui_river', '2026_zhuoshui_river_29_集集車站', 29);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('2026_zhuoshui_river_30_林先生廟', '林先生廟', '人文史蹟-古蹟/建築 - 530台灣彰化縣二水鄉員集路二段227號', 12, 'Point', 'POINT(120.6452979 23.7992993)', '{"category": "人文史蹟-古蹟/建築", "rating": 4.4, "place_id": "ChIJQX78_ezMbjQRzxD3t3IbeAY"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('2026_zhuoshui_river', '2026_zhuoshui_river_30_林先生廟', 30);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('2026_zhuoshui_river_31_竹山社寮敬聖亭_縣定古蹟', '竹山社寮敬聖亭（縣定古蹟）', '人文史蹟-古蹟/建築 - 557台灣南投縣竹山鎮集山路一段1738號', 12, 'Point', 'POINT(120.722177 23.8143469)', '{"category": "人文史蹟-古蹟/建築", "rating": 4.1, "place_id": "ChIJw_LhiVItaTQRZJ5EaQ7FDNw"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('2026_zhuoshui_river', '2026_zhuoshui_river_31_竹山社寮敬聖亭_縣定古蹟', 31);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('2026_zhuoshui_river_32_振文書院_文祠廟', '振文書院(文祠廟)', '人文史蹟-古蹟/建築 - 648台灣雲林縣西螺鎮興農西路6號', 12, 'Point', 'POINT(120.4644577 23.7945403)', '{"category": "人文史蹟-古蹟/建築", "rating": 4.4, "place_id": "ChIJzUP3oDy0bjQRpK-MAS3uJ8I"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('2026_zhuoshui_river', '2026_zhuoshui_river_32_振文書院_文祠廟', 32);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('2026_zhuoshui_river_33_明新書院', '明新書院', '人文史蹟-古蹟/建築 - 552台灣南投縣集集鎮東昌巷4號', 12, 'Point', 'POINT(120.7995314 23.8275444)', '{"category": "人文史蹟-古蹟/建築", "rating": 4.1, "place_id": "ChIJqck7NIMsaTQRdjaUSXMaNh8"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('2026_zhuoshui_river', '2026_zhuoshui_river_33_明新書院', 33);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('2026_zhuoshui_river_34_花蓮縣八通關古道', '花蓮縣八通關古道', '人文史蹟-古蹟/建築 - 台灣花蓮縣八通關古道', 12, 'Point', 'POINT(121.2479617 23.3237454)', '{"category": "人文史蹟-古蹟/建築", "rating": 0, "place_id": "ChIJ31zzuxkVbzQRLji2Yos29tE"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('2026_zhuoshui_river', '2026_zhuoshui_river_34_花蓮縣八通關古道', 34);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('2026_zhuoshui_river_35_詔安客家文化館', '詔安客家文化館', '人文史蹟-古蹟/建築 - 637台灣雲林縣崙背鄉東明村民生路28-8號', 12, 'Point', 'POINT(120.355071 23.763744)', '{"category": "人文史蹟-古蹟/建築", "rating": 4, "place_id": "ChIJR0vn5M2xbjQRILjNdDuDG94"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('2026_zhuoshui_river', '2026_zhuoshui_river_35_詔安客家文化館', 35);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('2026_zhuoshui_river_36_西螺福興宮_西螺媽祖太平媽_媽祖文化祭_丙午年網路點燈_安太歲_線上喜點福燈_2026點燈服務', '【西螺福興宮 西螺媽祖太平媽】媽祖文化祭｜丙午年網路點燈｜安太歲｜線上喜點福燈｜2026點燈服務', '人文史蹟-宗教信仰 - 648台灣雲林縣西螺鎮延平路180號', 13, 'Point', 'POINT(120.4605261 23.8015652)', '{"category": "人文史蹟-宗教信仰", "rating": 4.6, "place_id": "ChIJkzhtRj60bjQRioVRZXyC5WM"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('2026_zhuoshui_river', '2026_zhuoshui_river_36_西螺福興宮_西螺媽祖太平媽_媽祖文化祭_丙午年網路點燈_安太歲_線上喜點福燈_2026點燈服務', 36);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('2026_zhuoshui_river_37_縣定古蹟西螺廣福宮_西螺媽老大媽廟', '縣定古蹟西螺廣福宮 西螺媽老大媽廟', '人文史蹟-宗教信仰 - 648台灣雲林縣西螺鎮新街路32號', 13, 'Point', 'POINT(120.4647035 23.7971558)', '{"category": "人文史蹟-宗教信仰", "rating": 4.6, "place_id": "ChIJG3Zn9Tu0bjQRMlvDwkeIUwY"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('2026_zhuoshui_river', '2026_zhuoshui_river_37_縣定古蹟西螺廣福宮_西螺媽老大媽廟', 37);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('2026_zhuoshui_river_38_麥寮拱範宮', '麥寮拱範宮', '人文史蹟-宗教信仰 - 638台灣雲林縣麥寮鄉中正路3號', 13, 'Point', 'POINT(120.2555916 23.7482552)', '{"category": "人文史蹟-宗教信仰", "rating": 4.7, "place_id": "ChIJ-yiS7FOvbjQRIHnDWn-xc6A"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('2026_zhuoshui_river', '2026_zhuoshui_river_38_麥寮拱範宮', 38);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('2026_zhuoshui_river_39_竹山紫南宮', '竹山紫南宮', '人文史蹟-宗教信仰 - 557台灣南投縣竹山鎮大公街40號', 13, 'Point', 'POINT(120.7225793 23.8170767)', '{"category": "人文史蹟-宗教信仰", "rating": 4.7, "place_id": "ChIJiREHEVItaTQRCw4OxSRg5Lo"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('2026_zhuoshui_river', '2026_zhuoshui_river_39_竹山紫南宮', 39);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('2026_zhuoshui_river_40_武界部落', '武界部落', '人文史蹟-聚落(原民) - 546台灣南投縣仁愛鄉界山巷4號', 14, 'Point', 'POINT(121.0442446 23.9155571)', '{"category": "人文史蹟-聚落(原民)", "rating": 4.4, "place_id": "ChIJV73RK4XaaDQRsBQWVZtcYrE"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('2026_zhuoshui_river', '2026_zhuoshui_river_40_武界部落', 40);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('2026_zhuoshui_river_41_萬豐村曲冰部落', '萬豐村曲冰部落', '人文史蹟-聚落(原民) - 546台灣南投縣仁愛鄉', 14, 'Point', 'POINT(121.0767669 23.9460544)', '{"category": "人文史蹟-聚落(原民)", "rating": 4.2, "place_id": "ChIJQ-Z3toHaaDQR6gTMVwknZpg"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('2026_zhuoshui_river', '2026_zhuoshui_river_41_萬豐村曲冰部落', 41);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('2026_zhuoshui_river_42_過坑山', '過坑山', '人文史蹟-聚落(原民) - 555台灣南投縣魚池鄉過坑山', 14, 'Point', 'POINT(120.979574 23.884353)', '{"category": "人文史蹟-聚落(原民)", "rating": 3.9, "place_id": "ChIJ90_WyCnXaDQR8O2KMl-lHVs"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('2026_zhuoshui_river', '2026_zhuoshui_river_42_過坑山', 42);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('2026_zhuoshui_river_43_雙龍部落伊希岸農場露營區', '雙龍部落伊希岸農場露營區', '人文史蹟-聚落(原民) - 556台灣南投縣信義鄉', 14, 'Point', 'POINT(120.9473155 23.7645348)', '{"category": "人文史蹟-聚落(原民)", "rating": 4.5, "place_id": "ChIJDy1KgtTUaDQR4gdhc9Izxqo"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('2026_zhuoshui_river', '2026_zhuoshui_river_43_雙龍部落伊希岸農場露營區', 43);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('2026_zhuoshui_river_44_北斗鎮', '北斗鎮', '人文史蹟-聚落(漢人) - 521台灣彰化縣北斗鎮', 15, 'Point', 'POINT(120.5336665 23.869208)', '{"category": "人文史蹟-聚落(漢人)", "rating": 0, "place_id": "ChIJFfRZm1s1aTQRaNPfvKPIOBo"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('2026_zhuoshui_river', '2026_zhuoshui_river_44_北斗鎮', 44);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('2026_zhuoshui_river_45_竹山鎮', '竹山鎮', '人文史蹟-聚落(漢人) - 557台灣南投縣竹山鎮', 15, 'Point', 'POINT(120.6890055 23.712201)', '{"category": "人文史蹟-聚落(漢人)", "rating": 0, "place_id": "ChIJfZEn0PHRbjQR9pIp-ZNvupA"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('2026_zhuoshui_river', '2026_zhuoshui_river_45_竹山鎮', 45);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('2026_zhuoshui_river_46_水里鄉', '水里鄉', '人文史蹟-聚落(漢人) - 553台灣南投縣水里鄉', 15, 'Point', 'POINT(120.8613785 23.7919524)', '{"category": "人文史蹟-聚落(漢人)", "rating": 0, "place_id": "ChIJEUvZx5IqaTQR4Aea9veuLCE"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('2026_zhuoshui_river', '2026_zhuoshui_river_46_水里鄉', 46);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('2026_zhuoshui_river_47_麥寮鄉', '麥寮鄉', '人文史蹟-聚落(漢人) - 638台灣雲林縣麥寮鄉', 15, 'Point', 'POINT(120.2563528 23.7485672)', '{"category": "人文史蹟-聚落(漢人)", "rating": 0, "place_id": "ChIJqwPRB1OvbjQRxE6-ez7rCg8"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('2026_zhuoshui_river', '2026_zhuoshui_river_47_麥寮鄉', 47);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('2026_zhuoshui_river_48_車籠埔斷層保存園區', '車籠埔斷層保存園區', '災害與環境 - 557014台灣南投縣竹山鎮集山路二段345號', 16, 'Point', 'POINT(120.7115267 23.7945692)', '{"category": "災害與環境", "rating": 4.4, "place_id": "ChIJ4XN7jF_NbjQR0_E22tzTorI"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('2026_zhuoshui_river', '2026_zhuoshui_river_48_車籠埔斷層保存園區', 48);
        
COMMIT;