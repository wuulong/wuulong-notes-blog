---
title: "實作筆記：從 SQLite 到 NotebookLM，自動化產製卡通風格導覽地圖"
date: 2025-12-29T18:15:00+08:00
draft: false
categories: ["AI Workflow", "GenAI", "WalkGIS"]
tags: ["NotebookLM", "SQLite", "Automation", "RAG", "Prompt Engineering"]
summary: "如何將生硬的 GIS 數據變成生動的旅遊故事？本文分享我的 WalkGIS 自動化工作流：使用 Shell Script 從 SQLite 精準萃取地圖資料，餵給 Google NotebookLM，一鍵生成卡通風格導覽與投影片大綱。"
---

在 [WalkGIS V0.1 發布](/posts/20251229_walkgis_v0_1_release/) 後，我擁有了一個結構嚴謹的 SQLite 資料庫 (`walkgis.db`)，裡面躺著精確的經緯度、WKT 在地幾何資料，以及 24 個景點的詳細 Markdown 介紹。

這對開發者來說很完美，但對一般遊客來說太「硬」了。

**「我能不能把這些資料丟給 AI，讓它變成一份像是【宮崎駿風格】的導覽手冊，甚至直接生出一份旅遊介紹投影片？」**

答案是可以的，而且非常快。這篇文章將分享我如何建立這套 **「DB to NotebookLM」** 的自動化工作流。

## 🚀 工作流架構 (The Pipeline)

我的目標是將「特定地圖」的所有相關資料打包成一個巨大的 "Mega Context File"，然後上傳到 Google NotebookLM。

流程如下：
1.  **Select**: 輸入地圖 ID (例如 `2025_houfeng_dongfeng_loop`)。
2.  **Query**: 腳本自動查詢 SQLite，找出該地圖關聯的所有景點 (Features)。
3.  **Merge**: 將地圖結構 (Mermaid) 與所有景點內容 (Markdown) 合併。
4.  **Inject**: 在檔頭注入「卡通嚮導」的 System Prompt。
5.  **Generate**: NotebookLM 讀取後，產出視覺化描述與投影片內容。

![WalkGIS工作流心智圖](walkgis_workflow_mindmap.png)
*(圖說：從資料庫萃取資料到 AI 生成的完整邏輯路徑)*

## 🛠️ 關鍵技術 I: 智慧萃取腳本

最核心的挑戰在於：我的 `features/` 資料夾裡可能有上百個景點，但我只想抓取「屬於這張地圖」的那 25 個。

我寫了一個 Shell Script (`gen_notebooklm_context.sh`) 來完成這個任務。它利用 `sqlite3` 直接查詢關聯表：

```bash
# 從資料庫查詢特定地圖 (MAP_ID) 關聯的所有 Feature IDs
FEATURE_IDS=$(sqlite3 "$DB_FILE" "SELECT feature_id FROM walking_map_relations WHERE map_id = '$MAP_ID' ORDER BY display_order ASC;")

# 遍歷並合併檔案
for fid in $FEATURE_IDS; do
    cat "$FEATURES_DIR/$fid.md" >> "$OUTPUT_FILE"
done
```

這樣做的好處是**精準**。這份 Context File 裡不會有任何雜訊，每一行文字都跟這趟旅程有關。

## 🪄 關鍵技術 II: 角色賦能 (Prompt Engineering)

為了讓 NotebookLM 產出的內容不像是「維基百科」，而像是「旅遊繪本」，我在生成的 Markdown 檔頭 (Header) 強制注入了這段指令：

```markdown
# AI INSTRUCTION HEADER
Role: You are an enthusiastic, cartoon-style Travel Guide...
Tone: Fun, Energetic, Child-friendly, Vibrant.

## Output Requirements
1. **Visual Map Description**: Describe a hand-drawn, Ghibli-style map...
2. **Adventure Slide Deck**: Create a 10-15 slide presentation... highlight "Tunnel 9" as a mysterious time cave.
```

這段 Prompt 就像是給 AI 的「導演筆記」，確保它在消化硬數據時，會自動戴上「卡通濾鏡」。

## 📊 成果展示

將生成的 `walkgis_2025_houfeng_dongfeng_loop_notebooklm.md` 上傳後，效果驚人。

### 1. 資訊圖表化 (Infographic)
AI 根據我的指令，將 24 個景點轉化為一張充滿冒險感的概念地圖。它不再是線條與點，而是「巨人的鋼鐵手臂（花樑鋼橋）」與「神秘的時光隧道（九號隧道）」。

![WalkGIS資訊圖表](walkgis_infographic.png)
*(圖說：NotebookLM 生成的卡通地圖視覺描述與重點摘要)*

### 2. 自動生成投影片 (Slides)
我也要求它產出一份 10 頁的投影片大綱，它自動安排了起承轉合：從后里馬場的出發，到石岡水壩的震撼教育，最後在東勢客家園區享用美食。

![WalkGIS投影片](walkgis_slides.png)
*(圖說：由 AI 規劃的「后豐東豐冒險記」投影片大綱)*

## 💡 結語

這個實驗證明了 **「結構化資料 (Structured Data) + 長文本 AI (Long-Context AI)」** 的強大潛力。

*   **WalkGIS DB** 負責提供「正確性」與「關聯性」。
*   **NotebookLM** 負責提供「創造力」與「整合力」。
*   **Automation Script** 則是連接兩者的橋樑。

未來，每當我規劃一條新路線（例如「台中舊城區散步」），我只需要在 DB 裡建立關聯，然後跑一下腳本，一份全新的、客製化的卡通導覽手冊就誕生了。這才是自動化的浪漫！

---
### 🤖 AI 協作宣告
*   **本文內容**: 由人類作者規劃架構，Google Antigravity 協助撰寫與潤飾。
*   **程式碼**: Shell Script 與 SQL 查詢由 AI 輔助開發。
*   **示意圖構想**: Workflow 架構與 NotebookLM 應用場景由 AI 建議。
*   **AI 工具**: Antigravity (Gemini Pro), Google NotebookLM
