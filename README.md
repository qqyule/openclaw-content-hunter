# OpenClaw Content Hunter (爆款猎手) 🦞

> **24H 全网灵感收割机**：从「全网监控」到「深度拆解」，从「爆款文案」到「中文生图」，一站式助你成为自媒体大 V。

---

## 🦞 养虾挑战赛：一键养虾指南 (Moltbot 专享)

想要让你的 OpenClaw 变身为“爆款猎手”？只需将以下指令复制到你的 OpenClaw 会话中：

`为我安装这个项目 https://github.com/qqyule/openclaw-content-hunter/install.sh`

_(注：系统会自动完成脚本拉取、权限设置及定时任务配置，助你 1 分钟完成参赛作品部署。)_

---

## 🌟 核心亮点

- **全平台监控**：同时支持 **小红书 (XHS)** 和 **Twitter (X)** 的实时热点监控。
- **爆款逻辑引擎**：利用 Gemini 3 / Qwen-Max 深度拆解万赞笔记背后的流量密码。
- **中文生图流**：针对中文互联网审美优化的 Prompt 工作流，生成高质感配图。
- **24/7 阿里云运行**：部署在阿里云轻量服务器或无影云电脑，随时随地接收爆款简报。

## 🚀 3 分钟极速上手

### 1. 前置要求

- 已安装 [OpenClaw (Moltbot)](https://github.com/clawdbot/clawdbot).
- 已启用 `xiaohongshu` 和 `web_search` 技能。

### 2. 快速克隆与配置

```bash
git clone https://github.com/qqyule/openclaw-content-hunter.git
cd openclaw-content-hunter
# 配置你的关键词监控
cp config.example.json config.json
```

### 3. 一键开启猎手模式

```bash
openclaw cron add --task "运行 Content Hunter 扫描小红书 AI 赛道，并生成报告" --schedule "every 3 hours"
```

---

## 🛠️ 功能模块

### 1. 流量雷达 (Radar)

实时抓取指定赛道的高互动内容，过滤掉无价值的广告和水文。

### 2. 文案实验室 (Copywriting Lab)

分析原始文案的“钩子标题”、“冲突点”、“利益点”并生成符合平台调性的差异化副本（保持 XHS 风格的 Emoji）。

### 3. 生图工作流 (Visual Flow)

根据文案自动生成生图指令，使用高性能多模态模型产出高质量中文配图方案。

---

## 🤝 贡献与反馈

欢迎在 Issue 中提出建议，或提交 PR！

---

## 📜 许可证

MIT License.
