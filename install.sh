#!/bin/bash
# OpenClaw Content Hunter 一键养虾安装脚本 (工业增强版)
echo "🦞 正在为您配置 Content Hunter (爆款猎手)..."

# 1. Python 依赖检查
echo "📦 正在检查 Python 依赖工具..."
pip install requests --quiet

# 2. 核心技能检测与自动安装
SKILLS_LIST=$(openclaw skills list)
function ensure_skill() {
    SKILL_NAME=$1
    if [[ $SKILLS_LIST != *"$SKILL_NAME"* ]]; then
        echo "⚠️ 正在安装缺失技能 [$SKILL_NAME]..."
        openclaw skills install $SKILL_NAME --confirm
    fi
}
ensure_skill "xiaohongshu"
ensure_skill "agent-reach"
ensure_skill "summarize"

# 3. 目录与配置文件
mkdir -p scripts templates tests reports
if [ ! -f config.json ]; then
    cp config.example.json config.json
fi

echo "✅ 配置完成！如果您想使用豆包 Seedream，请确保已 export ARK_API_KEY。"
echo "🚀 运行测试: python3 scripts/content_radar.py"
