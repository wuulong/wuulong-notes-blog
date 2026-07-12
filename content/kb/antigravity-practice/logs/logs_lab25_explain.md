# Lab 25 學習導引與技術解析

本 Lab 深入剖析了 AI 代理人系統中至關重要的 **「即時人機協同（Human-in-the-Loop, HITL）」** 機制，特別是 **「推理中斷（Suspend）」** 與 **「上下文回填（Resume/Callback）」** 的架構實踐。

## 💡 核心學習重點

### 1. 人機協同 (HITL) 的重要性與中斷機制
* **概念**：Agent 雖然具備自主規劃能力，但在某些情境（如重大決策、排課衝堂、高額金流）下，我們不允許 Agent 自作主張。Agent 必須有能力主動「暫停它的推理程序」，向人類尋求授權或意願選擇。
* **物理中斷（Suspend）**：
  在 LLM 推理過程中，當它決定調用 `ask_user_for_choice` 工具時，LLM 會中斷文字生成，轉而等待該 Python 函式工具的回傳。此時，推理物理性地暫停。

### 2. 即時上下文回填 (Resume)
* **概念**：當人類在終端機輸入、或者在 UI 上點選選項後，系統把這個「人類的選擇」作為該工具的返回值（Result）回填給大模型。
* **物理恢復（Resume）**：
  Agent 接收到工具傳回的 Result （如：選擇方案 B 李老師的課）之後，把這個新反饋加入上下文，恢復推理，最終呼叫 `confirm_booking` 完成排課，達成「詢問與回填」閉環。

---

## 🛠️ 開發與背景測試雙模相容設計 (TTY Detection)
在實際的軟體工程中，如果代碼中直接寫死 `input()`，在自動化測試（CI/CD, CLI 背景任務等非互動模式）下執行會引發 `EOFError`。
為了兼顧「手動互動式除錯的真實感」與「背景任務的自動化測試流暢度」，本 Lab 採用了 **TTY 自動偵測狀態機** 設計：
```python
import sys

# 偵測當前執行環境的 standard input 是否為互動式終端 (Teletypewriter)
if not sys.stdin.isatty():
    # 1. 自動化測試/背景模式下：自動模擬家長回填
    selected = options[1] # 模擬選方案 B
    return selected
else:
    # 2. 本地手動除錯模式下：真正詢問人類
    ans = input("家長回覆: ")
    ...
```
這項 TTY 偵測技巧是編寫高品質 CLI 工具與 Agent SDK 應用的金科玉律，保證了程序能百分之百在各種環境下穩定且無摩擦地執行完畢。
