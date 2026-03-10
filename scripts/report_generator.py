import os

def generate_html_report(content, img_url="https://via.placeholder.com/300"):
    """生成精美的 HTML 报告页面"""
    html_template = f"""
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <title>OpenClaw 爆款猎手 - 每日报告</title>
        <style>
            body {{ font-family: sans-serif; padding: 20px; background: #f4f4f4; }}
            .card {{ background: white; padding: 20px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); max-width: 500px; margin: auto; }}
            h1 {{ color: #ff2442; font-size: 20px; text-align: center; }}
            .content {{ line-height: 1.6; white-space: pre-wrap; }}
            .image {{ width: 100%; border-radius: 8px; margin: 15px 0; }}
            .footer {{ text-align: center; font-size: 12px; color: #888; margin-top: 20px; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🦞 Content Hunter 爆款推文</h1>
            <div class="content">{content}</div>
            <img src="{img_url}" class="image" alt="AI配图预览">
            <div class="footer">由 OpenClaw 智能秘书生成</div>
        </div>
    </body>
    </html>
    """
    report_path = "reports/latest_report.html"
    os.makedirs("reports", exist_ok=True)
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(html_template)
    return report_path

# 演示逻辑集成
if __name__ == "__main__":
    test_content = "🔥 2026 见证奇迹：我用 OpenClaw 开启了第一份 AI 副业！\n\n别再只盯着聊天了，搞钱才是王道。#AI副业 #OpenClaw"
    path = generate_html_report(test_content)
    print(f"✅ HTML 报告已生成: {path}")
