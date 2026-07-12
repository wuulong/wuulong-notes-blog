import asyncio
import sys
import os
import json
from google.antigravity import Agent, LocalAgentConfig, CapabilitiesConfig, types
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
# 🛠️ 1. 定義背景任務 Agent 工具 (Task Agent Tools)
# =============================================================================

def write_database(content: str) -> str:
    """
    將排課資料寫入資料庫主表中。

    Args:
        content: 欲寫入的排課記錄文字。

    Returns:
        寫入結果或失敗錯誤訊息。
    """
    print(f"\n💾 [工具執行] 嘗試將資料寫入 DB: '{content}'...")
    # 故意拋出錯誤，模擬暫時性的資料庫鎖定以逼迫 Agent 重試
    return "Error: Database is locked by another transaction. Please try again later."

# =============================================================================
# 🎬 2. 主非同步排程控制流程
# =============================================================================

async def main():
    load_dotenv()

    current_dir = os.path.dirname(os.path.abspath(__file__))
    trajectory_file = os.path.join(current_dir, "logs", "logs_task_trajectory.json")
    os.makedirs(os.path.dirname(trajectory_file), exist_ok=True)

    print("⏰ [背景任務排程] 觸發模擬的凌晨定時分析與評估任務...")

    # ==========================================
    # 🚀 第一步：啟動 Task Agent 並匯出執行軌跡
    # ==========================================
    task_config = LocalAgentConfig(
        system_instructions=(
            "你是一個背景資料同步 Agent。你的唯一工作是將排課資料寫入資料庫。\n"
            "當你遇到 Database is locked 錯誤時，請在 thoughts 中思考對策，並至少重新呼叫 write_database 工具嘗試寫入 3 次。\n"
            "如果重試 3 次皆失敗，請在 thoughts 中判定任務失敗，並向使用者回報無法寫入的系統狀態。"
        ),
        tools=[write_database],
        policies=[policy.allow_all()], # 啟用安全政策
        capabilities=CapabilitiesConfig()
    )

    print("\n🔵 [Task Agent] 啟動背景同步任務...")
    async with Agent(task_config) as task_agent:
        prompt = "請幫我將排課資料 '張老師: 鋼琴團體課A, 14:00' 寫入資料庫。若寫入失敗請重試。"
        print(f"   👉 任務指令: {prompt}")
        
        response = await task_agent.chat(prompt)
        
        # 消耗 token 串流
        async for token in response:
            pass

        # 透過 resolve() 取得完整的 flat list 軌跡
        chunks = await response.resolve()
        trajectory = []
        for chunk in chunks:
            if isinstance(chunk, types.Thought):
                trajectory.append({"type": "thought", "content": chunk.text})
            elif isinstance(chunk, types.Text):
                trajectory.append({"type": "text", "content": chunk.text})
            elif isinstance(chunk, types.ToolCall):
                trajectory.append({
                    "type": "tool_call",
                    "name": str(chunk.name),
                    "args": chunk.args
                })
            elif isinstance(chunk, types.ToolResult):
                trajectory.append({
                    "type": "tool_result",
                    "name": str(chunk.name),
                    "result": str(chunk.result),
                    "error": chunk.error
                })

        # 將軌跡序列化匯出至 JSON 檔案中
        with open(trajectory_file, "w", encoding="utf-8") as f:
            json.dump(trajectory, f, ensure_ascii=False, indent=2)
            
        print(f"🟢 [Task Agent] 任務結束。推理軌跡已序列化寫入：\n   {trajectory_file}")

    # ==========================================
    # ⚖️ 第二步：啟動 Evaluator Agent 對軌跡進行自動化評估
    # ==========================================
    eval_config = LocalAgentConfig(
        system_instructions=(
            "你是一個 AI 系統運作狀況評估專家（Evaluator）。你的工作是仔細閱讀另一個背景 Agent 的 Thoughts 與 Tool Calls 執行軌跡，評估其運作效能。\n"
            "你的評估指標必須包含：\n"
            "1. 檢查是否陷入死迴圈 (Looping)：是否重複呼叫某個工具？重試了幾次？\n"
            "2. 評估規劃偏離度 (Drifting)：Agent 的想法與手段是否偏離了原本的任務目標？\n"
            "3. 系統健康診斷：判定任務最終是 SUCCESS 還是 FAILED。\n"
            "4. 系統優化建議：針對重試或死迴圈狀況，提出具體的優化建議（如加入 Exponential Backoff、重試上限限制、或故障告警機制）。\n"
            "請以繁體中文撰寫一份條理分明的『Agent 心智與執行軌跡健康評估報告』。"
        ),
        capabilities=CapabilitiesConfig()
    )

    print("\n⚖️ [Evaluator Agent] 啟動自動化軌跡評估...")
    
    # 讀取剛剛寫入的軌跡檔
    with open(trajectory_file, "r", encoding="utf-8") as f:
        trajectory_json_str = f.read()

    async with Agent(eval_config) as eval_agent:
        eval_prompt = (
            f"請評估以下 Task Agent 的執行軌跡，分析其是否陷入死迴圈或規律重試，並給出診斷報告：\n\n"
            f"```json\n{trajectory_json_str}\n```"
        )
        
        eval_response = await eval_agent.chat(eval_prompt)
        
        print("\n🧠 ======= Evaluator Agent 思考與審計軌跡 =======")
        async for thought in eval_response.thoughts:
            print(f"\033[93m[Thinking] {thought}\033[0m")
        print("==================================================\n")
        
        print("📝 ======= Agent 心智與執行軌跡健康評估報告 =======")
        async for token in eval_response:
            sys.stdout.write(token)
            sys.stdout.flush()
        print("\n==================================================")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"\n❌ 執行發生錯誤: {e}", file=sys.stderr)
