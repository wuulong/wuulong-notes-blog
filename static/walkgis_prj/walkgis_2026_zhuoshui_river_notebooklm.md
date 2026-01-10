# AI INSTRUCTION HEADER
Role: You are an enthusiastic, cartoon-style Travel Guide for the "WalkGIS Adventure".
Tone: Fun, Energetic, Child-friendly, Vibrant, and Imaginative.

## Your Task
Transform this structured GIS data (Map Topology + Feature Details) into a lively "Cartoon Adventure Guide".

## Output Requirements (When asked)
1. **Visual Map Description**: Describe a hand-drawn, Ghibli-style map connecting these specific locations.
2. **Slide Deck Outline**: Create a 10-15 slide presentation structure.
3. **Adventure Story**: Weave a route-based story using the connected features.

---
# DATA: MAP TOPOLOGY
---
id: 2026_zhuoshui_river
name: 濁水溪流域百科全書式探索
description: 濁水溪流域自然、人文、水利、交通與災害維度探索
---

# 濁水溪流域百科全書式探索

## 地圖結構
```mermaid
graph TD
    合歡山武嶺牌樓["合歡山武嶺牌樓"]
    合歡山主峰步道["合歡山主峰步道"]
    合歡山東峰["合歡山東峰"]
    集集大山["集集大山"]
    瑞龍瀑布園區["瑞龍瀑布園區"]
    日月潭["日月潭"]
    新草嶺潭觀景臺_受災小攤["新草嶺潭觀景臺（受災小攤）"]
    濁水溪出海口生態基地["濁水溪出海口生態基地"]
    雙龍瀑布["雙龍瀑布"]
    金門峒斷崖["金門峒斷崖"]
    濁水溪["濁水溪"]
    武界壩["武界壩"]
    霧社水庫["霧社水庫"]
    集集攔河堰["集集攔河堰"]
    八堡二圳取水口["八堡二圳取水口"]
    莿仔埤圳第一放水路["莿仔埤圳第一放水路"]
    斗六大圳["斗六大圳"]
    石山引水道入口處["石山引水道入口處"]
    台電大觀發電廠_大觀G_S["台電大觀發電廠(大觀G/S)"]
    西螺大橋["西螺大橋"]
    溪州大橋_新西螺大橋["溪州大橋(新西螺大橋)"]
    自強大橋["自強大橋"]
    中沙大橋["中沙大橋"]
    西濱大橋["西濱大橋"]
    553南投縣水里鄉龍神橋["553南投縣水里鄉龍神橋"]
    雙龍七彩吊橋["雙龍七彩吊橋"]
    名竹大橋["名竹大橋"]
    孫海橋與丹大吊橋遺構["孫海橋與丹大吊橋遺構"]
    北港溪糯米石橋["北港溪糯米石橋"]
    集集車站["集集車站"]
    林先生廟["林先生廟"]
    竹山社寮敬聖亭_縣定古蹟["竹山社寮敬聖亭（縣定古蹟）"]
    振文書院_文祠廟["振文書院(文祠廟)"]
    明新書院["明新書院"]
    花蓮縣八通關古道["花蓮縣八通關古道"]
    詔安客家文化館["詔安客家文化館"]
    西螺福興宮_西螺媽祖太平媽_媽祖文化祭_丙午年網路點燈_安太歲_線上喜點福燈_2026點燈服務["【西螺福興宮 西螺媽祖太平媽】媽祖文化祭｜丙午年網路點燈｜安太歲｜線上喜點福燈｜2026點燈服務"]
    縣定古蹟西螺廣福宮_西螺媽老大媽廟["縣定古蹟西螺廣福宮 西螺媽老大媽廟"]
    麥寮拱範宮["麥寮拱範宮"]
    竹山紫南宮["竹山紫南宮"]
    武界部落["武界部落"]
    萬豐村曲冰部落["萬豐村曲冰部落"]
    過坑山["過坑山"]
    雙龍部落伊希岸農場露營區["雙龍部落伊希岸農場露營區"]
    北斗鎮["北斗鎮"]
    竹山鎮["竹山鎮"]
    水里鄉["水里鄉"]
    麥寮鄉["麥寮鄉"]
    車籠埔斷層保存園區["車籠埔斷層保存園區"]
    自然地景_源頭與山岳(自然地景-源頭與山岳)
    自然地景_源頭與山岳 --> 合歡山武嶺牌樓
    自然地景_源頭與山岳 --> 合歡山主峰步道
    自然地景_源頭與山岳 --> 合歡山東峰
    自然地景_源頭與山岳 --> 集集大山
    自然地景_水文_濕地(自然地景-水文/濕地)
    自然地景_水文_濕地 --> 瑞龍瀑布園區
    自然地景_水文_濕地 --> 日月潭
    自然地景_水文_濕地 --> 新草嶺潭觀景臺_受災小攤
    自然地景_水文_濕地 --> 濁水溪出海口生態基地
    自然地景_水文_濕地 --> 雙龍瀑布
    自然地景_地質(自然地景-地質)
    自然地景_地質 --> 金門峒斷崖
    自然地景_地質 --> 濁水溪
    水利設施_壩堰(水利設施-壩堰)
    水利設施_壩堰 --> 武界壩
    水利設施_壩堰 --> 霧社水庫
    水利設施_壩堰 --> 集集攔河堰
    水利設施_圳路(水利設施-圳路)
    水利設施_圳路 --> 八堡二圳取水口
    水利設施_圳路 --> 莿仔埤圳第一放水路
    水利設施_圳路 --> 斗六大圳
    水利設施_圳路 --> 石山引水道入口處
    水利設施_電廠(水利設施-電廠)
    水利設施_電廠 --> 台電大觀發電廠_大觀G_S
    交通設施_橋樑(交通設施-橋樑)
    交通設施_橋樑 --> 西螺大橋
    交通設施_橋樑 --> 溪州大橋_新西螺大橋
    交通設施_橋樑 --> 自強大橋
    交通設施_橋樑 --> 中沙大橋
    交通設施_橋樑 --> 西濱大橋
    交通設施_橋樑 --> 553南投縣水里鄉龍神橋
    交通設施_橋樑 --> 雙龍七彩吊橋
    交通設施_橋樑 --> 名竹大橋
    交通設施_橋樑 --> 孫海橋與丹大吊橋遺構
    交通設施_橋樑 --> 北港溪糯米石橋
    交通設施_車站(交通設施-車站)
    交通設施_車站 --> 集集車站
    人文史蹟_古蹟_建築(人文史蹟-古蹟/建築)
    人文史蹟_古蹟_建築 --> 林先生廟
    人文史蹟_古蹟_建築 --> 竹山社寮敬聖亭_縣定古蹟
    人文史蹟_古蹟_建築 --> 振文書院_文祠廟
    人文史蹟_古蹟_建築 --> 明新書院
    人文史蹟_古蹟_建築 --> 花蓮縣八通關古道
    人文史蹟_古蹟_建築 --> 詔安客家文化館
    人文史蹟_宗教信仰(人文史蹟-宗教信仰)
    人文史蹟_宗教信仰 --> 西螺福興宮_西螺媽祖太平媽_媽祖文化祭_丙午年網路點燈_安太歲_線上喜點福燈_2026點燈服務
    人文史蹟_宗教信仰 --> 縣定古蹟西螺廣福宮_西螺媽老大媽廟
    人文史蹟_宗教信仰 --> 麥寮拱範宮
    人文史蹟_宗教信仰 --> 竹山紫南宮
    人文史蹟_聚落_原民(人文史蹟-聚落(原民))
    人文史蹟_聚落_原民 --> 武界部落
    人文史蹟_聚落_原民 --> 萬豐村曲冰部落
    人文史蹟_聚落_原民 --> 過坑山
    人文史蹟_聚落_原民 --> 雙龍部落伊希岸農場露營區
    人文史蹟_聚落_漢人(人文史蹟-聚落(漢人))
    人文史蹟_聚落_漢人 --> 北斗鎮
    人文史蹟_聚落_漢人 --> 竹山鎮
    人文史蹟_聚落_漢人 --> 水里鄉
    人文史蹟_聚落_漢人 --> 麥寮鄉
    災害與環境(災害與環境)
    災害與環境 --> 車籠埔斷層保存園區
```

## 景點列表
- [合歡山武嶺牌樓](../features/2026_zhuoshui_river_00_合歡山武嶺牌樓.md)
- [合歡山主峰步道](../features/2026_zhuoshui_river_01_合歡山主峰步道.md)
- [合歡山東峰](../features/2026_zhuoshui_river_02_合歡山東峰.md)
- [集集大山](../features/2026_zhuoshui_river_03_集集大山.md)
- [瑞龍瀑布園區](../features/2026_zhuoshui_river_04_瑞龍瀑布園區.md)
- [日月潭](../features/2026_zhuoshui_river_05_日月潭.md)
- [新草嶺潭觀景臺（受災小攤）](../features/2026_zhuoshui_river_06_新草嶺潭觀景臺_受災小攤.md)
- [濁水溪出海口生態基地](../features/2026_zhuoshui_river_07_濁水溪出海口生態基地.md)
- [雙龍瀑布](../features/2026_zhuoshui_river_08_雙龍瀑布.md)
- [金門峒斷崖](../features/2026_zhuoshui_river_09_金門峒斷崖.md)
- [濁水溪](../features/2026_zhuoshui_river_10_濁水溪.md)
- [武界壩](../features/2026_zhuoshui_river_11_武界壩.md)
- [霧社水庫](../features/2026_zhuoshui_river_12_霧社水庫.md)
- [集集攔河堰](../features/2026_zhuoshui_river_13_集集攔河堰.md)
- [八堡二圳取水口](../features/2026_zhuoshui_river_14_八堡二圳取水口.md)
- [莿仔埤圳第一放水路](../features/2026_zhuoshui_river_15_莿仔埤圳第一放水路.md)
- [斗六大圳](../features/2026_zhuoshui_river_16_斗六大圳.md)
- [石山引水道入口處](../features/2026_zhuoshui_river_17_石山引水道入口處.md)
- [台電大觀發電廠(大觀G/S)](../features/2026_zhuoshui_river_18_台電大觀發電廠_大觀G_S.md)
- [西螺大橋](../features/2026_zhuoshui_river_19_西螺大橋.md)
- [溪州大橋(新西螺大橋)](../features/2026_zhuoshui_river_20_溪州大橋_新西螺大橋.md)
- [自強大橋](../features/2026_zhuoshui_river_21_自強大橋.md)
- [中沙大橋](../features/2026_zhuoshui_river_22_中沙大橋.md)
- [西濱大橋](../features/2026_zhuoshui_river_23_西濱大橋.md)
- [553南投縣水里鄉龍神橋](../features/2026_zhuoshui_river_24_553南投縣水里鄉龍神橋.md)
- [雙龍七彩吊橋](../features/2026_zhuoshui_river_25_雙龍七彩吊橋.md)
- [名竹大橋](../features/2026_zhuoshui_river_26_名竹大橋.md)
- [孫海橋與丹大吊橋遺構](../features/2026_zhuoshui_river_27_孫海橋與丹大吊橋遺構.md)
- [北港溪糯米石橋](../features/2026_zhuoshui_river_28_北港溪糯米石橋.md)
- [集集車站](../features/2026_zhuoshui_river_29_集集車站.md)
- [林先生廟](../features/2026_zhuoshui_river_30_林先生廟.md)
- [竹山社寮敬聖亭（縣定古蹟）](../features/2026_zhuoshui_river_31_竹山社寮敬聖亭_縣定古蹟.md)
- [振文書院(文祠廟)](../features/2026_zhuoshui_river_32_振文書院_文祠廟.md)
- [明新書院](../features/2026_zhuoshui_river_33_明新書院.md)
- [花蓮縣八通關古道](../features/2026_zhuoshui_river_34_花蓮縣八通關古道.md)
- [詔安客家文化館](../features/2026_zhuoshui_river_35_詔安客家文化館.md)
- [【西螺福興宮 西螺媽祖太平媽】媽祖文化祭｜丙午年網路點燈｜安太歲｜線上喜點福燈｜2026點燈服務](../features/2026_zhuoshui_river_36_西螺福興宮_西螺媽祖太平媽_媽祖文化祭_丙午年網路點燈_安太歲_線上喜點福燈_2026點燈服務.md)
- [縣定古蹟西螺廣福宮 西螺媽老大媽廟](../features/2026_zhuoshui_river_37_縣定古蹟西螺廣福宮_西螺媽老大媽廟.md)
- [麥寮拱範宮](../features/2026_zhuoshui_river_38_麥寮拱範宮.md)
- [竹山紫南宮](../features/2026_zhuoshui_river_39_竹山紫南宮.md)
- [武界部落](../features/2026_zhuoshui_river_40_武界部落.md)
- [萬豐村曲冰部落](../features/2026_zhuoshui_river_41_萬豐村曲冰部落.md)
- [過坑山](../features/2026_zhuoshui_river_42_過坑山.md)
- [雙龍部落伊希岸農場露營區](../features/2026_zhuoshui_river_43_雙龍部落伊希岸農場露營區.md)
- [北斗鎮](../features/2026_zhuoshui_river_44_北斗鎮.md)
- [竹山鎮](../features/2026_zhuoshui_river_45_竹山鎮.md)
- [水里鄉](../features/2026_zhuoshui_river_46_水里鄉.md)
- [麥寮鄉](../features/2026_zhuoshui_river_47_麥寮鄉.md)
- [車籠埔斷層保存園區](../features/2026_zhuoshui_river_48_車籠埔斷層保存園區.md)

---
# DATA: FEATURES DETAIL

---
id: 2026_zhuoshui_river_00_合歡山武嶺牌樓
name: 合歡山武嶺牌樓
description: 自然地景-源頭與山岳 - 546台灣南投縣仁愛鄉仁和路170號
geometry:
  type: Point
  coordinates: [121.275739, 24.1371281]
properties:
  category: 自然地景-源頭與山岳
  rating: 4.8
  place_id: ChIJte6zETiTaDQRA6gtQKdhV8k
---

# 合歡山武嶺牌樓

- **類別**: 自然地景-源頭與山岳
- **地址**: 546台灣南投縣仁愛鄉仁和路170號
- **評分**: 4.8

## 簡介
(待補充詳細資料)

## 相關連結
- [Google Maps](https://www.google.com/maps/search/?api=1&query=24.1371281,121.275739&query_place_id=ChIJte6zETiTaDQRA6gtQKdhV8k)

---

---
id: 2026_zhuoshui_river_01_合歡山主峰步道
name: 合歡山主峰步道
description: 自然地景-源頭與山岳 - 546台灣南投縣仁愛鄉
geometry:
  type: Point
  coordinates: [121.2716627, 24.1336539]
properties:
  category: 自然地景-源頭與山岳
  rating: 4.8
  place_id: ChIJX4XFDjeTaDQRO0JqI8_K8-w
---

# 合歡山主峰步道

- **類別**: 自然地景-源頭與山岳
- **地址**: 546台灣南投縣仁愛鄉
- **評分**: 4.8

## 簡介
(待補充詳細資料)

## 相關連結
- [Google Maps](https://www.google.com/maps/search/?api=1&query=24.1336539,121.2716627&query_place_id=ChIJX4XFDjeTaDQRO0JqI8_K8-w)

---

---
id: 2026_zhuoshui_river_02_合歡山東峰
name: 合歡山東峰
description: 自然地景-源頭與山岳 - 546台灣南投縣仁愛鄉合歡山東峰
geometry:
  type: Point
  coordinates: [121.280984, 24.1353636]
properties:
  category: 自然地景-源頭與山岳
  rating: 4.8
  place_id: ChIJM3uNWz-TaDQRp2uAKgGlyPw
---

# 合歡山東峰

- **類別**: 自然地景-源頭與山岳
- **地址**: 546台灣南投縣仁愛鄉合歡山東峰
- **評分**: 4.8

## 簡介
(待補充詳細資料)

## 相關連結
- [Google Maps](https://www.google.com/maps/search/?api=1&query=24.1353636,121.280984&query_place_id=ChIJM3uNWz-TaDQRp2uAKgGlyPw)

---

---
id: 2026_zhuoshui_river_03_集集大山
name: 集集大山
description: 自然地景-源頭與山岳 - 552台灣南投縣集集鎮集集大山
geometry:
  type: Point
  coordinates: [120.838294, 23.854553]
properties:
  category: 自然地景-源頭與山岳
  rating: 4.2
  place_id: ChIJHxKWH8YraTQRDGfF3YiI8tA
---

# 集集大山

- **類別**: 自然地景-源頭與山岳
- **地址**: 552台灣南投縣集集鎮集集大山
- **評分**: 4.2

## 簡介
(待補充詳細資料)

## 相關連結
- [Google Maps](https://www.google.com/maps/search/?api=1&query=23.854553,120.838294&query_place_id=ChIJHxKWH8YraTQRDGfF3YiI8tA)

---

---
id: 2026_zhuoshui_river_04_瑞龍瀑布園區
name: 瑞龍瀑布園區
description: 自然地景-水文/濕地 - 557台灣南投縣竹山鎮坪頂路
geometry:
  type: Point
  coordinates: [120.6888271, 23.6646837]
properties:
  category: 自然地景-水文/濕地
  rating: 4.1
  place_id: ChIJewwDrJTPbjQRhWvZK4iOzT8
---

# 瑞龍瀑布園區

- **類別**: 自然地景-水文/濕地
- **地址**: 557台灣南投縣竹山鎮坪頂路
- **評分**: 4.1

## 簡介
(待補充詳細資料)

## 相關連結
- [Google Maps](https://www.google.com/maps/search/?api=1&query=23.6646837,120.6888271&query_place_id=ChIJewwDrJTPbjQRhWvZK4iOzT8)

---

---
id: 2026_zhuoshui_river_05_日月潭
name: 日月潭
description: 自然地景-水文/濕地 - 555台灣南投縣魚池鄉日月潭
geometry:
  type: Point
  coordinates: [120.9159131, 23.8573342]
properties:
  category: 自然地景-水文/濕地
  rating: 4.6
  place_id: ChIJBQDuduDVaDQRKKUSU_2mF-w
---

# 日月潭

- **類別**: 自然地景-水文/濕地
- **地址**: 555台灣南投縣魚池鄉日月潭
- **評分**: 4.6

## 簡介
(待補充詳細資料)

## 相關連結
- [Google Maps](https://www.google.com/maps/search/?api=1&query=23.8573342,120.9159131&query_place_id=ChIJBQDuduDVaDQRKKUSU_2mF-w)

---

---
id: 2026_zhuoshui_river_06_新草嶺潭觀景臺_受災小攤
name: 新草嶺潭觀景臺（受災小攤）
description: 自然地景-水文/濕地 - 646台灣雲林縣古坑鄉
geometry:
  type: Point
  coordinates: [120.683197, 23.5806866]
properties:
  category: 自然地景-水文/濕地
  rating: 3.8
  place_id: ChIJj_0E9pPEbjQRXpsZC65g8k0
---

# 新草嶺潭觀景臺（受災小攤）

- **類別**: 自然地景-水文/濕地
- **地址**: 646台灣雲林縣古坑鄉
- **評分**: 3.8

## 簡介
(待補充詳細資料)

## 相關連結
- [Google Maps](https://www.google.com/maps/search/?api=1&query=23.5806866,120.683197&query_place_id=ChIJj_0E9pPEbjQRXpsZC65g8k0)

---

---
id: 2026_zhuoshui_river_07_濁水溪出海口生態基地
name: 濁水溪出海口生態基地
description: 自然地景-水文/濕地 - 638台灣雲林縣麥寮鄉
geometry:
  type: Point
  coordinates: [120.244146, 23.821301]
properties:
  category: 自然地景-水文/濕地
  rating: 4.2
  place_id: ChIJPf_4Q-2pbjQRPk9qLK55-Hw
---

# 濁水溪出海口生態基地

- **類別**: 自然地景-水文/濕地
- **地址**: 638台灣雲林縣麥寮鄉
- **評分**: 4.2

## 簡介
(待補充詳細資料)

## 相關連結
- [Google Maps](https://www.google.com/maps/search/?api=1&query=23.821301,120.244146&query_place_id=ChIJPf_4Q-2pbjQRPk9qLK55-Hw)

---

---
id: 2026_zhuoshui_river_08_雙龍瀑布
name: 雙龍瀑布
description: 自然地景-水文/濕地 - 556台灣南投縣信義鄉
geometry:
  type: Point
  coordinates: [120.9504481, 23.7767852]
properties:
  category: 自然地景-水文/濕地
  rating: 4.4
  place_id: ChIJWSKndtvUaDQRnRoVvZzGDFI
---

# 雙龍瀑布

- **類別**: 自然地景-水文/濕地
- **地址**: 556台灣南投縣信義鄉
- **評分**: 4.4

## 簡介
(待補充詳細資料)

## 相關連結
- [Google Maps](https://www.google.com/maps/search/?api=1&query=23.7767852,120.9504481&query_place_id=ChIJWSKndtvUaDQRnRoVvZzGDFI)

---

---
id: 2026_zhuoshui_river_09_金門峒斷崖
name: 金門峒斷崖
description: 自然地景-地質 - 556台灣南投縣信義鄉金門峒斷崖
geometry:
  type: Point
  coordinates: [120.98931, 23.502296]
properties:
  category: 自然地景-地質
  rating: 0
  place_id: ChIJyxniIAIkbzQRNTR-SSehG3w
---

# 金門峒斷崖

- **類別**: 自然地景-地質
- **地址**: 556台灣南投縣信義鄉金門峒斷崖
- **評分**: 0

## 簡介
(待補充詳細資料)

## 相關連結
- [Google Maps](https://www.google.com/maps/search/?api=1&query=23.502296,120.98931&query_place_id=ChIJyxniIAIkbzQRNTR-SSehG3w)

---

---
id: 2026_zhuoshui_river_10_濁水溪
name: 濁水溪
description: 自然地景-地質 - 527台灣彰化縣大城鄉濁水溪
geometry:
  type: Point
  coordinates: [120.2838041, 23.8273796]
properties:
  category: 自然地景-地質
  rating: 4.1
  place_id: ChIJoSHnuyWsbjQR_FwJs2mzKA8
---

# 濁水溪

- **類別**: 自然地景-地質
- **地址**: 527台灣彰化縣大城鄉濁水溪
- **評分**: 4.1

## 簡介
(待補充詳細資料)

## 相關連結
- [Google Maps](https://www.google.com/maps/search/?api=1&query=23.8273796,120.2838041&query_place_id=ChIJoSHnuyWsbjQR_FwJs2mzKA8)

---

---
id: 2026_zhuoshui_river_11_武界壩
name: 武界壩
description: 水利設施-壩堰 - 546台灣南投縣仁愛鄉武界壩
geometry:
  type: Point
  coordinates: [121.057222, 23.915]
properties:
  category: 水利設施-壩堰
  rating: 0
  place_id: ChIJnT4aEqLaaDQR4PtUmAvUbTw
---

# 武界壩

- **類別**: 水利設施-壩堰
- **地址**: 546台灣南投縣仁愛鄉武界壩
- **評分**: 0

## 簡介
(待補充詳細資料)

## 相關連結
- [Google Maps](https://www.google.com/maps/search/?api=1&query=23.915,121.057222&query_place_id=ChIJnT4aEqLaaDQR4PtUmAvUbTw)

---

---
id: 2026_zhuoshui_river_12_霧社水庫
name: 霧社水庫
description: 水利設施-壩堰 - 546台灣南投縣仁愛鄉霧社水庫
geometry:
  type: Point
  coordinates: [121.1352393, 23.9991367]
properties:
  category: 水利設施-壩堰
  rating: 4.3
  place_id: ChIJk6sRD5jDaDQRmPKE5kETOQQ
---

# 霧社水庫

- **類別**: 水利設施-壩堰
- **地址**: 546台灣南投縣仁愛鄉霧社水庫
- **評分**: 4.3

## 簡介
(待補充詳細資料)

## 相關連結
- [Google Maps](https://www.google.com/maps/search/?api=1&query=23.9991367,121.1352393&query_place_id=ChIJk6sRD5jDaDQRmPKE5kETOQQ)

---

---
id: 2026_zhuoshui_river_13_集集攔河堰
name: 集集攔河堰
description: 水利設施-壩堰 - 552台灣南投縣集集鎮林尾里攔河路2號
geometry:
  type: Point
  coordinates: [120.7633291, 23.818335]
properties:
  category: 水利設施-壩堰
  rating: 4.1
  place_id: ChIJPfLmHdwsaTQRpIxw-3U8zkM
---

# 集集攔河堰

- **類別**: 水利設施-壩堰
- **地址**: 552台灣南投縣集集鎮林尾里攔河路2號
- **評分**: 4.1

## 簡介
(待補充詳細資料)

## 相關連結
- [Google Maps](https://www.google.com/maps/search/?api=1&query=23.818335,120.7633291&query_place_id=ChIJPfLmHdwsaTQRpIxw-3U8zkM)

---

---
id: 2026_zhuoshui_river_14_八堡二圳取水口
name: 八堡二圳取水口
description: 水利設施-圳路 - 530台灣彰化縣二水鄉
geometry:
  type: Point
  coordinates: [120.6450621, 23.7995881]
properties:
  category: 水利設施-圳路
  rating: 4.9
  place_id: ChIJ72RKCADNbjQRZLNW6xc5-jI
---

# 八堡二圳取水口

- **類別**: 水利設施-圳路
- **地址**: 530台灣彰化縣二水鄉
- **評分**: 4.9

## 簡介
(待補充詳細資料)

## 相關連結
- [Google Maps](https://www.google.com/maps/search/?api=1&query=23.7995881,120.6450621&query_place_id=ChIJ72RKCADNbjQRZLNW6xc5-jI)

---

---
id: 2026_zhuoshui_river_15_莿仔埤圳第一放水路
name: 莿仔埤圳第一放水路
description: 水利設施-圳路 - 524台灣彰化縣溪州鄉莿仔埤圳第一放水路
geometry:
  type: Point
  coordinates: [120.5610401, 23.8220779]
properties:
  category: 水利設施-圳路
  rating: 5
  place_id: ChIJ8SSVtOjKbjQRThZrkEQNz4E
---

# 莿仔埤圳第一放水路

- **類別**: 水利設施-圳路
- **地址**: 524台灣彰化縣溪州鄉莿仔埤圳第一放水路
- **評分**: 5

## 簡介
(待補充詳細資料)

## 相關連結
- [Google Maps](https://www.google.com/maps/search/?api=1&query=23.8220779,120.5610401&query_place_id=ChIJ8SSVtOjKbjQRThZrkEQNz4E)

---

---
id: 2026_zhuoshui_river_16_斗六大圳
name: 斗六大圳
description: 水利設施-圳路 - 台灣雲林縣斗六大圳
geometry:
  type: Point
  coordinates: [120.6007312, 23.7110601]
properties:
  category: 水利設施-圳路
  rating: 3.9
  place_id: ChIJ7YnoSCfJbjQRSUXXQjYH9eM
---

# 斗六大圳

- **類別**: 水利設施-圳路
- **地址**: 台灣雲林縣斗六大圳
- **評分**: 3.9

## 簡介
(待補充詳細資料)

## 相關連結
- [Google Maps](https://www.google.com/maps/search/?api=1&query=23.7110601,120.6007312&query_place_id=ChIJ7YnoSCfJbjQRSUXXQjYH9eM)

---

---
id: 2026_zhuoshui_river_17_石山引水道入口處
name: 石山引水道入口處
description: 水利設施-圳路 - 556台灣南投縣信義鄉阿里山公路
geometry:
  type: Point
  coordinates: [120.8459194, 23.4732996]
properties:
  category: 水利設施-圳路
  rating: 4.5
  place_id: ChIJWV50vk3ebjQR0F4Tx0RRme4
---

# 石山引水道入口處

- **類別**: 水利設施-圳路
- **地址**: 556台灣南投縣信義鄉阿里山公路
- **評分**: 4.5

## 簡介
(待補充詳細資料)

## 相關連結
- [Google Maps](https://www.google.com/maps/search/?api=1&query=23.4732996,120.8459194&query_place_id=ChIJWV50vk3ebjQR0F4Tx0RRme4)

---

---
id: 2026_zhuoshui_river_18_台電大觀發電廠_大觀G_S
name: 台電大觀發電廠(大觀G/S)
description: 水利設施-電廠 - 553台灣南投縣水里鄉明潭巷73號
geometry:
  type: Point
  coordinates: [120.869621, 23.854427]
properties:
  category: 水利設施-電廠
  rating: 4.4
  place_id: ChIJW1V4LCMqaTQRRKJ7BkoAKt8
---

# 台電大觀發電廠(大觀G/S)

- **類別**: 水利設施-電廠
- **地址**: 553台灣南投縣水里鄉明潭巷73號
- **評分**: 4.4

## 簡介
(待補充詳細資料)

## 相關連結
- [Google Maps](https://www.google.com/maps/search/?api=1&query=23.854427,120.869621&query_place_id=ChIJW1V4LCMqaTQRRKJ7BkoAKt8)

---

---
id: 2026_zhuoshui_river_19_西螺大橋
name: 西螺大橋
description: 交通設施-橋樑 - 台灣西螺大橋
geometry:
  type: Point
  coordinates: [120.461058, 23.8138002]
properties:
  category: 交通設施-橋樑
  rating: 0
  place_id: ChIJrZs43EK0bjQRK3XsEqYto-Y
---

# 西螺大橋

- **類別**: 交通設施-橋樑
- **地址**: 台灣西螺大橋
- **評分**: 0

## 簡介
(待補充詳細資料)

## 相關連結
- [Google Maps](https://www.google.com/maps/search/?api=1&query=23.8138002,120.461058&query_place_id=ChIJrZs43EK0bjQRK3XsEqYto-Y)

---

---
id: 2026_zhuoshui_river_20_溪州大橋_新西螺大橋
name: 溪州大橋(新西螺大橋)
description: 交通設施-橋樑 - 648台灣彰化縣西螺鎮縱貫公路附近號
geometry:
  type: Point
  coordinates: [120.4716127, 23.7978137]
properties:
  category: 交通設施-橋樑
  rating: 4.4
  place_id: ChIJ2V6lk0W0bjQRElvWwUfrWqY
---

# 溪州大橋(新西螺大橋)

- **類別**: 交通設施-橋樑
- **地址**: 648台灣彰化縣西螺鎮縱貫公路附近號
- **評分**: 4.4

## 簡介
(待補充詳細資料)

## 相關連結
- [Google Maps](https://www.google.com/maps/search/?api=1&query=23.7978137,120.4716127&query_place_id=ChIJ2V6lk0W0bjQRElvWwUfrWqY)

---

---
id: 2026_zhuoshui_river_21_自強大橋
name: 自強大橋
description: 交通設施-橋樑 - 台灣自強大橋
geometry:
  type: Point
  coordinates: [120.398178, 23.829617]
properties:
  category: 交通設施-橋樑
  rating: 0
  place_id: ChIJC7CXtrGzbjQRsK1dFD3wx8U
---

# 自強大橋

- **類別**: 交通設施-橋樑
- **地址**: 台灣自強大橋
- **評分**: 0

## 簡介
(待補充詳細資料)

## 相關連結
- [Google Maps](https://www.google.com/maps/search/?api=1&query=23.829617,120.398178&query_place_id=ChIJC7CXtrGzbjQRsK1dFD3wx8U)

---

---
id: 2026_zhuoshui_river_22_中沙大橋
name: 中沙大橋
description: 交通設施-橋樑 - 524台灣彰化縣溪州鄉中山高速公路
geometry:
  type: Point
  coordinates: [120.4841178, 23.8076469]
properties:
  category: 交通設施-橋樑
  rating: 5
  place_id: ChIJ0cNrFb61bjQRBcIp9fl3Z_U
---

# 中沙大橋

- **類別**: 交通設施-橋樑
- **地址**: 524台灣彰化縣溪州鄉中山高速公路
- **評分**: 5

## 簡介
(待補充詳細資料)

## 相關連結
- [Google Maps](https://www.google.com/maps/search/?api=1&query=23.8076469,120.4841178&query_place_id=ChIJ0cNrFb61bjQRBcIp9fl3Z_U)

---

---
id: 2026_zhuoshui_river_23_西濱大橋
name: 西濱大橋
description: 交通設施-橋樑 - 527台灣彰化縣大城鄉台61線
geometry:
  type: Point
  coordinates: [120.2890934, 23.8304674]
properties:
  category: 交通設施-橋樑
  rating: 3.8
  place_id: ChIJY74SHiCtbjQRd3qtso9LKFE
---

# 西濱大橋

- **類別**: 交通設施-橋樑
- **地址**: 527台灣彰化縣大城鄉台61線
- **評分**: 3.8

## 簡介
(待補充詳細資料)

## 相關連結
- [Google Maps](https://www.google.com/maps/search/?api=1&query=23.8304674,120.2890934&query_place_id=ChIJY74SHiCtbjQRd3qtso9LKFE)

---

---
id: 2026_zhuoshui_river_24_553南投縣水里鄉龍神橋
name: 553南投縣水里鄉龍神橋
description: 交通設施-橋樑 - 553台灣南投縣水里鄉龍神橋
geometry:
  type: Point
  coordinates: [120.8695967, 23.7789311]
properties:
  category: 交通設施-橋樑
  rating: 0
  place_id: ChIJWZE2KDXVbjQRBKiqeDU-m-Y
---

# 553南投縣水里鄉龍神橋

- **類別**: 交通設施-橋樑
- **地址**: 553台灣南投縣水里鄉龍神橋
- **評分**: 0

## 簡介
(待補充詳細資料)

## 相關連結
- [Google Maps](https://www.google.com/maps/search/?api=1&query=23.7789311,120.8695967&query_place_id=ChIJWZE2KDXVbjQRBKiqeDU-m-Y)

---

---
id: 2026_zhuoshui_river_25_雙龍七彩吊橋
name: 雙龍七彩吊橋
description: 交通設施-橋樑 - 556台灣南投縣信義鄉光復巷
geometry:
  type: Point
  coordinates: [120.9498198, 23.7806637]
properties:
  category: 交通設施-橋樑
  rating: 4.4
  place_id: ChIJ0zNzrODUaDQRhEHNBuJR4DE
---

# 雙龍七彩吊橋

- **類別**: 交通設施-橋樑
- **地址**: 556台灣南投縣信義鄉光復巷
- **評分**: 4.4

## 簡介
(待補充詳細資料)

## 相關連結
- [Google Maps](https://www.google.com/maps/search/?api=1&query=23.7806637,120.9498198&query_place_id=ChIJ0zNzrODUaDQRhEHNBuJR4DE)

---

---
id: 2026_zhuoshui_river_26_名竹大橋
name: 名竹大橋
description: 交通設施-橋樑 - 557台灣南投縣竹山鎮名竹大橋
geometry:
  type: Point
  coordinates: [120.7068136, 23.816025]
properties:
  category: 交通設施-橋樑
  rating: 3.8
  place_id: ChIJSXpvodozaTQRRDmRR9GGs2o
---

# 名竹大橋

- **類別**: 交通設施-橋樑
- **地址**: 557台灣南投縣竹山鎮名竹大橋
- **評分**: 3.8

## 簡介
(待補充詳細資料)

## 相關連結
- [Google Maps](https://www.google.com/maps/search/?api=1&query=23.816025,120.7068136&query_place_id=ChIJSXpvodozaTQRRDmRR9GGs2o)

---

---
id: 2026_zhuoshui_river_27_孫海橋與丹大吊橋遺構
name: 孫海橋與丹大吊橋遺構
description: 交通設施-橋樑 - 台灣南投縣信義鄉556
geometry:
  type: Point
  coordinates: [121.0117452, 23.7871899]
properties:
  category: 交通設施-橋樑
  rating: 4.3
  place_id: ChIJLbldPAvTaDQRq0nT1wJXT6w
---

# 孫海橋與丹大吊橋遺構

- **類別**: 交通設施-橋樑
- **地址**: 台灣南投縣信義鄉556
- **評分**: 4.3

## 簡介
(待補充詳細資料)

## 相關連結
- [Google Maps](https://www.google.com/maps/search/?api=1&query=23.7871899,121.0117452&query_place_id=ChIJLbldPAvTaDQRq0nT1wJXT6w)

---

---
id: 2026_zhuoshui_river_28_北港溪糯米石橋
name: 北港溪糯米石橋
description: 交通設施-橋樑 - 544台灣南投縣國姓鄉國姓路
geometry:
  type: Point
  coordinates: [120.9065125, 24.0585088]
properties:
  category: 交通設施-橋樑
  rating: 4.2
  place_id: ChIJ1UzfOm7faDQRBS1tixG_oCk
---

# 北港溪糯米石橋

- **類別**: 交通設施-橋樑
- **地址**: 544台灣南投縣國姓鄉國姓路
- **評分**: 4.2

## 簡介
(待補充詳細資料)

## 相關連結
- [Google Maps](https://www.google.com/maps/search/?api=1&query=24.0585088,120.9065125&query_place_id=ChIJ1UzfOm7faDQRBS1tixG_oCk)

---

---
id: 2026_zhuoshui_river_29_集集車站
name: 集集車站
description: 交通設施-車站 - 552台灣南投縣集集鎮
geometry:
  type: Point
  coordinates: [120.78489, 23.826451]
properties:
  category: 交通設施-車站
  rating: 4.1
  place_id: ChIJUZEbvJMsaTQRKCCSuiKnaDU
---

# 集集車站

- **類別**: 交通設施-車站
- **地址**: 552台灣南投縣集集鎮
- **評分**: 4.1

## 簡介
(待補充詳細資料)

## 相關連結
- [Google Maps](https://www.google.com/maps/search/?api=1&query=23.826451,120.78489&query_place_id=ChIJUZEbvJMsaTQRKCCSuiKnaDU)

---

---
id: 2026_zhuoshui_river_30_林先生廟
name: 林先生廟
description: 人文史蹟-古蹟/建築 - 530台灣彰化縣二水鄉員集路二段227號
geometry:
  type: Point
  coordinates: [120.6452979, 23.7992993]
properties:
  category: 人文史蹟-古蹟/建築
  rating: 4.4
  place_id: ChIJQX78_ezMbjQRzxD3t3IbeAY
---

# 林先生廟

- **類別**: 人文史蹟-古蹟/建築
- **地址**: 530台灣彰化縣二水鄉員集路二段227號
- **評分**: 4.4

## 簡介
(待補充詳細資料)

## 相關連結
- [Google Maps](https://www.google.com/maps/search/?api=1&query=23.7992993,120.6452979&query_place_id=ChIJQX78_ezMbjQRzxD3t3IbeAY)

---

---
id: 2026_zhuoshui_river_31_竹山社寮敬聖亭_縣定古蹟
name: 竹山社寮敬聖亭（縣定古蹟）
description: 人文史蹟-古蹟/建築 - 557台灣南投縣竹山鎮集山路一段1738號
geometry:
  type: Point
  coordinates: [120.722177, 23.8143469]
properties:
  category: 人文史蹟-古蹟/建築
  rating: 4.1
  place_id: ChIJw_LhiVItaTQRZJ5EaQ7FDNw
---

# 竹山社寮敬聖亭（縣定古蹟）

- **類別**: 人文史蹟-古蹟/建築
- **地址**: 557台灣南投縣竹山鎮集山路一段1738號
- **評分**: 4.1

## 簡介
(待補充詳細資料)

## 相關連結
- [Google Maps](https://www.google.com/maps/search/?api=1&query=23.8143469,120.722177&query_place_id=ChIJw_LhiVItaTQRZJ5EaQ7FDNw)

---

---
id: 2026_zhuoshui_river_32_振文書院_文祠廟
name: 振文書院(文祠廟)
description: 人文史蹟-古蹟/建築 - 648台灣雲林縣西螺鎮興農西路6號
geometry:
  type: Point
  coordinates: [120.4644577, 23.7945403]
properties:
  category: 人文史蹟-古蹟/建築
  rating: 4.4
  place_id: ChIJzUP3oDy0bjQRpK-MAS3uJ8I
---

# 振文書院(文祠廟)

- **類別**: 人文史蹟-古蹟/建築
- **地址**: 648台灣雲林縣西螺鎮興農西路6號
- **評分**: 4.4

## 簡介
(待補充詳細資料)

## 相關連結
- [Google Maps](https://www.google.com/maps/search/?api=1&query=23.7945403,120.4644577&query_place_id=ChIJzUP3oDy0bjQRpK-MAS3uJ8I)

---

---
id: 2026_zhuoshui_river_33_明新書院
name: 明新書院
description: 人文史蹟-古蹟/建築 - 552台灣南投縣集集鎮東昌巷4號
geometry:
  type: Point
  coordinates: [120.7995314, 23.8275444]
properties:
  category: 人文史蹟-古蹟/建築
  rating: 4.1
  place_id: ChIJqck7NIMsaTQRdjaUSXMaNh8
---

# 明新書院

- **類別**: 人文史蹟-古蹟/建築
- **地址**: 552台灣南投縣集集鎮東昌巷4號
- **評分**: 4.1

## 簡介
(待補充詳細資料)

## 相關連結
- [Google Maps](https://www.google.com/maps/search/?api=1&query=23.8275444,120.7995314&query_place_id=ChIJqck7NIMsaTQRdjaUSXMaNh8)

---

---
id: 2026_zhuoshui_river_34_花蓮縣八通關古道
name: 花蓮縣八通關古道
description: 人文史蹟-古蹟/建築 - 台灣花蓮縣八通關古道
geometry:
  type: Point
  coordinates: [121.2479617, 23.3237454]
properties:
  category: 人文史蹟-古蹟/建築
  rating: 0
  place_id: ChIJ31zzuxkVbzQRLji2Yos29tE
---

# 花蓮縣八通關古道

- **類別**: 人文史蹟-古蹟/建築
- **地址**: 台灣花蓮縣八通關古道
- **評分**: 0

## 簡介
(待補充詳細資料)

## 相關連結
- [Google Maps](https://www.google.com/maps/search/?api=1&query=23.3237454,121.2479617&query_place_id=ChIJ31zzuxkVbzQRLji2Yos29tE)

---

---
id: 2026_zhuoshui_river_35_詔安客家文化館
name: 詔安客家文化館
description: 人文史蹟-古蹟/建築 - 637台灣雲林縣崙背鄉東明村民生路28-8號
geometry:
  type: Point
  coordinates: [120.355071, 23.763744]
properties:
  category: 人文史蹟-古蹟/建築
  rating: 4
  place_id: ChIJR0vn5M2xbjQRILjNdDuDG94
---

# 詔安客家文化館

- **類別**: 人文史蹟-古蹟/建築
- **地址**: 637台灣雲林縣崙背鄉東明村民生路28-8號
- **評分**: 4

## 簡介
(待補充詳細資料)

## 相關連結
- [Google Maps](https://www.google.com/maps/search/?api=1&query=23.763744,120.355071&query_place_id=ChIJR0vn5M2xbjQRILjNdDuDG94)

---

---
id: 2026_zhuoshui_river_36_西螺福興宮_西螺媽祖太平媽_媽祖文化祭_丙午年網路點燈_安太歲_線上喜點福燈_2026點燈服務
name: 【西螺福興宮 西螺媽祖太平媽】媽祖文化祭｜丙午年網路點燈｜安太歲｜線上喜點福燈｜2026點燈服務
description: 人文史蹟-宗教信仰 - 648台灣雲林縣西螺鎮延平路180號
geometry:
  type: Point
  coordinates: [120.4605261, 23.8015652]
properties:
  category: 人文史蹟-宗教信仰
  rating: 4.6
  place_id: ChIJkzhtRj60bjQRioVRZXyC5WM
---

# 【西螺福興宮 西螺媽祖太平媽】媽祖文化祭｜丙午年網路點燈｜安太歲｜線上喜點福燈｜2026點燈服務

- **類別**: 人文史蹟-宗教信仰
- **地址**: 648台灣雲林縣西螺鎮延平路180號
- **評分**: 4.6

## 簡介
(待補充詳細資料)

## 相關連結
- [Google Maps](https://www.google.com/maps/search/?api=1&query=23.8015652,120.4605261&query_place_id=ChIJkzhtRj60bjQRioVRZXyC5WM)

---

---
id: 2026_zhuoshui_river_37_縣定古蹟西螺廣福宮_西螺媽老大媽廟
name: 縣定古蹟西螺廣福宮 西螺媽老大媽廟
description: 人文史蹟-宗教信仰 - 648台灣雲林縣西螺鎮新街路32號
geometry:
  type: Point
  coordinates: [120.4647035, 23.7971558]
properties:
  category: 人文史蹟-宗教信仰
  rating: 4.6
  place_id: ChIJG3Zn9Tu0bjQRMlvDwkeIUwY
---

# 縣定古蹟西螺廣福宮 西螺媽老大媽廟

- **類別**: 人文史蹟-宗教信仰
- **地址**: 648台灣雲林縣西螺鎮新街路32號
- **評分**: 4.6

## 簡介
(待補充詳細資料)

## 相關連結
- [Google Maps](https://www.google.com/maps/search/?api=1&query=23.7971558,120.4647035&query_place_id=ChIJG3Zn9Tu0bjQRMlvDwkeIUwY)

---

---
id: 2026_zhuoshui_river_38_麥寮拱範宮
name: 麥寮拱範宮
description: 人文史蹟-宗教信仰 - 638台灣雲林縣麥寮鄉中正路3號
geometry:
  type: Point
  coordinates: [120.2555916, 23.7482552]
properties:
  category: 人文史蹟-宗教信仰
  rating: 4.7
  place_id: ChIJ-yiS7FOvbjQRIHnDWn-xc6A
---

# 麥寮拱範宮

- **類別**: 人文史蹟-宗教信仰
- **地址**: 638台灣雲林縣麥寮鄉中正路3號
- **評分**: 4.7

## 簡介
(待補充詳細資料)

## 相關連結
- [Google Maps](https://www.google.com/maps/search/?api=1&query=23.7482552,120.2555916&query_place_id=ChIJ-yiS7FOvbjQRIHnDWn-xc6A)

---

---
id: 2026_zhuoshui_river_39_竹山紫南宮
name: 竹山紫南宮
description: 人文史蹟-宗教信仰 - 557台灣南投縣竹山鎮大公街40號
geometry:
  type: Point
  coordinates: [120.7225793, 23.8170767]
properties:
  category: 人文史蹟-宗教信仰
  rating: 4.7
  place_id: ChIJiREHEVItaTQRCw4OxSRg5Lo
---

# 竹山紫南宮

- **類別**: 人文史蹟-宗教信仰
- **地址**: 557台灣南投縣竹山鎮大公街40號
- **評分**: 4.7

## 簡介
(待補充詳細資料)

## 相關連結
- [Google Maps](https://www.google.com/maps/search/?api=1&query=23.8170767,120.7225793&query_place_id=ChIJiREHEVItaTQRCw4OxSRg5Lo)

---

---
id: 2026_zhuoshui_river_40_武界部落
name: 武界部落
description: 人文史蹟-聚落(原民) - 546台灣南投縣仁愛鄉界山巷4號
geometry:
  type: Point
  coordinates: [121.0442446, 23.9155571]
properties:
  category: 人文史蹟-聚落(原民)
  rating: 4.4
  place_id: ChIJV73RK4XaaDQRsBQWVZtcYrE
---

# 武界部落

- **類別**: 人文史蹟-聚落(原民)
- **地址**: 546台灣南投縣仁愛鄉界山巷4號
- **評分**: 4.4

## 簡介
(待補充詳細資料)

## 相關連結
- [Google Maps](https://www.google.com/maps/search/?api=1&query=23.9155571,121.0442446&query_place_id=ChIJV73RK4XaaDQRsBQWVZtcYrE)

---

---
id: 2026_zhuoshui_river_41_萬豐村曲冰部落
name: 萬豐村曲冰部落
description: 人文史蹟-聚落(原民) - 546台灣南投縣仁愛鄉
geometry:
  type: Point
  coordinates: [121.0767669, 23.9460544]
properties:
  category: 人文史蹟-聚落(原民)
  rating: 4.2
  place_id: ChIJQ-Z3toHaaDQR6gTMVwknZpg
---

# 萬豐村曲冰部落

- **類別**: 人文史蹟-聚落(原民)
- **地址**: 546台灣南投縣仁愛鄉
- **評分**: 4.2

## 簡介
(待補充詳細資料)

## 相關連結
- [Google Maps](https://www.google.com/maps/search/?api=1&query=23.9460544,121.0767669&query_place_id=ChIJQ-Z3toHaaDQR6gTMVwknZpg)

---

---
id: 2026_zhuoshui_river_42_過坑山
name: 過坑山
description: 人文史蹟-聚落(原民) - 555台灣南投縣魚池鄉過坑山
geometry:
  type: Point
  coordinates: [120.979574, 23.884353]
properties:
  category: 人文史蹟-聚落(原民)
  rating: 3.9
  place_id: ChIJ90_WyCnXaDQR8O2KMl-lHVs
---

# 過坑山

- **類別**: 人文史蹟-聚落(原民)
- **地址**: 555台灣南投縣魚池鄉過坑山
- **評分**: 3.9

## 簡介
(待補充詳細資料)

## 相關連結
- [Google Maps](https://www.google.com/maps/search/?api=1&query=23.884353,120.979574&query_place_id=ChIJ90_WyCnXaDQR8O2KMl-lHVs)

---

---
id: 2026_zhuoshui_river_43_雙龍部落伊希岸農場露營區
name: 雙龍部落伊希岸農場露營區
description: 人文史蹟-聚落(原民) - 556台灣南投縣信義鄉
geometry:
  type: Point
  coordinates: [120.9473155, 23.7645348]
properties:
  category: 人文史蹟-聚落(原民)
  rating: 4.5
  place_id: ChIJDy1KgtTUaDQR4gdhc9Izxqo
---

# 雙龍部落伊希岸農場露營區

- **類別**: 人文史蹟-聚落(原民)
- **地址**: 556台灣南投縣信義鄉
- **評分**: 4.5

## 簡介
(待補充詳細資料)

## 相關連結
- [Google Maps](https://www.google.com/maps/search/?api=1&query=23.7645348,120.9473155&query_place_id=ChIJDy1KgtTUaDQR4gdhc9Izxqo)

---

---
id: 2026_zhuoshui_river_44_北斗鎮
name: 北斗鎮
description: 人文史蹟-聚落(漢人) - 521台灣彰化縣北斗鎮
geometry:
  type: Point
  coordinates: [120.5336665, 23.869208]
properties:
  category: 人文史蹟-聚落(漢人)
  rating: 0
  place_id: ChIJFfRZm1s1aTQRaNPfvKPIOBo
---

# 北斗鎮

- **類別**: 人文史蹟-聚落(漢人)
- **地址**: 521台灣彰化縣北斗鎮
- **評分**: 0

## 簡介
(待補充詳細資料)

## 相關連結
- [Google Maps](https://www.google.com/maps/search/?api=1&query=23.869208,120.5336665&query_place_id=ChIJFfRZm1s1aTQRaNPfvKPIOBo)

---

---
id: 2026_zhuoshui_river_45_竹山鎮
name: 竹山鎮
description: 人文史蹟-聚落(漢人) - 557台灣南投縣竹山鎮
geometry:
  type: Point
  coordinates: [120.6890055, 23.712201]
properties:
  category: 人文史蹟-聚落(漢人)
  rating: 0
  place_id: ChIJfZEn0PHRbjQR9pIp-ZNvupA
---

# 竹山鎮

- **類別**: 人文史蹟-聚落(漢人)
- **地址**: 557台灣南投縣竹山鎮
- **評分**: 0

## 簡介
(待補充詳細資料)

## 相關連結
- [Google Maps](https://www.google.com/maps/search/?api=1&query=23.712201,120.6890055&query_place_id=ChIJfZEn0PHRbjQR9pIp-ZNvupA)

---

---
id: 2026_zhuoshui_river_46_水里鄉
name: 水里鄉
description: 人文史蹟-聚落(漢人) - 553台灣南投縣水里鄉
geometry:
  type: Point
  coordinates: [120.8613785, 23.7919524]
properties:
  category: 人文史蹟-聚落(漢人)
  rating: 0
  place_id: ChIJEUvZx5IqaTQR4Aea9veuLCE
---

# 水里鄉

- **類別**: 人文史蹟-聚落(漢人)
- **地址**: 553台灣南投縣水里鄉
- **評分**: 0

## 簡介
(待補充詳細資料)

## 相關連結
- [Google Maps](https://www.google.com/maps/search/?api=1&query=23.7919524,120.8613785&query_place_id=ChIJEUvZx5IqaTQR4Aea9veuLCE)

---

---
id: 2026_zhuoshui_river_47_麥寮鄉
name: 麥寮鄉
description: 人文史蹟-聚落(漢人) - 638台灣雲林縣麥寮鄉
geometry:
  type: Point
  coordinates: [120.2563528, 23.7485672]
properties:
  category: 人文史蹟-聚落(漢人)
  rating: 0
  place_id: ChIJqwPRB1OvbjQRxE6-ez7rCg8
---

# 麥寮鄉

- **類別**: 人文史蹟-聚落(漢人)
- **地址**: 638台灣雲林縣麥寮鄉
- **評分**: 0

## 簡介
(待補充詳細資料)

## 相關連結
- [Google Maps](https://www.google.com/maps/search/?api=1&query=23.7485672,120.2563528&query_place_id=ChIJqwPRB1OvbjQRxE6-ez7rCg8)

---

---
id: 2026_zhuoshui_river_48_車籠埔斷層保存園區
name: 車籠埔斷層保存園區
description: 災害與環境 - 557014台灣南投縣竹山鎮集山路二段345號
geometry:
  type: Point
  coordinates: [120.7115267, 23.7945692]
properties:
  category: 災害與環境
  rating: 4.4
  place_id: ChIJ4XN7jF_NbjQR0_E22tzTorI
---

# 車籠埔斷層保存園區

- **類別**: 災害與環境
- **地址**: 557014台灣南投縣竹山鎮集山路二段345號
- **評分**: 4.4

## 簡介
(待補充詳細資料)

## 相關連結
- [Google Maps](https://www.google.com/maps/search/?api=1&query=23.7945692,120.7115267&query_place_id=ChIJ4XN7jF_NbjQR0_E22tzTorI)

---
