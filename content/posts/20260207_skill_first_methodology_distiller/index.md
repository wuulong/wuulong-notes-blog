---
title: "「Skill 優先」的 AI 協作新實踐：從需求定義到知識點萃取的自動化進化"
date: 2026-02-07
categories:
  - Agentic AI (代理程式 AI)
  - Automation & Workflows (自動化與工作流程)
  - Maker & Hardware (創客與硬體)
  - Methodology (方法論)
  - Productivity & KM (生產力與知識管理)
  - Software Engineering (軟體工程)
  - System Engineering (系統工程)
series: ["哈爸實驗室"]
tags:
  - NotebookLM
  - Python
  - 工作流程
  - 知識管理
  - 自動化
description: "記錄第一次嘗試「先定義 Skill 通用邏輯，再投入實戰修正」的協作經驗。透過建立知識點萃取員 (Knowledge Point Distiller)，我們實現了會議錄影到結構化知識庫的高效轉化。"
---
# 「Skill 優先」的 AI 協作新實踐：從需求定義到知識點萃取的自動化進化

## 🚀 序言：一個新的協作節奏

在過去的 AI 協作中，我通常是先遇到問題，發出指令，解決之後再考慮是否要將它整理成工具。但這一次，我試著調換順序：**先說出一個「Skill」的構想，定義它的通用流程與腳本格式，然後直接用它來演練並修正。**

這次的目標是：如何高效地將長達一個多小時的「哈爸實驗室雙周會」錄影，拆解成一個個有價值的「知識點 (Knowledge Points)」。

---

## 🏗️ 第一步：Skill 的定義與構建 (Defining the Skill)

與其說「幫我切影片」，我對 AI 下達的指令是：「我們來做一個 `knowledge-point-distiller` Skill」。這個 Skill 必須具備以下完整閉環：

1.  **影音處理自動化**：能根據時間清單自動切割影片，並同步產出適合 NotebookLM (容量 < 20MB) 的優化 MP3。
2.  **資源歸檔結構化**：每一個知識點 (KP) 都有自己的資料夾，包含 MP4 片段、MP3 音訊與 `metadata.md`。
3.  **SOP 化**：將整套流程寫入 `.agent/skills/` 目錄下的 `SKILL.md`，讓 AI 與我都能隨時查閱操作標準。

這種「先建工具，後打仗」的做法，讓我在還沒開始處理影片前，就已經擁有了整套「生產線」。

---

## 🧪 第二步：實戰演練與即時修正 (Practice & Refinement)

有了工具後，我們直接拿「2/6 哈爸實驗室雙周會」進行測試。這個階段的「修正」是重點：

*   **全場音訊的需求**：在切割子片段的過程中，我發現除了個別知識點，我也需要一份「全場完整錄音」上傳到 NotebookLM 進行全局綜整。於是，我們立刻將這個功能補進 Skill 的 SOP 中。
*   **與 Git 的整合**：歸檔不是終點，提交才是。我們在 Skill 流程中補上了 GitHub 的 Commit 與 Push 指引。
*   **跨 Skill 調度**：在這個過程中，新的 Skill 自動調用了先前的 `media-processor` Skill 來處理高品質音訊壓縮，展現了技術模組之間的協同能力。

---

## 💡 關鍵體驗：為什麼「先說出 Skill」很有用？

這是我第一次嘗試「先定義、再運作、後修正」的模式，心得如下：

1.  **減少重複溝通**：當流程被定義為 Skill，AI 就能在處理過程中體現「一致性」。它不再只是執行一個指令，而是遵循一套規範。
2.  **結構化思維**：為了定義 Skill，我必須逼自己想清楚「這件事的標準化終點在哪裡？」。這大大提升了最後歸檔的整潔度。
3.  **即時強化的成就感**：看著一個剛定義出來的 Skill，在幾分鐘內就產出所有 KP 資料夾、MP3 檔案並完成 Git Commit，那種「流程穩定感」非常強大。

---

## 🏁 最終成果：哈爸實驗室雙周會 #2

最終，這場 72 分鐘的會議被成功轉化為：
*   **2 個高品質 KP 單元** (MP4 + MP3 + Metadata)。
*   **1 份全場優化音訊** (16.58 MB)。
*   **1 份完成的 GitHub 歸檔與 Commit**。

這不僅僅是處理完一場會議，而是我們為未來的無數場會議，預備好了一支強大的「AI 知識點萃取部隊」。

補充：[主題：2/6 #2 哈爸實驗室雙周會](https://docs.google.com/document/d/1NIs5vYOEiO_LCqQnJPqay7d_QxuDVzrYFeD6QFXoZVk/edit?tab=t.0#bookmark=kix.2lb1cu4fkbm4)

---
**協作紀錄：**
- **策劃**: USER (哈爸)
- **執行與 Skill 構建**: Antigravity (AI Coding Assistant)
- **技術棧**: Python, FFmpeg, NotebookLM, Git
- **里程碑**: 第一次成功的「Skill-First」協作實踐
- **日期**: 2026-02-07
