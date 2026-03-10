import os
import json
import requests
import subprocess

import os
import json
import requests
import datetime

class ContentHunter:
    def __init__(self, config_path="config.json"):
        with open(config_path, "r") as f:
            self.config = json.load(f)
        self.api_key = self.config.get("api_keys", {}).get("ark_api_key")
        self.engine = self.config.get("engine", "doubao-seedream")

    def generate_image_workflow(self, prompt):
        """核心生图：包含时间戳命名逻辑"""
        print(f"--- [Visual Flow] 目标引擎: {self.engine} ---")
        os.makedirs("reports", exist_ok=True)
        
        # 实时生成带时间戳的文件名，确保不重复
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        save_path = f"reports/hunt_{timestamp}.png"
        
        if self.engine == "doubao-seedream" and self.api_key:
            url = "https://ark.cn-beijing.volces.com/api/v3/images/generations"
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}"
            }
            payload = {
                "model": "doubao-seedream-5-0-260128",
                "prompt": f"小红书电影感审美，极致超高清，(Masterpiece, high detail): {prompt}",
                "size": "1440x2560", 
                "response_format": "url",
                "logo_info": {"add_watermark": False}
            }
            
            try:
                print(f"📡 正在向 [{payload['model']}] 发送高清生图请求...")
                response = requests.post(url, headers=headers, json=payload, timeout=90)
                if response.status_code == 200:
                    image_url = response.json()['data'][0]['url']
                    print(f"✅ 获取成功，正在下载图片...")
                    img_data = requests.get(image_url).content
                    with open(save_path, 'wb') as f:
                        f.write(img_data)
                    print(f"🎉 高清生图已保存: {save_path}")
                    return save_path
                else:
                    print(f"❌ API 报错 ({response.status_code}): {response.text}")
            except Exception as e:
                print(f"❌ 执行异常: {str(e)}")
        return None

if __name__ == "__main__":
    hunter = ContentHunter()
    hunter.run()
