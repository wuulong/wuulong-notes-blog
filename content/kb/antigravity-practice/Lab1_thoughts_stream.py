import asyncio
import sys
import os
from google.antigravity import Agent, LocalAgentConfig, CapabilitiesConfig

def load_dotenv():
    # 尋找當前工作目錄下的 .env 檔案
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
    
    # 使用唯讀設定 (CapabilitiesConfig 預設為唯讀，不帶額外權限)
    # 這能確保 Agent 只能進行推理與文字輸出，無法任意寫入檔案或跑 CLI 命令，安全無虞
    config = LocalAgentConfig(
        system_instructions=(
            "你是一個專業的繁體中文軟體工程導師。請在回答任何問題前，"
            "先在內心中進行深入的邏輯拆解與規劃，並以清晰的繁體中文回覆。"
        ),
        capabilities=CapabilitiesConfig(),
    )

    print("🚀 [Lab 1] 正在初始化 Antigravity Agent...")
    
    async with Agent(config) as agent:
        print("💡 您可以開始輸入自訂問題，輸入 'exit' 或 'quit' 可退出對話。\n")
        
        while True:
            try:
                prompt = input("💬 請輸入 Prompt: ").strip()
            except (KeyboardInterrupt, EOFError):
                print("\n👋 已退出對話。")
                break
                
            if not prompt:
                continue
            if prompt.lower() in ('exit', 'quit'):
                print("👋 已退出對話。")
                break
                
            print(f"\n💡 正在發送提問: {prompt}\n")
            
            # 發送 Chat 請求 (此 API 會立刻回傳，不阻塞)
            response = await agent.chat(prompt)
            
            # 1. 串流顯示 Agent 的思考軌跡 (Thoughts Stream)
            print("🧠 ======= Agent 思考軌跡 (Thinking Trace) =======")
            async for thought in response.thoughts:
                # 使用黃色 ANSI 色碼印出思考過程，這能讓我們看見 LLM 的 Reasoning 軌跡
                print(f"\033[93m[Thinking] {thought}\033[0m")
            print("==================================================\n")
                
            # 2. 串流顯示 Agent 最終產出的 Tokens (Tokens Stream)
            print("📝 ======= Agent 最終回覆 (Final Response) =======")
            async for token in response:
                sys.stdout.write(token)
                sys.stdout.flush()
            print("\n==================================================\n")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"\n❌ 執行發生錯誤: {e}", file=sys.stderr)
        print("💡 請確認是否已執行 'pip install --upgrade google-antigravity protobuf' 解決版本衝突問題。", file=sys.stderr)
