---
title: "AI 協作防禦工程：從 Rules 分流、偏好編譯、本體論降維到工具庫重組的實踐隨筆"
date: 2026-07-14T09:44:00+08:00
draft: false
categories:
  - Agentic AI (代理程式 AI)
  - GIS & Mapping (地理資訊與地圖)
  - Methodology (方法論)
  - Personal AI Empowerment (個人 AI 賦能)
  - Software Engineering (軟體工程)
series:
  - "個人AI賦能方法論"
tags:
  - AI
  - AIQA
  - Antigravity
  - GIS
  - Gemini
  - GitHub
  - Methodology
  - Python
cover:
  image: "cover_image.jpg"
  alt: "AI 協作防禦工程"
  relative: true
---
在與高階 AI 代理人（如 Antigravity）進行深度 Pair Programming 的過程中，開發者很快會面臨一個經典的系統挑戰——**「熵增 (Entropy Increase)」**。

當你沒有為 AI 建立邊界約束時，AI 會隨手寫出大量一次性的 ad-hoc 腳本、在每次對話初始化時重複載入十多個散落的規則檔、甚至在遇到大型文件時，產生 verbose 且昂貴的 Thoughts Token 刺客。

今天，這篇隨筆紀錄了我如何與 Antigravity 物理落地一套**「AI 協作防禦工程」**，將混沌的 ad-hoc 補丁，重塑為具備規則治理、本體論降維與 CLI 統一架構的智慧助理系統。

---

## 🧱 1. 地基：協作規則 (Rules) 的全域與專案級分流

> *[意圖說明] 奠定 AI 協作的憲法邊界。區分全域文化語境與專案物理開發環境，以剛性約束消除 AI 在依賴與編譯路徑上的不確定性。*

AI 協作的第一步是**「立憲」**。如果規則模糊，AI 就容易忘記 Conda 環境路徑，或在對話中 Dump 出冗長代碼塞爆 Token。我們將 Rules 物理分流為兩個層級：

### 🌍 A. 全域規則 (Global Rules) ➔ `~/.gemini/config/AGENTS.md`
*   **文化與語境定錨**：剛性約束 AI 使用繁體中文（台灣語境與觀點），自動過濾轉換中國大陸用語（如資訊/訊息、最佳化、軟體、資料庫）。
*   **歸檔頻率防禦 (AIQA-Scribe Guard)**：嚴禁 AI 在無實質成果的日常 Debug 中頻繁存檔。僅在「完成完整功能模組」、「解決重大 Bug」時觸發歸檔，節省磁碟與認知負載。

### 📁 B. 專案規則 (Project Rules) ➔ `.agents/AGENTS.md`
*   **環境硬綁定**：指定 Python 與 Pip 的實體 Conda 環境路徑（`/envs/m2504/`），避免 AI 在執行 CLI 時用錯系統環境。
*   **「先規劃建檔再動手 (TR-First)」**：當接收到複雜任務時，嚴禁 AI 直接修改程式碼。必須先自動註冊 `TASKS.md`，並在 `task-reports/` 下建立 `TR_[主題].md` 任務報告。AI 與人類先在大綱與 Impl Plan 上簽字（Sign-off），才能進入 Execution Phase。
*   **「Token-Saving 檔案優先」**：重要且長篇的回覆（如大綱、程式碼、設計文檔）必須自動寫入本地檔案，AI 在對話中僅提供 clickable 本地連結，消滅聊天 Context 的 Token 負荷。

---

## ⚙️ 2. 戰術一：LLM 偏好治理——從「載入摩擦」到「自動編譯」

> *[意圖說明] 解決多個規則檔併發載入帶來的 Token 浪費與讀取延遲。化零為整，實現單一真實來源 (Single Source of Truth) 以提升對話啟動效率。*

在專案中，隨著開發進程，我們會累積大量的行為規則（如格式偏好、工具偏好、特定專案脈絡）。如果每次開啟對話，AI 都需要用 `view_file` 載入十多個不同的規則檔，會產生極大的**工具調用摩擦與 Token 浪費**。

### 💡 解決方案：單一偏好編譯
我們開發了 `compile_preferences.py` 腳本（現整合為 `./pa pref compile`）。該工具會將 `llm_preferences/` 底下的所有設定檔以及戰略上下文，一鍵自動合併、去重並編譯為單一的總檔案 **`compiled_preferences.md`**。

化十次檔案讀取為單次讀取，徹底消滅了對話初始化的載入延遲，實現「單一真實來源 (Single Source of Truth)」。

---

## 📉 3. 戰術二：上下文預算控制——極簡本體論壓縮 (Ontology Card)

> *[意圖說明] 展示大長文的 Token 降維技術與審計數據。利用極低費率模型與嚴格輸出控制，實現 97% 成本削減與防截斷設計。*

當我們需要讓 AI 讀取或分析大於 10KB 的歷史文獻、複雜原始碼時，直接載入會迅速塞爆對話的 Context 預算。

### 💡 解決方案：本體論降維與預算審計
我們實作了 `compress_to_ontology.py` 壓縮工具。為了防止高昂的 API 費用，我們進行了實證審計測量：

| 測試樣本 | 輸入大小 | Input Tokens | Output Tokens | 提取三元組 | 資訊丟失率 (自評) | 壓縮比 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Small** | 0.7 KB | 501 | 363 | 4 行 | 10% | 72.46% |
| **Medium** | 4.6 KB | 1616 | 257 | 5 行 | 10% | 15.90% |
| **Large** | 15.2 KB | 4967 | 574 | 15 行 | 5% | 11.56% |

#### 📊 審計結論與關鍵技巧：
1.  **剛性觸發門檻 5KB**：小於 1KB 的輸入進行壓縮非常不劃算；而大於 5KB 的長文壓縮能省下 **84% 以上** 的 Token 負載。
2.  **分級預算收斂**：
    *   **微觀卡片 (Micro Card)**：輸入 5KB ~ 15KB，限制在 3~8 行三元組（S-P-O，主-謂-賓），字數控制在 **1KB 內**。
    *   **宏觀卡片 (Macro Card)**：輸入 >15KB，限制在 10~20 行三元組，字數控制在 **1.5KB 內**（實測 15 行三元組僅需 574 tokens，已能達到 95% 無損度）。
3.  **阻斷上限 1024**：因為 15KB 的輸入也僅消耗 574 tokens，故 API 的 `maxOutputTokens` 剛性限制在 1024，可防範 AI 產生冗餘幻想。
4.  **Thinking 模型的 maxOutputTokens 截斷坑**：實測發現，在 Gemini 3.5 系列等 Thinking 模型中，其思考鏈（Thinking Process）所消耗的 tokens 會計入 `maxOutputTokens` 的限制中！如果限制設得太低（例如 800），AI 剛在背後「想完」，還沒輸出半個字，就會被剛性截斷。因此在需要複雜 Reasoning 任務時，max 參數必須適度拉高（如 4000）。
5.  **模型降級省錢術**：壓縮與提取任務完全不需要推理能力。我們成功對接 **`gemini-2.5-flash-lite`**。此模型無任何思考 tokens 開銷，且費率僅為 3.5 Flash 的 **1/15** 左右，單次費用暴降 97%！

---

## 🛠️ 4. 戰術三：腳本工具庫的物理重組與 CLI 統一

> *[意圖說明] 物理重構混亂的腳本庫，以 Git 專屬指令保全代碼 Blame 歷史，並提供軟連結 Realpath Path Resolution 防禦的統一指令入口。*

專案開發久了，根目錄會堆積幾十個未分類的臨時腳本。為了讓 AI 在做事時有成體系、高複用性的工具可用，我們進行了「腳本庫大清掃」：

### 📂 A. 物理搬移與 Git Blame 歷史保全
我們物理掃描了既有的 15 個子目錄，並在 `scratch/` 撰寫了搬移腳本。為了避免直接使用 Python 的 `shutil.move` 導致 Git 檔案的 blame 提交歷史遺失，我們嚴格使用 **`git mv`** 進行物理遷移。
最後，執行 `./pa dev index`（`generate_index.py`）一鍵重建 **[scripts/README.md](file:///Users/wuulong/github/bmad-pa/scripts/README.md)**，將 55 個未分類腳本全部歸檔歸零。

### 📟 B. 統一子指令工具箱：`./pa` 與一鍵啟動
我們在根目錄軟連結了 `./pa` 命令行工具，並實作了 **Realpath Path Resolution 防禦**。不論你在哪裡以軟連結呼叫它，Python 都會先用 `os.path.realpath` 找到真實物理目錄，防範相對路徑解析 Bug。

現在，我們可以一鍵啟動任務：
```bash
./pa dev task-init -id T260714-HHH04 -t "任務名稱"
```
這會自動建立 TR 報告範本、在 `TASKS.md` 註冊 Ongoing 並掛載 TOC 連結，徹底消滅了每次起手任務時的手動配置摩擦。

---

## 🧭 5. 哈爸評註 (Navigator's Log)

> 以前寫程式是「人想好，丟給機器執行」；現在是「人制定法治，AI 在法治軌道上自指滑行」。
> 
> 這套 AI 協作防禦工程最迷人之處，不是我們寫出了多厲害的 AI 工具，而是我們用 Rules 重新定錨了「人機協作的心法」。AI 的推理能力再強，若是沒有環境的硬約束（如 conda 路徑）與流程的剛性鐵軌（如 TR-First 規則），它很快就會淪為一隻 ad-hoc 製造混亂的脫韁野馬。
> 
> 把「寫作」本身也作為 Rules 的自指執行，是我今天對人機對稱性協作最深刻的體會。

---

> **AI 協作聲明**：
> 本文由筆者提供原始個人偏好與 CLI 工具整合思路，由 AI 助手 Antigravity 整理架構並撰寫內文。結合了系統工程的規範與哈爸隨筆的坦率筆調，記錄 AI Pair Programming 的協作實踐。
