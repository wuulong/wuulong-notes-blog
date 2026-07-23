# 🚀 哈爸筆記首頁強化「知識庫 (KB)」入口與視覺定位改善方案

本方案旨在解決目前「哈爸筆記」首頁僅偏向傳統時間序部落格（Posts），導致核心知識庫（Knowledge Base, KB）入口與個人品牌資產強調不足的問題。

---

## 🔍 現況問題診斷 (Pain Point Analysis)

1. **主導覽選單權重過低**：
   `hugo.yml` 中 `kb` 的選單權重目前設為 `weight: 35`，排在搜尋、分類、流域、標籤與 Posts 之後，處於導覽列的最右側邊緣。
2. **首頁 `content/_index.md` 缺乏實質導覽內容**：
   目前的 `content/_index.md` 僅有基礎 Frontmatter，首頁直接呈現時間流文章清單，沒有「知識庫門戶 (KB Hub / Portal)」的視覺樞紐。
3. **核心 KB 模組未建立視覺卡片**：
   包含「哈爸自介」、「哈爸自學心法」、「LASS 時代報導」、「GitHub 公開專案」、「演講授課歷程」等高價值資產，未在首頁提供直覺的按鈕或卡片區塊。
4. **單篇文章缺乏回到 KB 的雙向連結**：
   外部讀者透過 Google 搜尋進入單篇 Post 時，缺乏顯眼的引導區塊跳轉至 KB 知識庫首頁。

---

## 💡 四大優化建議與實作規劃 (Four-Step Implementation Plan)

### 策略 1：重構首頁門戶 `content/_index.md` (置頂 KB 導航地圖)

將 `content/_index.md` 從空白頁面改造成兼具「個人品牌介紹」與「知識庫核心樞紐」的導覽門戶。在最新文章清單上方，注入高亮卡片區塊：

```markdown
# 🧠 哈爸知識庫與個人品牌門戶

歡迎來到哈爸筆記！這裡是我在 AI 時代人機協作、開源社群、流域探索與創客顧問的知識庫基地。

> 📢 **最新公告 (News)**：[👉 啟動「哈爸顧問與演講服務」！陪伴企業與個人在 Agentic AI 時代精準落地](https://wuulong.github.io/wuulong-notes-blog/posts/20260715_haba_consulting_and_speaking_services_launch/)

---

## 🗺️ 知識庫 (KB) 精選入口

| 📘 專題名稱 | 🎯 核心亮點與導覽 | 🔗 快速跳轉 |
| :--- | :--- | :--- |
| **哈爸自介** | 整合社群開源、企業創新、公部門與科技顧問四大維度經歷 | [👉 瀏覽自介](./kb/self-intro/) |
| **哈爸自學心法** | 痛點引擎、雙核共生、輸出驅動與主權治理四大自學支柱 | [👉 閱讀心法](./kb/hapa-hacker-learning/) |
| **網路報導與公開資料** | 主流媒體專訪、天下雜誌水治理、INSIDE AI 自學革命報導 | [👉 檢視報導](./kb/self-intro/media-coverage/) |
| **LASS 時代媒體報導** | 2015-2021 年 LASS 公民科技與 2021 總統盃黑客松獲獎文獻 | [👉 歷史檔案](./kb/self-intro/lass-media/) |
| **GitHub 公開專案** | 38+ 個開源專案與 GIS、WalkGIS、ATAK 工具庫索引 | [👉 專案清單](./kb/github-repos/) |
| **演講與授課歷程** | 78+ 場公開演講、企業培訓與工作坊紀錄 | [👉 演講紀錄](./kb/talks/) |

---

## 📝 最新文章與筆記隨筆 (Recent Posts)
```

---

### 策略 2：調整 `hugo.yml` 選單權重 (Highlight Menu Entry)

調整 `hugo.yml` 中的選單順序，將 `kb` 的權重提升至核心位置，並加入顯眼的 Emoji 圖示：

```yaml
menu:
  main:
    - identifier: search
      name: "🔍 Search"
      url: /search/
      weight: 5
    - identifier: kb
      name: "🧠 知識庫 (KB)"
      url: /kb/
      weight: 6                      # 👈 提升至搜尋旁的核心第二位
    - identifier: categories
      name: "📁 Categories"
      url: /categories/
      weight: 10
    - identifier: series
      name: "📚 Series"
      url: /series/
      weight: 15
    - identifier: posts
      name: "📝 Posts"
      url: /posts/
      weight: 30
```

---

### 策略 3：啟用 PaperMod 首頁 `ProfileMode` 或 `HomeInfoParams`

若要打造現代創客/顧問個人品牌的極致視覺，可啟用 PaperMod 內建的 Profile 模式或置頂告示：

```yaml
params:
  profileMode:
    enabled: true
    title: "哈爸 (許武龍) 知識庫"
    subtitle: "LASS 創辦人 ｜ TAIDE 創始 PM ｜ 2021 總統盃黑客松卓越團隊領隊 ｜ 創客 AI 轉型顧問"
    imageUrl: "/kb/self-intro/cover.jpg"
    imageWidth: 200
    imageHeight: 200
    buttons:
      - name: "🧠 進入知識庫 (KB)"
        url: "/kb/"
      - name: "💡 哈爸自學心法"
        url: "/kb/hapa-hacker-learning/"
      - name: "👨‍💻 瀏覽個人自介"
        url: "/kb/self-intro/"
```

---

### 策略 4：單篇文章底部注入 KB 延伸引導頁腳 (Footer Callout)

修改全站 Layout 或利用現有 `planning.md` / Partial，在所有單篇 Blog Post 的底部自動顯示：

```markdown
---
> 💡 **探索更多哈爸知識庫**：
> 想了解更多 AI 人機協作方法論、開源專案與創客顧問服務？
> 歡迎造訪 [🧠 哈爸知識庫 (KB Main Hub)](/kb/) 或檢視 [👨‍💻 哈爸個人自介與媒體報導](/kb/self-intro/)。
```

---

## 🎯 預期效益 (Expected Benefits)

1. **訪客點擊率大幅提升**：第一眼即可直擊「哈爸自介」與「自學心法」，減少在時間流文章中盲目尋找的摩擦。
2. **個人品牌與顧問業務落地**：置頂最新公告與顧問服務連結，提高商務諮詢與演講邀約的轉化率。
3. **知識架構清晰化**：區隔「時間序動態隨筆 (Posts)」與「結構化知識資產 (KB)」，建立雙軌式內容體驗。

---

> **下一步行動**：若您認可此規劃，我可以立即為您更新 `hugo.yml` 與重構 `content/_index.md` 門戶頁面！
