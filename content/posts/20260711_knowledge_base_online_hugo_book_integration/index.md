---
title: "知識庫 (KB) 正式上線！整合 Hugo Book 雙主題並行架構與踩坑實錄"
date: 2026-07-11T08:30:00+08:00
draft: false
categories:
  - Agentic AI (代理程式 AI)
  - Automation & Workflows (自動化與工作流程)
  - Methodology (方法論)
  - Personal AI Empowerment (個人 AI 賦能)
  - Productivity & KM (生產力與知識管理)
  - Software Engineering (軟體工程)
series:
  - "哈爸筆記網站"
tags:
  - AI
  - Antigravity
  - GitHub
  - Methodology
  - Obsidian
  - Python
  - 哈爸筆記
  - 工作流程
  - 知識管理
  - 自動化
cover:
  image: "cover.webp"
  alt: "Knowledge Base interface displaying tree menu, categories, and code files"
  relative: true
---
我的靜態部落格「哈爸筆記」一直以來都是以「時間流（部落格隨筆）」的形式呈現。但隨著累積的技術筆記與程式碼片段越來越多，我發現需要一個「空間流（結構化知識庫）」來將特定的專題系統化整理。

<!--more-->

今天，我正式在部落格頂部選單加入了 **「知識庫 (KB)」** 標籤！首波上線的內容，就是關於 **Antigravity AI 代理人專案** 的系列實踐與 6 大實驗室腳本。

在這次的升級過程中，我採用了 **「PaperMod (主站) + Hugo Book (知識庫) 雙主題並行」** 的做法。這篇文章將詳細記錄這個架構的實作方式，以及我與 Antigravity 攜手解決的各項 Hugo 踩坑問題。

---

## 📐 雙主題並行的架構設計 (手段 A)

為了在不破壞主站外觀的前提下讓 `/kb/` 路徑套用書本樣式，我們利用了 Hugo 的多主題鏈機制：

1. **更新配置**：在 `hugo.yml` 中設定 `theme: ["PaperMod", "hugo-book"]`。由於 `PaperMod` 排在首位，所有的首頁與部落格文章預設依然會使用 PaperMod。
2. **局部布局覆寫**：建立 `layouts/kb/` 目錄，將 `hugo-book` 的 `baseof.html`、`single.html` 和 `list.html` 複製進去。當讀者存取 `/kb/` 時，Hugo 的查找優先權會優先套用 `layouts/kb/` 底下的版型，從而無縫切換到書本樣式。

---

## 🪵 導入過程中的「踩坑與修復」實錄

由於我本地使用的 Hugo 版本為較新的 `v0.152.2`，在編譯 `hugo-book` 時遇到了不少語法相容性的挑戰。以下是我們逐一排查並解決的記錄：

### 1. Hugo 最低版本宣告衝突
* **問題**：`hugo-book` 宣告 `min_version = "0.158.0"`，本機編譯時狂跳相容性警告。
* **修復**：修改 `themes/hugo-book/theme.toml` 中的 `min_version = "0.152.0"`。由於版本功能差異極小，此警告順利消除。

### 2. 廢棄屬性衝突（`.Name`, `.Locale`, `.Direction`）
* **問題**：Hugo 在新版中簡化了 `Language` 物件，移除了多個舊屬性，導致編譯時拋出以下錯誤：
  * `can't evaluate field Name in type *langs.Language`
  * `can't evaluate field Locale in type *langs.Language`
  * `can't evaluate field Direction in type *langs.Language`
* **修復**：寫了一個 Python 腳本，全域將範本中的廢棄屬性重構：
  * 將 `.Site.Language.Name` 替換為標準的 `.Site.Language.Lang`（如 `zh-tw`）。
  * 移除 `.Locale` 的備用判斷，直接取 `.Language.Lang`。
  * 將針對中文排版恆為 ltr 的 `dir="{{ default "ltr" .Language.Direction }}"` 簡化為靜態的 `dir="ltr"`。

### 3. Go 範本傳參時的型態解析 Bug (hugo.Sites)
* **問題**：在 `home.html` 中，`hugo.Sites` 傳入 `cond` 函數時，會因為型態轉換失敗而拋出錯誤：`can't evaluate field Sites in type interface {}`。
* **修復**：這是 Go template 的底層解析限制。我們將 `home.html` 簡化為直接回傳 `{{ return .Site.Home.RelPermalink }}`，避開了在 `cond` 函數中傳遞全域物件的 Bug。同時，保留了 `languages.html` 與 `sw.js` 中直接使用 `{{ range hugo.Sites }}` 的寫法，使其正常運作。

### 4. 預設 BookSection 目錄衝突
* **問題**：Hugo Book 預設會去搜尋 `content/docs/`，但我的目錄是 `content/kb/`，編譯時報錯 `Section 'docs' not found`。
* **修復**：在 `hugo.yml` 中新增全域參數，指定知識庫根目錄：
  ```yaml
  params:
    BookSection: kb
  ```

---

## 🤖 Antigravity 實踐專案：相對路徑與動態連結的優雅解耦

在知識庫的 [Antigravity 實踐](file:///Users/wuulong/github/bmad-pa/events/notes/wuulong-notes-blog/content/kb/antigravity-practice/) 目錄下，我放了許多實作 Python 腳本（例如 `Lab1_thoughts_stream.py` 等）。

原本我是將連結寫死為 GitHub 上的絕對路徑。但這樣會帶來一個問題：**本地離線編輯（如用 Obsidian 閱讀）與本地預覽時，連結就無法點擊開啟本地檔案。**

為此，我們設計了一個非常優雅的 **Render Hook**：

1. **Markdown 寫法**：全部使用乾淨的本地相對路徑：
   ```markdown
   [Lab1 思考流模擬](./Lab1_thoughts_stream.py)
   ```
2. **Render Hook 攔截重寫**：我們在 `layouts/_markup/render-link.html` 寫入以下邏輯：
   ```html
   {{- $destination := .Destination -}}
   {{- if strings.HasSuffix $destination ".py" -}}
     {{- $githubRepo := default "https://github.com/wuulong/wuulong-notes-blog" .Page.Site.Params.githubRepo -}}
     {{- $branch := default "main" .Page.Site.Params.githubBranch -}}
     {{- $destination = printf "%s/blob/%s/content/%s%s" $githubRepo $branch .Page.File.Dir (strings.TrimPrefix "./" $destination) -}}
   {{- end -}}
   <a href="{{ $destination | safeURL }}">{{ .Text | safeHTML }}</a>
   ```

### 🏆 效果：
* **在地端 (Obsidian / VS Code)**：它是一個純粹的相對連結，Ctrl+點擊能直接在編輯器開啟本地的 `.py` 腳本。
* **在雲端 (GitHub 原始碼樹)**：同樣是相對連結，點擊能直接跳轉檢視。
* **在網站上 (網頁瀏覽)**：經由 Hugo 編譯時，連結會**自動重寫**為 GitHub 的 blob 網址，點擊會帶讀者前往 GitHub 閱讀具備語法高亮的程式碼，再也不會出現網頁端 404 錯誤！

這次的升級不僅讓知識管理有了更好的空間結構，也透過與 Antigravity 代理人的高度協作，實現了工程上的「精準落地與優雅解耦」！歡迎點擊上方選單進入我的 **「知識庫」** 參觀！
