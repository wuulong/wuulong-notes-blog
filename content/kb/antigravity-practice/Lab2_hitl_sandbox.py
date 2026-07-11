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
    
    # 這裡我們配置 Agent，並給予 write capabilities 以便它能夠呼叫指令執行等工具
    # 注意：在 Antigravity SDK 中，CapabilitiesConfig 可以用來限制或啟用特定系統工具的存取權限
    config = LocalAgentConfig(
        system_instructions=(
            "你是一個系統診斷小幫手。如果使用者要求查詢目前目錄的檔案，"
            "請呼叫對應的命令工具（例如 run_command 執行 'ls'）。"
        ),
        # 啟用能力配置。這讓 Agent 知道它可以使用 workspace 工具。
        capabilities=CapabilitiesConfig(),
    )

    print("🚀 [Lab 2] 正在初始化 HITL 沙盒 Agent...")
    
    async with Agent(config) as agent:
        prompt = "請幫我查看當前目錄下有哪些檔案。"
        print(f"\n💡 使用者提問: {prompt}\n")
        
        response = await agent.chat(prompt)
        
        # 1. 攔截並串流 Tool Calls (工具呼叫)
        # 這允許我們在工具真正發揮作用前或過程中，進行攔截與人為介入 (Human-in-the-Loop)
        print("🔍 ======= 偵測 Tool 呼叫軌跡 (Tool Calls Stream) =======")
        
        tool_executed = False
        async for tool_call in response.tool_calls:
            tool_executed = True
            print(f"\n🚨 [偵測到 Tool 呼叫請求] 函數名稱: {tool_call.name}")
            print(f"📌 參數: {tool_call.args}")
            print("--------------------------------------------------")
            
            # 實作 Human-in-the-loop (HITL) 審查機制
            user_decision = input("❓ [HITL 審查] 是否允許 Agent 執行此工具？ (y/N): ").strip().lower()
            
            if user_decision == 'y':
                print("✅ [審查通過] 允許執行此工具。")
                # 在實際應用中，您可以允許 SDK 繼續在後台執行該 command，
                # 或是使用自訂的 runner 來執行並回傳結果。
            else:
                print("❌ [審查拒絕] 拒絕此工具執行！")
                # 拒絕時，您可以拋出 Exception 或是中斷這個 agent 呼叫
                print("🚨 審查未通過，中止執行。")
                return
        
        if not tool_executed:
            print("（此回覆中 Agent 未呼叫任何工具）")
        print("==================================================\n")

        # 2. 串流最終的文字回覆
        print("📝 ======= Agent 最終回覆 (Tokens Stream) =======")
        async for token in response:
            sys.stdout.write(token)
            sys.stdout.flush()
        print("\n==================================================")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"\n❌ 執行發生錯誤: {e}", file=sys.stderr)
        print("💡 請確認是否已執行 'pip install --upgrade google-antigravity protobuf' 解決版本衝突問題。", file=sys.stderr)
