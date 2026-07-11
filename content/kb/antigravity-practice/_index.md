---
title: "Antigravity 實踐 (Antigravity Practice)"
bookCollapseSection: false
weight: 20
---

關於使用 Antigravity 進行開發與自動化協作的各項練習與實踐紀錄。
在這裡記錄了兩階段 AI 協作、工作流實踐以及各類 Sandbox 實驗。

---

## 📋 實踐腳本與實驗室 (Labs & Scripts)

以下為本主題下的練習與實作 Python 腳本，連結均已採用相對路徑，本地編輯器 (如 Obsidian) 與 GitHub 能直接跳轉，且 Hugo 編譯後會自動導向 GitHub 原始碼頁面：

* **Lab 1: 思考流模擬**
  * [Lab1_thoughts_stream.py](./Lab1_thoughts_stream.py) — 模擬 AI 代理人的思維鏈（CoT）推理過程。
* **Lab 2: 人機協作沙盒**
  * [Lab2_hitl_sandbox.py](./Lab2_hitl_sandbox.py) — 實作 Human-in-the-Loop（HITL）攔截與授權機制。
* **Lab 3: 多代理人協作**
  * [Lab3_multi_agent_collab.py](./Lab3_multi_agent_collab.py) — 建立與協調多個子代理人（Sub-agents）並行運作。
* **Lab 4: 自訂工具綁定**
  * [Lab4_custom_tool_binding.py](./Lab4_custom_tool_binding.py) — 為 AI 代理人註冊並綁定本地的自訂工具。
* **Lab 5: 工具調用策略**
  * [Lab5_tool_policies.py](./Lab5_tool_policies.py) — 設定與約束代理人的工具使用權限與安全策略。
* **Lab 6: 自我修正循環**
  * [Lab6_self_correction_loop.py](./Lab6_self_correction_loop.py) — 實現具有反思與自動錯誤修正能力的執行閉環。
* **其他基礎測試**
  * [factorial.py](./factorial.py) — 階乘計算的基礎單元測試。
