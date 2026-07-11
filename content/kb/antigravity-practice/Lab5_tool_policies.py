import asyncio
import sys
import os
from google.antigravity import Agent, LocalAgentConfig, CapabilitiesConfig, BuiltinTools
from google.antigravity.hooks.policy import deny, Decision
from google.antigravity.types import ToolCall

# 自動載入環境變數
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

# ==========================================
# 定義安全過濾規則 (Policy Predicate)
# 當該函式回傳 True 時，代表滿足過濾條件，Policy 將執行 DENY 決策阻斷呼叫
# ==========================================
def is_dangerous_command(call: ToolCall) -> bool:
    # 由於 Python 執行時型別解析的差異，call 可能是 ToolCall 實體，也可能是 call.args 字典
    # 我們進行安全相容性處理，並列印出真正的結構以供觀測
    if isinstance(call, dict):
        args = call
        call_name = "run_command"
    else:
        args = getattr(call, "args", {})
        call_name = getattr(call, "name", "unknown")
        
    print(f"\n🔍 [Policy 門禁除錯] 攔截工具: {call_name}")
    print(f"   參數內容: {args}")
    
    # 支援不同大小寫的參數名稱
    command_line = args.get("CommandLine") or args.get("command_line") or ""
    print(f"   解析到的指令: '{command_line}'")
    
    # 檢查命令中是否包含敏感關鍵字
    is_dangerous = "rm" in command_line or "sudo" in command_line
    if is_dangerous:
        print(f"❌ [Policy 門禁阻斷] 偵測到危險操作 (rm 或 sudo)，已直接攔截並拒絕執行！")
    else:
        print(f"✅ [Policy 門禁放行] 指令評估為安全，放行執行。")
    return is_dangerous

async def run_scenario(agent: Agent, prompt: str):
    print(f"\n💬 使用者提問: {prompt}")
    try:
        response = await agent.chat(prompt)
        
        # 串流思考軌跡與文字
        async for thought in response.thoughts:
            pass # 這裡我們主要觀測 tool 攔截，跳過 thoughts 列印
            
        async for token in response:
            sys.stdout.write(token)
            sys.stdout.flush()
        print("\n--------------------------------------------------")
    except Exception as e:
        # 當 Policy 觸發 DENY 時，Agent 呼叫可能會拋出 ValidationError 或是被中斷
        print(f"\n🚨 [系統防護攔截] Agent 執行被系統安全機制阻斷！原因: {e}")
        print("--------------------------------------------------")

async def main():
    load_dotenv()
    
    # 配置 Agent
    config = LocalAgentConfig(
        system_instructions=(
            "你是一個系統運維助手。你擁有操作系統工具的權利。"
            "當使用者要求你刪除檔案時，請呼叫 run_command 執行 'rm' 指令。"
            "當使用者要求你列出檔案時，請呼叫 run_command 執行 'ls' 指令。"
        ),
        # 啟用所有內建工具的能力 (包含 run_command)
        capabilities=CapabilitiesConfig(
            enabled_tools=[BuiltinTools.RUN_COMMAND, BuiltinTools.LIST_DIR]
        ),
        # 綁定安全 Policy：拒絕執行包含 rm 或 sudo 的 run_command 工具
        # 注意: 傳入 "run_command" 字串與 is_dangerous_command 判定函式
        policies=[
            deny("run_command", when=is_dangerous_command, name="BlockDangerousSystemCommands")
        ]
    )

    print("🚀 [Lab 5] 正在初始化帶有安全 Policy 的 Agent...")
    
    async with Agent(config) as agent:
        # 情境一：安全指令測試 (ls)
        print("\n=== 情境一：測試安全指令 (應可順利執行) ===")
        await run_scenario(agent, "請幫我呼叫工具，執行 'ls projects/antigravity-practice' 指令，以確認目錄下的檔案。")
        
        # 情境二：危險指令測試 (rm)
        print("\n=== 情境二：測試危險指令 (應被 Policy 自動攔截) ===")
        await run_scenario(agent, "請幫我呼叫工具，執行 'rm -rf projects/antigravity-practice/temp.txt' 以刪除臨時檔案。")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"\n❌ 執行發生錯誤: {e}", file=sys.stderr)
