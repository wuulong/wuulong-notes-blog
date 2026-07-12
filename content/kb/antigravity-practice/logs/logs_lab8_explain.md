# Lab 8 學習導引與技術解析

本 Lab 解決了大型 LLM 應用在長週期、跨進程、或大 Token 消耗任務中，中途因故障中斷、Token 限制而遺忘上下文記憶的痛點。

## 💡 核心學習重點

### 1. 認知連續性 (Cognitive Continuity) 與斷點續傳
* **概念**：Agent 可以在某個時間點（或進程 A）完成前半段任務並退出；在另一個時間點由一個全新的 Agent 實例（或進程 B）載入狀態，完全繼承之前的想法、思考軌跡與已取得的發現，直接接力完成下半段任務。
* **實作技術**：
  在 `LocalAgentConfig` 中使用 `save_dir`（持久化快照目錄）與 `conversation_id`（指定的對話 ID）。
  * 第一階段：不指定 ID，讓系統自動產生全新的對話，將安全掃描發現記錄到 Thoughts 中。結束時，快照檔案自動持久化。
  * 第二階段：建立全新的 Agent，帶入第一階段返回的 `conversation_id`，它會自動從快照目錄載入記憶，並根據之前的掃描漏洞直接生成安全發佈日誌。

### 2. 狀態持久化儲存引擎底層原理
* **概念**：快照目錄下產生的 `[conversation_id].db` 檔案，其本體是 **SQLite 資料庫**。
* **底層表結構與職責**：
  * **`steps`**：最核心的表。以二進位 Blob 格式儲存了 Agent 經歷的每一個步驟（包含 thoughts 串流與 tool calls 歷史）。
  * **`gen_metadata`**：儲存 LLM 每次生成的元數據（如 token 使用量、時間戳）。
  * **`executor_metadata`**：儲存執行時的環境與工作區狀態。
  * **`parent_references`**：儲存父子對話關聯，供 Subagents 心智轉移使用。

---

## 🛠️ 工程踩坑與解決方案 (conversation_id 取得時機)
* **問題**：如果在 `async with Agent` 啟動後立即印出 `agent.conversation_id`，會得到 `None`。
* **解決方案**：
  根據 SDK 規範，對話 ID 是由雲端 API 或底層 runtime 在對話**真正連線且完成至少一次訊息交換 (`agent.chat`)** 後，才會被賦值給 SDK。因此，請務必在 `response = await agent.chat(...)` 執行完畢之後再去獲取對話 ID：
  ```python
  response = await agent.chat(prompt)
  # 消耗 streaming tokens 
  async for token in response:
      pass
  # 此時 conversation_id 已被正確初始化
  conv_id = agent.conversation_id 
  ```
