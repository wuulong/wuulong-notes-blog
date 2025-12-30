---
title: "實戰 n8n 整合 Google Custom Search：從踩坑到成功"
date: 2025-12-19T10:40:00+08:00
draft: false
categories: ["Technology (技術)"]
series: ["n8n"]
tags: ["n8n", "Google Search", "API", "Troubleshooting"]
summary: "紀錄如何在 n8n 中透過 HTTP Request 節點實作 Google 搜尋功能，包括 API Key 申請、CSE 設定、網站驗證與除錯技巧。"

---

## 🎯 核心目標

在 n8n 的 AI Agent Workflow 中，賦予 Agent 「上網搜尋」的能力，特別是用於 Retrieve 針對特定網站（例如自己的部落格）的內容。

## 🛠️ 關鍵機制與架構

不需要安裝額外的社群節點 (Community Node)，直接使用 n8n 原生的 **HTTP Request Node** 呼叫 Google Custom Search JSON API 即可。

### 1. 申請 API Key (通行證)
*   **用途**：讓 Google 知道是誰在呼叫 API (計費與權限控管)。
*   **步驟**：前往 GCP Console 啟用 "Custom Search API" 並建立憑證。
*   **網址**：[GCP Console - Credentials](https://console.cloud.google.com/apis/credentials) <!-- 請確認或更新此連結 -->

### 2. 設定搜尋引擎 CSE (定義範圍)
*   **用途**：定義「要搜尋哪些網站」、「是否搜尋全網」。
*   **步驟**：
    1.  建立新的 Search Engine。
    2.  設定 "Sites to search" (例如 `https://wuulong.github.io/wuulong-notes-blog/*`)。
    3.  取得 **Search Engine ID (cx)**。
*   **網址**：[Programmable Search Engine 控制台](https://programmablesearchengine.google.com/controlpanel/all) <!-- 請確認或更新此連結 -->

### 3. n8n 實作設定 (HTTP Request)
*   **Node**: HTTP Request
*   **Method**: `GET`
*   **URL**: `https://www.googleapis.com/customsearch/v1`
*   **Query Parameters**:
    *   `key`: `{{ 您的 API Key }}`
    *   `cx`: `{{ 您的 Search Engine ID }}`
    *   `q`: `{{ 搜尋關鍵字 }}`
*   **參考文件 (API Spec)**：[Google Custom Search JSON API Reference](https://developers.google.com/custom-search/v1/reference/rest/v1/cse/list?apix=true&hl=zh-tw) <!-- 填入 API 參數說明頁網址 -->

## 💡 踩坑心得與除錯技巧 (The Tricks)

### 陷阱：查不到資料 (TotalResults: 0)
初次設定時，常遇到 API 回傳 200 OK 但 `items` 是空的。原因通常是：

1.  **索引延遲 (The "Slow Index")**：
    *   新網站或剛搬家的網站，Google 可能根本還沒爬到。
    *   **解法**：必須去 Google Search Console 進行**網站驗證 (Site Verification)** 並提交 Sitemap，加速索引。
    *   **GSC 網址**：[Google Search Console](https://search.google.com/search-console)

2.  **範圍設定太窄**：
    *   如果 CSE 設定只搜特定網站，而該網站還沒被索引，就會查無資料。
    *   **測試技巧**：在 CSE 控制台中，暫時開啟 **"Search the entire web" (搜尋全網)**。
    *   如果在 n8n 裡重測能抓到外部資料（如 Wikipedia），代表 **API 串接沒問題**，問題出在**網站索引**或**CSE 範圍設定**。

### 驗證工具
不要盲目在 n8n 裡試錯，Google 提供了測試工具：
*   **CSE Preview**：在 Programmable Search Engine 控制台右側，可以直接打字測試搜尋結果。如果這裡都沒資料，API 當然也抓不到。

## ✅ 最終流程總結

1.  GCP 拿 Key。
2.  CSE 拿 ID，並設定目標網站。
3.  (關鍵) 去 GSC 驗證網站，確保 Google 找得到你。
4.  在 CSE 控制台測試預覽，確認有資料。
5.  回到 n8n，用 HTTP Request 填入 URL 與參數。
6.  Agent 成功聯網！

### AI 協作宣告 (AI Collaboration Disclosure)

> ![AI Generated](https://img.shields.io/badge/Content-AI%20Assisted-8A2BE2?style=flat-square&logo=google-gemini&logoColor=white) 
> ![Human Reviewed](https://img.shields.io/badge/Review-Human%20Verified-green?style=flat-square)
>
> **本文內容由 AI 協作生成**：
> 1.  **踩坑經驗**：哈爸 (人類) 實戰測試。
> 2.  **文章整理**：AI (Gemini) 協助將口述經驗轉化為結構化筆記。
> 3.  **技術邏輯**：Antigravity 協助驗證 API 參數與步驟正確性。
