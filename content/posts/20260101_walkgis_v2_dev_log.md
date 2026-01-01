---
title: "WalkGIS V2：從「網站」進化為「地理資訊瀏覽器」"
date: 2026-01-01T09:10:00+08:00
draft: false
categories: ["Project (專案)"]
series: ["WalkGIS"]
tags: ["SQLite", "React", "Decentralized", "WebAssembly", "Data Sovereignty"]
summary: "首席架構師開發日誌：揭秘 V2 升級如何透過 DataSourceContext 實現從「內容網站」到「通用瀏覽器」的範式轉移，以及如何解決 WASM 重啟與跨域資源映射的技術挑戰。"
---

## —— 哈爸開發日誌：去中心化 GIS 的實現之路

在數位內容的世界裡，大部分的網站都是「封閉的城堡」：資料被鎖在特定的伺服器中，App 與內容緊密耦合。但在 WalkGIS V2 的升級中，我們完成了一次從「地圖網站」到「地圖瀏覽器」的範式轉移 (Paradigm Shift)。

這篇文章將揭開這套「去中心化地理資訊協議」背後的設計邏輯與技術亮點。

## 💡 那個「靈光乍現」的瞬間：App 即瀏覽器

V1 的 WalkGIS 是為了展示特定專案而存在的，所有的資料路徑都是寫死的。但在 V2 中，我們問了一個大膽的問題：「如果 App 只是外殼，而地理資料（SQLite）才是真正的內容呢？」

這就是 V2 核心架構 `DataSourceContext` 的誕生契機。

我們將整個應用的「真相來源 (Source of Truth)」從常數轉變為一個動態的上下文環境。這改變了應用的本質：

*   **V1 (網站)**：使用者造訪一個網址，閱讀我們準備好的資料。
*   **V2 (瀏覽器)**：使用者可以「掛載 (Mount)」任何符合規範的網址。你可以想像這是一個具備地圖能力的「地理網頁瀏覽器」，它能讀取任何地方的 `walkgis.db`。

這讓 WalkGIS 變成了一個通用的工具。任何人只要擁有一個 GitHub Pages 空間，並上傳自己的資料庫，就能立即擁有一個功能齊全、支援 AI 脈絡產出的 GIS 導覽介面。

## 🏛 「市場」設計：App 配置與資料內容的解耦

我們在系統中設計了兩個層次：

1.  **市場註冊中心 (Market Registry)**：一個中心化的 JSON 文件，像「應用商店」一樣推薦優質節點。
2.  **數據節點 (Data Node)**：完全去中心化的實體，存放於世界各地的 GitHub 儲存庫。

這種設計實現了 **「治理與自由」** 的平衡。我們維持一個高品質的推薦清單（Market），但保留了使用者輸入「自定義網址」的權利。這種結構吸引了研究者與社群愛好者自建節點，因為他們不需要寫任何一行程式碼，只需要管理自己的 `walkgis.db` 與 Markdown 文件。

## 🛠 三大技術亮點：挑戰與優雅的解決方案

### 1. WASM 虛擬化與環境隔離

在瀏覽器中運行 SQLite (sql.js) 是一件很重的事。為了在切換數據節點時確保絕對的「環境純淨」，我們採用了 **重啟式切換 (Reload-based Switching)**：

當使用者點擊「連線」新節點時，我們不只是更新變數，而是透過全域標記 `__WALKGIS_RELOADING__` 鎖定異步操作，隨後進行頁面重整。

這確保了重型 WASM 引擎每次都在最乾淨的內存環境下啟動，徹底避免了多節點切換時可能產生的內存溢出或索引衝突。

### 2. 跨網域資產的路徑映射 (Portable Assets)

當 App 放在 A 網址，資料放在 B 網址（例如 GitHub Pages），Markdown 內的相對路徑圖片會失效。

**技術亮點**：我們實作了一套 **動態路徑解析器**。不管是圖片標籤、封面圖還是 Markdown 內容，系統會自動辨識並將相對路徑重新映射至當前掛載的 `baseUrl`。這意味著你的內容在本地預覽與遠端掛載時，表現完全一致，具備極高的可移植性。

### 3. 優雅的上下文驅動架構 (Code Highlights)

這是 `DataSourceContext` 中處理節點切換的關鍵邏輯，展現了如何透過簡單的封裝實現複雜的節點同步：

```typescript
// DataSourceContext.tsx 核心邏輯
export const DataSourceProvider: React.FC = ({ children }) => {
  const setBaseUrl = (url: string) => {
    // 1. 確保 URL 格式標準化
    const formattedUrl = url.endsWith('/') ? url : `${url}/`;
    
    // 2. 設置全域標記，抑制重整瞬間的異步網路錯誤回報
    window.__WALKGIS_RELOADING__ = true;
    
    // 3. 存儲選擇，並強制刷新頁面以初始化全新的 SQLite WASM 實例
    localStorage.setItem('walkgis_current_source', formattedUrl);
    window.location.reload();
  };

  return (
    <DataSourceContext.Provider value={{ baseUrl, setBaseUrl }}>
      {children}
    </DataSourceContext.Provider>
  );
};
```

## 🌟 結語：邀請您成為節點的主人

WalkGIS V2 的願景是讓地理資訊不再被壟斷。如果你有老照片、文史調查資料或社區散步路線，你不需要學習資料庫架構或前端技術，只需要：

1.  下載我們的 **[Starter Template](https://wuulong.github.io/walkgis-template/)**。
2.  填入你的資料。
3.  部署到 GitHub Pages。

接著，全世界的 WalkGIS 使用者都能透過這台「瀏覽器」，看見你筆下的土地記憶。

讓地理資訊的分享，像發布部落格一樣簡單。

👉 **[立即探索 WalkGIS 市場](https://walkgis-544663807110.us-west1.run.app/)**

---
### 🤖 AI 協作宣告
*   **本文內容**: 由 WalkGIS 網站開發過程中的 AI 協作對話紀錄轉寫而成。
*   **技術實作**: 文中提及的 V2 架構升級程式碼與 Prompt Engineering，皆由人類架構師引導 Antigravity 與 Google AI Studio 共同完成。
