---
map_id: 2025_houfeng_dongfeng_loop
name: 后豐鐵馬道 & 東豐綠廊精華遊
region: 台中/后里/豐原/石岡/東勢
difficulty: Easy
date: 2025-12-29
---

# 后豐鐵馬道 & 東豐綠廊精華遊

這是一條結合「舊山線鐵道歷史」與「大甲溪水岸風光」的經典自行車路線。全程約 18 公里，串聯了后里馬場、花樑鋼橋、石岡水壩與東勢客家文化園區，是台中最受歡迎的綠色隧道。

## 🗺️ 地圖概覽 (Map Overview)

![后豐鐵馬道與東豐綠廊道導覽圖](../assets/images/2025_houfeng_dongfeng_loop.jpg)

## 🛤️ 路線拓樸 (Route Topology)

```mermaid
graph LR;
    %% 子圖：后豐鐵馬道
    subgraph Houfeng ["后豐鐵馬道 (4.5km)"]
        direction TB
        H1(1. 后里馬場) --> HA(樟樹平台);
        HA --> H2(2. 夫妻樹);
        H2 --> H3(3. 九號隧道);
        H3 --> H4(4. 花樑鋼橋);
        H4 --> HB(鐵道之鄉酒莊);
        HB -.-> HC(榮町雜貨店);
    end

    %% 子圖：東豐綠廊 (前段)
    subgraph Dongfeng_Start ["東豐綠廊-起點段"]
        D7(7. 豐原大道) --> Junction{綠廊交接處};
        HB --> Junction;
        Junction --> D5(5. 朴口車站);
        D5 --> HE(200days冰店);
        HE --> D6(6. 豐榮水利碑);
    end

    %% 子圖：石岡精華段
    subgraph Shigang ["石岡精華段"]
        D6 --> D9(9. 石岡水壩);
        D9 -.-> D10(10. 石岡斷層月台);
        D9 --> D11(11. 0蛋月台);
        D11 --> D12(12. 九房3D彩繪村);
        D12 --> D13(13. 石岡旅服中心);
        D13 --> D14(14. 情人木橋);
        D14 -.-> D15(15. 土牛客家館);
    end

    %% 子圖：東勢段
    subgraph Dongshi ["東勢終點段"]
        D14 --> D16(16. 梅子車站);
        D16 --> D17(17. 梅子百年芒果樹);
        D17 --> D18(18. 梅子鐵橋);
        D18 --> D19(19. 東勢客家園區);
    end

    %% 周邊景點
    D8(8. 公老坪) -.-> D7;

    %% 樣式設定
    classDef spot fill:#fff,stroke:#333,stroke-width:2px;
    classDef highlight fill:#fcf,stroke:#f00,stroke-width:2px;
    class H1,H3,H4,D9,D11,D19 highlight;
    class Junction fill:#ff9,stroke:#333,stroke-width:2px,shape:rhombus;
```

## 🗺️ AI 深度探索 (Deep Research)
如果您擁有 Gemini Advanced 或其他 Deep Research 工具，可以複製以下 Prompt，將單純的騎車行程升級為深度的文史走讀：

```markdown
# Context
「后豐鐵馬道」與「東豐綠廊」是台中最經典的兩條自行車專用道，前身分別是「舊山線鐵路」與「東勢支線鐵路」。這一路見證了台灣中部山線鐵路的興衰、921地震的傷痕，以及客家聚落的發展。

# Task
針對以下景點列表，進行深度的文史挖掘與旅遊資訊整合。

**景點列表：**
1. 后里馬場 (百年馬場)
2. 九號隧道 (舊山線經典)
3. 花樑鋼橋 (大甲溪上的鋼鐵巨人)
4. 朴口車站/石岡車站 (消失的車站)
5. 石岡水壩 (地震遺跡)
6. 0蛋月台 (廢棄車廂)
7. 情人木橋 (全台最大木造橋)
8. 梅子鐵橋 (跨越石角溪)
9. 東勢客家文化園區 (舊東勢車站)

# Requirements (請分析以下維度)
1. **鐵道記憶**: 舊山線與東勢支線的建造歷史與停駛原因？
2. **震殤與重生**: 921地震如何改變地貌（石岡壩斷層、埤豐大橋）？
3. **建築美學**: 花樑鋼橋的結構特色？情人木橋的建造工法？
4. **在地美食**: 石岡蜂巢蛋糕、東勢牛肉麵/水餃、沿線特色冰店 (如 200days)。
```

## 📍 包含景點 (Points of Interest)

### 后豐段 (Houfeng Section)
*   [后里馬場](../features/20251229_houli_ranch.md)
*   [九號隧道](../features/20251229_tunnel_9.md)
*   [花樑鋼橋](../features/20251229_old_beam_bridge.md)

### 東豐段 (Dongfeng Section)
*   [石岡水壩](../features/20251229_shigang_dam.md)
*   [0蛋月台](../features/20251229_0_dan_platform.md)
*   [情人木橋](../features/20251229_lovers_bridge.md)
*   [東勢客家文化園區](../features/20251229_dongshi_hakka.md)

*(完整清單請參閱 features 目錄)*
