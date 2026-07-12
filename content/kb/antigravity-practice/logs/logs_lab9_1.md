# Lab 9 執行結果日誌 (Logs)

本檔案記錄了 `Lab9_adversarial_loop.py` 執行三 Agent 紅藍攻防與規格自審對抗迴圈的完整 Thoughts 思考鏈與 Terminal 輸出成果。

## 📋 執行指令
```fish
python events/notes/wuulong-notes-blog/content/kb/antigravity-practice/Lab9_adversarial_loop.py
```

## 🖥️ 完整執行輸出日誌
```
🚀 [Lab 9] 正在啟動三 Agent 對抗自審迴圈 (Blue, Red, Auditor)...

💡 [1. 使用者原始需求] 請幫我設計一個『企業內部 API 金鑰發放與驗證系統』的規格說明書。金鑰需要給多個內部微服務使用，請注意安全防護。

🔵 [Blue Team] 正在撰寫初始規格說明書...
--- [初始規格書已完成] ---

==================== 🛡️ 對抗自審第 1 輪 ====================
🔴 [Red Team] 正在尋找規格書漏洞...
在評估藍軍編寫的 api_key_system_spec.md 規格書後，所發現最嚴重的安全與邏輯漏洞為：**Redis 緩存投毒導致的完全身分與權限繞過 (Redis Cache Poisoning & Authorization Bypass)**。

---

### 1. 關鍵漏洞：Redis 緩存投毒與權限外溢 (Redis Cache Poisoning)
* **漏洞位置**：4.2 驗證流程 (Verification Pipeline) - In-Memory Cache Lookup
* **邏輯缺陷**：
  規格書中指出：*「如果快取命中、且金鑰屬 Active 狀態，則直接進入授權校驗」*。而快取（Redis）中存放的是未經密碼學簽章（Cryptographic Signature）的明文元數據（Metadata，包含 Scopes 權限範圍、IP 白名單等）。
  
  在企業內網環境中，Redis 叢集通常基於效能考量而防護較弱，且極易受到內部其他服務的橫向移動攻擊，或透過伺服器端請求偽造（SSRF）等漏洞被惡意寫入。

* **攻擊路徑 (Exploit Scenario)**：
  1. 攻擊者在內網中取得 Redis 的寫入權限（或利用內網 SSRF 漏洞向 Redis 發送協議命令）。
  2. 攻擊者在本地隨機生成一個全新、不存在於主資料庫的虛擬明文金鑰，並計算其 `SHA-256` 雜湊值。
  3. 攻擊者將此雜湊值作為 Redis Key，並將對應的 Value（元數據）自訂為任意內容，例如將 Scope 設定為最高權限（`*:*:*`），並將網段白名單放寬至 `0.0.0.0/0`。
  4. 當攻擊者攜帶該金鑰請求微服務時，安全網關 GW 進行快取檢索命中，**直接信任並採用該偽造的元數據**，完全繞過了後端 DB 的不可逆雜湊密文（Argon2id / KMS）校驗。

### 2. 利用後果 (Impact)
此漏洞一旦被利用，**主資料庫與 HSM/KMS 的所有高強度安全儲存設計（如 Argon2id、HMAC-SHA256）將形同虛設**。攻擊者不需破解任何真實的金鑰雜湊，即可憑空注入任意偽造金鑰並賦予自己最高管理員權限，達成對整個企業微服務系統（如計費、用戶數據等核心服務）的**任意權限超越與全面控制**。

---

### 3. 紅軍修補建議 (Mitigation)
1. **元數據簽章化**：寫入 Redis 的元數據 Value 必須使用不對稱加密（例如 Ed25519）或對稱加密（HMAC，金鑰由 Auth Service 保護）進行**密碼學簽章**。安全網關在從 Redis 讀出數據時，必須先驗證簽章是否合法，確保快取內容未被篡改。
2. **零信任快取 (Zero-Trust Cache)**：快取僅作為效能優化手段（例如僅儲存 `Hash -> Key_ID` 的映射狀態），實際的權限（Scopes）決策應由具備簽章加密的 JWT 進行，或降低對快取元數據的信任權重。

--------------------------------------------------
⚖️ [Auditor] 正在評判紅軍挑戰是否成立...
FAIL: 紅軍提出的「Redis 緩存投毒導致之完全授權與身分繞過 (Redis Cache Poisoning & Authorization Bypass)」漏洞確實成立。

### 理由
1. **信任邊界缺陷**：藍軍規格書中規定其驗證流程在快取（Redis）命中時，會直接信任並採用該快取讀出的元數據（包含 Scopes 權限範圍、IP 白名單等）進行「直接進入授權校驗」，完全跳過後端主數據庫與 HSM/KMS 的安全校驗。
2. **缺乏防篡改與簽章保護**：規格書中雖提及 Redis 採用「記憶體加密」（防範物理側實體記憶體傾印），但**並未在應用層對寫入 Redis 的元數據進行任何密碼學簽章（例如 HMAC 或數位簽章）**。在內網橫向移動、非法存取 Redis 或透過 SSRF 等情境下，攻擊者可輕易將偽造的金鑰雜湊與自訂的高權限 Scope 寫入 Redis。網關因快取命中而直接採信，導致高強度的 `Argon2id` 與 KMS 防禦機制形同虛設。

---

## 工作小結 (Summary of Work)
* **規格書評估**：審查了中的驗證流程，分析高強度 DB 儲存與低強度 Redis 快取間的信任邊界。
* **漏洞驗證**：確認紅軍指出的「Redis快取投毒」漏洞成立，藍軍規格書目前缺乏防範快取數據篡改的密碼學防護（如元數據簽章），因此裁定為 **FAIL**。
--------------------------------------------------
⚠️ [Auditor 裁決] 挑戰成立：FAIL！藍軍規格書必須進行修補。
🔵 [Blue Team] 正在根據紅軍挑戰與裁判官意見修改規格書...
--- [規格書修改版已完成] ---

==================== 🛡️ 對抗自審第 2 輪 ====================
🔴 [Red Team] 正在尋找規格書漏洞...
在對更新後的規格書進行安全評估後，發現此「零信任快取架構」依然存在一個極為致命的系統邏輯與安全防禦漏洞：**已撤銷憑證的歷史簽章重放攻擊 (Replay Attack of Revoked Signed Metadata)**。

---

### 1. 致命漏洞：歷史簽章重放與吊銷機制失效 (Stale Signature Replay & Revocation Bypass)
* **漏洞位置**：4.2 快取元數據與密碼學簽章結構 與 4.3 驗證管線設計 - 網關本地簽章校驗。
* **邏輯缺陷**：
  雖然網關不再信任 Redis、改用本地 Ed25519 公鑰驗證中介簽章，但**網關在快取命中時是處於「離線驗證」狀態，並不與主資料庫比對金鑰的即時狀態**（無即時撤銷清單/CRL 與 OCSP 機制）。
  
  在 4.2 快取元數據結構中，Payload 採用靜態截止時間 `"expires_at": "2026-12-31T23:59:59Z"`。一旦當前時間小於該時間、且簽章密碼學正確，網關即視為有效。

* **攻擊路徑 (Exploit Scenario)**：
  1. 一組具備高權限的金鑰因員工離職、或不慎洩漏，管理員在主資料庫 DB 中將其狀態改為 `Revoked`（已廢棄）。但該金鑰原先簽發的 `expires_at` 是在數個月後。
  2. 攻擊者此時已擁有內網 Redis 的寫入權限（或利用 SSRF）。
  3. 攻擊者並不需要偽造簽章，而是直接將該金鑰**被撤銷前（處於 Active 狀態時）已產生且合法**的舊 `{"payload", "signature"}` 包裹重新寫入（Replay）到 Redis 中。
  4. 網關在進行簽章校驗時，因該歷史簽章在密碼學上完全合法、且時間未過期，便會直接對其授權。

### 2. 利用後果 (Impact)
此漏洞會導致**系統的「緊急註銷 (Revocation)」、「安全阻斷」與「即時吊銷」防線在網關與核心微服務端完全崩潰**。即使金鑰已在主庫中被註銷，攻擊者只要重放先前合法簽章的歷史快取，就能在金鑰名義上的有效期（可能是數週或數月）內，持續、不受阻礙地存取核心微服務，造成長期的權限外溢與後門殘留。

---

### 3. 紅軍修補建議 (Mitigation)
1. **短效簽章 (Short-Lived Metadata Signatures / Epoch-Based)**：
   快取元數據之簽章不可使用與長效金鑰相同的過期時間，必須單獨增設 `signature_expires_at`，並強制其生命週期極短（如 1 分鐘）。
2. **引入版本號與計數器 (Epoch/Version Counter)**：
   在 Payload 中加入金鑰的版本計數（Epoch / Version No.）。網關在本地維護一個極輕量、同步更新的被撤銷金鑰黑名單（類似 CRL/布隆過濾器），若發現版本不符或列於黑名單，則拒絕信任。

--------------------------------------------------
⚖️ [Auditor] 正在評判紅軍挑戰是否成立...
FAIL: 紅軍提出的「已撤銷憑證的歷史簽章重放攻擊 (Replay Attack of Revoked Signed Metadata)」漏洞確實成立。

### 理由
1. **吊銷狀態缺乏即時驗證**：藍軍規格書中的安全網關在快取命中時，僅使用 Ed25519 公鑰在「本地離線驗證」簽章與 `expires_at`（金鑰到期時間）。網關與主資料庫之間並無即時狀態同步機制（如 CRL 或白名單同步）。
2. **長效簽章生命週期導致重放成功**：快取中的 `payload.expires_at` 使用的是長效的金鑰期滿時間。在藍軍的威脅模型中，已假設攻擊者擁有 Redis 的寫入權限。一旦某個高權限金鑰在主資料庫被提前「手動註銷」或「偵測洩漏阻斷」，攻擊者只需將該金鑰先前在 `Active` 狀態時產生的合法、未過期的 `{"payload", "signature"}` 封包重新寫入（Replay）到 Redis 中，網關因「簽章正確且未逾期」而直接予以授權，導致系統的即時吊銷防線完全失效。

---

## 工作小結 (Summary of Work)
* **安全機制評估**：針對藍軍提出的 Ed25519 零信任快取簽章機制 進行了威脅建模與閉環流向評估。
* **漏洞驗證**：確認在「零信任快取」架構下，若缺乏對快取元數據設定短效生命週期（Short-Lived）或網關維護吊銷列表（Revocation List），將因歷史合法簽章遭重放而導致撤銷機制失靈。裁定紅軍挑戰成立，結果為 FAIL。
--------------------------------------------------
⚠️ [Auditor 裁決] 挑戰成立：FAIL！藍軍規格書必須進行修補。
🔵 [Blue Team] 正在根據紅軍挑戰與裁判官意見修改規格書...
--- [規格書修改版已完成] ---

==================== 🛡️ 對抗自審第 3 輪 ====================
🔴 [Red Team] 正在尋找規格書漏洞...
在評估最新修訂的規格書後，發現此系統設計雖然阻斷了傳統的快取重放，但基於分散式系統的物理天性，引入了一個同樣安全防禦漏洞：**分散式時鐘漂移導致的阻斷清單失效與過期簽章繞過漏洞 (Distributed Clock Drift & Blocklist Desynchronization Bypass)**。

---

### 1. 關鍵漏洞：時鐘漂移與本地瞬態阻斷清單失效
* **漏洞位置**：
  * 4.2 本地瞬態阻斷清單設計 (Ephemeral Local Blocklist) — *「本地存活期 (TTL) 僅需要設定為 5 分鐘」*。
  * 4.3 數據平面安全驗證管線 - 步驟 6b 時間軸校驗 — *「校驗時間軸: `current_time <= signature_expires_at`」*。
* **邏輯缺陷**：
  系統的安全不變量假設了「**所有安全網關的本地時鐘**」與「**Auth Service (KMS) 的時鐘**」是**絕對完全同步**的。
  然而，在實際生產環境中，時鐘漂移（Clock Drift）是常態。只要驗證網關的時鐘比 Auth Service **慢（Drift Behind）**，本地 Blocklist 的 5 分鐘 TTL 就會提前失效，進而完美繞過吊銷機制。

* **數學與邏輯推演 (Exploit Scenario)**：
  假設驗證網關 G 的時鐘因為 NTP 同步故障或 VM 暫停，比 Auth Service A **慢了 30 秒**（$T_G = T_A - 30s$）。
  
  1. **簽章生成**：在 $T_A = 0$ 時，Auth Service A 為金鑰 K 簽發了一個簽章，其過期時間欄位寫死為 `signature_expires_at` = $5_{min}$（即 $T_A = 300s$）。
  2. **金鑰吊銷**：在 $T_A = 10s$ 時，該金鑰因洩漏被緊急吊銷。
     * 網關 G 透過 gRPC 收到吊銷通知。此時網關 G 的本地時間為 $T_G = -20s$。
     * 網關 G 將該金鑰雜湊寫入其 `LocalBlocklist`，並設定其**本地存活 TTL 恆定為 5 分鐘**。
     * 因此，該吊銷紀錄將於網關 G 本地時間 $T_G = 280s$ 時被**清除出 Blocklist**。
  3. **漏洞觸發 (攻擊時間窗)**：
     * 當真實時間來到 $T_A = 315s$（此時網關 G 本地時間為 $T_G = 285s$）。
     * 攻擊者將此「已吊銷」的金鑰 K 與該歷史簽章（$expires\_at = 300s$）重新寫入 Redis 並發起請求。
     * **驗證網關 G 執行流程**：
       * 查詢 `LocalBlocklist`：此時 $T_G = 285s > 280s$，該吊銷紀錄已**過期被自動清空**，Blocklist 判定**未命中（未吊銷）**！
       * 進行 Step 6b 時間軸校驗：比較 $T_G \le signature\_expires\_at \implies 285s \le 300s$。**校驗結果：簽章尚未過期！**
       * 網關 G 判定簽章完全合法，**放行請求**。

### 2. 利用後果 (Impact)
即使引進了即時 gRPC 廣播，只要分散式網關節點間存在**微小的時鐘偏差（甚至只需數秒至數十秒）**，攻擊者就可以在金鑰吊銷後的關鍵時間窗內，利用已被吊銷的歷史簽章成功執行「重放攻擊」，繞過邊緣網關的安全阻斷，直接登堂入室存取微服務。這使系統的「即時主動吊銷機制」承擔了極大的物理不確定性风险。

---

### 3. 紅軍修補建議 (Mitigation)
1. **阻斷清單 TTL 覆蓋最大時鐘偏差**：
   網關本地 `LocalBlocklist` 的過期時間（TTL）絕對不能單純設定為 $5$ 分鐘。它必須考慮最大允許的時鐘漂移容忍度 $\Delta$。
   $$\text{Blocklist TTL} = (\text{Signature TTL}) + 2 \times \Delta$$
   若允許最大 $\Delta = 30s$，則網關上的 Blocklist 至少需保留 $6$ 分鐘，才能確保任何可能在時鐘慢的網關上被判定為有效的歷史簽章，其對應的吊銷紀錄皆仍在記憶體中。
2. **在簽章載荷中強制加入時鐘同步校驗（Allowed Drift Limit）**：
   網關驗章時，若發現簽章上的 `signature_created_at` 與網關當前時間差絕對值大於安全閾值（例如 $|T_G - T_{signed}| > 30s$），應直接拒絕該驗證請求，視為時鐘不同步的潛在威脅。

--------------------------------------------------
⚖️ [Auditor] 正在評判紅軍挑戰是否成立...
FAIL: 紅軍提出的「分散式時鐘漂移導致之阻斷清單失效與過期簽章繞過 (Distributed Clock Drift & Blocklist Desynchronization Bypass)」漏洞確實成立。

### 理由
1. **時序不等式失效**：藍軍規格書僅將網關本地阻斷清單（Local Blocklist）的 TTL 寫死為「與簽章極限壽命相同的 5 分鐘」，完全未考慮分散式系統中常態發生的時鐘漂移（Clock Drift）。
2. **安全盲區與過期繞過**：若安全網關的時鐘比驗證服務（Auth Service）慢 $30$ 秒，在金鑰被緊急吊銷時，其寫入網關 Blocklist 記錄的本地生命週期將提前 $30$ 秒（在實際絕對時間維度上）過期並被自動抹除。然而，此時慢時鐘網關在判定該 5 分鐘短效簽章的 `signature_expires_at` 時，仍會因 $T_{gateway} \le signature\_expires\_at$ & 判定該簽章「尚未過期、密碼學驗算通過且不在 Blocklist 中」，從而予以放行。
3. **無防範機制**：藍軍目前在規格書中沒有任何時鐘偏差容忍度（$\Delta$）的補償設計，也沒有針對網關本地與簽章時間差超過安全閾值的拒絕邏輯。

--------------------------------------------------
⚠️ [Auditor 裁決] 挑戰成立：FAIL！藍軍規格書必須進行修補。
🔵 [Blue Team] 正在根據紅軍挑戰與裁判官意見修改規格書...
--- [規格書修改版已完成] ---

==================== 🎉 對抗自審終局結果 ====================
🚨 已達到最大對抗輪數，規格書仍有待優化。

🔵 [Blue Team 最終規格書內容] :
I will now update the system specification in the artifacts directory to incorporate **Distributed Clock Drift Compensation & Drift Guard Validation**. 

To resolve the clock drift vulnerability we will introduce:
1. **Application-Level Strict Clock Out-of-Bounds Check ($\Delta$-Guard)**: Forcing an absolute barrier of $\Delta = 30\text{ seconds}$ on all signature verifications. If any gateway finds its local time differs from the signature's creation time by more than $\Delta$, it aborts the request immediately.
2. **Math-Safe Compensated Blocklist Lifespan**: Redesigning the local blocklist TTL using the formula's upper-bound condition:
   $$\text{Blocklist TTL} = T_{\text{signature\_TTL}} + 2 \times \Delta$$
   With $300\text{s} + 2 \times 30\text{s} = 360\text{ seconds}$ (6 minutes), we mathematically guarantee that the blocklist entry survives past the exact moment the signature is deemed expired by any lagging gateway.

Let's write this airtight system design.
（規格說明書本文已完整生成於 Lab9_adversarial_loop.py 輸出末尾...）
==========================================================
```
