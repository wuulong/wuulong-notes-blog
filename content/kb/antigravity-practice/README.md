# 🚀 Antigravity SDK 極簡實作練習專案指南

本指南旨在幫助您在極簡的架構下，快速實作並掌握 Google Antigravity SDK 的核心能力，並理解其相較於傳統 Google GenAI (GAI) SDK 的優勢。

專案所有的練習程式碼已為您部署在工作區

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

### 🔬 [Lab 1: 思維與文字雙串流 (Lab1_thoughts_stream.py)](file:///Lab1_thoughts_stream.py)
*   **核心練習**：學習如何同時讀取 `response.thoughts` 與 `response` 文字 token 串流。
*   **優勢體驗**：看見 LLM 如何在產出程式碼前「在內心默默規劃步驟」，這對於 Debug 與提示詞最佳化非常關鍵。
*   **執行命令**：
    ```fish
    python projects/antigravity-practice/Lab1_thoughts_stream.py
    ```

### 🛡️ [Lab 2: 動態權限控管與人為審查沙盒 (Lab2_hitl_sandbox.py)](file:///Lab2_hitl_sandbox.py)
*   **核心練習**：實作 **Human-in-the-Loop (HITL)** 機制。當 Agent 企圖呼叫 any 系統工具時，程式會攔截並在 terminal 跳出 `[y/N]` 詢問，待使用者輸入允許後才放行。
*   **未來趨勢**：未來的 AI Agent 必須是「受控且安全」的。本 Lab 展示了如何利用 `response.tool_calls` 在程式碼層面死守安全底線。
*   **執行命令**：
    ```fish
    python projects/antigravity-practice/Lab2_hitl_sandbox.py
    ```

### 🤝 [Lab 3: 雙 Agent 協作循環 (Lab3_multi_agent_collab.py)](file:///Lab3_multi_agent_collab.py)
*   **核心練習**：在同一個 Python 腳本中實作兩個角色定位不同的 Agent——**程式設計師（Coder）**與**代碼審查員（Reviewer）**。
*   **未來趨勢**：單一 Agent 的能力有其上限，未來的趨勢是 Multi-Agent 團隊協作。本 Lab 展示了如何讓 Reviewer 挑戰 Coder 的程式碼，並在 Coder 收到 FAIL 意見後自動進行第二輪修改的最佳化。
*   **執行命令** :
    ```fish
    python projects/antigravity-practice/Lab3_multi_agent_collab.py
    ```

### ⚙️ [Lab 4: 自訂 Tool 綁定與自動 Schema 解析 (Lab4_custom_tool_binding.py)](file:///Lab4_custom_tool_binding.py)
*   **核心練習**：型別感知工具綁定（Type-Aware Tool Binding）。您只需宣告一般的 Python 函數，並加上 docstring 與 type hints，SDK 就會自動幫其建立 Schema 並讓 Agent 能夠自主呼叫，還能進行鏈式工具呼叫（例如先查資料再進行計算）。
*   **執行命令**：
    ```fish
    python projects/antigravity-practice/Lab4_custom_tool_binding.py
    ```

### 🛡️ [Lab 5: 基於 Policy 的工具權限管控 (Lab5_tool_policies.py)](file:///Lab5_tool_policies.py)
*   **核心練習**：安全沙盒（Sandboxing）與 Policy 門禁防禦。使用 `deny` 規則在 SDK 底層建立防線。即使 Agent 擁有執行系統指令的權力，當它企圖執行包含 `rm` 或 `sudo` 等危險命令時，會被 Policy 直接攔截，而安全的指令（如 `ls`）則能順利放行。
*   **執行命令**：
    ```fish
    python projects/antigravity-practice/Lab5_tool_policies.py
    ```

### 🔄 [Lab 6: 自動除錯自我修正迴圈 (Lab6_self_correction_loop.py)](file:///Lab6_self_correction_loop.py)
*   **核心練習**：迴圈工程（Loop Engineering）與反饋控制。利用 `PreToolCallDecideHook` 在 Agent 企圖寫檔時進行靜態編譯與「業務規則」審核（例如：檢查程式碼中是否包含繁體中文單行註解 `# 核心演算法`）。若檢查失敗，Hook 將在底層阻斷並將編譯錯誤直接回饋給 Agent，驅使 Agent 自我反思與修正代碼，直到完全符合規範才准予寫入。
*   **執行命令**：
    ```fish
    python projects/antigravity-practice/Lab6_self_correction_loop.py
    ```

### 🔄 [Lab 7: 資料自動合規與資料庫約束閉環 (Lab7_data_compliance.py)](file:///Lab7_data_compliance.py)
*   **核心練習**：狀態迴圈 (Stateful Loop) 與物理對合檢核。讓 Agent 扮演資料合規工程師，在「嘗試寫入 $\rightarrow$ 觸發資料庫約束/合規失敗 $\rightarrow$ 自動清洗資料 $\rightarrow$ 重新寫入」的閉環中自主運行。
*   **技術特點**：整合 SQLite 的 DDL 外鍵與唯一性約束，並結合自訂 `ComplianceVerifierHook` (繁繁簡轉換政策)，讓 Agent 經歷「簡體字攔截修正」$\rightarrow$「外鍵錯誤查詢修正」$\rightarrow$「唯一性重複跳過」的自我修正迴圈。
*   **執行命令**：
    ```fish
    python events/notes/wuulong-notes-blog/content/kb/antigravity-practice/Lab7_data_compliance.py
    ```
### 📦 [Lab 8: 長週期認知接力與 Session 持久化 (Lab8_cognitive_handover.py)](file:///Lab8_cognitive_handover.py)
*   **核心練習**：認知連續性 (Cognitive Continuity) 與 Session 快照復原。解決大型 LLM 在長達數天或跨進程的任務中，因為中斷、Token 限制而遺忘上下文的痛點。
*   **技術特點**：在 `LocalAgentConfig` 中使用 `save_dir` 與固定的 `conversation_id`。展示第一個 Agent 執行程式碼靜態掃描並在 thoughts 記憶中記錄漏洞後關閉；第二個全新的 Agent 連線相同 ID 與存檔目錄，無痛承接上一階段的記憶與推理軌跡，直接生成安全發佈日誌。
*   **執行命令**：
    ```fish
    python events/notes/wuulong-notes-blog/content/kb/antigravity-practice/Lab8_cognitive_handover.py
    ```
### 🛡️ [Lab 9: 紅藍軍對抗與規格自審拓撲 (Lab9_adversarial_loop.py)](file:///Lab9_adversarial_loop.py)
*   **核心練習**：對抗式迴圈 (Adversarial Loop) 與多 Agent 動態協調拓撲。透過讓兩個性格或目標互斥的 Agent 在沙盒中進行對抗，快速逼出系統工程方案的缺陷與邊界。
*   **技術特點**：在 Python 腳本中同時宣告三個配置與 Instructions 不同的 Agent：**藍軍**（規格設計師）、**紅軍**（安全威脅挑戰者）以及**裁判官**（中立評判）。使用 Python 迴圈控制對抗輪數，紅軍尋找漏洞，裁判官裁決，判定失敗（FAIL）時驅使藍軍修改並强化規格，直到裁判官給予 PASS。
*   **執行命令**：
    ```fish
    python events/notes/wuulong-notes-blog/content/kb/antigravity-practice/Lab9_adversarial_loop.py
    ```
### 🔌 [Lab 21: MCP 生態系整合與結構化輸出 (Lab21_mcp_leads_sync.py)](file:///Lab21_mcp_leads_sync.py)
*   **核心練習**：Model Context Protocol (MCP) 標準化工具接入與結構化輸出 (Structured Output) 強制約束。解耦傳統應用開發中對外部 API 呼叫邏輯的寫死，實踐聲明式工具探索。
*   **技術特點**：在 Python 腳本中透過 `types.McpStdioServer` 定義與連線本地 Mock Stdio MCP 服務（`mock_mcp_server.py`），動態曝光 Google Sheets 寫入與 Slack 發送兩大工具。同時宣告 `response_schema` 為 Pydantic Model，強制將 Agent 動態呼叫 MCP 工具後的最終回覆約束為 100% 符合欄位定義的 JSON。
*   **執行命令**：
    ```fish
    python events/notes/wuulong-notes-blog/content/kb/antigravity-practice/Lab21_mcp_leads_sync.py
    ```
### 🛡️ [Lab 22: 動態安全網與沙盒審查 (Lab22_security_sandbox.py)](file:///Lab22_security_sandbox.py)
*   **核心練習**：權限最小化原則 (Least Privilege) 與動態安全網攔截。藉由 Hook 機制實作高風險 API 或 Tool Call 的動態審批與提權，維護應用系統的執行期安全。
*   **技術特點**：在 Python 腳本中實作自訂的 `PreToolCallDecideHook`（`StudioSecurityHook`），動態攔截 Agent 呼叫的敏感工具。當 Agent 嘗試執行高風險的 `delete_student_record` 時，安全 Hook 予以拒絕並傳回 `Permission Denied` 錯誤，迫使其重規劃；而當 Agent 改為執行許可範圍內的 `update_tuition_fee` 時，則模擬核准通過。
*   **執行命令**：
    ```fish
    python events/notes/wuulong-notes-blog/content/kb/antigravity-practice/Lab22_security_sandbox.py
    ```
### 🗂️ [Lab 23: 聲明式 Skill 封裝與 Rules 治理 (Lab23_declarative_skills.py)](file:///Lab23_declarative_skills.py)
*   **核心練習**：聲明式 Skills 載入與 Rules 動態治理。解耦硬編碼（Hardcoding）在 Python 程式碼中的營運規則與 SOP，透過純 Markdown 文件動態控制 Agent 的行為模式。
*   **技術特點**：在 `LocalAgentConfig` 中使用 `skills_paths` 載入外部定義的音樂營運 SOP 技能檔（`skills/music-ops/SKILL.md`）。在 Python 腳本中，藉由動態修改專案規則檔 `.agents/AGENTS.md` 中的「團體課補課上限」（先設定為 2 次，後修改為 4 次），展示在不更改任何程式碼的前提下，同個對話提問中 Agent 的答覆自動由「拒絕」演變為「接受」的動態 Rules 適應能力。
*   **執行命令**：
    ```fish
    python events/notes/wuulong-notes-blog/content/kb/antigravity-practice/Lab23_declarative_skills.py
    ```
### 🔍 [Lab 24: 非同步背景任務與軌跡可觀測性 (Lab24_observability_eval.py)](file:///Lab24_observability_eval.py)
*   **核心練習**：非同步背景任務排程、軌跡序列化匯出（Trajectory Observability）與 LLM 自動化健康評估（LLM-as-a-Judge）。
*   **技術特點**：使用 Python 模擬定時分析的背景任務。第一階段執行「資料庫寫入任務」，因資料庫鎖定錯誤使 Agent 觸發重試機制。任務結束後調用 `response.resolve()` 解析 flat list 軌跡，並序列化匯出至 `logs/logs_task_trajectory.json`。第二階段宣告 `Evaluator Agent`，讀取此軌跡 JSON，以 Judge 視角診斷是否陷入死迴圈，分析規劃偏離度，並自動產出系統優化評估報告。
*   **執行命令**：
    ```fish
    python events/notes/wuulong-notes-blog/content/kb/antigravity-practice/Lab24_observability_eval.py
    ```
### 💬 [Lab 25: 即時人機協同 - 詢問與回填 (Lab25_human_in_the_loop.py)](file:///Lab25_human_in_the_loop.py)
*   **核心練習**：推理中斷 (Suspend) 與即時回填 (Resume/Callback) 交互機制。實現 AI 排課中遇到衝突時暫停推理，詢問家長決策並回填結果後恢復執行的閉環。
*   **技術特點**：在 Python 腳本中實作 `ask_user_for_choice` 互動工具。當排課 Agent 呼叫 `check_teacher_availability` 發現陳老師額滿後，中斷推理並拋出替代方案。在背景自動化環境（非 TTY）下，腳本自動回填模擬決策並恢復推理，隨後呼叫 `confirm_booking` 完成排課；若在互動式終端，則提示使用者手動輸入編號決策。
*   **執行命令**：
    ```fish
    python events/notes/wuulong-notes-blog/content/kb/antigravity-practice/Lab25_human_in_the_loop.py
    ```

---

## 💡 未來即將到來的趨勢概念與實作練習建議

在完成基礎的 6 個 Lab 後，您可以嘗試以下更進階的實作方向：
1.  **對話銜接與情境快照 (Conversation Handover & Snapshots)**：嘗試在 Agent 結束階段任務時，將其對話歷史與心智狀態序列化（Serialize），並在另一個時間點或另一個 Agent 中載入，達成「斷點續傳」與「心智轉移」。
2.  **帶有資料庫狀態的 Agent (Stateful Agents)**：結合工作區的 `walkgis.db` SQLite 資料庫，給予 Agent 專屬的查詢 Tool，讓它自動產生 SQL、查詢並回報分析結論。
3.  **非同步背景任務與定時提醒**：在 SDK 中結合 `agy` CLI 的背景任務與定時功能，建立自動排程運作的 Agent。
