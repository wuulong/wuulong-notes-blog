import asyncio
import sys
import os
from google.antigravity import Agent, LocalAgentConfig, CapabilitiesConfig
from google.antigravity.hooks.hooks import PreToolCallDecideHook, HookContext, HookResult
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
# 1. 定義一個自訂的寫入檔案工具
# ==========================================
def write_code_to_file(filename: str, content: str) -> str:
    """
    將產生的 Python 程式碼寫入指定的檔案中。

    Args:
        filename: 目標檔名 (例如 'factorial.py')
        content: 要寫入的 Python 程式碼內容

    Returns:
        寫入結果的狀態訊息。
    """
    print(f"\n💾 [工具執行] 正在寫入檔案: {filename}...")
    # 確保寫在專案練習目錄下
    target_dir = "projects/antigravity-practice"
    os.makedirs(target_dir, exist_ok=True)
    filepath = os.path.join(target_dir, filename)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    return f"成功寫入檔案 {filepath}"


# ==========================================
# 2. 定義一個 CodeLinterHook (繼承 PreToolCallDecideHook)
# 這就是 Loop Engineering 的「品質閘門 (Quality Gate)」
# ==========================================
class CodeLinterHook(PreToolCallDecideHook):
    async def run(self, context: HookContext, data: ToolCall) -> HookResult:
        # 當 Agent 企圖呼叫 write_code_to_file 時進行攔截審查
        if data.name == "write_code_to_file" or data.name == write_code_to_file.__name__:
            content = data.args.get("content", "")
            filename = data.args.get("filename", "")
            
            print(f"\n🔍 [Hook 門禁稽核] 偵測到代碼寫入請求: {filename}")
            
            # 門禁檢查 A：進行語法編譯檢查 (Syntax Check)
            try:
                compile(content, "<string>", "exec")
                print("   ✅ 語法檢查：編譯成功。")
            except SyntaxError as e:
                print(f"   ❌ 語法檢查：編譯失敗！原因: {e}")
                return HookResult(
                    allow=False,
                    message=f"拒絕寫入！您的 Python 程式碼編譯失敗，有語法錯誤：{e}。請修正後重新嘗試寫入。"
                )
            
            # 門禁檢查 B：檢查是否有包含特定的繁體中文註解（業務規格檢查）
            # 我們故意不在 Prompt 裡告訴 Agent 這個規則，以強迫它觸發這個失敗反饋
            required_comment = "# 核心演算法"
            if required_comment not in content:
                print(f"   ❌ 業務檢查：未包含必要註解 '{required_comment}'！")
                return HookResult(
                    allow=False,
                    message=(
                        f"拒絕寫入！我們的系統規範要求：產出的 Python 代碼中，"
                        f"必須包含名為 '{required_comment}' 的繁體中文單行註解。請修正代碼後重新寫入。"
                    )
                )
            
            print("   ✅ 業務檢查：符合註解規範，准予放行！")
            return HookResult(allow=True)
            
        # 其他工具不干涉
        return HookResult(allow=True)


async def main():
    load_dotenv()
    
    # 註冊我們自訂的 Hook 與 Tool
    config = LocalAgentConfig(
        system_instructions=(
            "你是一個資深 Python 開發助手。當使用者要求你寫代碼時，"
            "請呼叫 write_code_to_file 工具將程式碼存入檔案中。"
            "如果工具呼叫失敗被拒絕，請詳細閱讀拒絕原因，修正你的程式碼後再次嘗試呼叫工具，"
            "直到成功寫入為止。"
        ),
        tools=[write_code_to_file],
        # 綁定生命週期 Hook
        hooks=[CodeLinterHook()],
        capabilities=CapabilitiesConfig(),
    )

    print("🚀 [Lab 6] 正在初始化 Self-Correction Loop Agent...")
    
    async with Agent(config) as agent:
        prompt = "請幫我寫一個計算階乘（factorial）的 Python 函數，並將代碼寫入名為 'factorial.py' 的檔案。"
        print(f"\n💡 使用者提問: {prompt}\n")
        
        response = await agent.chat(prompt)
        
        print("🧠 ======= Agent 思考與自動反思循環軌跡 =======")
        async for thought in response.thoughts:
            print(f"\033[93m[Thinking] {thought}\033[0m")
            
        async for tool_call in response.tool_calls:
            print(f"\033[96m[Tool Call] 呼叫工具: {tool_call.name}\033[0m")
            
        print("==================================================\n")
            
        print("📝 ======= Agent 最終回覆 =======")
        async for token in response:
            sys.stdout.write(token)
            sys.stdout.flush()
        print("\n==================================================")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"\n❌ 執行發生錯誤: {e}", file=sys.stderr)
