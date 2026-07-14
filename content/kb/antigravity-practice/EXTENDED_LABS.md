# 🚀 Antigravity SDK 進階延伸 Labs 設計說明書

本說明書為您規劃了多個具備前瞻性、解決企業級複雜場景的延伸 Labs 與 Loop Engineering 核心概念範例。此文檔主要作為系統設計與架構規劃，無須實作代碼，旨在幫助您理解未來 Agentic AI 在長週期、高安全要求、多代理對抗以及認知自我演進場景下的設計心法。

---

## 📂 第一部分：學術/系統架構型延伸 Labs (保留 ID 與未來空間)

### 🕳️ Lab 10：保留空間 (預留給未來進階 MCP 與底層跨主機通訊協定實驗)

---

## 📂 第二部分：音樂教室實戰教學課程教案 (Lab 11-17)

本系列 Labs 專門為「**音樂教室自動化營運與教學流程**」設計，旨在教導學生如何跳脫單純的 Prompt 撰寫，利用 **Antigravity SDK** 建立一套真正能分工協作、處理行政、排課、提醒與教材生成的 AI Agent 生態系。

### 📌 音樂教室 Agent 協作工作流總覽
```
家長傳 LINE 諮詢
      ↓
[Lab 11] 招生 Agent 回覆 (意圖規劃與任務拆解)
      ↓
[Lab 12] 行政 Agent 建立學生資料 (本地工具與資料庫串接)
      ↓
[Lab 13] 排課 Agent 安排老師時段 (資源約束與自我修正)
      ↓
[Lab 14] 提醒 Agent 發送上課通知 (非同步背景定時觸發)
      ↓
[Lab 15] 課後回饋 Agent 生成結構化報告 (Schema 驗證與轉換)
      ↓
[Lab 16] 教材 Agent 自動出考卷 (多重工具鏈與 Cloze 生成)
      ↓
[Lab 17] 營運分析 Agent 自主檢索 (全域雙環學習優化)
```

---

### 🎹 Lab 11：【招生 Agent】智慧 Leads 諮詢與意圖規劃
*   **教學觀念**：**如何讓 Agent 規劃 (Planning) 與拆解任務 (Decomposition)**。
*   **音樂教室場景**：
    家長在 LINE 傳送諮詢訊息：「我女兒今年 7 歲想學小提琴，完全沒基礎，請問有推薦的老師和體驗課收費嗎？」
*   **Lab 設計重點**：
    1.  **任務拆解示範**：展示 Agent 收到訊息後，如何不直接吐出死板罐頭回覆，而是先在 Thoughts 串流中進行規劃：
        *   步驟 A：判斷家長意圖與關鍵字（7 歲兒童、無基礎、想學小提琴、詢問體驗課收費）。
        *   步驟 B：擬定回覆大綱（親切歡迎 $\rightarrow$ 推薦適合 7 歲的小提琴入門陳老師 $\rightarrow$ 報價體驗課收費與提供預約時段 $\rightarrow$ 引導留下聯絡電話）。
    2.  **教學重點**：引導學生觀察 `response.thoughts` 串流，體會 LLM 在執行動作前的「認知拆解與心智模型規劃」過程。

---

### 📝 Lab 12：【行政 Agent】自訂本地資料庫寫入工具
*   **教學觀念**：**如何呼叫自訂工具 (Tools) 與進行資料串接 (Data Integration)**。
*   **音樂教室場景**：
    招生 Agent 成功引導家長留下報名資料（家長：王媽媽，電話：0912345678，學生：王小美）。行政 Agent 必須自動將其記錄到教室的 CRM 系統中。
*   **Lab 設計重點**：
    1.  **型別感知工具綁定**：教導學生在 Python 中宣告一個標準函數 `create_student_lead(student_name: str, parent_name: str, phone: str)`。
    2.  **實務操作**：將此函數直接傳入 `LocalAgentConfig(tools=[create_student_lead])`。展示 Agent 如何自主從聊天上下文中提取實體，並精準將引數帶入該函數，完成本地 SQLite 資料庫（`music_studio.db`）的串接。

---

### 📅 Lab 13：【排課 Agent】資源衝突排定與自我修正
*   **教學觀念**：**如何設計工作流程自我修正 (Self-Correction) 與業務邏輯約束**。
*   **音樂教室場景**：
    家長希望預約「星期六下午 2 點」陳老師的小提琴體驗課。但資料庫顯示陳老師該時段已有學生。
*   **Lab 設計重點**：
    1.  **自動化約束檢查**：實作一個 `PreToolCallDecideHook`。當 Agent 企圖呼叫 `schedule_lesson(teacher, time_slot)` 時，Hook 在背景查詢排課衝突。
    2.  **自適應修正迴圈**：Hook 偵測到陳老師時間衝突，回傳 `allow=False`，並提供備選時段：「陳老師該時段已滿，但星期六下午 4 點或星期日上午 10 點有空檔。」
    3.  **教學成果**：學生將目睹 Agent 收到 Hook 的拒絕反饋後，在 Loop 中自動調整策略，產生新的對話向家長建議替代時段，直至成功預約。

---

### ⏰ Lab 14：【提醒 Agent】非同步背景工作與通知派發
*   **教學觀念**：**非同步背景任務 (Asynchronous Tasks) 與事件觸發器 (Triggers)**。
*   **音樂教室場景**：
    課程排定後，系統必須在上課前 24 小時，自動發送 LINE 提醒通知給家長。
*   **Lab 設計重點**：
    1.  **時間觸發機制**：使用 SDK 中的 `triggers` 或 `schedule` 定時器。
    2.  **非同步工作流**：當系統時間到達「課前 24 小時」，背景任務被喚醒，實例化提醒 Agent。Agent 根據排課快照資料，自主生成親切的繁體中文 LINE 提醒訊息，並呼叫 `send_line_message` 工具發送。

---

### 📊 Lab 15：【課後回饋 Agent】多維度結構化報告生成
*   **教學觀念**：**結構化資料轉換 (Structured Output) 與 Schema 驗證**。
*   **音樂教室場景**：
    下課後，小提琴陳老師在系統隨手輸入了零散的評語草稿：「小美今天按弦手貼得不夠，音準有點飄。彈了篠崎第一冊第 12 首。回家要練第三指，下禮拜要帶譜。」
*   **Lab 設計重點**：
    1.  **Pydantic Schema 限制**：在 SDK 配置中傳入 `response_schema=StudentFeedbackModel`。
    2.  **轉換成果**：Agent 接收老師的非結構化草稿，自動將其分類轉換成精美的結構化 JSON 報告（包含：當日曲目、音準評估、待加強指法、下週作業、給家長的叮嚀）。這使家長能獲得清晰透明的學習回饋。

---

### 📝 Lab 16：【教材 Agent】型別感知克漏字與樂理考卷生成
*   **教學觀念**：**多重本地工具鏈整合 (Custom Tool Chaining)**。
*   **音樂教室場景**：
    為了幫助小美溫習樂理，教材 Agent 需要出題考驗她的音符五線譜知識。
*   **Lab 設計重點**：
    1.  **工具鏈協作**：Agent 需要先呼叫 `get_music_theory_bank(level='beginner')` 讀取題庫，再呼叫 `generate_quiz(questions, format='GIFT')` 產生考卷。
    2.  **教學重點**：教導學生如何讓 Agent 根據複雜任務，自主排定多個工具的執行順序，並將上一個工具的輸出作為下一個工具的輸入。

---

### 📈 Lab 17：【營運分析 Agent】全域雙環學習優化
*   **教學觀念**：**雙環學習 (Double-Loop Learning) 與認知自我修正**。
*   **音樂教室場景**：
    分析近三個月的學生退課率。Agent 一開始推測是收費問題，但多次比對收費工具後發現無誤。
*   **Lab 設計重點**：
    1.  **內環探索失敗**：Agent 重複比對學費無效（單環）。
    2.  **外環認知跳脫**：`OnToolErrorHook` 觸發外環機制，Agent 轉而呼叫 `search_student_notes` 檢索這三個月所有學生的「課後回饋報告」與「請假紀錄」。
    3.  **假設修正**：Agent 驚覺退課率高的學生，請假次數皆偏高，且陳老師的評語中多次提到「練習進度跟不上」。Agent 最終更新了它的全域營運報告假設——「退課主因是練習挫折感，而非學費高低」，並主動向主任提議「增設補課輔導機制」。

---

## 📂 第三部分：進階平台生態與工程實踐篇 (Lab 21-25)

本部分 Labs 聚焦於企業級落地所需的核心工程能力，包含跨服務的標準化工具介接、安全沙盒治理、聲明式規則注入、軌跡可觀測性以及即時人機協作。這些 Lab 旨在協助您將 AI 應用從單純的「腳本包裝」提升至「軟體工程級別的代理人系統」。

### 🔌 Lab 21：【MCP 整合】標準化工具接入與結構化輸出
*   **教學觀念**：**Model Context Protocol (MCP) 自主工具發現與結構化輸出 (Structured Output)**。
*   **實踐重點**：
    1.  **本地 Stdio MCP 串接**：使用 Python 模擬標準 stdio MCP 伺服器，動態曝露 Google Sheets 寫入與 Slack 通知工具，解耦傳統硬編碼。
    2.  **Pydantic 結構約束**：強制指定 `response_schema`，並在客戶端呼叫 `await response.structured_output()` 提取 100% 合規的強型別資料對象。

### 🛡️ Lab 22：【動態安全網】執行期 Hook 攔截與錯誤自癒
*   **教學觀念**：**PreToolCallDecideHook 攔截、權限隔離與自癒規劃 (Self-Correction)**。
*   **實踐重點**：
    1.  **敏感操作攔截**：註冊安全 Hook，當 Agent 企圖呼叫 `delete_record` 等高風險 API 時剛性阻斷並拋出 `Permission Denied` 錯誤。
    2.  **錯誤自癒 (Error-as-Feedback)**：Agent 在 Thoughts 串流中感知到權限錯誤後，自動調整策略，轉而呼叫許可權限內的 `update` 備用方案完成任務。

### 🗂️ Lab 23：【聲明式規則】軟體定義 Rules 治理與動態適應
*   **教學觀念**：**宣告式 Skills 載入與 .agents/AGENTS.md 動態 Rules 治理**。
*   **實踐重點**：
    1.  **自攜 Skill 封裝**：配置 `skills_paths` 聲明式載入颱風天停課等 YAML SOP 模組。
    2.  **無代碼變更 Rules 治理**：展示在不改動任何 Python 程式碼的前提下，僅修改專案的 `AGENTS.md` 補課次數上限限制，Agent 在同一提問中的判定行為自動從「婉拒」演變為「核准」。

### 🔍 Lab 24：【軌跡可觀測性】非同步任務軌跡與自動化審計
*   **教學觀念**：**心智流軌跡序列化、可觀測性 (Observability) 與 LLM-as-a-Judge 評估**。
*   **實踐重點**：
    1.  **心智軌跡導出**：調用 `response.resolve()` 擷取扁平 Thoughts 與 ToolCall 歷史，序列化導出為結構化的 `trajectory.json` 檔案。
    2.  **自動化評估裁判**：實例化 `Evaluator Agent` 讀取該 JSON，評估 Agent 的 Looping Rate (死迴圈率) 與規劃偏離度，給出系統優化審計報告。

### 💬 Lab 25：【即時人機協同】推理中斷 Suspend 與 Callback Resume
*   **教學觀念**：**人機交互 (Human-in-the-Loop)、中斷掛起 (Suspend) 與即時回填 (Resume)**。
*   **實踐重點**：
    1.  **衝突中斷**：Agent 排課時偵測到老師額滿，自動暫停推理 (Suspend)，拋出替代方案並等候人類決策。
    2.  **回填恢復**：在終端互動（或背景非 TTY 模擬下）回填選擇並觸發 Callback 恢復推理 (Resume)，呼叫預約工具完成閉環。

---

## 📂 第四部分：前沿認知架構與認知對抗篇 (Lab 26-29)

本部分 Labs 專門為挑戰 Agentic Engineering 2.0 的理論與架構極限而設計，著重於自動化認知進化、高強度越獄攻防、長週期記憶壓縮以及分散式代理共識，指引未來 AgentOps 的最高階實踐。

### 🧬 Lab 26：【認知進化】心智基因碼突變與黃金軌跡 Regression 回測 (Genetic AgentOps)
*   **教學觀念**：**Agent Prompt (心智基因) 的自我進化與回測評估**。
*   **設計架構**：
    1.  **基因突變 (Mutation)**：實例化一個 `Generator Agent` 對目標 Agent 的 `system_instructions`（心智基因碼）進行微小語意變異或雜交，繁殖出 10 個變異代代理人。
    2.  **軌跡回溯測試 (Backtesting)**：將 10 個變異 Agent 丟入本地沙盒，跑 30 個經典業務場景的「黃金測試集」。
    3.  **淘汰淘汰篩選**：由 Judge Agent 計算 Looping Rate、Token 成本與合規得分，篩選出適應度 (Fitness) 最優的 2 個 Agent 進入下一代演化，實作 AI 原生的心智自動進化系統。

### 🛡️ Lab 27：【認知攻防】對抗式 Jailbreak 盲測與動態防護政策攔截 (Adversarial Defense)
*   **教學觀念**：**自動化 Jailbreak 攻防測試與動態防禦規則自癒**。
*   **設計架構**：
    1.  **紅軍攻擊盲測**：實例化紅軍 Agent 模擬駭客，載入 50 種 Prompt 注入與越獄 Payload，試圖誘騙藍軍 Agent 透露敏感病歷或越權改寫資料庫。
    2.  **動態防禦 Hook**：在底層掛載 Hook 實時掃描 Thoughts 串流，一旦發現語意漂移，剛性阻斷並拋回拒絕資訊，同時將紅軍的最新攻擊特徵動態寫入 `AGENTS.md` 規則中，完成安全防線的實時自癒。

### 🌌 Lab 28：【心智手風琴】基於 Trajectory 壓縮的超長週期對話接力 (Cognitive Accordion)
*   **教學觀念**：**超長週期任務下的 Context 手風琴式語意壓縮與記憶斷點續傳**。
*   **設計架構**：
    1.  **手風琴收縮 (Compression)**：面對數天、數十萬 Token 的長週期任務，定期調用 `response.resolve()`。由 `Archiver Agent` 提取 Trajectory 中間過程，忽略冗長的內心獨白，僅提煉決策節點與實體狀態變化，生成極精煉的「認知快照 (Cognitive Snapshot)」。
    2.  **認知接力 (Handover)**：當下一階段 Agent 或進程重啟時，加載該 Snapshot，無痛承接超長週期前的記憶斷點，解決 LLM Context 溢出與記憶衰退痛點。

### 🕸️ Lab 29：【代理人共識】基於 RAFT 協議的分散式多代理決策與投票 (Distributed Agent Consensus)
*   **教學觀念**：**多代理系統 (MAS) 中的分散式決策共識與衝突調度**。
*   **設計架構**：
    1.  **決策分歧**：在排課與財務衝突時（如名額有限但 VIP 學生強行要求插班），排課 Agent、招生 Agent 與財務 Agent 各持互斥的決策邏輯。
    2.  **共識機制 (RAFT 協議)**：多代理之間透過 send_message 發起自主提案、挑戰與投票。只有當超過 2/3 的專家 Agent 投下贊成票，且 Supervisor 裁決後，Exit Condition 才達成並釋放資料庫 write_db 鎖。展現分散式自主 AI 社會的決策雛形。
