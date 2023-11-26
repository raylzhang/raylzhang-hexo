---
title: lf
tags:
  - CMD
categories:
  - Coding
abbrlink: 2c40f239
date: 2023-07-06 21:23:36
---

> ref: [官方文档](https://pkg.go.dev/github.com/gokcehan/lf#section-readme)

# 安装
```bash
brew install lf
```

# 配置
在 `.zshrc` 中添加：
```bash
## lf
lfcd () {
    tmp="$(mktemp)"
    lf -last-dir-path="$tmp" "$@"
    if [ -f "$tmp" ]; then
        dir="$(cat "$tmp")"
        rm -f "$tmp"
        [ -d "$dir" ] && [ "$dir" != "$(pwd)" ] && cd "$dir"
    fi
}

bindkey -s '^o' 'lfcd\n'
```

# 快捷键
- 选择：`space`
- 取消选择：`u`

- 剪切：`d`
- 粘贴：`p`
- 复制：`y`
- 清除：`c`

## mark
- mark-save：`m`
- mark-load：`'`
- mark-remove：`"`