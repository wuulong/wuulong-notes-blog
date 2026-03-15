---
title: 全台重要探索點位匯總地圖 (National Exploration Spots)
date: 2026-03-15
description: 整合古蹟、森林遊樂區、博物館及國家公園等 1200+ 個國家級重要點位，提供跨領域的探索脈絡。
---

```mermaid
graph TD
    A[全台探索點位] --> B[人文歷史]
    A --> C[自然生態]
    A --> D[文化藝術]
    
    B --> B1[古蹟/建築]
    C --> C1[森林遊樂區]
    C --> C2[國家公園/風景區]
    D --> D1[博物館/美術館]
```

# 全台重要探索點位匯總地圖

本圖資透過數位考古方式，整合了台灣目前營運中且具備高度探索價值的國家級重要節點。

## 💧 歷史與空間脈絡 (Project Context)
- **官方資源**: [文化部 iCulture](https://cloud.culture.tw/), [農業部山林悠遊網](https://recreation.forest.gov.tw/)
- **資料規模**: 本地圖集成了全台 22 縣市的 1060 處古蹟、19 處森林遊樂區以及 236 處博物館。
- **定位技術**: 採用官方與 Google Places API 雙重定錨，確保 L0 骨架準確。

## 🗺️ AI 深度探索 (Deep Research)
如果您擁有 Gemini Advanced 或其他 Deep Research 工具，可以複製以下 Prompt，針對本地圖進行深度的文史與美食探索：

```markdown
# Context
本專案為 WalkGIS 全台探索計畫的一環，旨在連結現代地景與歷史摺層。

# Task
請針對以下景點列表進行 Deep Research，挖掘背後的「歷史深度」、「生活溫度」與「在地美食」。

**景點列表：**
- 嘉義仁武宮
- 嘉義西門長老教會禮拜堂
- 嘉義火車站
- 菸酒公賣局嘉義分局
- 新竹鄭氏家廟
- 新竹長和宮
- 新竹都城隍廟
- 李錫金孝子坊
- 張氏節孝坊
- 蘇氏節孝坊
- 楊氏節孝坊
- 新竹州廳
- 新竹水仙宮
- 香山火車站(前香山驛)
- 新竹神社殘蹟及其附屬建築
- 新竹市役所
- 李克承博士故居
- 新竹少年刑務所演武場
- 吉利第
- 春官第
... (詳見索引)

# Requirements
1. **歷史與工程脈絡**: 該點在台灣開發史或文化遺產中的地位？
2. **在地文化與生態**: 周邊的隱藏亮點。
3. **順遊景點**: 同區域值得探訪的節點。
4. **必吃在地美食**: 在地人認證的味蕾記憶。
```

## 📊 用 Dynamic View 視覺化您的研究
研究報告完成後，請在 Dynamic View 中使用以下 Prompt 進行結構化呈現：

- **Timeline**: `請以時間軸呈現這些古蹟或館舍的核心建造/開放年份。`
- **Comparison Table**: `建立比較表格分析不同類別點位的探索價值。`

## 景點 Feature 索引
- [嘉義仁武宮](?map=national_exploration_spots&feature=20260315_嘉義仁武宮)
- [嘉義西門長老教會禮拜堂](?map=national_exploration_spots&feature=20260315_嘉義西門長老教會禮拜堂)
- [嘉義火車站](?map=national_exploration_spots&feature=20260315_嘉義火車站)
- [菸酒公賣局嘉義分局](?map=national_exploration_spots&feature=20260315_菸酒公賣局嘉義分局)
- [新竹鄭氏家廟](?map=national_exploration_spots&feature=20260315_新竹鄭氏家廟)
- [新竹長和宮](?map=national_exploration_spots&feature=20260315_新竹長和宮)
- [新竹都城隍廟](?map=national_exploration_spots&feature=20260315_新竹都城隍廟)
- [李錫金孝子坊](?map=national_exploration_spots&feature=20260315_李錫金孝子坊)
- [張氏節孝坊](?map=national_exploration_spots&feature=20260315_張氏節孝坊)
- [蘇氏節孝坊](?map=national_exploration_spots&feature=20260315_蘇氏節孝坊)
- [楊氏節孝坊](?map=national_exploration_spots&feature=20260315_楊氏節孝坊)
- [新竹州廳](?map=national_exploration_spots&feature=20260315_新竹州廳)
- [新竹水仙宮](?map=national_exploration_spots&feature=20260315_新竹水仙宮)
- [香山火車站(前香山驛)](?map=national_exploration_spots&feature=20260315_香山火車站(前香山驛))
- [新竹神社殘蹟及其附屬建築](?map=national_exploration_spots&feature=20260315_新竹神社殘蹟及其附屬建築)
- [新竹市役所](?map=national_exploration_spots&feature=20260315_新竹市役所)
- [李克承博士故居](?map=national_exploration_spots&feature=20260315_李克承博士故居)
- [新竹少年刑務所演武場](?map=national_exploration_spots&feature=20260315_新竹少年刑務所演武場)
- [吉利第](?map=national_exploration_spots&feature=20260315_吉利第)
- [春官第](?map=national_exploration_spots&feature=20260315_春官第)
- [康朗段防空碉堡](?map=national_exploration_spots&feature=20260315_康朗段防空碉堡)
- [康樂段防空碉堡](?map=national_exploration_spots&feature=20260315_康樂段防空碉堡)
- [周益記](?map=national_exploration_spots&feature=20260315_周益記)
- [觀音禪堂](?map=national_exploration_spots&feature=20260315_觀音禪堂)
- [原大阪商船株式會社臺北支店](?map=national_exploration_spots&feature=20260315_原大阪商船株式會社臺北支店)
- [臺北府城—東門、南門、小南門、北門](?map=national_exploration_spots&feature=20260315_臺北府城—東門、南門、小南門、北門)
- [欽差行臺](?map=national_exploration_spots&feature=20260315_欽差行臺)
- [原臺灣教育會館](?map=national_exploration_spots&feature=20260315_原臺灣教育會館)
- [黃氏節孝坊](?map=national_exploration_spots&feature=20260315_黃氏節孝坊)
- [急公好義坊](?map=national_exploration_spots&feature=20260315_急公好義坊)
- [勸業銀行舊廈](?map=national_exploration_spots&feature=20260315_勸業銀行舊廈)
- [臺北郵局](?map=national_exploration_spots&feature=20260315_臺北郵局)
- [臺灣總督府博物館](?map=national_exploration_spots&feature=20260315_臺灣總督府博物館)
- [總統府](?map=national_exploration_spots&feature=20260315_總統府)
- [監察院](?map=national_exploration_spots&feature=20260315_監察院)
- [行政院](?map=national_exploration_spots&feature=20260315_行政院)
- [臺北賓館](?map=national_exploration_spots&feature=20260315_臺北賓館)
- [司法大廈](?map=national_exploration_spots&feature=20260315_司法大廈)
- [臺北撫臺街洋樓](?map=national_exploration_spots&feature=20260315_臺北撫臺街洋樓)
- [曹洞宗大本山臺灣別院鐘樓](?map=national_exploration_spots&feature=20260315_曹洞宗大本山臺灣別院鐘樓)
- [寶藏巖](?map=national_exploration_spots&feature=20260315_寶藏巖)
- [臺大醫學院舊館](?map=national_exploration_spots&feature=20260315_臺大醫學院舊館)
- [臺北第一高女](?map=national_exploration_spots&feature=20260315_臺北第一高女)
- [建國中學紅樓](?map=national_exploration_spots&feature=20260315_建國中學紅樓)
- [原臺北信用組合](?map=national_exploration_spots&feature=20260315_原臺北信用組合)
- [臺灣電力株式會社社長宿舍](?map=national_exploration_spots&feature=20260315_臺灣電力株式會社社長宿舍)
- [臺灣銀行](?map=national_exploration_spots&feature=20260315_臺灣銀行)
- [帝國生命保險株式會社臺北支店](?map=national_exploration_spots&feature=20260315_帝國生命保險株式會社臺北支店)
- [臺灣總督府電話交換局](?map=national_exploration_spots&feature=20260315_臺灣總督府電話交換局)
- [濟南基督長老教會](?map=national_exploration_spots&feature=20260315_濟南基督長老教會)
- [原三井物產株式會社臺北支店](?map=national_exploration_spots&feature=20260315_原三井物產株式會社臺北支店)
- [婦聯總會](?map=national_exploration_spots&feature=20260315_婦聯總會)
- [國定古蹟嚴家淦故居](?map=national_exploration_spots&feature=20260315_國定古蹟嚴家淦故居)
- [臺北水道水源地](?map=national_exploration_spots&feature=20260315_臺北水道水源地)
- [李國鼎故居](?map=national_exploration_spots&feature=20260315_李國鼎故居)
- [臺北酒廠](?map=national_exploration_spots&feature=20260315_臺北酒廠)
- [原臺灣軍司令部](?map=national_exploration_spots&feature=20260315_原臺灣軍司令部)
- [原臺灣軍司令官官邸(孫立人將軍官邸)](?map=national_exploration_spots&feature=20260315_原臺灣軍司令官官邸(孫立人將軍官邸))
- [紀州庵](?map=national_exploration_spots&feature=20260315_紀州庵)
- [孫運璿重慶南路寓所](?map=national_exploration_spots&feature=20260315_孫運璿重慶南路寓所)
- [南海學園科學館](?map=national_exploration_spots&feature=20260315_南海學園科學館)
- [原大磯內科醫院](?map=national_exploration_spots&feature=20260315_原大磯內科醫院)
- [牯嶺街高等官舍群](?map=national_exploration_spots&feature=20260315_牯嶺街高等官舍群)
- [國立臺灣大學日式宿舍－福州街20、22、26號](?map=national_exploration_spots&feature=20260315_國立臺灣大學日式宿舍－福州街20、22、26號)
- [齊東街日式宿舍](?map=national_exploration_spots&feature=20260315_齊東街日式宿舍)
- [專賣局(今臺灣菸酒股份有限公司)](?map=national_exploration_spots&feature=20260315_專賣局(今臺灣菸酒股份有限公司))
- [福州街11號日式宿舍](?map=national_exploration_spots&feature=20260315_福州街11號日式宿舍)
- [前南菜園日式宿舍](?map=national_exploration_spots&feature=20260315_前南菜園日式宿舍)
- [清代機器局遺構](?map=national_exploration_spots&feature=20260315_清代機器局遺構)
- [陳天來故居](?map=national_exploration_spots&feature=20260315_陳天來故居)
- [歸綏街文萌樓](?map=national_exploration_spots&feature=20260315_歸綏街文萌樓)
- [機器局第五號倉庫](?map=national_exploration_spots&feature=20260315_機器局第五號倉庫)
- [鐵道部部長宿舍](?map=national_exploration_spots&feature=20260315_鐵道部部長宿舍)
- [大稻埕千秋街店屋](?map=national_exploration_spots&feature=20260315_大稻埕千秋街店屋)
- [大稻埕圓環防空蓄水池](?map=national_exploration_spots&feature=20260315_大稻埕圓環防空蓄水池)
- [台灣基督長老教會大稻埕教會](?map=national_exploration_spots&feature=20260315_台灣基督長老教會大稻埕教會)
- [台北霞海城隍廟](?map=national_exploration_spots&feature=20260315_台北霞海城隍廟)
- [新芳春茶行](?map=national_exploration_spots&feature=20260315_新芳春茶行)
- [大稻埕辜宅](?map=national_exploration_spots&feature=20260315_大稻埕辜宅)
- [臺北市政府舊廈(原建成小學校)](?map=national_exploration_spots&feature=20260315_臺北市政府舊廈(原建成小學校))
- [原臺北北警察署](?map=national_exploration_spots&feature=20260315_原臺北北警察署)
- [陳德星堂](?map=national_exploration_spots&feature=20260315_陳德星堂)
- [臺北孔子廟](?map=national_exploration_spots&feature=20260315_臺北孔子廟)
- [鐵道部臺北工場車輛修理工場](?map=national_exploration_spots&feature=20260315_鐵道部臺北工場車輛修理工場)
- [前美國大使官邸](?map=national_exploration_spots&feature=20260315_前美國大使官邸)
- [臨濟護國禪寺](?map=national_exploration_spots&feature=20260315_臨濟護國禪寺)
- [臺北第三高女(中山女中)](?map=national_exploration_spots&feature=20260315_臺北第三高女(中山女中))
- [圓山別莊](?map=national_exploration_spots&feature=20260315_圓山別莊)
- [中山基督長老教會](?map=national_exploration_spots&feature=20260315_中山基督長老教會)
- [臺北市政府衛生局舊址](?map=national_exploration_spots&feature=20260315_臺北市政府衛生局舊址)
- [蔡瑞月舞蹈研究社](?map=national_exploration_spots&feature=20260315_蔡瑞月舞蹈研究社)
- [建國啤酒廠](?map=national_exploration_spots&feature=20260315_建國啤酒廠)
- [松山市場](?map=national_exploration_spots&feature=20260315_松山市場)
- [總督府山林課宿舍](?map=national_exploration_spots&feature=20260315_總督府山林課宿舍)
- [殷海光故居](?map=national_exploration_spots&feature=20260315_殷海光故居)
- [臺灣大學校門](?map=national_exploration_spots&feature=20260315_臺灣大學校門)
- [臺北工業學校紅樓](?map=national_exploration_spots&feature=20260315_臺北工業學校紅樓)
- [清真寺](?map=national_exploration_spots&feature=20260315_清真寺)
- [芳蘭大厝](?map=national_exploration_spots&feature=20260315_芳蘭大厝)
- [紫藤廬](?map=national_exploration_spots&feature=20260315_紫藤廬)
- ...以及其他 1157 個點位。

---
*數位紀錄：全台重要探索點位 L0/L1 補完計畫 (2026-03-15)*
