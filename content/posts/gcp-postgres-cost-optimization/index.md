---
title: "GCP 雲端省錢術：PostgreSQL 瘦身與架構優化實錄"
date: 2025-12-17T09:00:00+08:00
draft: false
tags: ["GCP", "PostgreSQL", "Docker", "Cost Optimization", "DevOps"]
categories: ["Technical", "Cloud"]
description: "如何將 GCP 上的 PostgreSQL 資料庫成本最佳化？紀錄從刪除閒置的 500GB 硬碟，到利用 Docker 容器化部署、設定權限分流，以及申請免費固定 IP 的完整過程。"
summary: "近期為了優化個人專案的雲端成本，我對 GCP 上的 PostgreSQL 資料庫進行了一次「大手術」。將原本掛載的 500GB 閒置硬碟移除，改用 Docker 部署在 10GB 的系統碟上，並配置了固定 IP 與防火牆。這篇文章紀錄了如何從每月數百元的硬碟費中解套，同時建立更安全、標準化的 DB 架構。"
top: false
---

最近在整理手邊的 Side Project 時，發現 GCP 的帳單上有個顯眼的項目：一顆 500GB 的 Persistent Disk。

仔細一查，這顆硬碟只為了跑一個資料量不到 200MB 的 PostgreSQL 資料庫。每個月光是這顆閒置硬碟就要花掉約 **$20 USD (約 NT$600)**，而實際上使用的空間連 0.1% 都不到。這對於個人專案來說，簡直是暴殄天物。

於是，我決定進行一次 **「雲端瘦身手術」**，目標是：**成本最小化、架構標準化**。

## 1. 斷捨離：砍掉重練

第一步最痛快，也最需要勇氣：**刪除那顆 500GB 的硬碟**。

在 GCP 中，硬碟 (Persistent Disk) 和運算實例 (VM Instance) 是分開計費的。即使你把 VM 關機了，掛在上面的硬碟還是會持續扣款。

確認資料都有備份 (`.sql`檔) 後，我執行了 detach 和 delete 指令。瞬間，每個月的固定支出就少了一大筆。

## 2. 移花接木：Docker 容器化部署

少了外部資料碟，資料要存哪？答案是 **VM 本身的系統碟 (Boot Disk)**。
一般的 `e2-small` 實例通常會配 10GB 的系統碟，扣掉 OS，剩下 6-7GB 對於一個 200MB 的資料庫來說綽綽有餘。

我選擇使用 **Docker** 來部署 PostgreSQL，好處是環境乾淨、升級容易，而且如果機器掛了，只要資料夾還在，Docker 一跑起來服務就回來了。

### 關鍵指令

這是經過去蕪存菁後的啟動指令，這裡有幾個細節值得紀錄：

```bash
# 1. 建立資料目錄 (使用絕對路徑以避免雷)
mkdir -p /home/wuulong/postgres_data
chmod 777 /home/wuulong/postgres_data  # 避免容器內的 Postgres 無權寫入

# 2. 啟動容器
docker run -d \
    --name lawdb \
    --restart always \
    -e POSTGRES_PASSWORD='YourStrongPassword' \
    -v /home/wuulong/postgres_data:/var/lib/postgresql/data \
    -p 5432:5432 \
    postgres:15-alpine
```

*   **`--restart always`**：這是關鍵。加上這個參數，即使 VM 重開機，Docker Daemon 啟動後也會自動把這個 DB 容器帶起來，達成類似 System Service 的效果。
*   **權限陷阱**：如果不將 Host 的資料夾權限設為 `777` (或正確設定 owner)，容器內的 Postgres (uid=999) 會因為 `Permission Denied` 而無限重啟。

## 3. 安全升級：帳號分流與連線字串的各種坑

以往為了方便，直接用 `postgres` 或 `root` 走天下。這次趁著重建，落實了權限分級的 Best Practice：

1.  **`admin_user` (Admin)**：應用程式用，擁有讀寫權限。
2.  **`read_only_user` (Reader)**：分析或只有查詢需求的服務用，只能 `SELECT`。

透過 `docker exec` 進入容器執行 SQL 來建立：

```sql
-- 建立唯讀使用者範例
CREATE USER read_only_user WITH PASSWORD 'SecurePassword123';
GRANT CONNECT ON DATABASE law_db TO read_only_user;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO read_only_user;
-- 這行最重要，確保未來新增的 Table 也能被讀取
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO read_only_user;
```

### Connection String 的「特殊符號」地雷

在設定密碼時，我學到了一個教訓：**不要在密碼裡用 `@` or `$` **。

PostgreSQL 的連線字串格式通常是：
`postgres://user:password@host:port/database`

如果你把密碼設成 `P@ssword`，解析器會把第一個 `@` 當成分隔符，導致連線失敗。雖然可以用 URL Encode 解決，但最簡單的方法還是：**密碼改用純英數混合，避開 URL 保留字**。

## 4. 網路優化：固定 IP 其實不用錢？

在 GCP 上，VM 重開機後，原本的 External IP (外部 IP) 通常會改變，這對設定連線字串很困擾。

很多人以為申請固定 IP (Static IP) 要錢，其實規則是這樣的：
*   **沒在用**的固定 IP：**要收錢** (約 $0.01/hr)。
*   **綁定在運行中 VM** 的固定 IP：**免費**！

既然我的 DB 伺服器是 7x24 小時運行的，申請一個固定 IP 綁上去，既方便又不會增加成本。

```bash
# 將目前的動態 IP 轉為靜態
gcloud compute addresses create my-static-ip \
    --addresses=xxx.xxx.xxx.xxx \
    --region=us-central1
```

### 防火牆管理

為了安全，不要直接對 `0.0.0.0/0` 開放所有 Port。我利用 **Network Tags** 來精準控制：
1.  幫 VM 貼上 `db-server` 的標籤。
2.  防火牆規則設定為只允許 `db-server` 標籤的機器通過 5432 Port。

這樣未來新增其他 VM 時，就不會意外暴露資料庫端口。

## 總結：花小錢辦大事

經過這番折騰，現在的架構是：
*   **運算**：e2-small (2 vCPU / 2GB RAM)。
*   **儲存**：10GB 系統碟 (放置 Docker Volume)。
*   **網路**：免費固定 IP。

每月的帳單從原本因為閒置硬碟而墊高的 $30+ USD，降回了純運算的 **$9 USD (台幣約 300 元)** 左右。

以每個月一杯星巴克的價格，擁有一台獨立 IP、Root 權限、且架構乾淨的 PostgreSQL 伺服器，這絕對是高 CP 值的選擇。

### AI 協作宣告 (AI Collaboration Disclosure)

> ![AI Generated](https://img.shields.io/badge/Content-AI%20Assisted-8A2BE2?style=flat-square&logo=google-gemini&logoColor=white) 
> ![Human Reviewed](https://img.shields.io/badge/Review-Human%20Verified-green?style=flat-square)
>
> **本文內容由 AI 協作生成**：
> 1.  **素材來源**：作者實際操作經驗與技術筆記。
> 2.  **AI 工具**：使用 Antigravity (Gemini) 協助指令執行、除錯與文章撰寫。
> 3.  **人工審核**：由哈爸本人確認觀點準確性並進行最終潤飾。
