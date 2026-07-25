---
title: "實戰派的懶人 AI 學習法：以執行、檢視、改 code 來肉身探測 Antigravity SDK"
date: 2026-07-05T09:25:00+08:00
draft: false
categories:
  - Agentic AI (代理程式 AI)
  - Methodology (方法論)
  - Personal AI Empowerment (個人 AI 賦能)
  - Productivity & KM (生產力與知識管理)
  - Software Engineering (軟體工程)
series:
  - "個人 AI 賦能方法論"
tags:
  - AI
  - AI Agent
  - Antigravity
  - Methodology
  - Python
  - 哈爸筆記
  - 知識管理
cover:
  image: "assets/images/20260705_antigravity_sdk_lazy_learning.jpg"
  alt: "Antigravity SDK 實戰練習"
  relative: false
---
最近這陣子人變得很慵懶，老實說，有點快跟不上這波狂飆的 AI 最新進展。但心裡很清楚，對於 Google Antigravity SDK 的新架構，我勢必得做一次紮實的掌握。

以往面對新技術，直覺就是去翻那幾百頁、結構繁複的官方文件，讀得昏昏欲睡。這次我決定換個方式——來一場**「實戰派的懶人學習法」**。

不囉唆，直接由 AI 幫我產生最簡化的實作範例，然後在我的 `conda` 與 `fish` 環境中直接**執行、檢視、看 code、改 code**。沒想到，這樣肉身探測的學習效果出奇得好。

---

## 💡 為什麼「範例驅動」的學習效果這麼好？

過去我們習慣先理解理論再動手，但在 Agentic AI 時代，這種模式太慢了。這次我的核心策略就是：**「直接直擊關鍵痛點，省去所有繁瑣的解析過程。」**

*   **實作與概念同步**：我們從最基礎的 `Lab 1` 串流 Thoughts 開始，寫一個幾十行的 Python 檔。一跑起來，看見 Agent 的推理獨白在終端機流動，我就立刻懂了什麼是「思維與文字雙串流」。
*   **關鍵不懂直接看 Code**：遇到看不懂的機制，不再上網搜尋。直接在編輯器點開 code 讀它的結構，甚至自己動手修改、跑看看。
*   **在實戰中除錯 (Debugging)**：過程中我們遇到了 `protobuf` 套件版本衝突的 `TypeError`，以及 `.env` 環境變數沒有自動載入的問題。我們一邊踩坑一邊在 Python 中寫了一個無相依性的 `load_dotenv` 輔助函式，這些實戰中的微小調整，才是一個人真正掌握技術的瞬間。

---

## 🧠 最特別的體驗：AI Agent 主動去「讀原始碼」來解釋概念

在這次練習中，最讓我驚豔的並不是我自己看 code 的過程，而是 **AI Agent 的行為**。

當我完成了基礎的三個 Labs，想要深入了解 Antigravity SDK 相比傳統 Google GenAI SDK (GAI) 更深層的核心觀念時（例如底層的安全策略 Policy 或 Hook 機制），Agent 做了一件非常特別的事：

> **它並沒有胡亂猜測或吐出一堆八股的文件說明，而是主動調用工具，在我的 Python 環境裡執行 `inspect.getsource`，把 SDK 底層的 `_PolicyDecideHook` 與 `_evaluate_predicate` 的 raw code 讀了一遍！**

它看完原始碼後，發現了極其關鍵的細節：原來在 SDK 內部，當我們定義 Predicate 函數時，如果沒有寫特定 type hint，傳入的參數會自動被解析為 `dict`（也就是 `tool_call.args`），而不是 `ToolCall` 物件。

就是因為它「先看 code，再來決定呈現什麼」，我們才能當場揪出引數大小寫與型別不對合的 Bug，並將 `Lab 5` 改寫成相容性極佳的代碼。這種「AI 讀 code 解 code」的技術對齊，感覺非常震撼。

---

## 💻 順便玩玩 Antigravity CLI，體會 UI 的溫差

在整個實作過程中，我除了寫 Python 程式碼，也順便在終端機把玩了 Antigravity CLI (`agy`)。

相較於精美、包裝妥當的網頁 UI（瀏覽器面板），`agy` CLI 給人一種更加硬核且直接的「手感」。在 CLI 中，所有的背景任務、Subagents 的狀態都可以透過簡單的斜線指令（如 `/help`）或 terminal status 來掌握。

這種感覺就像是，網頁 UI 是做給消費者或終端使用者的精緻沙盒；而 CLI 與 Python SDK，則是專門開放給開發者、讓我們能用程式碼來「程式化租賃（Lease）與調度」AI Agent 的底層 API。這兩者之間的溫差，只有親自操作過才能體會。

---

## 🎯 這次收穫的 5 個極簡 Labs 麵包屑

這次肉身探測，最後在我的工作區留下了五個寶貴的實作 Labs：
1.  **[Lab 1: Thoughts Stream](file:///projects/antigravity-practice/Lab1_thoughts_stream.py)**：學會串流思維軌跡。
2.  **[Lab 2: HITL Sandbox](file:///projects/antigravity-practice/Lab2_hitl_sandbox.py)**：實作人為介入工具審查。
3.  **[Lab 3: Multi-Agent Collaboration](file:///projects/antigravity-practice/Lab3_multi_agent_collab.py)**：Coder 與 Reviewer 的對抗修正循環。
4.  **[Lab 4: Custom Tool Binding](file:///projects/antigravity-practice/Lab4_custom_tool_binding.py)**：本地 Python 函式自動 Schema 解析與鏈式調用。
5.  **[Lab 5: Tool Policies](file:///projects/antigravity-practice/Lab5_tool_policies.py)**：SDK 底層安全門禁，自動攔截 `rm` 或是 `sudo` 指令。

這種直接在專案裡長出程式碼、肉身實測的感覺，真的比在瀏覽器裡盲目打 Prompt 踏實太多了。未來的 AI 協作，手感就該是這樣。

---

> **AI 協作聲明**：
> 本文由筆者提供原始概念與實戰心得，由 AI 助手 Antigravity 彙整架構與修辭。結合了 Antigravity SDK 的技術實作特點與哈爸筆記的敘事風格，展現人機協作下的技術探索成果。
