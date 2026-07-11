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

# ==========================================
# 定義兩個本地 Python 函數作為 Agent 的 Tools
# 注意：Docstring 與 Type Hints 是關鍵，Agent 會依據它們自動產生 Schema 並決定何時呼叫
# ==========================================

def get_river_flow(river_name: str) -> str:
    """
    查詢台灣特定河流的即時流量資訊（模擬數據）。

    Args:
        river_name: 河流名稱 (例如：二仁溪、曾文溪、頭前溪)

    Returns:
        該河流的即時流量說明字串。
    """
    print(f"\n⚙️ [本地 Python 執行] 正在查詢河流 {river_name} 的流量資料...")
    flows = {
        "二仁溪": "當前流量為 4.2 萬立方公尺/日，水位偏低。",
        "曾文溪": "當前流量為 12.8 萬立方公尺/日，水位正常。",
        "頭前溪": "當前流量為 8.5 萬立方公尺/日，水位正常。"
    }
    return flows.get(river_name, f"未找到 {river_name} 的即時資料，預設流量為 1.0 萬立方公尺/日。")


def calculate_water_index(flow_rate: float, alert_threshold: float) -> str:
    """
    依據即時流量與警戒門檻值，計算當前的水位警戒指標狀態。

    Args:
        flow_rate: 當前流量值 (例如 4.2)
        alert_threshold: 警戒門檻值 (例如 5.0)

    Returns:
        水位警戒指標狀態說明。
    """
    print(f"\n⚙️ [本地 Python 執行] 正在計算水位警戒指標... (流量: {flow_rate}, 門檻: {alert_threshold})")
    if flow_rate < alert_threshold:
        return "⚠️ 水位警報：當前流量低於安全警戒值，可能面臨乾枯或供水吃緊！"
    else:
        return "✅ 水位安全：當前流量高於警戒值，供水狀況良好。"


async def main():
    load_dotenv()
    
    # 將本地定義的 Python 函數傳入 tools 列表
    # Antigravity SDK 會自動利用 inspect 解析函數簽名、參數型別與 Docstring 說明
    config = LocalAgentConfig(
        system_instructions=(
            "你是一個水利監測助理。請協助使用者查詢河川流量並評估安全狀態。"
            "當使用者提問時，請依據需求呼叫 get_river_flow 查詢流量，"
            "並依據取得的數字與使用者提供的警戒門檻，呼叫 calculate_water_index 計算狀態。"
            "最後以繁體中文向使用者回報分析結論。"
        ),
        tools=[get_river_flow, calculate_water_index],
        capabilities=CapabilitiesConfig(),
    )

    print("🚀 [Lab 4] 正在初始化 Custom Tool 綁定 Agent...")
    
    async with Agent(config) as agent:
        prompt = "請幫我查詢『二仁溪』的即時流量，並以警戒門檻 5.0 評估水位安全狀態。"
        print(f"\n💡 使用者提問: {prompt}\n")
        
        response = await agent.chat(prompt)
        
        print("🧠 ======= Agent 思考與 Tool 呼叫軌跡 =======")
        
        # 串流思維與工具呼叫
        async for thought in response.thoughts:
            print(f"\033[93m[Thinking] {thought}\033[0m")
            
        async for tool_call in response.tool_calls:
            print(f"\033[96m[Tool Call] 準備呼叫: {tool_call.name}，參數: {tool_call.args}\033[0m")
            
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
