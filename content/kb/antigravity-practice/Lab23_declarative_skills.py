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

# =============================================================================
# 📁 專案規則檔 (.agents/AGENTS.md) 讀寫工具
# =============================================================================
AGENTS_MD_PATH = "./.agents/AGENTS.md"

def backup_rules() -> str:
    with open(AGENTS_MD_PATH, "r", encoding="utf-8") as f:
        return f.read()

def restore_rules(original_content: str):
    with open(AGENTS_MD_PATH, "w", encoding="utf-8") as f:
        f.write(original_content)
    print("🧹 [Rules 治理] 專案級規則檔 .agents/AGENTS.md 已還原清潔。")

def apply_rule(original_content: str, limit: int):
    rule_text = (
        f"\n\n## 2. 音樂教室行政政策 (Music Studio Policy)\n"
        f"*   **團體課補課次數上限**：每位學生每學期團體課補課上限為 **{limit} 次**。若申請次數超過此上限，行政人員必須堅定予以拒絕，並請家長體諒。"
    )
    with open(AGENTS_MD_PATH, "w", encoding="utf-8") as f:
        f.write(original_content + rule_text)
    print(f"📝 [Rules 治理] 已將補課規則寫入專案：團體課上限調整為 **{limit} 次**。")

# =============================================================================
# 🎬 主程式
# =============================================================================

async def run_agent_query(skills_dir: str, stage_name: str, query: str):
    config = LocalAgentConfig(
        system_instructions=(
            "你是一個音樂教室行政助手。你的工作是回答家長關於補課與颱風天停課的疑問。\n"
            "1. 你必須嚴格遵守專案級規則（.agents/AGENTS.md 中定義的『團體課補課次數上限』）來判定是否能補課。\n"
            "2. 你必須檢索你的 Skill 知識庫（music-ops 中的颱風天停課退費 SOP）來回答颱風天課程安排。\n"
            "請以繁體中文親切作答。"
        ),
        skills_paths=[skills_dir],
        capabilities=CapabilitiesConfig()
    )

    print(f"\n🎬 [{stage_name}] 正在實例化 Agent 並讀取聲明式規則...")
    async with Agent(config) as agent:
        response = await agent.chat(query)
        
        print(f"🧠 ======= Agent 思考與規則匹配軌跡 =======")
        async for thought in response.thoughts:
            print(f"\033[93m[Thinking] {thought}\033[0m")
            
        print("==================================================\n")
            
        print(f"📝 ======= Agent 最終答覆 =======")
        async for token in response:
            sys.stdout.write(token)
            sys.stdout.flush()
        print("\n==================================================")

async def main():
    load_dotenv()
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    skills_dir = os.path.join(current_dir, "skills")
    
    # 1. 備份原始 Rules
    original_content = backup_rules()
    
    query = (
        "您好，我是小明的家長。小明這學期請假比較多，他現在想申請第 3 次團體課補課，請問這樣可以嗎？\n"
        "另外，如果颱風天政府宣布停課，我們的課程會怎麼安排與退費？"
    )
    print(f"💡 [家長詢問] {query}\n")

    try:
        # ==========================================
        # 階段一：補課上限設為 2 次
        # ==========================================
        apply_rule(original_content, limit=2)
        await run_agent_query(skills_dir, "第一階段：上限 2 次", query)
        
        print("\n⏳ 模擬教務會議決議：因應家長反映，行政主管動態放寬補課限制為 4 次。")
        print("💡 [注意] 此處完全不修改任何 Python 程式碼，僅由背景寫入修改規則檔！")
        
        # ==========================================
        # 階段二：補課上限放寬為 4 次
        # ==========================================
        apply_rule(original_content, limit=4)
        await run_agent_query(skills_dir, "第二階段：上限 4 次", query)

    finally:
        # 3. 還原 Rules
        restore_rules(original_content)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"\n❌ 執行發生錯誤: {e}", file=sys.stderr)
