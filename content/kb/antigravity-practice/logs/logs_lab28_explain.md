# 🌌 Lab 28：心智手風琴壓縮與長週期記憶接力 (Cognitive Accordion) 技術剖析

本實驗展示了解決長週期 Agent 運作時 **「Context 記憶溢出與 Token 費用飆漲」** 的核心武器：**「心智手風琴 (Cognitive Accordion) 壓縮與斷點續傳」**。模擬診斷 Agent 執行複雜問診與多工具調用後，如何將冗長的推理軌跡壓縮為精煉的「認知快照」，並無縫傳遞給全新 Agent 接力對話。

---

## 🛠️ 1. 核心代碼架構與 SDK API

代碼實作於 [Lab28_cognitive_accordion.py](file:///Users/wuulong/github/bmad-pa/events/notes/wuulong-notes-blog/content/kb/antigravity-practice/Lab28_cognitive_accordion.py)：

1.  **生理數據與過敏查詢工具**：
    `check_patient_vitals` 與 `check_allergy_history` 模擬底層臨床數據庫。
2.  **軌跡序列化解析**：
    第一階段 Agent 執行完畢後，呼叫 `await response.resolve()`。此 API 能將 Agent 在後台發生的所有內部思考（Thoughts）、工具調用（ToolCall）與工具輸出（ToolResult）解析為一個扁平的物件列表，並序列化為軌跡 JSON。
3.  **手風琴收縮 (Cognitive Squeeze)**：
    實例化 `Archiver Agent`，其唯一任務是讀取軌跡 JSON，過濾掉冗長無意義的獨白，提煉出『核心決策節點與實體狀態變化』，輸出為極精簡的 **「認知快照 (Cognitive Snapshot)」**。
4.  **心智轉移與接力 (Handover)**：
    實例化一個全新的第二階段 Agent (護理諮詢助手)，將上述生成的「認知快照」直接注入其 `system_instructions` 中，做為其初始記憶，處理患者的後續追問。

---

## 🔍 2. 運行軌跡與關鍵決策解讀

根據實體日誌 [logs_lab28.md](file:///Users/wuulong/github/bmad-pa/events/notes/wuulong-notes-blog/content/kb/antigravity-practice/logs/logs_lab28.md)：

*   **第一階段問診**：
    診斷 Agent 針對「頭痛頭暈」提問，調用了生理數據（血壓 145/95 mmHg ⚠️，體溫 37.2°C）與過敏史（對青黴素 Penicillin 嚴重過敏 ⚠️），並給出了一份詳細的初步診斷書。這段交互包含大量的 Thoughts 推理與工具輸出，上下文長度約數千 Token。
*   **記憶壓縮成果**：
    `Archiver Agent` 成功將這段冗長的軌跡手風琴式收縮為一份乾淨、精美的快照：
    > **【認知快照】**：
    > *   **主訴症狀**：頭痛、頭暈。
    > *   **生命徵象**：血壓 145/95 mmHg、心率 88 bpm、體溫 37.2°C。
    > *   **藥物過敏**：對青黴素 (Penicillin) 有嚴重過敏史。
    > *   **當前診斷**：頭痛頭暈與高血壓高度臨床相關，需規避高風險用藥。
*   **第二階段諮詢接力**：
    患者追問：「*那我回家後需要注意什麼？可以吃一般的消炎止痛藥嗎？*」
    全新實例化的諮詢 Agent 載入快照後，**在沒有任何歷史對話 Context 的情況下**，精準做出了以下臨床護理判斷：
    1.  **NSAIDs 類消炎止痛藥 (Ibuprofen、EVE) 禁用警告**：指出這類藥物會導致水鹽滯留、收縮腎血管，直接使血壓 (145/95) 進一步升高，加劇症狀。
    2.  **安全止痛替代 (普拿疼 / Acetaminophen)**：推薦純止痛、不影響血壓的普拿疼。
    3.  **過敏安全釋疑**：明確指出普拿疼、消炎止痛藥與青黴素（抗生素）**完全不同類別，無交叉過敏風險**。
    4.  **下床防跌倒三部曲** 與 **722 血壓監測原則**。
    5.  自動為患者在本地目錄生成了照護卡 `home_care_card.md`！

---

## 💡 3. 對在宅醫療系統工程的啟發

1.  **對抗 Token 刺客的終極方案**：在長週期的在宅照護中，如果把每一次生理監測、問診問答都硬性塞在 Session 歷史中，很快就會因為 Context 超限而崩潰。**心智手風琴機制**讓我們能以極低成本，在多個 specialized Agents 之間無痛移交「核心記憶斷點」，徹底解決記憶衰退。
2.  **多代理管線協作 (Pipeline)**：這套機制支持「專科醫生 Agent 診斷 $\rightarrow$ 快照壓縮 $\rightarrow$ 護理指導 Agent 衛教」的流水線，實現真正符合臨床分工的 Multi-Agent Platform。
