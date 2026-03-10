import os
import json

def scan_hot_content(platform="xhs", keyword="AI副业"):
    print(f"--- 猎手模式开启: 平台 {platform}，关键词 {keyword} ---")
    # 模拟 OpenClaw 技能调用逻辑
    # 实际运行中，用户通过 openclaw cron 触发
    mock_data = [
        {"title": "普通人如何用 AI 赚第一桶金", "likes": 5600, "platform": "xhs"},
        {"title": "OpenClaw 自动化工作流实战", "likes": 3200, "platform": "x"}
    ]
    return mock_data

if __name__ == "__main__":
    results = scan_hot_content()
    for item in results:
        print(f"捕捉到爆款: {item['title']} (点赞: {item['likes']})")
