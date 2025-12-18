---
title: "實驗紀錄：使用 Fabric 封裝 Gemini CLI 提升 AI Agent 協作效率"
date: 2025-12-13T13:29:48+08:00
draft: false
series: ["GenAI"]
categories: ["DevOps", "GenAI", "Tooling"]
tags: ["Fabric", "Python", "Gemini CLI", "Automation", "Workflow"]
author: "Wuulong"
summary: "本實驗記錄了如何透過 Python Fabric 構建中間層來驅動 Google Gemini CLI，解決直接操作命令列時遇到的轉義字元問題、日誌雜訊干擾，並實現模型參數的靈活配置。"
---

## 實驗目的

與 Antigravity (AI Agent) 進行 Pair Programming 時，發現 AI Agent 在直接調用 CLI 工具時常面臨語法轉義錯誤、輸出解析困難等問題。本實驗旨在透過 **Fabric** 建立一個穩定、可程式化的中間層 (Wrapper)，讓 AI Agent 能更穩定地呼叫 Google Gemini CLI，並實現進階的參數控制與輸出清洗。

## 實驗環境

*   **作業系統**：macOS (Darwin)
*   **專案目錄**：`~/github/bmad-pa`
*   **語言與工具**：Python 3.x, Fabric, Google Gemini CLI
*   **Conda 環境**：`m2504` (已預裝 Fabric 與 Gemini)

## 實驗動機：為什麼不直接用 Shell？

在實驗初期，我詢問 Agent 是否應該直接敲命令列。Agent 給出了極具洞見的分析，指出直接使用 CLI 有以下風險：
1.  **幻覺與語法風險**：複雜 Prompt 包含的特殊字元（引號、換行）極易在 Shell 中造成解析錯誤。
2.  **後處理困難**：CLI 輸出常夾帶非結構化的 Log 或 Metadata，難以直接提取核心答案。
3.  **上下文管理**：直接塞入長 Context 到 Shell 參數既不優雅也容易超出長度限制。

因此，決定採用 **Fabric** (`fabfile.py`) 來封裝這些邏輯。

## 實驗步驟

### 1. 初始架構設計
在 `fabfile.py` 中新增一個名為 `ask` 的 task。這個 task 的設計目標是：
*   接受純文字問題 (`--question`) 或 檔案路徑 (`--file`)。
*   負責處理 Shell 轉義 (Escaping)。
*   負責呼叫底層的 `gemini` executable。
*   負責清洗輸出，移除系統 Log。

### 2. 實作與除錯
第一版的實作遇到了一個有趣的問題：`fab` 指令在 Shell 中找不到。
*   **問題發掘**：系統回報 `fab not found`。
*   **原因分析**：雖然環境變數有設，但 Agent 當下的 Shell context 可能未正確吃到 Conda path。
*   **解決方案**：發現本地有一個 wrapper script `./fab` 直接指向 `/Users/wuulong/opt/anaconda3/envs/m2504/bin/fab`。我們決定統一改用 `./fab` 來呼叫，確保環境一致性。

### 3. Log 清洗與輸出優化
Gemini CLI 在啟動時會印出許多 `[STARTUP]` 開頭的效能追蹤 Log。這些對使用者來說是雜訊。
**解決方案**：在 Python 程式碼中攔截 stdout，透過簡單的字串比對過濾掉 `[STARTUP]` 與 `Loaded cached credentials` 行，只回傳乾淨的 LLM 回覆。

### 4. 進階功能：模型參數化
為了讓 Agent 能根據任務難度選擇模型（例如用 Flash 模型處理簡單任務，Pro 模型處理複雜推理），我們後續為 `ask` task 增加了 `model` 參數。
*   **預設值**：`gemini-2.5-flash` (快速、省錢)
*   **客製化**：可透過 `--model="gemini-1.5-pro"` 指定。

### 核心程式碼片段

```python
@task
def ask(c, question=None, file=None, model="gemini-2.5-flash", debug=False):
    """
    向 Gemini 提問。支援檔案輸入與模型切換。
    """
    import os
    
    # ... (省略檔案讀取邏輯) ...

    # 跳脫雙引號以免 shell 出錯
    safe_prompt = prompt.replace('"', '\\"')
    
    # 執行 Gemini CLI，指定模型
    cmd = f'gemini -m "{model}" "{safe_prompt}"'
    
    try:
        # 使用 hide=True 隱藏原始輸出，由 Python 接管 stdout
        result = local_run(cmd, hide=True, warn=True)
        
        # 過濾雜訊
        lines = result.stdout.split('\n')
        clean_lines = [line for line in lines if not line.startswith('[STARTUP]')]
        output = '\n'.join(clean_lines).strip()
        
        print(f"{Fore.GREEN}Gemini 回覆 ({model})：{Style.RESET_ALL}")
        print(output)
        
    except Exception as e:
        print(f"{Fore.RED}發生錯誤: {e}{Style.RESET_ALL}")
```

## 實驗結果

成功建立了一個高強健性的 AI 呼叫工具。
*   **穩定性**：成功解決了 Prompt 中包含特殊字元導致的執行失敗。
*   **可讀性**：輸出的雜訊被過濾，Agent 能更準確地讀取並理解 LLM 的回覆。
*   **靈活性**：支援了檔案輸入模式，未來可以將長篇的 System Prompt 或 Context 寫在文件中直接餵給模型，不再受限於 Shell 參數長度。

## 學習與反思

1.  **AI for AI**：為 AI Agent 準備好的工具（Tools），比直接讓它去用給人類用的介面（CLI）更重要。Fabric 在這裡扮演了完美的「膠水」角色。
2.  **Wrapper Pattern**：當底層工具（如 Gemini CLI）輸出不穩定或過於囉嗦時，寫一層薄薄的 Python wrapper 能大幅提升自動化腳本的品質。
3.  **環境一致性**：明確指定執行路徑（如 `./fab` vs `fab`）在自動化環境中至關重要，能避免因 `$PATH` 差異導致的執行錯誤。
