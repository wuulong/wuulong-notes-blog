# Lab 7 學習導引與技術解析

本 Lab 深入探討如何讓 Agent 在自動化寫入資料庫時，進行「自動合規校驗」與「資料庫約束自我修正閉環」。

## 💡 核心學習重點

### 1. 資料庫物理防線 (Database Constraints)
* **概念**：最安全的系統不能只依賴 Prompt 去約束 Agent。我們必須將防線下移至資料庫層，利用 SQLite 的 DDL 強約束（外鍵約束 `FOREIGN KEY`、欄位值檢查 `CHECK`、唯一性限制 `UNIQUE`）來物理阻斷違規寫入。
* **物理防禦代碼**：
  * 外鍵約束：`PRAGMA foreign_keys = ON;`
  * 經緯度範圍 `CHECK` 約束：`latitude REAL CHECK(latitude BETWEEN 21.0 AND 26.0)`

### 2. 應用層安全 Hook (PreToolCallDecideHook)
* **概念**：在工具調用執行**之前**進行稽核攔截。
* **實作技術**：
  繼承 `PreToolCallDecideHook` 並實作 `async def run(self, context: HookContext, data: ToolCall) -> HookResult`。
  在本 Lab 中，`ComplianceVerifierHook` 用來檢查地名是否含有簡體中文字元。如果包含，Hook 直接攔截並拒絕（回傳 `allow=False`），不調用資料庫，向 Agent 回傳合規政策拒絕訊息。

### 3. Stateful Loop 自我修正閉環
* **概念**：當寫入失敗時，Agent 絕不能直接崩潰，而必須具備「解析錯誤原因」並「重新規劃 thoughts」以自我修正的能力。
* **Agent 的修正策略**：
  * **簡體字攔截（Hook 拒絕）**：Agent 接收到 Hook 傳回的繁體正體中文合規要求，主動將地名轉換為繁體（如「台南孔庙」 $\rightarrow$ 「臺南孔廟」）重新試寫。
  * **外鍵約束失敗**：說明該行政區代碼（如 `TW-TNN-99`）無效。Agent 查閱失敗 payload，主動呼叫 `query_valid_districts` 查詢合法代碼，找到最相近的 `'TW-TNN-01'` 修正後重新試寫。
  * **唯一性約束失敗**：說明資料已導入。Agent 自動判定無須重複寫入，在 thought 中記錄並安全跳過。

---

## 🛠️ 工程踩坑與解決方案 (SQLite Multi-Threading)
* **問題**：在背景多執行緒運行中，Python 常會拋出 SQLite 跨執行緒操作錯誤。
* **解決方案**：在初始化 SQLite 連線時，加入 `check_same_thread=False`：
  ```python
  sqlite3.connect(":memory:", check_same_thread=False)
  ```
