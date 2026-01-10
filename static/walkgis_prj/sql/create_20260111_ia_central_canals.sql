BEGIN TRANSACTION;

    INSERT OR REPLACE INTO walking_maps (map_id, name, description, region, created_at) 
    VALUES ('20260111_ia_central_canals', '農田水利署中區圳路地圖', '彰化、雲林、南投管理處重要圳路設施', '中台灣', CURRENT_TIMESTAMP);
    

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('20260111_ia_central_canals_00_八堡一圳', '八堡一圳', '水利設施-彰化管理處 - 510台灣彰化縣員林市惠明街53巷26弄7號', 17, 'Point', 'POINT(120.5711887 23.9499528)', '{"category": "水利設施-彰化管理處", "rating": 4.5, "place_id": "ChIJe_ArEQA3aTQRnTf8VqLvlH4"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('20260111_ia_central_canals', '20260111_ia_central_canals_00_八堡一圳', 0);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('20260111_ia_central_canals_01_農田水利署彰化管理處_用水管制中心', '農田水利署彰化管理處 用水管制中心', '水利設施-彰化管理處 - 530台灣彰化縣二水鄉員集路二段227號', 17, 'Point', 'POINT(120.644819 23.7991988)', '{"category": "水利設施-彰化管理處", "rating": 4, "place_id": "ChIJf3zrHO3MbjQRrT7xnDiO5k4"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('20260111_ia_central_canals', '20260111_ia_central_canals_01_農田水利署彰化管理處_用水管制中心', 1);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('20260111_ia_central_canals_02_葫蘆墩圳舊進水口', '葫蘆墩圳舊進水口', '水利設施-彰化管理處 - 420台灣臺中市豐原區萬順二街', 17, 'Point', 'POINT(120.7448105 24.2789675)', '{"category": "水利設施-彰化管理處", "rating": 4.3, "place_id": "ChIJZ4izogEbaTQRjUrAvaNyoLk"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('20260111_ia_central_canals', '20260111_ia_central_canals_02_葫蘆墩圳舊進水口', 2);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('20260111_ia_central_canals_03_500彰化縣彰化市河濱路', '500彰化縣彰化市河濱路', '水利設施-彰化管理處 - 500台灣彰化縣彰化市河濱路', 17, 'Point', 'POINT(120.6125935 24.0852657)', '{"category": "水利設施-彰化管理處", "rating": 0, "place_id": "ChIJcyT3IlA5aTQRwYrSgg-JrKk"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('20260111_ia_central_canals', '20260111_ia_central_canals_03_500彰化縣彰化市河濱路', 3);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('20260111_ia_central_canals_04_義和共同制水埧管理站', '義和共同制水埧管理站', '水利設施-彰化管理處 - 號, No. 32環河路一段溪湖鎮彰化縣台灣 514', 17, 'Point', 'POINT(120.4719921 23.9270752)', '{"category": "水利設施-彰化管理處", "rating": 4.5, "place_id": "ChIJf1FDFLdLaTQRrUZgz9KDOJI"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('20260111_ia_central_canals', '20260111_ia_central_canals_04_義和共同制水埧管理站', 4);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('20260111_ia_central_canals_05_斗六大圳進水口', '斗六大圳進水口', '水利設施-雲林管理處 - 號 堤防, No. 1新光路林內鄉雲林縣台灣 643', 18, 'Point', 'POINT(120.6444247 23.7704728)', '{"category": "水利設施-雲林管理處", "rating": 3, "place_id": "ChIJwU2mGELMbjQR2R2hFfCcTBY"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('20260111_ia_central_canals', '20260111_ia_central_canals_05_斗六大圳進水口', 5);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('20260111_ia_central_canals_06_水圳綠道起點__雲林農田水利文物館', '水圳綠道起點 (雲林農田水利文物館)', '水利設施-雲林管理處 - 雲林縣林內鄉三星路9-2號 (農田水利文物館)', 18, 'Point', 'POINT(120.6155 23.7595)', '{"category": "水利設施-雲林管理處", "rating": 4.5, "place_id": "corrected_manual"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('20260111_ia_central_canals', '20260111_ia_central_canals_06_水圳綠道起點__雲林農田水利文物館', 6);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('20260111_ia_central_canals_07_林內二號進水口', '林內二號進水口', '水利設施-雲林管理處 - 643台灣雲林縣林內鄉林內二號堤防', 18, 'Point', 'POINT(120.6161865 23.7829556)', '{"category": "水利設施-雲林管理處", "rating": 4.3, "place_id": "ChIJ90MHR4bLbjQRogAWi5qwkP8"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('20260111_ia_central_canals', '20260111_ia_central_canals_07_林內二號進水口', 7);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('20260111_ia_central_canals_08_林內分水工', '林內分水工', '水利設施-雲林管理處 - 八卦 池, 林內鄉雲林縣台灣 643', 18, 'Point', 'POINT(120.6137271 23.7801608)', '{"category": "水利設施-雲林管理處", "rating": 3.5, "place_id": "ChIJxzPRMY_LbjQR_0hBNVzsXbE"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('20260111_ia_central_canals', '20260111_ia_central_canals_08_林內分水工', 8);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('20260111_ia_central_canals_09_後庄埤親水公園', '後庄埤親水公園', '水利設施-雲林管理處 - 640台灣雲林縣斗六市大學路三段', 18, 'Point', 'POINT(120.524815 23.6941231)', '{"category": "水利設施-雲林管理處", "rating": 4.1, "place_id": "ChIJBZaUHQC3bjQRRfJIMMZwNRk"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('20260111_ia_central_canals', '20260111_ia_central_canals_09_後庄埤親水公園', 9);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('20260111_ia_central_canals_10_新頂埤頭線大排', '新頂埤頭線大排', '水利設施-雲林管理處 - 648台灣雲林縣西螺鎮新頂埤頭線大排', 18, 'Point', 'POINT(120.475997 23.7804772)', '{"category": "水利設施-雲林管理處", "rating": 3.3, "place_id": "ChIJKZbui9q1bjQRwhh-7Uj8Wi8"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('20260111_ia_central_canals', '20260111_ia_central_canals_10_新頂埤頭線大排', 10);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('20260111_ia_central_canals_11_嘉南大圳濁幹線調蓄池', '嘉南大圳濁幹線調蓄池', '水利設施-雲林管理處 - 632台灣雲林縣虎尾鎮工專路281號', 18, 'Point', 'POINT(120.4217521 23.7082724)', '{"category": "水利設施-雲林管理處", "rating": 0, "place_id": "ChIJEXbWL7uxbjQR4lTPyhbE3wA"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('20260111_ia_central_canals', '20260111_ia_central_canals_11_嘉南大圳濁幹線調蓄池', 11);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('20260111_ia_central_canals_12_北圳步道', '北圳步道', '水利設施-南投管理處 - 544台灣南投縣國姓鄉北圳巷28-1號', 19, 'Point', 'POINT(120.9229141 24.0623798)', '{"category": "水利設施-南投管理處", "rating": 3.9, "place_id": "ChIJxVyKlAvfaDQRk9iJYEi_yzY"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('20260111_ia_central_canals', '20260111_ia_central_canals_12_北圳步道', 12);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('20260111_ia_central_canals_13_阿罩霧圳幹線', '阿罩霧圳幹線', '水利設施-南投管理處 - 413台灣臺中市霧峰區阿罩霧圳幹線', 19, 'Point', 'POINT(120.700924 24.0114824)', '{"category": "水利設施-南投管理處", "rating": 4.4, "place_id": "ChIJ54GhN8Y6aTQRJtW3nohVIOM"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('20260111_ia_central_canals', '20260111_ia_central_canals_13_阿罩霧圳幹線', 13);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('20260111_ia_central_canals_14_鳳雛生態步道', '鳳雛生態步道', '水利設施-南投管理處 - 545台灣南投縣埔里鎮投72鄉道', 19, 'Point', 'POINT(120.972365 23.9408611)', '{"category": "水利設施-南投管理處", "rating": 4.1, "place_id": "ChIJHX_ZJu7ZaDQRuy0tavEqPy0"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('20260111_ia_central_canals', '20260111_ia_central_canals_14_鳳雛生態步道', 14);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('20260111_ia_central_canals_15_農業部農田水利署南投管理處土城工作站', '農業部農田水利署南投管理處土城工作站', '水利設施-南投管理處 - 542台灣南投縣草屯鎮中正路128號', 19, 'Point', 'POINT(120.7490451 23.9841342)', '{"category": "水利設施-南投管理處", "rating": 4.7, "place_id": "ChIJR36uoHslaTQRrnK7Oopsdsg"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('20260111_ia_central_canals', '20260111_ia_central_canals_15_農業部農田水利署南投管理處土城工作站', 15);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('20260111_ia_central_canals_16_頭社水庫', '頭社水庫', '水利設施-南投管理處 - 555台灣南投縣魚池鄉頭社水庫', 19, 'Point', 'POINT(120.8967211 23.8363861)', '{"category": "水利設施-南投管理處", "rating": 4.3, "place_id": "ChIJOfdsuIrVaDQRzoMw46RoLTU"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('20260111_ia_central_canals', '20260111_ia_central_canals_16_頭社水庫', 16);
        

        INSERT OR REPLACE INTO walking_map_features 
        (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data, created_at, updated_at) 
        VALUES 
        ('20260111_ia_central_canals_17_頭社水庫生態步道', '頭社水庫生態步道', '水利設施-南投管理處 - 555台灣南投縣魚池鄉頭社村', 19, 'Point', 'POINT(120.8984715 23.8387831)', '{"category": "水利設施-南投管理處", "rating": 4.3, "place_id": "ChIJgyyOHvXVaDQRoGM2r74ANJw"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
        

        INSERT OR REPLACE INTO walking_map_relations 
        (map_id, feature_id, display_order) 
        VALUES 
        ('20260111_ia_central_canals', '20260111_ia_central_canals_17_頭社水庫生態步道', 17);
        
COMMIT;