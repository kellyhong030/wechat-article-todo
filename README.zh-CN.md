# wechat-article-to-todo

将微信公众号文章转化为可执行的 todo list。

粘贴公众号文章链接，自动过滤广告、提炼任务、按优先级排序，生成结构化的待办清单。

## 功能

- **自动提取**公众号文章内容
- **广告过滤** — 自动去除营销、课程推广、社群推广
- **任务提炼** — 识别可执行项（安装、配置、编码、学习）
- **优先级排序** — 按依赖关系和重要性排序
- **审计检查** — 确保无遗漏
- **安全审查** — 安装前自动检查安全性
- **用户确认** — 执行前必须用户确认

## 快速开始

### 安装到现有项目

```bash
git clone https://github.com/YOUR_USERNAME/wechat-article-to-todo.git
cd wechat-article-to-todo
./install.sh /你的项目路径
```

### 手动安装

**Claude Code:**
```bash
cp -r skills/wechat-article-to-todo /你的项目/.claude/skills/
cp tools/extract_from_imagenie.py /你的项目/tools/
```

**OpenClaw:**
```bash
cp -r skills/wechat-article-to-todo /你的项目/.agents/skills/
cp tools/extract_from_imagenie.py /你的项目/tools/
```

**Codex:** 仓库根目录的 `AGENTS.md` 提供兼容支持。

### 直接使用

```bash
git clone https://github.com/YOUR_USERNAME/wechat-article-to-todo.git
cd wechat-article-to-todo
claude  # 打开 Claude Code，skill 自动发现
```

然后粘贴公众号链接：
```
帮我转成 todolist：https://mp.weixin.qq.com/s/XXXXX
```

## 依赖

- Python 3.7+
- `requests`: `pip install requests`

## 平台兼容

| 平台 | 工作方式 |
|------|---------|
| **Claude Code** | 自动发现 `.claude/skills/` 目录 |
| **OpenClaw** | 读取 `.agents/skills/` 目录 |
| **Codex** | 读取根目录 `AGENTS.md` |

## 工作流程

```
文章链接 → 提取内容 → 过滤广告 → 总结观点 → 提炼任务 → 审计 → 确认 → 执行
```

## 目录结构

```
wechat-article-to-todo/
├── skills/
│   └── wechat-article-to-todo/
│       └── SKILL.md              # Skill 定义（通用格式）
├── tools/
│   └── extract_from_imagenie.py  # 文章提取工具
├── AGENTS.md                     # Codex 兼容
├── install.sh                    # 一键安装
├── .gitignore
├── LICENSE
└── README.md
```

## 许可

MIT
