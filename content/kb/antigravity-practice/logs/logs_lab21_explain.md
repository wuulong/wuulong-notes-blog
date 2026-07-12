# Lab 21 學習導引與技術解析

本 Lab 展示了如何利用 Model Context Protocol (MCP) 標準協定來解耦外部 API 工具，並透過強型別的 Pydantic Schema 強制約束 Agent 的最終輸出。

## 💡 核心學習重點

### 1. Model Context Protocol (MCP) 的工具解耦價值
* **概念**：在傳統軟體開發中，如果我們要串接 Google Sheets 或 Slack，通常必須在 Python 專案中寫死 API 連線、SDK 安裝與認證邏輯。MCP 協定透過「Stdio/HTTP 通訊」將工具實作完全與 Agent 程式碼解耦。
* **實作技術**：
  在 `LocalAgentConfig` 中註冊 `mcp_servers`，我們使用本地標準輸入輸出（Stdio）的 `types.McpStdioServer`：
  ```python
  types.McpStdioServer(
      name="mock-leads-server",
      command="python",
      args=[server_path]
  )
  ```
  在執行時，Agent 會透過 JSON-RPC 與該 Stdio 服務對接，自動進行 `tools/list` 探索與 `tools/call` 調用。這代表 Agent 的 API 工具可以是用 Go、Node.js 或任何語言在另一個進程中運行的服務，達成高解耦性。

### 2. Pydantic 約束結構化輸出 (Structured Output via response_schema)
* **概念**：企業級資料流程中，如果 Agent 最終輸出的格式不符，會造成下游解析失敗。我們使用 Pydantic Model 作為 `response_schema`，強制約束 Agent 的輸出。
* **實作技術**：
  ```python
  class LeadSyncModel(BaseModel):
      sync_status: str
      synced_count: int
      notification_sent: bool
      summary_report: str
  ```

### 3. 如何提取結構化輸出 (structured_output)
* **工程關鍵**：
  當配置了 `response_schema` 後，如果直接對 `response` 進行 `async for token in response` 的文字 token 遍歷，最終只會拿到 `Finished` 或空的字串。
  這是因為真正的 Pydantic 物件是由 API 與 SDK 在底層透過 finish tool 自動接收、驗證並封裝的。我們必須依據 SDK 標準規範，調用 `structured_output()` 方法來獲得這個強型別對象：
  ```python
  # 1. 消耗完 token 串流
  async for token in response:
      pass
  # 2. 獲取已解析驗證的強型別 Python 對象
  structured_data = await response.structured_output()
  print(structured_data.model_dump_json(indent=2))
  ```

---

## 🛠️ 安全政策要點 ( safety policy for MCP )
* **核心原則**：為了防範安全風險，只要在 Local Connection 中啟用了 **寫入工具 (Write Tools)** 或 **MCP 伺服器 (mcp_servers)**，Agent 的初始化設定必須包含至少一條安全政策，否則會拒絕啟動。我們在此註冊了 `policies=[policy.allow_all()]` 予以放行。
