# 🕸️ Lab 29：代理人共識與 RAFT 衝突調度機制 (Distributed Consensus) 技術剖析

本實驗展示了在多代理系統 (MAS, Multi-Agent Systems) 中，面對**互斥的業務邏輯與利益衝突**時，多個自主 Agent 如何透過共識協議進行提案、辯論與 RAFT 仲裁，實現自治決策。

---

## 🛠️ 1. 核心代碼架構與 SDK API

代碼實作於 [Lab29_agent_consensus.py](file:///Users/wuulong/github/bmad-pa/events/notes/wuulong-notes-blog/content/kb/antigravity-practice/Lab29_agent_consensus.py)：

1.  **專科專家 Agent 實例化**：
    我們在 Python 中同時配置並啟動三個具有截然不同立場偏好與目標指令的 Agent：
    *   **Academic Expert (教務專家)**：恪守「教育品質」防線，反對超出人數限制的特權插班。
    *   **Finance Expert (財務專家)**：以「商業利潤與客戶留存」為導向，警惕年付大戶退班 (Churn Risk) 損失，積極爭取插班。
    *   **Operations Director (營運總監 / Supervisor)**：中立路由器，傾聽教務與財務對立觀點，尋求雙贏的折衷仲裁。
2.  **分散式對話協調**：
    在 Python 應用層模擬對話串流，將前一個 Agent 的發言 text 做為下一個 Agent 的輸入 context 傳遞，模擬自主會議辯論。
3.  **RAFT 投票共識達成**：
    營運總監接收辯論上下文，產出最終的折衷提案與裁決，若提案滿足雙方的核心關切，則 Exit Condition 判定達成共識，輸出仲裁決議書。

---

## 🔍 2. 運行軌跡與關鍵決策解讀

根據實體日誌 [logs_lab29.md](file:///Users/wuulong/github/bmad-pa/events/notes/wuulong-notes-blog/content/kb/antigravity-practice/logs/logs_lab29.md)：

*   **教務專家的強烈反對 (品質防線)**：
    指出強行插班會嚴重稀釋現有學生的練習與陳老師個別指導時間，違反教育公平，且小提琴拉奏持弓需要足夠的物理伸展空間，人太擠存在意外琴弓擦撞安全隱患。提議一對一私人課或協調其他未滿班級。
*   **財務專家的犀利反駁 (商業防線)**：
    直接進行 **「財務損益分析 (Financial Impact Analysis)」**。反駁教務的一對一方案因黃金時段開班的固定成本與教室機會成本過高而不可行，且 VIP 退班 Churn Cost 估計損失高達 25 萬元。
    財務專家提出了極為高明的雙贏方案：
    1.  **微調課時方案**：由教室提供「延長工時津貼」，讓陳老師週六的課稍微**延長 10 - 15 分鐘**。這樣原班級學生的個別指導時間非但沒有減少，反而因課時延長變相升級。
    2.  **增設行政助教隨堂**：每週撥款行政津貼安排助教課前調音、引導座位與收拾，讓陳老師能 100% 專注教學，解決物理擁擠空間的安全秩序隱患。
    3.  **尊榮升級公關包裝**：包裝為「雙師照護特仕班」，既安撫舊生，又給予 VIP 尊榮感。
*   **營運總監的 RAFT 仲裁**：
    總監認可財務提出的「課時延長補貼 + 助教隨堂配置」方案，認為其以極低的邊際成本解決了教務的「品質稀釋」與「物理安全」痛點，同時保住了 25 萬營收，發布了官方仲裁決議書 `arbitration_decision.md`，宣告雙方共識達成。

---

## 💡 3. 對在宅醫療系統工程的啟發

1.  **跨領域 Agent 共識決策**：在複雜在宅診所中，醫療 Agent（堅持嚴格臨床檢查）與運營 Agent（追求快速服務）也常面臨衝突。引進 **Agent RAFT 共識機制**，能讓不同專業的 Agent 彼此對話辯論，尋求臨床安全與運作效率的妥協，避免單一 Prompt 決策的盲點。
2.  **軟體定義決策 (Software-Defined Consensus)**：這代表未來的企業運營流程中，重大商業或醫療決策可先由多個專科 AI 代理進行 24/7 的沙盒對抗演練與損益計算，產出最優折衷提案供人類主管最終「簽字 (Sign-off)」，極大降低了人為決策的摩擦與失誤率。
