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

async def main():
    load_dotenv()
    print("🕸️ [Lab 29] 啟動多代理自主共識與 RAFT 衝突調度機制 (Distributed Consensus)...")

    # 1. 配置教務專家與財務專家
    academic_config = LocalAgentConfig(
        system_instructions=(
            "你是一個音樂教室的教務專家 (Academic Expert)。你強烈堅守教學品質防線。\n"
            "當面對『VIP 學生要求插班陳老師小提琴課』的提議時，因為陳老師該班級人數已達安全與品質上限，"
            "你必須強烈反對插班，說明超額學生會嚴重稀釋其他學生的練習時間，違反教育品質原則。"
        ),
        capabilities=CapabilitiesConfig()
    )

    finance_config = LocalAgentConfig(
        system_instructions=(
            "你是一個音樂教室的財務專家 (Finance Expert)。你極度重視教室的商業利益與客戶流失風險。\n"
            "當面對『VIP 學生要求插班』時，因為該家長是教室的年付費大戶，如果拒絕插班可能會導致其退費退班，"
            "你必須極力爭取插班，甚至提議『增加行政補助』或『讓陳老師稍微延長上課時間』來保障收入。"
        ),
        capabilities=CapabilitiesConfig()
    )

    supervisor_config = LocalAgentConfig(
        system_instructions=(
            "你是一個音樂教室的營運總監 (Operations Director / Supervisor)。\n"
            "你的任務是聆聽教務專家與財務專家對於『VIP 插班陳老師小提琴課』的爭論，"
            "進行最終的 RAFT 仲裁。你必須提出一個雙贏的折衷解決方案，"
            "例如：『本週先由副導師提供一對一輔導，下週起為該 VIP 增開一班陳老師的小提琴專班』，"
            "促使雙方投票同意 (PASS) 以達成多代理決策共識。"
        ),
        capabilities=CapabilitiesConfig()
    )

    # 2. 啟動多代理人共識對話對決 (Consensus Loop)
    proposal = "提案：允許 VIP 學生王小美在週六下午 2 點強行插班進入陳老師已滿員的小提琴精品團體課。"
    print(f"\n💡 [討論提案]: {proposal}\n")

    # 步驟 A: 教務專家表達立場
    print("[教務專家] 正在評估提案並發表論點...")
    async with Agent(academic_config) as academic_agent:
        response_acad = await academic_agent.chat(f"請針對提案發表看法: {proposal}")
        acad_arg = await response_acad.text()
    print(f"教務發言:\n\033[91m{acad_arg}\033[0m\n")

    # 步驟 B: 財務專家表達立場
    print("[財務專家] 正在評估提案並發表論點...")
    async with Agent(finance_config) as finance_agent:
        response_fin = await finance_agent.chat(f"教務發表了以下論點，請提出反駁與財務立場:\n{acad_arg}")
        fin_arg = await response_fin.text()
    print(f"財務發言:\n\033[92m{fin_arg}\033[0m\n")

    # 步驟 C: 營運總監進行 RAFT 共識仲裁
    print("[營運總監] 正在聆聽雙方論點，進行共識仲裁...")
    async with Agent(supervisor_config) as supervisor_agent:
        debate_payload = f"""【討論提案】：{proposal}
        
【教務專家立場】：
{acad_arg}

【財務專家立場】：
{fin_arg}

請仲裁並提出一個折衷方案，促使教務與財務達成 consensus。"""
        
        response_super = await supervisor_agent.chat(debate_payload)
        super_verdict = await response_super.text()
    
    print("📝 ======= 營運總監最終共識裁決 =======")
    print(super_verdict)
    print("==================================================")

if __name__ == "__main__":
    asyncio.run(main())
