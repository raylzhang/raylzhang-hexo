---
title: iTerm2
tags:
  - Terminal
categories:
  - Coding
abbrlink: 10a3695f
date: 2023-07-07 04:32:08
---
# 配置
## 主题
设置路径：**Profiles - Colors - Color Presets**。
推荐主题：[catppuccin](https://github.com/catppuccin/catppuccin)

## 窗口
- `Appearance - General`
	- `Theme`：`Minimal`
	- `Tab bar location`：`Left`。一般都是单页面，这样设置可以隐藏顶部 Tab 栏

# 快捷键
## 默认
- 多窗口（当前打开的所有窗口）同时输入相同的指令：`cmd+shift+i`
	- 恢复：`option+cmd+shift++i`
- 新建 tab 页：`cmd+t`
- 切换 tab：`cmd+左右方向键` 或 `cmd+数字`
- 水平分屏：`cmd+d`
- 垂直分屏：`cmd+shift+d`
- 分屏移动：`cmd+[` 或 `]`
- 显示时间线：`cmd+shift+e`
- 查看历史命令：`cmd+;`
- 查看剪切板历史：`cmd+shift+h`

## 修改操作快捷键
- `Keys - Key Bindings` 新增
- 常用快捷键
	- 分屏跳转：`Cmd + Shift + kjhl`

## 修改命令行快捷键
- 位置：`Profiles - Keys - Key Bindings` 新增
- 常用快捷键

	|快捷方式|命令|动作|发送|
	|---|---|---|---|
	|⌥←|跳到字的开头|发送逃逸序列|`b`|
	|⌥→|跳到字的末尾|发送逃逸序列|`f`|
	|⌘←|跳到行的开头|发送十六进制代码|`0x01`|
	|⌘→|跳到行尾|发送十六进制代码|`0x05`|
	|⌥⌫|删除到字的开头|发送十六进制代码|`0x17`|
	|⌘⌫|删除整行|发送十六进制代码|`0x15`|

# 设置下拉窗口
**Preferences - Keys - Hotkey - Craete a Delicated Hotkey Window**

# Ref
> [iTerm2超详细安装和配置 - 简书](https://www.jianshu.com/p/f45f64cd6cca)
> [iTerm2中跳转和删除的键盘快捷键设置方法 - 掘金](https://juejin.cn/post/7133138258556354573)