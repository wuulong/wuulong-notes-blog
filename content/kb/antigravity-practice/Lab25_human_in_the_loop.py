import asyncio
import sys
import os
from google.antigravity import Agent, LocalAgentConfig, CapabilitiesConfig
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
# 🛠️ 1. 定義排課系統工具 (Booking Tools)
# =============================================================================

def check_teacher_availability(teacher_name: str, time_slot: str) -> bool:
    """
    確認指定老師在該時段是否可以預約課程。

    Args:
        teacher_name: 老師姓名（例如 '陳老師', '李老師'）。
        time_slot: 預約時段說明（例如 '週三 14:00', '週日 10:00'）。

    Returns:
        若該時段可供預約回傳 True，已滿額回傳 False。
    """
    print(f"\n🔍 [工具執行] 正在確認 {teacher_name} 在 {time_slot} 的可用性...")
    # 模擬陳老師週三 14:00 已額滿
    if teacher_name == "陳老師" and "週三 14:00" in time_slot:
        print("   ❌ 該時段已額滿！")
        return False
    print("   ✅ 該時段可供預約。")
    return True

def ask_user_for_choice(options: list[str]) -> str:
    """
    向家長（使用者）發送排課衝突詢問，並取得其替代選擇 (中斷推理與即時回填)。

    Args:
        options: 供家長選擇的替代方案列表。

    Returns:
        家長最終選擇的替代方案。
    """
    print(f"\n⚠️ [HITL 中斷推理] 排課出現衝突！正在發送選項給家長進行決策...")
    for idx, opt in enumerate(options):
        print(f"   [{idx + 1}] {opt}")

    # 判斷是否為背景自動化測試（非 TTY）
    if not sys.stdin.isatty():
        # 背景非互動式測試，自動模擬家長回填選擇
        selected = options[1]  # 模擬選擇方案 B
        print(f"🤖 [背景模擬回填] 偵測到非互動式環境，系統自動模擬家長選擇：'{selected}'")
        return selected
    else:
        # 手動互動式測試，真正詢問人類
        try:
            print("\n請在下方輸入選項編號（如 1 或 2）進行即時決策回填：")
            ans = input("家長回覆: ").strip()
            idx = int(ans) - 1
            if 0 <= idx < len(options):
                return options[idx]
            return options[0]
        except Exception:
            return options[0]

def confirm_booking(teacher_name: str, time_slot: str, student_name: str) -> str:
    """
    最終確認並預約課程。

    Args:
        teacher_name: 預約的老師姓名。
        time_slot: 預約的課程時段。
        student_name: 學生姓名。

    Returns:
        確認成功的預約單狀態。
    """
    print(f"\n💾 [工具執行] 正在寫入預約單：學生 {student_name} / 老師 {teacher_name} / 時段 {time_slot}...")
    return f"【預約確認成功】已成功為學生 {student_name} 預約 {teacher_name} 的課（時段：{time_slot}）。"

# =============================================================================
# 🎬 2. 主程式
# =============================================================================

async def main():
    load_dotenv()

    # 設定 Agent
    config = LocalAgentConfig(
        system_instructions=(
            "你是一個音樂教室排課助理。你的任務是為學生 '小明' 預約週三 14:00 陳老師的鋼琴課。\n"
            "排課流程如下：\n"
            "1. 呼叫 check_teacher_availability 工具確認陳老師在該時段是否可以預約。\n"
            "2. 如果可用，直接呼叫 confirm_booking 確認預約。\n"
            "3. 如果不可用（滿額），說明排課衝突，並主動呼叫 ask_user_for_choice 工具，提供以下兩個方案供家長選擇：\n"
            "   - '方案 A: 改預約星期日早上 10:00 的陳老師鋼琴課'\n"
            "   - '方案 B: 改預約同時間（週三 14:00）的李老師鋼琴課'\n"
            "4. 取得家長選擇後，依據家長的決定，呼叫 confirm_booking 完成該方案預約，最後向家長親切回報預約狀態。"
        ),
        tools=[check_teacher_availability, ask_user_for_choice, confirm_booking],
        policies=[policy.allow_all()], # 啟用安全政策
        capabilities=CapabilitiesConfig()
    )

    print("🚀 [Lab 25] 正在啟動排課助理，掛載 HITL 中斷與即時回填機制...")
    
    async with Agent(config) as agent:
        prompt = (
            "行政助理，請幫小明預約週三 14:00 陳老師的鋼琴課。如果衝堂，請向我詢問替代方案並完成預約。"
        )
        print(f"\n💡 [1. 使用者指令] {prompt}\n")

        print("🧠 ======= Agent 思考、工具調用與即時人機交互軌跡 =======")
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
