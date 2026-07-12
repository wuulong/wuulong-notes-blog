import asyncio
import sys
import os
from google.antigravity import Agent, LocalAgentConfig, CapabilitiesConfig
from google.antigravity.hooks.hooks import PreToolCallDecideHook, HookContext, HookResult
from google.antigravity.types import ToolCall
from google.antigravity.hooks import policy

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

# =============================================================================
# 🛠️ 定義音樂教室系統工具 (Tools) —— 普通 Python 函數搭配 Docstring
# =============================================================================

def query_class_schedule(class_id: str) -> str:
    """
    查詢指定課程的排課時間。

    Args:
        class_id: 課程識別碼。

    Returns:
        該課程的排課時間。
    """
    return f"課程 {class_id} 的排課時間為 每週三 14:00 - 16:00。"

def register_student(student_name: str) -> str:
    """
    註冊一名新學生到音樂教室系統中。

    Args:
        student_name: 新註冊的學生姓名。

    Returns:
        註冊狀態描述。
    """
    return f"新學生 {student_name} 已註冊成功。"

def delete_student_record(student_name: str) -> str:
    """
    刪除指定學生的歷史學習與請假紀錄 (高風險操作)。

    Args:
        student_name: 欲刪除學習紀錄的學生姓名。

    Returns:
        操作結果狀態。
    """
    return f"學生 {student_name} 的所有歷史紀錄已被物理刪除。"

def update_tuition_fee(amount: int) -> str:
    """
    更新音樂教室的學費收費標準 (高風險操作)。

    Args:
        amount: 新的學費金額。

    Returns:
        更新結果狀態。
    """
    return f"學費標準已成功更新為每學期 {amount} 元。"

# =============================================================================
# 🛡️ 定義安全審查 Hook (PreToolCallDecideHook)
# =============================================================================

class StudioSecurityHook(PreToolCallDecideHook):
    """
    自訂安全沙盒審查 Hook。
    攔截高風險工具調用，執行「動態阻斷」與「模擬提權核准」。
    """
    async def run(self, context: HookContext, data: ToolCall) -> HookResult:
        tool_name = data.name
        args = data.args

        # 攔截高風險操作
        if tool_name in ["delete_student_record", "update_tuition_fee"]:
            print(f"\n[🛡️ 安全網監聽] 偵測到 Agent 嘗試呼叫高風險工具: {tool_name}")
            print(f"   呼叫參數: {args}")
            
            # 分支 1：阻斷刪除歷史紀錄（拒絕）
            if tool_name == "delete_student_record":
                print("   ⚖️ [安全主管評判] 拒絕此高風險操作！(DENIED)")
                return HookResult(
                    allow=False, 
                    message=(
                        "Permission Denied. 刪除學生的歷史請假與學習紀錄屬於敏感隱私操作，"
                        "安全政策規定必須由系統超級管理員手動執行，安全網已依法予以阻斷。"
                    )
                )
                
            # 分支 2：核准修改學費標準（動態授權核准）
            elif tool_name == "update_tuition_fee":
                print("   ⚖️ [安全主管評判] 偵測到調整學費請求，安全防禦政策判定在許可區間內：核准執行！(APPROVED)")
                return HookResult(allow=True)
                
        # 其他一般工具直接放行
        return HookResult(allow=True)

# =============================================================================
# 🎬 主程式
# =============================================================================

async def main():
    load_dotenv()

    # 設定 Agent
    config = LocalAgentConfig(
        system_instructions=(
            "你是一個音樂教室行政 Agent。你擁有對系統的查詢、註冊與各類修改工具。\n"
            "你的工作任務是：\n"
            "1. 嘗試刪除學生 '小明' 的學習歷史紀錄（以回應家長撤回隱私的要求）。\n"
            "2. 如果該刪除被系統安全網阻斷，請向使用者回報阻斷原因，並改為嘗試將學費調整為 6000 元（以配合新一季活動政策）。\n"
            "3. 如果調整成功，請回報最終處理狀態。"
        ),
        tools=[query_class_schedule, register_student, delete_student_record, update_tuition_fee],
        hooks=[StudioSecurityHook()], # 註冊安全沙盒 Hook
        policies=[policy.allow_all()], # 啟用安全審計
        capabilities=CapabilitiesConfig()
    )

    print("🚀 [Lab 22] 正在啟動音樂行政 Agent 並掛載動態安全網...")
    
    async with Agent(config) as agent:
        prompt = (
            "行政助理，請幫我刪除小明的歷史學習紀錄。如果被安全網擋下來，請改幫我調整學費為 6000 元。"
        )
        print(f"\n💡 [1. 使用者指令] {prompt}\n")

        print("🧠 ======= Agent 思考、工具調用與安全攔截軌跡 =======")
        response = await agent.chat(prompt)
        
        async for thought in response.thoughts:
            print(f"\033[93m[Thinking] {thought}\033[0m")
            
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
