#!/bin/bash
# OpenClaw Content Hunter 一键安装脚本 (ClawdHub 增强版)
echo "🦞 正在为您配置 Content Hunter (爆款猎手)..."

# 1. 基础环境检查
if ! command -v openclaw &> /dev/null
then
    echo "❌ 未检测到 openclaw 环境，请先安装 OpenClaw。"
    exit 1
fi

# 2. 从 ClawdHub 安装核心技能 (由老大指定的高效源)
echo "📦 正在从 ClawdHub 安装必备技能..."
openclaw skills install guohongbin-git/xiaohongshu-cn --confirm
openclaw skills install agent-reach --confirm
openclaw skills install summarize --confirm
openclaw skills install nano-banana-pro --confirm

# 3. Python 依赖补全
pip install requests --quiet

# 4. 目录与配置文件初始化
mkdir -p scripts templates tests reports
if [ ! -f config.json ]; then
    cp config.example.json config.json
    echo "✅ 配置文件已就绪。"
fi

echo ""
echo "🎉 [恭喜] Content Hunter 已在您的 OpenClaw 中配置完成！"
echo "🚀 运行指令开启猎手模式: python3 scripts/content_radar.py"
