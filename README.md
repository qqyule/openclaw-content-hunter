# OpenClaw Content Hunter (爆款猎手) 🦞

> **24H 全网灵感收割机**：从「全网监控」到「深度拆解」，从「爆款文案」到「高清中文生图」，一站式助你成为自媒体大 V。

---

## 🦞 极简一键部署 (含环境自修复)

即便你的 OpenClaw 是「纯净版」，我们也为你准备了全自动安装脚本。它会自动检测并安装缺少的 `xiaohongshu`、`agent-reach (Twitter)` 和 `summarize` 技能。

只需将以下指令复制到你的 OpenClaw 会话中：

```
为我安装这个项目 https://github.com/qqyule/openclaw-content-hunter/install.sh
```

_(注：系统会自动完成脚本拉取、权限设置、必备技能安装及定时任务配置，助你 1 分钟完成参赛作品部署。)_

---

## 🌟 核心亮点

- **交互式配置向导 (User Wizard)**：首创交互式引导，只需输入关键词，脚本自动生成配置文件，新手 0 门槛开机。
- **双重文案润色逻辑**：内置「初稿生成+主编精修」双阶段 AI 流程，确保每一篇推文都具备万赞潜力。
- **2K 高清 & 去水印生图**：深度适配 **豆包 Seedream 5.0 Lite** (原生 2K 1440x2560 导出)，针对中文审美深度优化，输出无水印高清大片。
- **全平台监控**：同时支持 **小红书 (XHS)** 和 **Twitter (X)** 的实时热点监控。
- **24/7 阿里云运行**：部署在阿里云轻量服务器或无影云电脑，随时随地接收爆款简报。

## 🚀 3 分钟上手指南 (手动版)

### 1. 克隆与安装

```bash
git clone https://github.com/qqyule/openclaw-content-hunter.git
cd openclaw-content-hunter
# 运行安装脚本（极其推荐，自动安装所有依赖与技能）
bash install.sh
```

### 2. 交互式启动

```bash
# 第一次运行会引导你输入 keywords 和 API Key
python3 scripts/content_radar.py
```

### 3. 一键开启猎手模式 (自动化运行)

```bash
openclaw cron add --task "运行 Content Hunter 扫描 [你的关键词] 赛道，并生成报告" --schedule "every 6 hours"
```

---

## 🛠️ 功能模块简介

### 1. 流量雷达 (Radar)

实时抓取指定赛道的高互动内容，过滤虚假信息，直击爆款核心。

### 2. 文案实验室 (Copywriting Lab)

分析原笔记的“钩子标题”、“冲突点”、“利益点”，由大模型进行「主编级」二次深加工，产出极具情绪价值的文案。

### 3. 高清视觉流 (Visual Flow)

根据文案自动生成生图指令，适配 **Doubao-Seedream** 和 **nano-banana** 引擎，产出 2K 级高质感中文配图。

---

## 📜 许可证

MIT License.
