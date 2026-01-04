---
title: "Antigravity 實戰：解放 Google Maps MCP 的力量，AI 導遊帶你去吃喝"
date: 2026-01-05T07:50:00+08:00
draft: false
tags: ["AI", "Google Maps", "MCP", "Antigravity", "Gemini", "Automation"]
categories: ["GenAI (生成式 AI)"]
series: ["GenAI實驗"]
description: "這篇文章紀錄了如何突破 CLI 與 API 的限制，成功讓 AI Agent (Antigravity) 接入 Google Maps Grounding Lite MCP，並實戰應用於自行車道美食搜尋。"
---

# Antigravity 實戰：解放 Google Maps MCP 的力量，AI 導遊帶你去吃喝

身為一個依賴 AI 協作的開發者，我一直在思考如何讓我的 Agent (Antigravity) 擁有「真實世界的眼睛」。雖然它能寫程式、能搜尋網頁，但遇到「地理空間」的問題時——例如「這條路沿線有什麼好吃的？」——它往往只能給我模糊的網頁摘要，而不是精確的地點資訊。

這篇文章記錄了我如何從零開始，克服 API 權限、工具缺失、通訊協定不相容等困難，最終成功讓 Antigravity 使用 **Google Maps Grounding Lite MCP (Model Context Protocol)**，變身為超強 AI 導遊的過程。

## 1. 緣起：尋找 Agent 的「地圖外掛」

一開始，我希望能透過 Command Line Interface (CLI) 工具，讓 Agent 直接操作 Google Maps。但我發現：
*   **沒有官方 CLI**: Google 只有 `gcloud` (管機器的)，沒有 `gmaps` (查地圖的)。
*   **Gemini CLI 的潛力**: Google 推出了 `gemini` CLI，且支援 MCP (Model Context Protocol)，這是一個讓 LLM 能標準化呼叫外部工具的協定。

目標確立：**把 Google Maps MCP Server 裝進 Gemini CLI，再讓 Antigravity 呼叫它。**

## 2. 關卡與突破

### 關卡一：API Key 權限被鎖
我原本已有 GCP 專案與 API Key，但 Agent 測試 Python 腳本時這直接報錯。
**診斷**: 該 API Key 先前被設定為「僅限 Maps JavaScript API (前端用)」。
**解法**: 使用 `gcloud` 指令，將後端服務 (`geocoding-backend`, `places-backend`, `mapstools`) 加入白名單。

```bash
# 關鍵指令：解放 API Key 的後端權限
gcloud services api-keys update "$KEY_NAME" \
  --api-target=service=maps-backend.googleapis.com \
  --api-target=service=places.googleapis.com \
  ...
```

### 關卡二：找不到 MCP Server 安裝包
我試圖 `npm install @google/maps-mcp-server`，結果發現這個套件根本不存在。
**發現**: Google 官方提供的方案是 **Maps Grounding Lite**，這是一個 **Cloud-hosted MCP Server** (`https://mapstools.googleapis.com/mcp`)，不需要自己架設 Server！

### 關卡三：Gemini CLI 的非互動模式限制
當我們設定好 Server 後，Antigravity 試圖呼叫時被擋了下來：
`I cannot execute the search_places tool in this non-interactive environment.`
因為安全考量，Gemini CLI 預設執行工具前需要人類按 `Y` 確認，但 Agent 自動化執行時沒人能按。

**解法**: 啟用 **YOLO Mode (You Only Look Once)**。
1.  修改 `fabfile.py`，在呼叫指令加上 `--yolo` flag。
2.  在 `.gemini/settings.json` 中設定 `"autoAccept": true`。

```python
# fabfile.py 修改片段
cmd = f'gemini --yolo -m "{model}" "{safe_prompt}"'
```

## 3. 實戰驗證：后豐鐵馬道美食搜查

突破所有技術屏障後，我向 Antigravity 下了終極指令：
> 「搜尋台中『后豐鐵馬道』和『東豐自行車綠廊』沿線有哪些有名氣的在地小吃或美食？」

這一次，它不再是瞎掰，而是直接呼叫了 `search_places` 工具，回傳了極具參考價值的清單：

**🚲 后豐鐵馬道**
*   **橫喜堂**: 日式職人點心，騎車補充熱量首選。
*   **200days**: 純白玻璃屋與草湖芋仔冰，網美必去。
*   **新幹線列車餐廳**: 直接在火車車廂裡吃飯，體驗獨特。

**🌳 東豐綠廊**
*   **簡單就好**: 百年芒果樹下的古早味肉捲與剉冰。
*   **石岡擔擔麵**: 在地老店，招牌是軟嫩豬腳。
*   **梅子屋**: 強調在地食材的窯烤披薩。

## 4. 結語

這次的與 Antigravity 的協作經驗證明了 **MCP (Model Context Protocol)** 的強大。
我們不需要為了查地圖去寫複雜的 Python 爬蟲，只需要把「地圖能力 (MCP Server)」掛載給 Agent，它就能像人類一樣，理解地理位置、規劃行程，甚至推薦美食。

這就是 AI Agent 的未來：**工具化、標準化、自動化**。現在，我的 Agent 已經準備好帶我去下一個旅程了！

---
### 🤖 AI 協作宣告
*   **本文內容**: 由人類作者提供核心經驗與觀察，Antigravity 協助架構文章、潤飾文字並生成技術細節描述。
*   **技術實作**: 文中提及的 Google Maps API 整合方案、Gemini CLI 配置與相關測試指令，均由 Antigravity 根據人類指令編寫與驗證。
