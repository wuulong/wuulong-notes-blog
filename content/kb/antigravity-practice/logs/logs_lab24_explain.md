# Lab 24 學習導引與技術解析

本 Lab 深入解析了企業級 LLM 系統中，如何實現「推理軌跡可觀測性（Observability）」以及「基於大模型的自動化評估與診斷（LLM-as-a-Judge）」。

## 💡 核心學習重點

### 1. 什麼是推理軌跡（Trajectory）？
* **概念**：Agent 在接收 Prompt 後，到最終生成回覆之前，所經歷的 Thought、Tool Call、Tool Result 序列，稱為推理軌跡。
* **觀測價值**：在生產環境中，Agent 是在背景非同步執行的。當任務失敗、或者花費了過高 Token 時，開發人員不能只看最終回覆，必須回溯這段軌跡來診斷「它在哪個決策點走偏了（Drifting）」或「是否陷入無限重試（Looping）」。

### 2. 軌跡序列化匯出 (Trajectory Serialization)
* **實實技術**：
  透過 SDK 的 `response.resolve()` 方法，將非同步的串流與決策扁平化（Flatten）為一個 `list[StreamChunk | ToolCall | ToolResult]`。
  我們藉由類型比對將其轉為結構化的 JSON 檔案：
  ```python
  chunks = await response.resolve()
  for chunk in chunks:
      if isinstance(chunk, types.Thought):
          # 記錄思考鏈
      elif isinstance(chunk, types.ToolCall):
          # 記錄工具呼叫與參數
      elif isinstance(chunk, types.ToolResult):
          # 記錄工具回傳與錯誤訊息
  ```
  這份 JSON 會自動保存到 [logs_task_trajectory.json](file:///Users/wuulong/github/bmad-pa/events/notes/wuulong-notes-blog/content/kb/antigravity-practice/logs/logs_task_trajectory.json) 中。

### 3. 自動化評估與裁判官 (LLM-as-a-Judge)
* **概念**：手動閱讀成千上萬的背景 Agent 軌跡是不現實的。我們實例化另一個專職的 `Evaluator Agent`，給予其「系統診斷與優化建議」的 Instructs，讓它自動去讀取上述導出的軌跡 JSON，生成評估報告。
* **評估要點**：
  * **死迴圈判定**：Task Agent 在寫入資料庫時，遇到了鎖定錯誤（Locked），總共重試了 4 次工具。
  * **規劃偏離度（Drifting）**：評估為零偏離。Agent 自始至終圍繞著「排課寫入」，失敗後主動回退。
  * **優化建議**：評估者 Agent 敏銳指出「兩次重試之間沒有 thought 或等待，屬於緊密重試」，會加劇資料庫死鎖與效能雪崩。建議引入「指數退避（Exponential Backoff）與時間等待工具（Sleep）」。

---

## 🛠️ 架構優化：如何防範 LLM Looping？
根據評估報告，為防止 LLM 因異常或幻覺陷入死迴圈，我們在架構上應採用：
1. **Tool 層級限制**：在 Python 函式或 SDK 底層控制重試次數上限。
2. **Exponential Backoff**：重試等待時間隨次數呈指數增長（如 $1\text{s}, 2\text{s}, 4\text{s}, \dots$），並加隨機抖動（Jitter）。
3. **電路熔斷器 (Circuit Breaker)**：當錯誤達到閾值，直接將該資料區間寫入離線佇列並觸發管理員告警。
