# 🚀 Antigravity SDK 極簡實作練習專案指南

本指南旨在幫助您在極簡的架構下，快速實作並掌握 Google Antigravity SDK 的核心能力，並理解其相較於傳統 Google GenAI (GAI) SDK 的優勢。

專案所有的練習程式碼已為您部署在工作區：
👉 [projects/antigravity-practice/](file:///Users/wuulong/github/bmad-pa/projects/antigravity-practice)

---

## 🛠️ 環境配置與啟動建議

### 1. 執行環境建議
*   **Conda 虛擬環境**：請在您的 **`m2504`** 環境下執行。
*   **Shell**：在 `fish` 中，請先執行 `conda activate m2504` 啟用環境，再執行 Python 腳本或 `agy` CLI 命令。這能確保 Python SDK 的依賴庫版本與 `agy` 工具鏈一致。

### 2. 解決常見的 Protobuf 版本相容性問題
在載入 `google-antigravity` 套件時，若遇到以下錯誤：
`TypeError: Couldn't build proto file into descriptor pool: Edition UNKNOWN is later than the maximum edition 2023 given in the defaults`

這是因為環境中舊有的 `protobuf` 執行庫與 Antigravity 使用的最新編譯格式衝突。**請在您的 fish shell 中指令進行更新**：
```fish
pip install --upgrade google-antigravity protobuf grpcio-tools
```

---

## 🆚 Antigravity SDK vs 傳統 Google GAI SDK

| 比較維度 | 傳統 Google GAI SDK | Google Antigravity SDK |
| :--- | :--- | :--- |
| **Agent 生命週期與沙盒管理** | 須自行撰寫 `while` 迴圈手動解析 `FunctionCall`、執行並回傳 `FunctionResponse`。無內建安全權限管控。 | 透過 `async with Agent(config)` 上下文管理器自動託管。可利用 `CapabilitiesConfig` 動態宣告與限制 Agent 對工作區的讀寫權限。 |
| **思考軌跡（Thoughts）串流** | 必須等整個 Response 結束，或手動透過複雜的 API 結構拆解，難以流式監控中間的思考過程。 | 提供一等公民非同步產生器 `response.thoughts`，可即時串流 LLM 的「內心獨白」（Reasoning Trace）。 |
| **工具調用（Tool Calls）攔截** | 工具呼叫是由 API 回傳後，在客戶端程式碼被動執行，代碼結構零碎，不便於進行前置審查。 | 提供 `response.tool_calls` 串流，可於工具執行前、中、後進行攔截，是實作 **Human-in-the-Loop (HITL)** 審查的完美機制。 |
| **多代理協作（Multi-Agent）** | 必須在應用層手動維護多個 Chat Session 的歷史紀錄，並自行設計上下文傳遞機制。 | 支援巢狀與平行的 Agent Contexts，多個 Agent 可直接在 Python 中交互對話、共享或繼承工作區。 |
| **安全策略（Policies）防禦** | 必須在應用層自己解析引數、撰寫過濾邏輯，缺乏統一且標準化的門禁原則宣告。 | 內建 Policy 機制（如 `deny`），能在工具真正執行前於 SDK 底層完成條件式比對與自動阻斷。 |
| **生命週期 Hook 攔截 (Loop Engineering)** | 難以在 Model 決定執行工具到工具真正執行的生命週期節點插入自訂程式碼，Loop 手寫成本極高。 | 提供完整的生命週期 Hooks（如 `PreToolCallDecideHook`），方便在 SDK 最底層對 Agent 決策進行編譯、校驗並提供反饋。 |

---

## 🧑‍💻 實作練習 Labs 導覽

專案已為您實作了六個由淺入深的實作練習檔：

### 🔬 [Lab 1: 思維與文字雙串流 (Lab1_thoughts_stream.py)](file:///Users/wuulong/github/bmad-pa/projects/antigravity-practice/Lab1_thoughts_stream.py)
*   **核心練習**：學習如何同時讀取 `response.thoughts` 與 `response` 文字 token 串流。
*   **優勢體驗**：看見 LLM 如何在產出程式碼前「在內心默默規劃步驟」，這對於 Debug 與提示詞最佳化非常關鍵。
*   **執行命令**：
    ```fish
    python projects/antigravity-practice/Lab1_thoughts_stream.py
    ```

### 🛡️ [Lab 2: 動態權限控管與人為審查沙盒 (Lab2_hitl_sandbox.py)](file:///Users/wuulong/github/bmad-pa/projects/antigravity-practice/Lab2_hitl_sandbox.py)
*   **核心練習**：實作 **Human-in-the-Loop (HITL)** 機制。當 Agent 企圖呼叫 any 系統工具時，程式會攔截並在 terminal 跳出 `[y/N]` 詢問，待使用者輸入允許後才放行。
*   **未來趨勢**：未來的 AI Agent 必須是「受控且安全」的。本 Lab 展示了如何利用 `response.tool_calls` 在程式碼層面死守安全底線。
*   **執行命令**：
    ```fish
    python projects/antigravity-practice/Lab2_hitl_sandbox.py
    ```

### 🤝 [Lab 3: 雙 Agent 協作循環 (Lab3_multi_agent_collab.py)](file:///Users/wuulong/github/bmad-pa/projects/antigravity-practice/Lab3_multi_agent_collab.py)
*   **核心練習**：在同一個 Python 腳本中實作兩個角色定位不同的 Agent——**程式設計師（Coder）**與**代碼審查員（Reviewer）**。
*   **未來趨勢**：單一 Agent 的能力有其上限，未來的趨勢是 Multi-Agent 團隊協作。本 Lab 展示了如何讓 Reviewer 挑戰 Coder 的程式碼，並在 Coder 收到 FAIL 意見後自動進行第二輪修改的最佳化。
*   **執行命令** :
    ```fish
    python projects/antigravity-practice/Lab3_multi_agent_collab.py
    ```

### ⚙️ [Lab 4: 自訂 Tool 綁定與自動 Schema 解析 (Lab4_custom_tool_binding.py)](file:///Users/wuulong/github/bmad-pa/projects/antigravity-practice/Lab4_custom_tool_binding.py)
*   **核心練習**：型別感知工具綁定（Type-Aware Tool Binding）。您只需宣告一般的 Python 函數，並加上 docstring 與 type hints，SDK 就會自動幫其建立 Schema 並讓 Agent 能夠自主呼叫，還能進行鏈式工具呼叫（例如先查資料再進行計算）。
*   **執行命令**：
    ```fish
    python projects/antigravity-practice/Lab4_custom_tool_binding.py
    ```

### 🛡️ [Lab 5: 基於 Policy 的工具權限管控 (Lab5_tool_policies.py)](file:///Users/wuulong/github/bmad-pa/projects/antigravity-practice/Lab5_tool_policies.py)
*   **核心練習**：安全沙盒（Sandboxing）與 Policy 門禁防禦。使用 `deny` 規則在 SDK 底層建立防線。即使 Agent 擁有執行系統指令的權力，當它企圖執行包含 `rm` 或 `sudo` 等危險命令時，會被 Policy 直接攔截，而安全的指令（如 `ls`）則能順利放行。
*   **執行命令**：
    ```fish
    python projects/antigravity-practice/Lab5_tool_policies.py
    ```

### 🔄 [Lab 6: 自動除錯自我修正迴圈 (Lab6_self_correction_loop.py)](file:///Users/wuulong/github/bmad-pa/projects/antigravity-practice/Lab6_self_correction_loop.py)
*   **核心練習**：迴圈工程（Loop Engineering）與反饋控制。利用 `PreToolCallDecideHook` 在 Agent 企圖寫檔時進行靜態編譯與「業務規則」審核（例如：檢查程式碼中是否包含繁體中文單行註解 `# 核心演算法`）。若檢查失敗，Hook 將在底層阻斷並將編譯錯誤直接回饋給 Agent，驅使 Agent 自我反思與修正代碼，直到完全符合規範才准予寫入。
*   **執行命令**：
    ```fish
    python projects/antigravity-practice/Lab6_self_correction_loop.py
    ```

---

## 💡 未來即將到來的趨勢概念與實作練習建議

在完成基礎的 6 個 Lab 後，您可以嘗試以下更進階的實作方向：
1.  **對話銜接與情境快照 (Conversation Handover & Snapshots)**：嘗試在 Agent 結束階段任務時，將其對話歷史與心智狀態序列化（Serialize），並在另一個時間點或另一個 Agent 中載入，達成「斷點續傳」與「心智轉移」。
2.  **帶有資料庫狀態的 Agent (Stateful Agents)**：結合工作區的 `walkgis.db` SQLite 資料庫，給予 Agent 專屬的查詢 Tool，讓它自動產生 SQL、查詢並回報分析結論。
3.  **非同步背景任務與定時提醒**：在 SDK 中結合 `agy` CLI 的背景任務與定時功能，建立自動排程運作的 Agent。
