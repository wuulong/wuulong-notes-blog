import asyncio
import sys
import os
import sqlite3
from google.antigravity import Agent, LocalAgentConfig, CapabilitiesConfig
from google.antigravity.hooks.hooks import PreToolCallDecideHook, HookContext, HookResult
from google.antigravity.types import ToolCall

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
# 1. 初始化 SQLite 記憶體資料庫
# ==========================================
db_conn = sqlite3.connect(":memory:", check_same_thread=False)
# 啟用外鍵約束
db_conn.execute("PRAGMA foreign_keys = ON;")

# 建立表格
db_conn.execute("""
CREATE TABLE districts (
    district_code TEXT PRIMARY KEY,
    district_name TEXT NOT NULL
);
""")

db_conn.execute("""
CREATE TABLE pois (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    poi_name TEXT UNIQUE NOT NULL,
    district_code TEXT NOT NULL,
    latitude REAL CHECK(latitude BETWEEN 21.0 AND 26.0),
    longitude REAL CHECK(longitude BETWEEN 119.0 AND 123.0),
    FOREIGN KEY (district_code) REFERENCES districts(district_code)
);
""")

# 插入合規行政區劃
db_conn.executemany("INSERT INTO districts (district_code, district_name) VALUES (?, ?);", [
    ('TW-TPE-01', '臺北市大安區'),
    ('TW-TNN-01', '臺南市中西區'),
    ('TW-NWT-01', '新北市板橋區')
])
db_conn.commit()

# ==========================================
# 2. 定義資料庫操作工具 (Tools)
# ==========================================
def query_valid_districts() -> list:
    """
    查詢目前資料庫中所有合規的行政區劃代碼與名稱。
    當遇到行政區劃代碼外鍵約束錯誤時，可使用此工具查詢合規的代碼。

    Returns:
        包含 (district_code, district_name) 的清單。
    """
    print("\n🔍 [工具執行] 正在查詢合規的行政區劃代碼...")
    cursor = db_conn.cursor()
    cursor.execute("SELECT district_code, district_name FROM districts;")
    results = cursor.fetchall()
    return results

def insert_poi(poi_name: str, district_code: str, latitude: float, longitude: float) -> str:
    """
    嘗試將一筆 POI 資料寫入資料庫中。

    Args:
        poi_name: POI 名稱（必須是正體中文，且在資料庫中必須唯一）
        district_code: 行政區劃代碼（必須存在於 districts 表中，例如 'TW-TPE-01'）
        latitude: 緯度（必須在 21.0 到 26.0 之間）
        longitude: 經度（必須在 119.0 到 123.0 之間）

    Returns:
        寫入結果狀態或詳細錯誤訊息。
    """
    print(f"\n💾 [工具執行] 嘗試寫入 POI: {poi_name} ({district_code})...")
    cursor = db_conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO pois (poi_name, district_code, latitude, longitude) VALUES (?, ?, ?, ?);",
            (poi_name, district_code, latitude, longitude)
        )
        db_conn.commit()
        return f"成功寫入 POI: {poi_name}"
    except sqlite3.IntegrityError as e:
        db_conn.rollback()
        error_msg = str(e)
        print(f"   ❌ 寫入失敗 (IntegrityError): {error_msg}")
        return f"寫入失敗：違反資料庫完整性約束。詳細錯誤原因: {error_msg}"
    except sqlite3.Error as e:
        db_conn.rollback()
        error_msg = str(e)
        print(f"   ❌ 寫入失敗 (DatabaseError): {error_msg}")
        return f"寫入失敗：資料庫錯誤。詳細錯誤原因: {error_msg}"

def query_pois() -> list:
    """
    查詢資料庫中目前已成功寫入的所有 POI 資料。

    Returns:
        包含 POI 資料清單。
    """
    print("\n🔍 [工具執行] 正在查詢已寫入 of POI 資料...")
    cursor = db_conn.cursor()
    cursor.execute("SELECT poi_name, district_code, latitude, longitude FROM pois;")
    results = cursor.fetchall()
    return results

# ==========================================
# 3. 定義合規稽核 Hook (RAG / 政策防線)
# ==========================================
class ComplianceVerifierHook(PreToolCallDecideHook):
    async def run(self, context: HookContext, data: ToolCall) -> HookResult:
        # 當 Agent 嘗試呼叫 insert_poi 時進行合規審查
        if data.name == "insert_poi" or data.name == insert_poi.__name__:
            poi_name = data.args.get("poi_name", "")
            
            print(f"\n🛡️ [Hook 門禁稽核] 偵測到 POI 寫入請求: {poi_name}")
            
            # 檢查是否含有簡體字
            simplified_chars = {"庙": "廟", "门": "門", "区": "區"}
            detected_chars = [c for c in simplified_chars if c in poi_name]
            
            if detected_chars:
                suggestions = ", ".join([f"'{c}' -> '{simplified_chars[c]}'" for c in detected_chars])
                print(f"   ❌ 合規政策拒絕：偵測到簡體中文字元 {detected_chars}！")
                return HookResult(
                    allow=False,
                    message=(
                        f"拒絕寫入！根據地名合規政策，POI 名稱必須使用繁體正體中文。"
                        f"偵測到簡體字元：{detected_chars}。請修正名稱後重新寫入。建議轉換：{suggestions}"
                    )
                )
            
            print("   ✅ 合規政策檢查通過。")
            return HookResult(allow=True)
            
        return HookResult(allow=True)


async def main():
    load_dotenv()
    
    # 設定 Agent
    config = LocalAgentConfig(
        system_instructions=(
            "你是一個專業的地理資訊資料合規工程師。"
            "你的任務是將外部傳入的 POI 髒數據導入本地 SQLite 資料庫。"
            "如果呼叫 insert_poi 失敗或被拒絕，請詳細閱讀失敗的約束原因並進行自我修正："
            "1. 若因簡體中文被 Hook 拒絕，請使用正體中文（繁體）修正地名後重新寫入。\n"
            "2. 若因外鍵約束錯誤 (FOREIGN KEY constraint failed)，說明該行政區劃代碼不存在於主表，"
            "   請呼叫 query_valid_districts 工具查詢合規的代碼，並找到最匹配的代碼（如台南對應 TW-TNN-01）修正後重新寫入。\n"
            "3. 若因唯一性約束錯誤 (UNIQUE constraint failed)，說明該資料已經導入過，請直接安全跳過該筆資料。\n"
            "完成所有資料處理後，請呼叫 query_pois 工具確認最終導入結果，並向使用者報告總結。"
        ),
        tools=[query_valid_districts, insert_poi, query_pois],
        hooks=[ComplianceVerifierHook()],
        capabilities=CapabilitiesConfig(),
    )

    print("🚀 [Lab 7] 正在初始化 Data Compliance Agent (Stateful Loop)...")
    
    async with Agent(config) as agent:
        prompt = (
            "請幫我將以下外部原始 POI 數據導入資料庫：\n"
            "1. {'poi_name': '臺大校門', 'district_code': 'TW-TPE-01', 'latitude': 25.017, 'longitude': 121.539}\n"
            "2. {'poi_name': '台南孔庙', 'district_code': 'TW-TNN-99', 'latitude': 22.990, 'longitude': 120.204}\n"
            "3. {'poi_name': '臺大校門', 'district_code': 'TW-TPE-01', 'latitude': 25.017, 'longitude': 121.539}\n"
            "\n導入結束後，請列出資料庫中的所有 POI 記錄。"
        )
        print(f"\n💡 使用者提問:\n{prompt}\n")
        
        response = await agent.chat(prompt)
        
        print("🧠 ======= Agent 思考與自動反思循環軌跡 =======")
        async for thought in response.thoughts:
            print(f"\033[93m[Thinking] {thought}\033[0m")
            
        async for tool_call in response.tool_calls:
            print(f"\033[96m[Tool Call] 呼叫工具: {tool_call.name}\033[0m")
            
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
    finally:
        db_conn.close()
