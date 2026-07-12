import asyncio
import sys
import os
from pydantic import BaseModel, Field
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

# 1. 定義 Pydantic 輸出結構約束 (Structured Output)
class LeadSyncModel(BaseModel):
    sync_status: str = Field(description="同步狀態，必須為 'SUCCESS' 或 'FAILED'")
    synced_count: int = Field(description="成功同步的潛在客戶 (Leads) 筆數")
    notification_sent: bool = Field(description="是否已成功在 Slack 上發送通知給管理團隊")
    summary_report: str = Field(description="本次同步與通知的精簡中文摘要報告")

async def main():
    load_dotenv()

    # 2. 定義本地 MCP Stdio Server 設定
    # 執行路徑為此目錄底下的 mock_mcp_server.py
    current_dir = os.path.dirname(os.path.abspath(__file__))
    server_path = os.path.join(current_dir, "mock_mcp_server.py")
    
    mcp_config = types.McpStdioServer(
        name="mock-leads-server",
        command="python",
        args=[server_path]
    )

    # 3. 宣告 Agent 的 LocalAgentConfig
    # 注意：使用 MCP 工具時，必須傳入 policies 安全政策
    config = LocalAgentConfig(
        system_instructions=(
            "你是一個企業資料同步助理。你的任務是處理使用者傳入的潛在客戶 (Leads) 資料。\n"
            "你必須依序執行以下工作：\n"
            "1. 呼叫 `mock-leads-server/sync_leads_data` 工具，將資料同步到 Google Sheets 試算表。\n"
            "2. 同步完成後，呼叫 `mock-leads-server/send_slack_notification` 工具，在 Slack 上通知團隊。\n"
            "3. 執行成功後，嚴格根據 response_schema 規定的 JSON 格式回傳最終結果。"
        ),
        mcp_servers=[mcp_config],
        policies=[policy.allow_all()], # 安全策略：核准所有工具調用
        response_schema=LeadSyncModel, # 強制結構化輸出約束
        capabilities=CapabilitiesConfig()
    )

    print("🚀 [Lab 21] 正在啟動 Agent 並載入本地 Stdio MCP 服務...")
    
    async with Agent(config) as agent:
        # 使用者傳入的 Leads 原始資料
        prompt = (
            "請幫我將以下今天的潛在客戶 Leads 資料同步到試算表，並在 #marketing 頻道通知團隊成員：\n"
            "1. Name: 林小明, Email: xiaoming@example.com, Source: Google Ads\n"
            "2. Name: 陳大華, Email: dahua@example.com, Source: Facebook Referral"
        )
        print(f"\n💡 [1. 使用者需求] {prompt}\n")

        print("🧠 ======= Agent 思考、工具調用與規劃軌跡 =======")
        response = await agent.chat(prompt)
        
        async for thought in response.thoughts:
            print(f"\033[93m[Thinking] {thought}\033[0m")
            
        print("==================================================\n")
            
        print("📝 ======= Agent 最終結構化 JSON 輸出 =======")
        # 消耗 text 串流
        async for token in response:
            pass
            
        # 獲取經 Pydantic 驗證的結構化數據
        structured_data = await response.structured_output()
        if structured_data:
            if hasattr(structured_data, "model_dump_json"):
                print(structured_data.model_dump_json(indent=2))
            else:
                import json
                print(json.dumps(structured_data, ensure_ascii=False, indent=2))
        else:
            print("無法獲取結構化輸出。")
        print("==================================================")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"\n❌ 執行發生錯誤: {e}", file=sys.stderr)
