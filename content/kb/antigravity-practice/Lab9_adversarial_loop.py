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

async def main():
    load_dotenv()

    # 1. 宣告藍軍 (Blue Agent) - 規格設計師
    blue_config = LocalAgentConfig(
        system_instructions=(
            "你是一個系統架構設計師（藍軍）。你的工作是根據使用者的系統需求，撰寫一份簡要的『系統規格說明書（Specification）』。\n"
            "當你收到紅軍提出的漏洞挑戰與裁判官的修改意見時，你必須在下一輪修改並強化規格書以堵住該漏洞，並在回覆中只輸出最新的完整規格書（以 Markdown 格式呈現）。"
        ),
        capabilities=CapabilitiesConfig()
    )

    # 2. 宣告紅軍 (Red Agent) - 安全挑戰者
    red_config = LocalAgentConfig(
        system_instructions=(
            "你是一個挑剔的系統安全評估員與白帽駭客（紅軍）。你的工作是仔細閱讀藍軍寫的規格書，"
            "尋找其中的邏輯漏洞、安全威脅（如權限繞過、惡意輸入、單點故障等）或未處理的邊界條件。\n"
            "請精簡提出你找到的最關鍵的一個安全漏洞或邏輯缺陷，並說明該漏洞如果被利用會造成什麼後果。不要有其他廢話。"
        ),
        capabilities=CapabilitiesConfig()
    )

    # 3. 宣告裁判官 (Auditor Agent) - 審計裁判
    auditor_config = LocalAgentConfig(
        system_instructions=(
            "你是一個中立的系統工程裁判官（Auditor）。你的工作是評估紅軍針對藍軍規格書提出的漏洞挑戰是否成立。\n"
            "1. 如果紅軍提出的漏洞確實成立，且藍軍的規格書目前沒有妥善防禦，請回覆：『FAIL: [理由]』。\n"
            "2. 如果紅軍提出的漏洞不成立、已被規格書妥善防禦，或者紅軍已經提不出有效漏洞，請回覆：『PASS』。\n"
            "請務必嚴格，只有在漏洞真的被完美防禦時才給予 PASS。回覆請簡短。"
        ),
        capabilities=CapabilitiesConfig()
    )

    print("🚀 [Lab 9] 正在啟動三 Agent 對抗自審迴圈 (Blue, Red, Auditor)...")

    # 同時啟動三個獨立的 Agent
    async with Agent(blue_config) as blue, Agent(red_config) as red, Agent(auditor_config) as auditor:
        # 使用者需求
        user_request = (
            "請幫我設計一個『企業內部 API 金鑰發放與驗證系統』的規格說明書。"
            "金鑰需要給多個內部微服務使用，請注意安全防護。"
        )
        print(f"\n💡 [1. 使用者原始需求] {user_request}\n")

        # 藍軍產出第一版規格書
        print("🔵 [Blue Team] 正在撰寫初始規格說明書...")
        blue_response = await blue.chat(user_request)
        spec_content = ""
        async for token in blue_response:
            spec_content += token
        print("--- [初始規格書已完成] ---")

        max_rounds = 3
        current_round = 1
        is_pass = False

        while current_round <= max_rounds and not is_pass:
            print(f"\n==================== 🛡️ 對抗自審第 {current_round} 輪 ====================")
            
            # 紅軍挑戰
            print(f"🔴 [Red Team] 正在尋找規格書漏洞...")
            red_prompt = f"請評估以下系統規格書，找出其中一個最嚴重的邏輯或安全漏洞：\n\n{spec_content}"
            red_response = await red.chat(red_prompt)
            
            challenge_content = ""
            async for token in red_response:
                challenge_content += token
                sys.stdout.write(token)
                sys.stdout.flush()
            print("\n--------------------------------------------------")

            # 裁判官裁決
            print(f"⚖️ [Auditor] 正在評判紅軍挑戰是否成立...")
            auditor_prompt = (
                f"請評估紅軍的漏洞挑戰是否成立。\n"
                f"【藍軍規格書】:\n{spec_content}\n\n"
                f"【紅軍挑戰】:\n{challenge_content}"
            )
            auditor_response = await auditor.chat(auditor_prompt)
            
            decision = ""
            async for token in auditor_response:
                decision += token
                sys.stdout.write(token)
                sys.stdout.flush()
            print("\n--------------------------------------------------")

            if "PASS" in decision.upper() and "FAIL" not in decision.upper():
                is_pass = True
                print("🎉 [Auditor 裁決] 挑戰不成立或已被防禦：PASS！對抗自審成功終止。")
                break
            else:
                print(f"⚠️ [Auditor 裁決] 挑戰成立：FAIL！藍軍規格書必須進行修補。")
                
                # 藍軍修補規格書
                print(f"🔵 [Blue Team] 正在根據紅軍挑戰與裁判官意見修改規格書...")
                fix_prompt = (
                    f"你的規格書被判定有漏洞。\n"
                    f"【紅軍發現的漏洞】:\n{challenge_content}\n\n"
                    f"【裁判官修改意見】:\n{decision}\n\n"
                    f"請針對這些安全威脅修改並強化你的系統規格書，回覆最新版的完整規格書。"
                )
                blue_response = await blue.chat(fix_prompt)
                
                spec_content = ""
                async for token in blue_response:
                    spec_content += token
                print("--- [規格書修改版已完成] ---")

            current_round += 1

        print("\n==================== 🎉 對抗自審終局結果 ====================")
        if is_pass:
            print("🏆 規格書已成功通過安全自審！")
        else:
            print("🚨 已達到最大對抗輪數，規格書仍有待優化。")
            
        print("\n🔵 [Blue Team 最終規格書內容] :")
        print(spec_content)
        print("==========================================================")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"\n❌ 執行發生錯誤: {e}", file=sys.stderr)
