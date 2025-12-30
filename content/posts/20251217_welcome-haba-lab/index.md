---
title: "【公告】歡迎加入「哈爸實驗室」Discord 社群！"
date: 2025-12-17T18:00:00+08:00
draft: false
tags: ["Discord", "Community", "Announcement", "Haba Lab"]
series: ["公告"]
categories: ["Project (專案)"]
description: "哈爸實驗室是一個專注於技術實作、自動化 (n8n) 與 AI Agent 的交流社群。這裡沒有空泛的理論，只有捲起袖子的實戰。最近我們更新了 Discord Bot 功能，歡迎進來體驗最新的法規查詢助手！"
summary: "一個人埋頭苦幹，不如一群人一起實驗！「哈爸實驗室」Discord 群組正式開放，這裡匯集了對 n8n 自動化、AI Agent 開發有興趣的朋友。最新上線功能：AI 法規查詢機器人 (!law)，快進來試玩！"
top: true
weight: 1
---

## 🧪 關於哈爸實驗室 (Haba Lab)

這裡是一個**「動手做」**的技術社群。
我們相信，技術的樂趣在於解決真實世界的問題。無論是自動化工作流程 (n8n)、雲端架構 (GCP)、還是最新的 Agentic AI 應用，我們都強調**實戰與分享**。

我們最近也開啟了台灣河川探索，歡迎大家一起來看看台灣美麗的河川與在地的文化！

如果你厭倦了單向的閱讀，想要找人討論「為什麼這個 Docker 跑不起來？」、「這個 n8n 節點怎麼接？」，歡迎加入我們！

👉 **[點擊加入 哈爸實驗室 Discord 頻道](https://discord.gg/DMknUBmV)**

## 🚀 最新功能發佈：AI 法規查詢助手

為了展示 **Agentic AI** 的威力，我們在 Discord 群組中部署了一個最新的實驗性機器人。

*   **功能**：自動查詢法律資料庫。
*   **指令**：在對話框輸入 `!law 你的問題`
*   **背後原理**：它不是單純的關鍵字搜尋，而是由 AI 理解你的問題後，**自動撰寫 SQL** 到後端 Postgres 資料庫查詢，再將結果整理給你。(想知道怎麼做的？請看 [這篇教學](/wuulong-notes-blog/posts/20251217_building-agentic-discord-bot/))

### 範例：
> **User**: `!law 政府採購法有幾條？`
> **Bot**: *(自動執行 SQL COUNT)* 根據資料庫紀錄，目前共有 123 條。

法規查詢功能只在 #genai-數位遊牧 頻道開放，歡迎進來試玩，請使用 prefix `!law` 進行查詢，順便和我們分享你的測試結果！

## 🤝 這裡可以做什麼？

1.  **技術問答**：卡關了？貼出 Log，大家一起 Debug (就像我們一起解決 Discord Intent 問題一樣)。
2.  **專案展示**：做出了好玩的 Workflow？Show 出來讓大家崇拜一下。
3.  **共筆學習**：不定期的技術筆記與心得分享。

**[立即加入，開始你的實驗之旅！](https://discord.gg/DMknUBmV)**
