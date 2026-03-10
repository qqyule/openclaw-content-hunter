# Visual Flow: 中文高质量生图工作流 (基于 OpenClaw)

## 1. 核心提示词框架 (Chinese Content Aesthetics)
我们在 `scripts/content_radar.py` 中集成了以下高质量 Prompt 生成逻辑：

### 📸 小红书精致风格 (XHS Aesthetic)
**通用后缀**: 
> "Soft lighting, minimalist interior, high quality macro photography, aesthetic composition, lifestyle vibe, Nikon Z9, film-like color grading, 8k resolution."

**中文关键词映射**:
- "简约" -> "Minimalist"
- "日系风" -> "Japanese minimalist style"
- "科技感" -> "Sleek tech desk, ambient blue light"

## 2. 工具调用说明 (Tools)
该工作流支持通过 OpenClaw 技能一键产出：
```bash
openclaw skill call nano-banana-pro --task "基于 {MY_TEXT} 生成一张高质感的小红书头图"
```

## 3. 高质量示例 (Example)
**文案**: "2026 年，我用 AI 赚了第一桶金。"
**配套图**: 一个在极简书房里，阳光洒在干净的桌面上，旁边是一杯咖啡和一台正在运行 AI 助力的笔记电脑。
