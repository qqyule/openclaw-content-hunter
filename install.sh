#!/bin/bash
# OpenClaw Content Hunter 一键养虾安装脚本
echo "🦞 正在为您配置 Content Hunter (爆款猎手)..."

# 1. 检查环境
if ! command -v openclaw &> /dev/null
then
    echo "❌ 未检测到 openclaw 环境，请先安装 OpenClaw。"
    exit
fi

# 2. 目录初始化
mkdir -p scripts templates tests

# 3. 提示配置
echo "✅ 项目结构已就绪。"
echo "💡 请确保您已在 openclaw 中启用以下技能："
echo "   - xiaohongshu (用于抓取小红书)"
echo "   - web_search (用于抓取 Twitter/X)"
echo "   - summarize (用于爆款拆解)"
echo ""
echo "🚀 您现在可以运行: openclaw cron add --task '运行 Content Hunter 监控 AI 副业赛道' --schedule 'every 6 hours'"
echo "🎉 祝您在‘养虾挑战赛’中旗开得胜！"
