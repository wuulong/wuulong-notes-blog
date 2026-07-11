import asyncio
import sys
import os
from google.antigravity import Agent, LocalAgentConfig, CapabilitiesConfig

def load_dotenv():
    dotenv_path = os.path.join(os.getcwd(), '.env')
    if os.path.exists(dotenv_path):
        with open(dotenv_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, val = line.split('=', 1)
                    key = key.strip().strip('"').strip("'")
                    val = val.strip().strip('"').strip("'")
                    os.environ[key] = val

async def main():
    # 載入當前目錄的環境變數 (.env)
    load_dotenv()
    
    # 宣告程式設計師 Agent (Coder)
    coder_config = LocalAgentConfig(
        system_instructions=(
            "你是一個程式設計師 Agent。你的工作是根據使用者的需求撰寫 Python 程式碼。"
            "請只回傳程式碼區塊（使用 ```python 包裝），不要有其他廢話。"
        ),
        capabilities=CapabilitiesConfig(),
    )

    # 宣告審查員 Agent (Reviewer)
    reviewer_config = LocalAgentConfig(
        system_instructions=(
            "你是一個嚴格的代碼審查員 Agent。你的工作是檢查程式設計師寫的程式碼是否有 bug 或不夠優雅。"
            "如果程式碼完美，請只回傳 'PASS'。"
            "如果有問題，請列出具體的修改建議，並以 'FAIL: [建議內容]' 開頭。"
        ),
        capabilities=CapabilitiesConfig(),
    )

    print("🚀 [Lab 3] 正在啟動雙 Agent 協作模式 (Coder & Reviewer)...")
    
    # 同時在 contexts 中啟動兩個獨立的 Agent
    async with Agent(coder_config) as coder, Agent(reviewer_config) as reviewer:
        user_request = "請幫我寫一個 Python 函式，輸入一個整數 n，回傳 n 以內的所有質數（Prime Numbers）列表。"
        print(f"\n💡 [1. 使用者需求] {user_request}\n")
        
        # 第一輪：Coder 寫扣
        print("💻 [Coder] 正在撰寫程式碼...")
        coder_response = await coder.chat(user_request)
        code_result = ""
        async for token in coder_response:
            code_result += token
            sys.stdout.write(token)
            sys.stdout.flush()
        print("\n--------------------------------------------------")
        
        # 第二輪：Reviewer 審核 Coder 的成果
        print("\n🔍 [Reviewer] 正在審核程式碼品質...")
        review_prompt = f"請審核以下 Coder 產出的程式碼，是否有邊界條件沒處理（例如 n<=1）或效能問題？\n\n{code_result}"
        reviewer_response = await reviewer.chat(review_prompt)
        
        review_result = ""
        async for token in reviewer_response:
            review_result += token
            sys.stdout.write(token)
            sys.stdout.flush()
        print("\n--------------------------------------------------")
        
        # 第三輪：如果 FAIL，Coder 根據審查意見進行修正
        if "FAIL" in review_result:
            print("\n🛠️ [Coder] 收到修正建議，正在進行最佳化修改...")
            fix_prompt = f"Reviewer 給了以下修改意見：\n{review_result}\n\n請根據建議修改你的程式碼，並重新回傳修正後的程式碼。"
            coder_fix_response = await coder.chat(fix_prompt)
            
            final_code = ""
            async for token in coder_fix_response:
                final_code += token
                sys.stdout.write(token)
                sys.stdout.flush()
            print("\n==================================================")
            print("🎉 雙 Agent 協作完成！已成功產生並修正程式碼。")
        else:
            print("\n==================================================")
            print("🎉 審查通過 (PASS)！程式碼品質優良，無須修正。")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"\n❌ 執行發生錯誤: {e}", file=sys.stderr)
        print("💡 請確認是否已執行 'pip install --upgrade google-antigravity protobuf' 解決版本衝突問題。", file=sys.stderr)
