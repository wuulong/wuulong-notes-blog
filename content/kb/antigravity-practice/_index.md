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
* **Lab 7: 資料庫合規與約束**
  * [Lab7_data_compliance.py](./Lab7_data_compliance.py) — 實作資料庫約束與簡繁轉換合規政策，解決 SQLite 多執行緒跨執行緒調用限制。
  * 👉 [技術學習導引](./logs/logs_lab7_explain.md)
* **Lab 8: 長週期認知接力**
  * [Lab8_cognitive_handover.py](./Lab8_cognitive_handover.py) — 利用 `save_dir` 與對話 ID 實現記憶中斷與全新接力。
  * 👉 [技術學習導引](./logs/logs_lab8_explain.md)
* **Lab 9: 紅藍軍對抗規格自審**
  * [Lab9_adversarial_loop.py](./Lab9_adversarial_loop.py) — 藍軍、紅軍與裁判官三 Agent 沙盒對抗，引入 $\Delta$-Guard 強校驗封堵重放漏洞。
  * 👉 [技術學習導引](./logs/logs_lab9_explain.md)
* **Lab 21: MCP 整合與結構化輸出**
  * [Lab21_mcp_leads_sync.py](./Lab21_mcp_leads_sync.py) — 串接本地 Mock Stdio MCP 服務並以 Pydantic Constraint 強制 JSON 輸出。
  * 👉 [技術學習導引](./logs/logs_lab21_explain.md)
* **Lab 22: 動態安全網與沙盒審查**
  * [Lab22_security_sandbox.py](./Lab22_security_sandbox.py) — 以 `PreToolCallDecideHook` 攔截高風險工具並執行提權審核。
  * 👉 [技術學習導引](./logs/logs_lab22_explain.md)
* **Lab 23: 聲明式 Skill 與 Rules 治理**
  * [Lab23_declarative_skills.py](./Lab23_declarative_skills.py) — 聲明式載入 `music-ops` 技能檔，並動態改寫專案級 `AGENTS.md` 行為規則。
  * 👉 [技術學習導引](./logs/logs_lab23_explain.md)
* **Lab 24: 推理軌跡可觀測性評估**
  * [Lab24_observability_eval.py](./Lab24_observability_eval.py) — 使用 `resolve()` 解析 flat list 軌跡 JSON 並以 Judge 診斷死迴圈重試。
  * 👉 [技術學習導引](./logs/logs_lab24_explain.md)
* **Lab 25: 即時人機對話詢問與回填**
  * [Lab25_human_in_the_loop.py](./Lab25_human_in_the_loop.py) — 實現衝堂時 Suspend 推理，詢問決策回填後 Resume 完成預約。
  * 👉 [技術學習導引](./logs/logs_lab25_explain.md)
* **📖 Antigravity SDK 與 Agentic 2.0 觀念自測題庫**
  * 👉 [sdk_quiz.md](./sdk_quiz.md) — 整理了 30 題涵蓋基礎 SDK 原理、工具與安全 Hook 治理、快照 Session 持久化，以及 Agentic 2.0 軟體架構設計（如限流自癒、資訊屏障、專家分權路由等）的折疊式離線問答集。
* **其他基礎測試**
  * [factorial.py](./factorial.py) — 階乘計算的基礎單元測試。
