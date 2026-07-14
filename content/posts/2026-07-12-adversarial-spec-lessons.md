---
title: "Agent 時代的軟體設計變革：對抗式規格生成與 Token 刺客防禦實戰"
date: 2026-07-12T07:55:00+08:00
categories:
  - "Agentic AI (代理程式 AI)"
  - "System Engineering (系統工程)"
  - "Methodology (方法論)"
series:
  - "個人AI賦能方法論"
tags:
  - "Google Antigravity"
  - "Agentic Engineering"
  - "AgentOps"
  - "Token Optimization"
cover:
  image: "assets/images/adversarial_spec_cover.webp"
  alt: "紅藍軍規格對抗與心智除錯概念圖"
  relative: false
---

在 AI Agent 時代，我們發現傳統寫代碼 (Code) 的工法正被「定義 Goal、推理迴圈 (Loop) 與結束條件 (Exit Conditions)」所徹底顛覆。

在學習 Google Antigravity SDK 時，我慢慢體會到新的開發概念與傳統寫 Code 的根本性不同。當我們要建構一個新的 Agent 軟體或平台時，到底該如何提供精確的 Initial Prompt 與系統規格？這篇文章就來聊聊我這陣子在個人環境下，利用 **「對抗式規格生成」** 進行系統工程開發，以及如何死守錢包、擊退 **「Token 刺客」** 的第一手踩坑與自癒實戰。

---

## 🧐 為什麼我們需要「對抗式規格生成」？

傳統寫軟體是人類想好邏輯後硬寫代碼；但在 Agentic 的時代，大模型是根據我們給予的任務目標進行自主推理。這就產生了一個巨大的挑戰：**人類大腦並不擅長窮舉所有的邊界條件與安全漏洞**。

如果我們的初始 Goal 寫得太模糊，Agent 在執行時就容易踩到「天災退費算法漏洞」、「併發狀態鎖死」或「Prompt 注入繞過」等紅線。

既然 AI 最擅長挑刺，我們為什麼不直接讓 AI 互相攻防來幫我們淬煉規格？這就是 **「對抗式規格生成 (Adversarial Specification)」** 的由來：

*   **藍軍 (Spec Writer)**：負責根據初始想法，起草第一版功能規格書 (`spec_functional.md`)。
*   **紅軍 (Red Teamer)**：扮演刁鑽奧客與故障模擬器，死命尋找規格書中的 Edge Cases 與安全漏洞進行挑戰。
*   **裁判官 (Judge)**：中立審計。挑戰成立就強制藍軍修改，直到紅軍再也找不出漏洞，達成 **Verdict Lock (判決鎖定)**。

這個自動化對決聽起來非常完美，對吧？但當我興奮地在本地背景跑起對決腳本時，卻迎面撞上了一個巨大的坑。

---

## 🚨 恐怖的「Token 刺客」是怎麼產生的？

在執行對決腳本 `run_spec_duel.py` 時，我發現 Token 費用與 API 延遲以一種極其誇張的曲線暴漲，進程甚至幾度卡死。

經過深入底層追查，我發現了 `google-antigravity` SDK 內部的運作真相：

> **當同一個 `Agent` 實體多次呼叫 `chat()` 時，SDK 預設會自動持久化並累積對話歷史 (Session History)。**

這在一般的對話聊天中是標配，但在「紅藍對抗迴圈」中卻是致命的。
想像一下：
1. 藍軍起草了 1 萬字的規格書。
2. 紅軍針對這 1 萬字提出挑戰。
3. 裁判官進行仲裁。
4. 第二輪開始時，藍軍再次呼叫 `chat()`。因為歷史記憶累積，藍軍會把「第一輪起草的規格 + 第一輪紅軍的挑戰 + 裁判官的判決 + 第二輪修改意見」全部打包送給 API。

到了第三輪，這個 Context 體積呈 $O(N^2)$ 指數重疊。我們在 Prompt 中已經顯式把規格貼給對方了，大模型大腦內卻還塞著幾萬字重複的歷史垃圾。這影響了極其高昂的 Token 費用，更因為 Context 體積過大導致 API Gateway 頻繁超時卡死，成為名副其實的 **「Token 刺客」**！

---

## 🛠️ 擊退 Token 刺客的防禦型設計

為了在享受 AI 對抗的高智力產出時，還能保護好錢包，我對對決架構做出了三項關鍵重構：

### 1. 無狀態單輪優化 (Single-turn Optimization) ★最省錢突破
我們在程式碼中將 `Agent` 的長週期會話解耦，改寫為無狀態的 `chat_once` 輔助函數：
```python
async def chat_once(config: LocalAgentConfig, prompt: str) -> str:
    # 每次對話時，臨時宣告並進入一個乾淨的 Agent 上下文，結束後即刻釋放
    async with Agent(config) as agent:
        response = await agent.chat(prompt)
        return await response.text()
```
這在 SDK 物理層面**徹底清空了對話 Session 的歷史記憶**。每次對決呼叫都是全新、無污染的 Context。
*   **成果**：Context 體積瞬間壓縮 70% 以上，Token 費用直接降為舊版的 10%~20%，對局速度提升 5 倍！

### 2. Goal 需求確認簽字 (Sign-off) 里程碑
我們不能直接把一句模糊的想法丟去對決，那樣會因為起點太差導致對決輪數變多，平白浪費 Token。
*   **解法**：在工作流中加入 **階段 1.5：產出與確認 Goal**。蘇格拉底拷問後，AI 會自動在 `sys_eng/01_requirements/` 下生成 `goal_專案名.md` 需求檔。經由人類點擊打開、審閱微調、確認簽字 (Sign-off) 後，再以 `--goal-file` 送入對決。確保對決起步點 100% 精準。

### 3. 即時日誌行緩衝 (Line Buffering)
在背景執行背景任務時，常因 Python 的 stdout block-buffering 導致日誌寫入延遲，出現監控黑洞。
*   **解法**：在腳本入口強制設定 line-buffering：
    ```python
    sys.stdout.reconfigure(line_buffering=True)
    ```
    配合 Python `-u` 參數，保證每一行對抗軌跡都能即刻寫入磁碟 log，讓我們隨時掌握對決心智進度。

---

## 💡 結語與反思

進入 Agentic AI 時代，開發人員不再是「把功能代碼硬塞給系統」，而是站在 **「AI 總架構師 (Chief AI Architect)」** 的高度，去定義 Goal、設計推理迴圈、並以心智軌跡為依據進行 CI/CD 測試。

在實踐這套先進方法論的路上，我們既需要 AI 對抗帶來的「防禦型安全設計」，也必須時刻提防「API 歷史膨脹」帶來的 Token 費用。

> **AI 協作聲明**：
> 本文由筆者提供原始筆記草稿與思維對齊，由 AI 助手 Antigravity 彙整架構與修辭。結合了 Antigravity 系統工程的實踐與哈爸筆記的敘事風格，展現人機協作下的 AI 2.0 開發思維。
