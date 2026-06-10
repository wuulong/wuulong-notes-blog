---
title: "Antigravity 升級體驗：從 Task 到 Skill，為我的河流探索法建立標準化技能"
date: 2026-01-17
draft: false
tags:
  - AI協作
  - Antigravity
  - 自動化
categories:
  - Agentic AI (代理程式 AI)
  - Automation & Workflows (自動化與工作流程)
  - River Exploration (河流探索)
series: ["2026台灣河流探索"]
---> **寫在升級後**：
> 剛整理完濁水溪的探索方法論 (SOP)，正準備發佈時，發現我的 AI 助手 Antigravity 也有了新功能——支援 **Skill (技能)** 系統。
> 於是，我順手請 AI 將原本單純的文字版 Task，升級為更具結構化的 Skill。這不僅是一次工具的迭代，更是 AI 協作模式的進化。

## 什麼是 Antigravity Skill？

過去我們習慣用 `Task` (任務) 來告訴 AI 做什麼，通常是一份 Markdown 文件，寫滿了步驟與指令。
而新的 `Skill` (技能) 則更像是一個 **「可執行的軟體包」**。它不僅有說明文件 (`SKILL.md`)，還可以包含專屬的腳本 (`scripts/`)、模板 (`templates/`) 與範例。

簡言之，Task 是給 AI 看的「說明書」，Skill 則是給 AI 用的「工具箱」。

## 實戰：建立 River Exploration Skill

我請 AI 將剛剛總結的「河流探索工作流」封裝成一個 Skill。
AI 迅速在 `.agent/skills/river-exploration/` 建立了以下結構：

*   **SKILL.md**：核心 SOP，包含了我強調的「黃金時間 (The Golden Hour)」當日結算流程。
*   **scripts/gen_map_urls.py**：把之前散落在專案裡的 Google Maps 連結生成程式，收納為此技能專用的工具。
*   **templates/blog_post_template.md**：標準化的遊記 Markdown 模板，確保每次產出的格式一致。

## Task vs. Skill：優缺點比一比

在實際體驗後，我對這兩種模式做了簡單的比較：

| 特性 | Task (舊模式) | Skill (新模式) |
| :--- | :--- | :--- |
| **結構** | 單一 Markdown 文件 | 文件夾結構 (MD + Scripts + Templates) |
| **可執行性** | 需手動複製貼上指令或腳本 | 腳本與模板隨手可得，AI 可直接調用 |
| **維護性** | 容易隨著對話變長而失焦 | 模組化管理，邏輯清晰，易於迭代 |
| **情境** | 適合一次性、非標準化的任務 | 適合**重複性高**、**流程固定**的專業工作 |
| **學習曲線** | 低，像寫筆記 | 高，需要定義清楚的目錄結構與介面 |

### 結論：為什麼 Skill 更好？

對於我的「台灣河流探索」計畫來說，**Skill 絕對是大升級**。
因為這不是一次性的旅行，而是要重複十幾次的標準流程。有了 Skill：
1.  **工具隨身帶**：不用再翻以前的對話找 Python 腳本，AI 加載 Skill 後就能直接跑程式生成地圖。
2.  **品質一致**：每次生成的遊記草稿都使用同一份 Template，格式統一，省去排版時間。
3.  **知識固化**：將「黃金時間」這種心法寫入 Skill，等於賦予了 AI 這項價值觀，它會主動提醒我執行，而不是等我下令。

Antigravity 的這次升級，讓 AI 從「聽話的助理」進化為「帶裝備的專家」。期待帶著這個新技能，去探索下一條河流——大甲溪！
