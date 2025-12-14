# 哈爸筆記 (Wuulong Notes Blog)

這是一個基於 [Hugo](https://gohugo.io/) 和 [PaperMod](https://github.com/adityatelange/hugo-PaperMod) 主題構建的個人筆記網站。

## 快速開始

### 1. 安裝 Hugo

請參考 [Hugo 官方安裝指南](https://gohugo.io/installation/) 安裝 Hugo (建議安裝 `extended` 版本)。

### 2. 啟動本地伺服器

在專案根目錄執行以下指令：

```bash
# 啟動伺服器並包含草稿內容 (-D)
hugo server -D
```

啟動後，請在瀏覽器開啟 [http://localhost:1313/](http://localhost:1313/) 檢視網站。

## 內容管理

### 建立新文章

```bash
hugo new posts/your-post-name.md
```

### 資料夾結構

- `content/posts/`: 主要部落格文章
- `content/series/`: 系列文章索引
- `content/planning/`: 規劃與筆記
- `hugo.yml`: 網站主要設定檔

## 設定說明

網站設定位於 `hugo.yml`。若要修改網站標題、作者或其他參數，請編輯此檔案。
