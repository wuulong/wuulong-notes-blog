# Lab 22 學習導引與技術解析

本 Lab 探討如何在執行期（Runtime）限制 Agent 對敏感/高風險工具（如刪除學生紀錄、更新學費）的操作，實施「權限最小化原則」與「動態安全攔截網」。

## 💡 核心學習重點

### 1. 執行期工具攔截 (PreToolCallDecideHook)
* **概念**：在 Agent 推理思考出需要呼叫某個 Tool，但**還沒有真正發送參數並執行該 Tool 之前**，系統可以掛載攔截網對其進行審計。
* **實作技術**：
  繼承 `PreToolCallDecideHook`。在 `async def run(self, context, data)` 中，`data` 為 `types.ToolCall` 對象。
  * 對於 `delete_student_record` 操作，安全 Hook 回傳 `allow=False` 與詳細的拒絕原因（Permission Denied）。
  * 對於 `update_tuition_fee` 操作，安全 Hook 回傳 `allow=True`（核准執行）。

### 2. 最小權限與安全降級 (Graceful Fallback)
* **概念**：當 Agent 面臨安全網阻斷並回傳 `Permission Denied` 時，它在 Thoughts 中能主動捕獲此異常，更新其心智模型，改為尋求替代的、符合權限的安全方案（在本 Lab 中為改調整新學費）。這展示了軟體工程級別的安全性與穩健性。

---

## 🛠️ 本地背景測試無阻塞設計 (HITL Terminal Prompt Bypass)
* **工程痛點**：
  在 SDK 原生的 `ToolConfirmationHook` 中，它是透過 `input("Allow execution? y/n")` 來讓人類進行確認（Human-in-the-loop, HITL）。
  然而，在自動化 CI/CD、測試腳本、或是 Antigravity 的背景任務（Task Running）中，標準輸入是**非互動式**的，調用 `input()` 會直接引發 `EOFError` 或卡死程序。
* **解決方案**：
  我們在自訂的 `StudioSecurityHook` 內部引入了「狀態機邏輯判定」，動態對特定高風險工具給予 `allow=False`（拒絕）與 `allow=True`（接受）的回應。這完美模擬了人機協同審核的兩種分支，又保證了背景自動化指令能無阻塞地流暢跑完。
