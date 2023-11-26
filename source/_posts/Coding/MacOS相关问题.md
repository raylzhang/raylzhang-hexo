---
title: MacOS相关问题
tags:
  - MacOS
categories:
  - Coding
abbrlink: fbe2a0bc
date: 2023-06-09 23:35:49
---
# 设置
## 关闭 SIP

[Disabling and Enabling System Integrity Protection | Apple Developer Documentation](https://developer.apple.com/documentation/security/disabling_and_enabling_system_integrity_protection)

## 全键盘操作
### 方法 1
https://space.bilibili.com/394425489/channel/collectiondetail?sid=99741
- 快捷键映射
	- [Karabiner配置](https://github.com/LintaoAmons/karabiner-config/tree/main)
-  窗口管理
	- Mac 上没有炫酷的 `dwm`，我使用 [Amethyst](https://github.com/ianyh/Amethyst) 进行窗口管理，外加 [ShiftIt](https://github.com/fikovnik/ShiftIt) 辅助
### 方法 2 [[Yabai]]

## 设置 Capslock 切换输入法
https://trainspott.in/2018/12/05/macOs-%E4%B8%8B%E8%AE%BE%E7%BD%AECapslock%E5%88%87%E6%8D%A2%E8%BE%93%E5%85%A5%E6%B3%95/

## 禁用 `.DS_Store` 文件
- ~~（没有作用）系统禁用：`defaults write com.apple.desktopservices DSDontWriteNetworkStores true`（需要重启电脑!！）~~
- 查看是否禁用成功：`defaults read com.apple.desktopservices DSDontWriteNetworkStores`
- 系统启用：`defaults delete com.apple.desktopservices DSDontWriteNetworkStores`
- 删除 `.DS_Store` 文件：`sudo find / -name ".DS_Store" -type f -exec rm -f {} \; -print 2>/dev/null`

# 问题
## 笔记本合盖无法熄屏
[重置 Mac 的 SMC](https://support.apple.com/zh-cn/HT201295)

## 命令行无法访问 raw.githubusercontent.com
更改 DNS 为 `114.114.114.114` 或 `8.8.8.8`

## 解决：已损坏，无法打开，您应该将它移到废纸篓
```bash
sudo xattr -d com.apple.quarantine /Applications/xxx.app
``` 
> 如名称中有空格，可用 `\` 加空格代替。
