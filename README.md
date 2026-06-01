# wechat-article-to-todo

Convert WeChat public account (公众号) articles into actionable todo lists with AI agents.

Paste a WeChat article link, get a structured, prioritized todo list — ads filtered, tasks extracted, priorities sorted.

## Features

- **Auto-extract** article content from WeChat URLs
- **Ad filtering** — removes marketing, paid courses, community promotions
- **Task extraction** — identifies actionable items (install, configure, code, learn)
- **Priority sorting** — dependency-first ordering
- **Audit check** — ensures nothing is missed
- **Safety review** — security checks before installing anything
- **User confirmation** — always asks before executing

## Quick Start

### Option 1: Install to an existing project

```bash
git clone https://github.com/kellyhong030/wechat-article-to-todo.git
cd wechat-article-to-todo
./install.sh /path/to/your/project
```

### Option 2: Manual install

**For Claude Code:**
```bash
cp -r skills/wechat-article-to-todo /your-project/.claude/skills/
cp tools/extract_from_imagenie.py /your-project/tools/
```

**For OpenClaw:**
```bash
cp -r skills/wechat-article-to-todo /your-project/.agents/skills/
cp tools/extract_from_imagenie.py /your-project/tools/
```

**For Codex:** The `AGENTS.md` file at the repo root provides compatibility.

### Option 3: Use directly in this repo

```bash
git clone https://github.com/kellyhong030/wechat-article-to-todo.git
cd wechat-article-to-todo
# Open with Claude Code — the skill is auto-discovered via .claude/skills/
claude
```

Then paste a WeChat article URL:
```
帮我转成 todolist：https://mp.weixin.qq.com/s/XXXXX
```

## Requirements

- Python 3.7+
- `requests` library: `pip install requests`

## Platform Compatibility

| Platform | How it works |
|----------|-------------|
| **Claude Code** | Auto-discovers `.claude/skills/` in project |
| **OpenClaw** | Reads `.agents/skills/` directory |
| **Codex** | Reads `AGENTS.md` at project root |

## Project Structure

```
wechat-article-to-todo/
├── skills/
│   └── wechat-article-to-todo/
│       └── SKILL.md              # Skill definition (shared format)
├── tools/
│   └── extract_from_imagenie.py  # WeChat article extraction tool
├── .claude/
│   └── skills/
│       └── wechat-article-to-todo/
│           └── SKILL.md          # Claude Code auto-discover
├── .agents/
│   └── skills/
│       └── wechat-article-to-todo/
│           └── SKILL.md          # OpenClaw auto-discover
├── AGENTS.md                     # Codex compatibility
├── install.sh                    # One-click installer
├── .gitignore
├── LICENSE
└── README.md
```

## Workflow

```
Article URL → Extract → Filter Ads → Summarize → Extract Tasks → Audit → Confirm → Execute
```

1. **Extract** — Fetch article markdown via imagenie.us API
2. **Filter** — Remove ads, promotions, paid content
3. **Summarize** — Key insights and AI's analysis
4. **Extract** — Identify actionable tasks with types and priorities
5. **Audit** — Check for completeness and accuracy
6. **Confirm** — Present to user for approval
7. **Execute** — Run with safety checks

## License

MIT
