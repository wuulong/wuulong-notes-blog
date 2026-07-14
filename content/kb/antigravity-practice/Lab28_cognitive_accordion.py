import asyncio
import sys
import os
import json
from google.antigravity import Agent, LocalAgentConfig, CapabilitiesConfig, types

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
# 🛠️ 1. 定義診斷輔助工具
# =============================================================================
def check_patient_vitals(patient_name: str) -> str:
    """查詢病患目前的生理量測數據。"""
    print(f"\n🔍 [工具執行] 查詢生理量測：{patient_name}")
    return "血壓: 145/95 mmHg, 心跳: 88次/分, 體溫: 37.2°C"

def check_allergy_history(patient_name: str) -> str:
    """查詢病患的藥物過敏歷史。"""
    print(f"\n🔍 [工具執行] 查詢過敏歷史：{patient_name}")
    return "對『盤尼西林 (Penicillin)』有嚴重過敏史。"

# =============================================================================
# 🎬 2. 主程式 ( 長週期記憶手風琴壓縮與對話接力 )
# =============================================================================
async def main():
    load_dotenv()
    print("🌌 [Lab 28] 啟動心智手風琴 (Cognitive Accordion) 壓縮與認知接力...")

    # -------------------------------------------------------------------------
    # 📌 階段一：診斷 Agent 進行首輪推理與診斷
    # -------------------------------------------------------------------------
    config_1 = LocalAgentConfig(
        system_instructions=(
            "你是在宅診所的第一階段診斷 Agent。你的任務是評估病患的身體狀況並給予初步診斷。\n"
            "你必須先調用 check_patient_vitals 查詢生理數據，並調用 check_allergy_history 確認過敏史，"
            "最後給出詳細的臨床診斷回覆。"
        ),
        tools=[check_patient_vitals, check_allergy_history],
        capabilities=CapabilitiesConfig()
    )

    prompt_1 = "請幫我看看王小明的生理狀況，他今天覺得頭痛頭暈。"
    print(f"\n💡 [階段一 使用者提問]: '{prompt_1}'")

    async with Agent(config_1) as agent_1:
        response_1 = await agent_1.chat(prompt_1)
        
        # 擷取 thoughts 軌跡與工具紀錄
        chunks = await response_1.resolve()
        trajectory = []
        for chunk in chunks:
            if isinstance(chunk, types.Thought):
                trajectory.append({"type": "Thought", "content": chunk.text})
            elif isinstance(chunk, types.ToolCall):
                trajectory.append({"type": "ToolCall", "name": chunk.name, "args": chunk.args})
            elif isinstance(chunk, types.ToolResult):
                trajectory.append({"type": "ToolResult", "output": chunk.output})

        reply_1 = await response_1.text()
        print(f"\n📝 [階段一 醫生最終回覆]:\n{reply_1}\n")

    # -------------------------------------------------------------------------
    # 📌 階段二：Archiver Agent 進行手風琴壓縮 (Cognitive Squeeze)
    # -------------------------------------------------------------------------
    archiver_instructions = (
        "你是一個記憶手風琴歸檔者。你的任務是閱讀上一階段 Agent 的詳細執行軌跡 JSON，"
        "忽略其中冗長、無意義的思考與工具調用細節，只提取『核心決策節點與實體狀態變化』。\n"
        "請輸出一份極簡的『認知快照 (Cognitive Snapshot)』作為下一階段 Agent 的記憶。格式需包含：\n"
        "- 症狀與血壓結果\n"
        "- 過敏硬性限制\n"
        "- 當前診斷結論"
    )
    
    config_archiver = LocalAgentConfig(
        system_instructions=archiver_instructions,
        capabilities=CapabilitiesConfig()
    )

    print(" Squeezing thoughts... 正在進行心智軌跡壓縮...")
    async with Agent(config_archiver) as archiver:
        response_archive = await archiver.chat(f"執行軌跡 JSON: {json.dumps(trajectory)}")
        snapshot = await response_archive.text()
    
    print(f"\n🌌 [生成的認知快照 (Cognitive Snapshot)]:\n{snapshot}\n")

    # -------------------------------------------------------------------------
    # 📌 階段三：階段二全新 Agent 載入快照接力對話
    # -------------------------------------------------------------------------
    config_2 = LocalAgentConfig(
        system_instructions=(
            f"你是在宅診所的第二階段護理與諮詢 Agent。你剛剛接收了第一階段傳遞給你的記憶快照：\n"
            f"=== 認知快照 ===\n{snapshot}\n===============\n"
            "請基於這份快照記憶，親切回答病患後續的照護與用藥諮詢。"
        ),
        capabilities=CapabilitiesConfig()
    )

    prompt_2 = "那我回家後需要注意什麼？可以吃一般的消炎止痛藥嗎？"
    print(f"💡 [階段二 使用者追問]: '{prompt_2}'")

    async with Agent(config_2) as agent_2:
        response_2 = await agent_2.chat(prompt_2)
        reply_2 = await response_2.text()
        print(f"\n📝 [階段二 護理諮詢最終回覆]:\n{reply_2}\n")

if __name__ == "__main__":
    asyncio.run(main())
