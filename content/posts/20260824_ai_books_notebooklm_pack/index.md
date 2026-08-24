---
title: "從「不會就叫 AI 寫本書教我」到 45 本大書：用 NotebookLM 降維回顧我的 AI 寫書學習之旅"
date: 2026-08-24T07:55:00+08:00
draft: false
categories:
  - "Personal AI Empowerment (個人 AI 賦能)"
  - "Productivity & KM (生產力與知識管理)"
  - "GenAI (生成式 AI)"
  - "Agentic AI (代理程式 AI)"
tags:
  - "NotebookLM"
  - "BGS"
  - "Python"
  - "Token節省"
cover:
  image: "cover.webp"
  alt: "NotebookLM 匯入 45 本 AI 專書清單截圖"
  relative: true
---

進入生成式 AI 時代後，我自己一直有一個簡單、直接卻極度高效的學習心法：**「只要遇到不會、陌生或想深入的領域，就叫 AI 幫我寫一整本書來教我！」**

從早期的 LLM 深度學習原理、Vibe Coding 實戰、Kubernetes 進階管理、法規資料庫檢閱、生物統計，一路到台灣水理地景、高山水文圖譜與開源實務指引……不知不覺間，我運用這套「寫書學習法」累積了大量結構化的 Markdown 專書資產。


然而，Antigravity NT 650 的周限制，讓我想把更多不需要 Antigravity 才能做的事，到別的地方做。

---

## 💡 痛點：為了省 Tokens，把專書送到 NotebookLM 檢閱

書還是到 notebooklm 看比較方便！


為了解決這個問題，我決定將所有的專書打包，匯入到 Google NotebookLM 中建立專屬的「個人圖書館」筆記本。NotebookLM 本身具備極強的長文本處理與零幻覺 Grounding 能力，而且**完全不消耗我們日常開發的 LLM API Tokens**！

只要把書打包好放進去，就能在 NotebookLM 的介面中進行跨書檢索、摘要、podcast 廣播生成與實時問答。

---

## 🛠️ 建立規範與工具：BGS v2.0 規格與一鍵打包 CLI

理想很豐滿，但現實很骨感——專案裡的專書有各式各樣的型態：有些是一整本幾萬字的單檔 Markdown (`📄 single_file_book`)，有些則是分成十幾篇章節資料夾的目錄型大書 (`📁 directory_book`)。如果沒有統一的規範，匯入 NotebookLM 後只會是一團混亂的章節碎片。

為了實現極致自動化，我動手做了兩件事：

### 1. 制定 BGS v2.0 專書治理規格 (Book Governance Spec)
* 於目錄型大書中導入 `00_toc.md` 剛性錨點與 YAML Frontmatter 宣告（包含 `book_spec_version: "2.0"`、`book_id` 與 `title`）。
* 原生支援單檔大書與目錄大書雙型態，實現零破壞性的專書資產盤點。

### 2. 開發一鍵打包 CLI (`./pa notebooklm pack-books`)
* **自動清理**：每次執行前自動完全清空舊輸出目錄 (`tmp/notebooklm/all_books_pack/`)，避免新舊檔案混雜。
* **智慧內容時間排序 (mtime Ascending)**：排除自動寫入 `00_toc.md` 的元資料干擾，嚴格計算各書「實質寫作章節 (`01_...md`)」的最晚修改時間，並以「舊到新」排序。這樣未改動的舊書順序永遠固定，新寫的書自然追加在尾端。
* **帶補零序號前綴 (`01_Book_...` ~ `45_Book_...`)**：為每個產出的單一全書 Markdown 檔加上補零序號，讓 NotebookLM 在 Sources 來源清單中能 100% 依序清晰排列。

```bash
# 終端機一鍵執行打包
./pa notebooklm pack-books
```

---

## 😲 簡單的驚喜：竟然已經累積了 45 本大書！

當自動化腳本執行完畢，我打開 [`tmp/notebooklm/all_books_pack/`](file:///Users/wuulong/github/bmad-pa/tmp/notebooklm/all_books_pack/) 資料夾、並將檔案整包上傳到 NotebookLM 時，看到 Sources 側邊欄那一排整整齊齊帶有序號的專書清單（如首圖），心頭突然震了一下。

**整整 45 本大書！**

從 `01_Book_覺醒公民行動指南...md`、`02_Book_民主社會的運作...md`，一路延伸到最近剛完成的 `44_Book_agro-db-in_tw-agro-db...md` 與 `45_Book_gov-db-in_tw-gov-db...md`（台灣政府開放資料通用基石圖鑑）。

這 45 本書，每一本都記錄了我這一段時間以來，從一個「不懂該領域的新手」，透過蘇格拉底式逼問、Intent-Driven 兩層大綱設計、到引導 AI 深度寫出萬字教案的認知擴展軌跡。

---

## 🎉 結語：開啟 NotebookLM 的回顧與檢閱新篇章

現在打包工作與自動化工具鏈已經完全就緒。這 45 本書在 NotebookLM 中安放妥當後，我隨時可以：
1. **零 Token 成本詢問**：跨領域提問，讓 NotebookLM 從 45 本專書中迅速精準抽取 Grounding 依據。
2. **自動生成 Audio Overview**：把幾本相關的 AI 專書變成 Podcast 雙人對談，開車或散步時用聽的來溫故知新。
3. **保持知識庫清潔與演進**：未來只要寫了新書，下一次執行 `./pa notebooklm pack-books`，新書就會自動帶上 `46_Book_...` 的序號出現在末尾。

從「不會就叫 AI 寫本書教我」的個體賦能起點，到「標準化規範 ➔ 一鍵打包 ➔ NotebookLM 檢閱」的自動化閉環，這正是個人 AI 知識工程最迷人的地方。

> **AI 協作聲明**：
> 本文紀錄之 BGS v2.0 專書治理規格、`./pa notebooklm pack-books` CLI 工具設計與文章草稿編撰，均由作者 (wuulong) 與 AI Pairing Agent (Antigravity) 共同設計、測試與對合完成。
