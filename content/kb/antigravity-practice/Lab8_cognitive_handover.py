import asyncio
import sys
import os
from google.antigravity import Agent, LocalAgentConfig, CapabilitiesConfig

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

async def run_stage_1(save_dir: str) -> str:
    """
    第一階段：啟動一個全新的 Agent 進行安全掃描。
    不指定 conversation_id，讓系統自動生成。
    結束時，會自動將心智狀態與對話保存到 save_dir。
    """
    print("\n==================================================")
    print("🎬 [第一階段] 啟動安全掃描 Agent (Stage 1)...")
    print(f"   存檔目錄: {save_dir}")
    print("==================================================")

    config = LocalAgentConfig(
        system_instructions=(
            "你是一個專業的程式碼安全審查助手。你的任務是分析並記錄系統中的安全漏洞。"
            "當執行安全掃描時，請在你的推理思考（Thoughts）與回答中，精確記錄漏洞的檔案與行數。"
        ),
        # 不指定對話 ID，讓系統動態產生全新的 Session
        save_dir=save_dir,
        capabilities=CapabilitiesConfig()
    )
    async with Agent(config) as agent:
        prompt = (
            "請幫我對目前的 codebase 進行安全掃描，並在你的心智狀態中記錄以下發現的漏洞：\n"
            "1. 檔案: main.py, 行數: 45, 類型: 潛在的 SQL Injection 漏洞。\n"
            "2. 檔案: helper.py, 行數: 88, 類型: 檔案控制代碼（File Handle）未正確關閉。\n"
            "\n完成記錄後，請簡短回覆：『掃描已完成，已將報告與漏洞快照寫入 session 狀態。』"
        )
        print(f"\n💡 使用者提問: {prompt}\n")

        response = await agent.chat(prompt)
        
        print("🧠 ======= Agent 思考與規劃軌跡 =======")
        async for thought in response.thoughts:
            print(f"\033[93m[Thinking] {thought}\033[0m")
            
        print("==================================================\n")
            
        print("📝 ======= Agent 最終回覆 =======")
        async for token in response:
            sys.stdout.write(token)
            sys.stdout.flush()
        print("\n==================================================")
        
        # 獲取系統動態生成的對話 ID（此時已完成一輪對話，ID 已被初始化）
        conv_id = agent.conversation_id
        print(f"   👉 系統已為此對話動態分配 ID: {conv_id}")
        return conv_id

async def run_stage_2(conversation_id: str, save_dir: str):
    """
    第二階段：啟動另一個全新的 Agent。
    傳入第一階段生成的 conversation_id 與 save_dir，接力讀取上一階段的記憶。
    """
    print("\n==================================================")
    print("🎬 [第二階段] 啟動發佈日誌 Agent (Stage 2 - 認知接力)...")
    print(f"   連線對話 ID: {conversation_id}")
    print(f"   讀取存檔目錄: {save_dir}")
    print("==================================================")

    config = LocalAgentConfig(
        system_instructions=(
            "你是一個專業的軟體發佈經理。你需要根據上一階段安全掃描的結果，生成發佈日誌。"
            "請注意，你的系統中已經載入了之前的對話快照，你必須讀取之前的記憶來取得漏洞資訊。"
        ),
        # 帶入上一階段產生的 Session ID 以進行復原
        conversation_id=conversation_id,
        save_dir=save_dir,
        capabilities=CapabilitiesConfig()
    )

    # 重新實例化一個全新的 Agent
    async with Agent(config) as agent:
        # 直接詢問成果，不再提示漏洞內容
        prompt = (
            "根據我們剛才（或上一階段）在 session 中記錄的程式碼安全掃描結果，"
            "請幫我生成一份繁體中文的安全發佈日誌 (Security Release Log)。"
            "日誌中必須指出被掃描出漏洞的檔案名稱、行數、漏洞類型，並提供具體的修補建議。"
        )
        print(f"\n💡 使用者提問: {prompt}\n")
        
        response = await agent.chat(prompt)
        
        print("🧠 ======= Agent 思考與認知復原軌跡 =======")
        async for thought in response.thoughts:
            print(f"\033[93m[Thinking] {thought}\033[0m")
            
        print("==================================================\n")
            
        print("📝 ======= Agent 最終回覆 =======")
        async for token in response:
            sys.stdout.write(token)
            sys.stdout.flush()
        print("\n==================================================")

async def main():
    load_dotenv()
    
    # 動態規劃 session 存檔目錄
    base_dir = os.path.dirname(os.path.abspath(__file__))
    save_dir = os.path.join(base_dir, "sessions")
    os.makedirs(save_dir, exist_ok=True)
    
    # 執行第一階段：掃描並持久化，回傳對話 ID
    conv_id = await run_stage_1(save_dir)
    
    print("\n⏳ 模擬進程中斷，等待安全主管審批與時間流逝 3 秒...")
    await asyncio.sleep(3)
    
    # 執行第二階段：載入同一個對話快照並接力
    await run_stage_2(conv_id, save_dir)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"\n❌ 執行發生錯誤: {e}", file=sys.stderr)
