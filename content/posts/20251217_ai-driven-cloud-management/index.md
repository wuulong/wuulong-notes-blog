---
title: "出一隻嘴做系統管理：AI Agent 讓 GCP 變得像點餐一樣簡單"
date: 2025-12-17T10:00:00+08:00
draft: false
tags: ["AI Agent", "GCP", "DevOps", "Antigravity", "gcloud"]
series: ["GCP學習旅程"]
categories: ["GenAI (生成式 AI)"]
description: "以前面對 GCP 複雜的 Web Console 和記不完的 CLI 命令總是很頭痛，也不知道該選什麼服務才划算。現在發現透過 AI Agent (Antigravity) 搭配 gcloud，只需要用口語下指令，就能輕鬆完成複雜的雲端維運，甚至連計費模式都能問得清清楚楚。"
summary: "雲端服務最讓人卻步的往往不是技術本身，而是那複雜到像迷宮的控制台介面，以及永遠搞不懂的計費陷阱。這篇文章分享我如何使用 AI Agent (Antigravity)，把原本痛苦的 GCP 系統管理工作，變成了一場輕鬆的對話。不用再查文件、不用背指令，只要「出一隻嘴」，機器就開好了，錢也省下來了。"
top: false
---

說實話，我以前對 GCP (Google Cloud Platform) 是又愛又恨。

愛的是它的強大和穩定，恨的是它的 **Web Console (管理控制台) 真的太有深度了**。每次要找個「防火牆設定」或「硬碟管理」，都要在左側迷宮般的選單裡點半天。好不容易找到了，又充滿了各種看不懂的參數選項。

至於 CLI (`gcloud` 指令)？那更是另一個門檻。雖然知道它很強，但誰背得起來那麼多參數組合？每次用之前都要先 Google 半天，複製貼上還因為版本不同而報錯。

## 轉機：當 AI 接手終端機

最近我發現了一種全新的工作模式：**直接讓 AI Agent (Antigravity) 幫我操作 `gcloud`**。

這個體驗只能用「回不去了」來形容。我發現這才是雲端管理該有的樣子。

### 1. 擺脫 GUI 迷宮，指令隨口下

以前我要開一個防火牆 Port，流程是：
`搜尋 VPC -> 防火牆 -> 建立規則 -> 填一堆欄位 -> 檢查有沒有套用到機器 -> 按儲存`。

現在我的流程是：
> 「幫我把這台機器的 3000 到 32767 port 打開，我要跑 K8s。」

然後 AI 就會直接回傳一行精準的 `gcloud compute firewall-rules create ...`，我只要說「好」，幾秒鐘就搞定。完全不用管它在選單的第幾層。

### 2. 選擇困難症的救星

GCP 的服務多如牛毛。以前我想架個資料庫，會陷入選擇障礙：
*   要開 VM 自己裝？
*   還是用 Cloud SQL？
*   Cloud SQL 有分 Enterprise, Standard 還有 Shared Core？

光是研究這些規格差異就要花掉一下午。現在我直接問：
> 「我只有 200MB 的資料，流量很小，不想花大錢，Cloud SQL 適合嗎？」

AI 直接幫我分析：
> 「Cloud SQL 雖然方便但最便宜的 Shared Core 每月也要 10 美金以上。既然你資料量小，建議直接在既有的 VM 上跑 Docker，成本幾乎是 0。」

這種 **「顧問級」的建議**，比單純的執行指令更有價值。

### 3. 最可怕的「計費」，終於看懂了

雲端最怕的就是月底帳單震撼。以前很多服務都是「先用了再說」，收到帳單才知道那個 IP 要錢、那個流量要錢。

現在我在做任何決定前，都會多問一句：
> 「這台機器固定 IP 如果我不關機，會收錢嗎？」

AI 清楚地告訴我規則：
> 「只要綁定在『運行中』的機器，固定 IP 是免費的。但如果你關機，就會開始收空置費。」

這種隱藏規則，以前可能要翻爛官方文件才找得到，現在 AI 直接幫我避雷。

## 結論：出一隻嘴做系統管理

這種 **「Intent-based (意圖導向)」** 的操作方式，極大程度地降低了維運的心理負擔。

我不需要成為 GCP 的專家，不需要背誦 `gcloud` 的語法，我只需要清楚 **「我想做什麼」**。剩下的細節、參數、甚至防呆檢查，AI Agent 都幫我包辦了。

如果你也覺得雲端控制台很難用，不妨試試看把權限交給 AI，體驗一下什麼叫「出一隻嘴」就能運籌帷幄的快感。

### AI 協作宣告 (AI Collaboration Disclosure)

> ![AI Generated](https://img.shields.io/badge/Content-AI%20Assisted-8A2BE2?style=flat-square&logo=google-gemini&logoColor=white) 
> ![Human Reviewed](https://img.shields.io/badge/Review-Human%20Verified-green?style=flat-square)
>
> **本文內容由 AI 協作生成**：
> 1.  **素材來源**：作者實際操作經驗與技術筆記。
> 2.  **AI 工具**：使用 Antigravity (Gemini) 協助指令執行、除錯與文章撰寫。
> 3.  **人工審核**：由哈爸本人確認觀點準確性並進行最終潤飾。
