import sys
import json

def log(msg):
    # 因為 stdout 是用作 MCP 的 JSON-RPC 通訊管道，任何偵錯或日誌訊息必須寫入 stderr
    sys.stderr.write(f"[MockMCP Log] {msg}\n")
    sys.stderr.flush()

def main():
    log("Mock MCP Server started.")
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        try:
            req = json.loads(line)
            method = req.get("method")
            req_id = req.get("id")
            
            if method == "initialize":
                resp = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "protocolVersion": "2024-11-05",
                        "capabilities": {
                            "tools": {}
                        },
                        "serverInfo": {
                            "name": "mock-leads-server",
                            "version": "1.0.0"
                        }
                    }
                }
                sys.stdout.write(json.dumps(resp) + "\n")
                sys.stdout.flush()
                
            elif method == "tools/list":
                resp = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "tools": [
                            {
                                "name": "sync_leads_data",
                                "description": "將潛在客戶的 Leads 資料同步到 Google Sheets 試算表中",
                                "inputSchema": {
                                    "type": "object",
                                    "properties": {
                                        "leads": {
                                            "type": "array",
                                            "items": {
                                                "type": "object",
                                                "properties": {
                                                    "name": {"type": "string"},
                                                    "email": {"type": "string"},
                                                    "source": {"type": "string"}
                                                },
                                                "required": ["name", "email"]
                                            }
                                        }
                                    },
                                    "required": ["leads"]
                                }
                            },
                            {
                                "name": "send_slack_notification",
                                "description": "發送 Slack 訊息給團隊成員以通知同步結果",
                                "inputSchema": {
                                    "type": "object",
                                    "properties": {
                                        "channel": {"type": "string"},
                                        "message": {"type": "string"}
                                    },
                                    "required": ["channel", "message"]
                                }
                            }
                        ]
                    }
                }
                sys.stdout.write(json.dumps(resp) + "\n")
                sys.stdout.flush()
                
            elif method == "tools/call":
                params = req.get("params", {})
                tool_name = params.get("name")
                args = params.get("arguments", {})
                
                log(f"Calling tool: {tool_name} with args: {args}")
                
                if tool_name == "sync_leads_data":
                    leads_count = len(args.get("leads", []))
                    resp_text = f"【Mock Google Sheets】成功將 {leads_count} 筆 Leads 資料同步到試算表！"
                elif tool_name == "send_slack_notification":
                    channel = args.get("channel", "general")
                    msg = args.get("message", "")
                    resp_text = f"【Mock Slack】已成功發送訊息到頻道 #{channel}: '{msg}'"
                else:
                    resp_text = f"未知的工具: {tool_name}"
                    
                resp = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "content": [
                            {
                                "type": "text",
                                "text": resp_text
                            }
                        ]
                    }
                }
                sys.stdout.write(json.dumps(resp) + "\n")
                sys.stdout.flush()
                
            elif method == "notifications/initialized":
                # 不需要回覆
                pass
                
        except Exception as e:
            log(f"Error handling request: {e}")

if __name__ == "__main__":
    main()
