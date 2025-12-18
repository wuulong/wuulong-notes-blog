---
title: "社群經營自動化暖身：用 n8n 打造 Discord 每日歡迎機器人"
date: 2025-12-18T12:00:00+08:00
draft: false
tags: ["n8n", "Discord", "Automation", "Community Management"]
series: ["AI Agent 開發實戰"]
categories: ["Technical", "Automation"]
description: "在打造複雜的 AI Agent 之前，我們先來個社群自動化的暖身操。這篇文章教學如何使用 n8n 建立一個「Discord 每日歡迎機器人」，定時整理過去 24 小時加入的新夥伴名單並發送歡迎訊息，既能活絡社群氣氛，又不會像即時歡迎那樣頻繁洗版。"
summary: "覺得 Discord 的 MEE6 歡迎訊息太制式？或是討厭每次有人加入就跳通知洗版？本文分享如何用 n8n 自幹一個「每日歡迎機器人」。這個自動化流程會在每天中午定時執行，抓取過去 24 小時加入的新成員名單，整理成一則溫馨的歡迎總結。過程中我們也會學到 Discord Developer Portal 裡最容易被忽略的「Server Members Intent」隱藏權限設定。"
---

在深入研究 [AI Agent 架構](/wuulong-notes-blog/posts/20251217_building-agentic-discord-bot/) 這種比較硬核的技術之前，我們今天先來做個輕鬆的 **社群自動化 (Community Automation)** 暖身操。

經營 Discord 社群時，我們通常希望給新加入的朋友一點溫暖，但又面臨兩難：
1.  **即時歡迎 (Real-time)**：每進一個人就 `@` 一次，如果剛好這天進來 50 個人，頻道就會被洗版，舊成員反而會想把通知關掉。
2.  **完全不歡迎**：新成員進來覺得冷清，默默就潛水了。

我的解法是：**「每日晨間播報」**。
每天中午 12:00，機器人自動整理一份「過去 24 小時加入的新夥伴名單」，一次性地歡迎大家。這樣既有儀式感，又不會造成資訊干擾。

## Workflow 架構總覽

這是在 n8n 上的實作流程，邏輯非常簡單清晰：

![n8n Welcome Workflow](n8n_welcome_workflow.png)

1.  **Schedule Trigger**：每天固定時間 (12:00) 叫醒機器人。
2.  **Get Many Members**：從 Discord 抓取成員名單。
3.  **Code (JS)**：核心邏輯，篩選出「加入時間 (joined_at)」在 24 小時內的人。
4.  **If**：判斷人數是否大於 0 (沒人就不用發文了)。
5.  **Send Message**：發送整理好的歡迎訊息。

## 實作關鍵與踩坑筆記

雖然流程看起來只有五個節點，但裡面藏了一個 **90% 人都會撞牆** 的權限陷阱。

### 1. 權限陷阱：Server Members Intent

當你使用 n8n 的 `Discord` 節點選擇 `Get Many Members` 時，你可能會發現：**「奇怪，為什麼只抓得到機器人自己？」** 或是直接報錯。

這是因為 Discord 為了隱私保護，預設**不讓機器人讀取成員清單**。你必須手動開啟這個「特權」。

*   **解決方法**：
    1.  前往 [Discord Developer Portal](https://discord.com/developers/applications)。
    2.  點選你的 App -> 左側 **Bot** 選單。
    3.  往下滑找到 **Privileged Gateway Intents**。
    4.  將 **SERVER MEMBERS INTENT** 打開 (開關變綠色)。
    5.  記得按 **Save Changes**。

![Intent Setting](https://i.imgur.com/example-intent-setting.png) *(示意圖: 請記得去後台打開 Server Members Intent)*

### 2. 用 Code 節點過濾時間

雖然 Discord API 可以抓取成員，但它沒有「給我昨天加入的人」這種方便的參數。所以我們的策略是：**「抓一堆人下來，然後用 JavaScript 自己過濾」**。

在 `Code` 節點中，我們寫一段簡單的 JS：

```javascript
// 1. 設定時間基準：現在時間往回推 24 小時
const now = new Date();
const cutoffTime = new Date(now.getTime() - (24 * 60 * 60 * 1000)); 

// 2. 過濾 items
// n8n input 都在 'items' 陣列裡
const newMembers = items.filter(item => {
    const joinDate = new Date(item.json.joined_at);
    return joinDate >= cutoffTime; // 留下加入時間晚於基準線的人
});

// 3. 處理沒人的狀況
if (newMembers.length === 0) {
    // 即使沒人，回傳 count: 0 讓後面的 IF node 好判斷
    return [{ json: { count: 0 } }];
}

// 4. 產生提及列表 (Discord 格式是 <@ID>)
const mentionList = newMembers.map(m => `<@${m.json.user.id}>`).join(', ');

return [{
    json: {
        count: newMembers.length,
        mentions: mentionList,
        message: `🎉 歡迎過去 24 小時加入的 ${newMembers.length} 位新夥伴：\n${mentionList}\n記得去 #self-intro 自我介紹喔！`
    }
}];
```

這段程式碼做了三件事：**過濾時間**、**處理空值**、**格式化文字**。這樣後面的 Discord 發送節點就只需要單純引用 `{{ $json.message }}` 即可，邏輯分離得更乾淨。

### 3. If node 的小細節

如果昨天沒人加入，Code 節點回傳 `count: 0`。我們在 `If` 節點設定條件：
*   **Condition**: Number
*   **Expression**: `{{ $json.count }}`
*   **Operation**: `Larger` (>)
*   **Value**: `0`

只有 `True` 的時候才發送訊息，這樣就不會出現機器人每天早上洗版說「昨天沒人加入喔...」的尷尬場面。

## 為什麼不用 MEE6 就好？

MEE6 雖然方便，但它的歡迎訊息通常是**即時**的，且客製化程度有限（要付費才能解鎖進階功能）。

使用 n8n 自己刻的好處是：
1.  **完全免費**：配合自架伺服器或免費額度。
2.  **邏輯自訂**：你可以改成「每週五歡迎」、「滿 10 人才歡迎」，或是針對不同身分組發送不同歡迎詞。
3.  **整合強**：歡迎完之後，還可以順便把名單寫入 Notion 或 Google Sheets 做分析，這就是 MEE6 做不到的了。

這只是一個簡單的暖身，但它展示了 **n8n + Code Node** 的強大靈活性。當你能自由控制資料流時，社群經營就能變出更多有趣的玩法！

### AI 協作宣告 (AI Collaboration Disclosure)

> ![AI Generated](https://img.shields.io/badge/Content-AI%20Assisted-8A2BE2?style=flat-square&logo=google-gemini&logoColor=white) 
> ![Human Reviewed](https://img.shields.io/badge/Review-Human%20Verified-green?style=flat-square)
>
> **本文內容由 AI 協作生成**：
> 1.  **素材來源**：作者實際 N8n 實作截圖與需求。
> 2.  **AI 工具**：使用 Antigravity (Gemini) 協助撰寫文章架構與技術細節說明。
> 3.  **人工審核**：由哈爸本人確認技術觀點與程式碼邏輯準確性。
