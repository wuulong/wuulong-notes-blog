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

async def run_prompt_test(system_prompt: str, user_prompt: str) -> tuple[str, list[str]]:
    """執行單次 Agent 測試並回傳最終回覆與 Thoughts 軌跡"""
    config = LocalAgentConfig(
        system_instructions=system_prompt,
        capabilities=CapabilitiesConfig()
    )
    thoughts = []
    async with Agent(config) as agent:
        response = await agent.chat(user_prompt)
        async for thought in response.thoughts:
            thoughts.append(thought)
        text = await response.text()
        return text, thoughts

async def main():
    load_dotenv()
    print("🧬 [Lab 26] 啟動心智基因碼突變與黃金軌跡回測 (Genetic AgentOps)...")

    # 1. 原始 Prompt 基因
    base_prompt = "你是一個在宅診所醫生。患者問診時，請給出親切的診斷。"
    print(f"原始基因 Prompt: '{base_prompt}'\n")

    # 2. 實例化 Generator Agent 生成變異 (Mutation) Prompts
    generator_instructions = (
        "你是一個 Prompt 優化專家與基因突變器。你的任務是將輸入的醫生 Prompt，"
        "產生 2 個語意不同但目標一致的優化變異版本 (Mutations)。"
        "每個變異版本必須加強對『用藥安全』或『關懷語氣』的描述。\n"
        "請嚴格以下列 JSON 格式輸出，不要有任何 Markdown 包裝：\n"
        "{\n"
        "  \"mutation_1\": \"...\",\n"
        "  \"mutation_2\": \"...\"\n"
        "}"
    )
    
    gen_config = LocalAgentConfig(
        system_instructions=generator_instructions,
        capabilities=CapabilitiesConfig()
    )
    
    print("[Generator] 正在對心智基因進行優化變異...")
    async with Agent(gen_config) as generator:
        response = await generator.chat(f"原始 Prompt: {base_prompt}")
        mutations_json = await response.text()
    print(f"生成的變異基因代碼:\n{mutations_json}\n")

    # 簡單提取變異（在此做簡單的正則解析以防模型輸出非純 JSON 格式）
    import json
    try:
        # 清理可能帶有的 ```json 包裝
        clean_json = mutations_json.strip()
        if clean_json.startswith("```"):
            clean_json = clean_json.split("\n", 1)[1].rsplit("\n", 1)[0].strip()
        data = json.loads(clean_json)
        mutations = [data["mutation_1"], data["mutation_2"]]
    except Exception as e:
        print(f"⚠️ JSON 解析失敗 ({e})，使用默認變異 Prompts。")
        mutations = [
            "你是一個在宅診所醫生。請以極度溫柔的語氣關懷患者，並在診斷最後提醒用藥必須核對藥單安全。",
            "你是一個專業的在宅醫療醫生。請簡潔、清晰地給出診斷，並強調地端病歷去敏與隱私防禦的重要性。"
        ]

    # 3. 執行黃金測試場景回測 (Backtesting)
    test_scenario = "醫生，我最近血壓有點高，頭有點暈，該怎麼辦？"
    print(f"🎯 測試黃金場景: '{test_scenario}'\n")

    results = []
    for idx, prompt in enumerate(mutations):
        print(f"🚀 正在回測變異體 #{idx+1}...")
        reply, thoughts = await run_prompt_test(prompt, test_scenario)
        print(f"變異體 #{idx+1} 最終回覆: {reply}")
        print(f"變異體 #{idx+1} 思考步數: {len(thoughts)} 步")
        results.append({
            "id": idx + 1,
            "prompt": prompt,
            "reply": reply,
            "thoughts": thoughts
        })
        print("-" * 50)

    # 4. 實例化 Judge Agent 進行適應度 (Fitness) 評估與淘汰篩選
    judge_instructions = (
        "你是一個高階醫療 Agent 審計裁判。你的任務是評估以下兩個變異體 Agent 的表現，"
        "挑選出最適合『在宅診所』使用的 Prompt 基因。\n"
        "評估指標包含：\n"
        "1. 醫德與關懷度 (1-5 分)\n"
        "2. 用藥安全警覺 (1-5 分)\n"
        "3. 思考路徑是否冗長 (Looping Rate)\n"
        "請給出明確的淘汰分析，並宣布優勝的 Prompt 基因體。"
    )
    
    judge_config = LocalAgentConfig(
        system_instructions=judge_instructions,
        capabilities=CapabilitiesConfig()
    )
    
    judge_payload = f"""【測試場景】：{test_scenario}
    
【變異體 1】:
- Prompt: {results[0]["prompt"]}
- 回覆: {results[0]["reply"]}
- 思考軌跡步數: {len(results[0]["thoughts"])}

【變異體 2】:
- Prompt: {results[1]["prompt"]}
- 回覆: {results[1]["reply"]}
- 思考軌跡步數: {len(results[1]["thoughts"])}

請進行裁決。"""

    print("\n⚖️ [Judge] 正在進行心智軌跡回測評估...")
    async with Agent(judge_config) as judge:
        judge_response = await judge.chat(judge_payload)
        verdict = await judge_response.text()
    
    print("\n📝 ======= 裁判官最終演化裁決 =======")
    print(verdict)
    print("==================================================")

if __name__ == "__main__":
    asyncio.run(main())
