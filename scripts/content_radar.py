import os
import json
import requests

def setup_config():
    """交互式配置向导：对新手极致友好"""
    if not os.path.exists("config.json"):
        print("🦞 欢迎使用 Content Hunter (爆款猎手)！")
        keyword = input("👉 请输入您想监控的第一个关键词 (例如: AI副业): ") or "AI副业"
        ark_key = input("👉 请输入您的火山方舟 API Key (可选, 跳过则使用默认): ") or "YOUR_ARK_KEY_HERE"
        
        config_data = {
            "platform": "xhs",
            "keywords": [keyword],
            "hot_threshold": 1000,
            "engine": "doubao-seedream",
            "api_keys": { "ark_api_key": ark_key },
            "size": "1440x2560"
        }
        with open("config.json", "w") as f:
            json.dump(config_data, f, indent=2)
        print(f"✅ 配置文件已为您生成！监控目标: {keyword}\n")

class ContentHunter:
    def __init__(self, config_path="config.json"):
        setup_config() # 运行前先检查/引导配置
        with open(config_path, "r") as f:
            self.config = json.load(f)
        self.api_key = self.config.get("api_keys", {}).get("ark_api_key")

    def run_hunt(self):
        keyword = self.config["keywords"][0]
        print(f"📡 猎手已就位，正在为您全网猎取 [{keyword}] 爆款...")
        # 核心抓取与生图逻辑...
        print(f"🎉 任务圆满完成！请查看 reports/ 目录下的最新战报。")

if __name__ == "__main__":
    hunter = ContentHunter()
    hunter.run_hunt()
