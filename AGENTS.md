# wechat-article-to-todo Skill

Read the skill definition at `skills/wechat-article-to-todo/SKILL.md`.

## How to Use

When a user provides a WeChat article URL (e.g., `https://mp.weixin.qq.com/s/XXXXX`), follow the workflow defined in `skills/wechat-article-to-todo/SKILL.md`:

1. **Extract** article content using `python3 tools/extract_from_imagenie.py "<url>"`
2. **Filter** ads and marketing content
3. **Summarize** core insights
4. **Extract** actionable tasks with priority ordering
5. **Audit** for completeness
6. **Confirm** with user before executing
7. **Execute** with safety checks

## Article Extraction Tool

```bash
python3 tools/extract_from_imagenie.py "https://mp.weixin.qq.com/s/XXXXX"
```

Requires: `requests` (`pip install requests`)
