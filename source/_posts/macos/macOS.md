---
title: macOS
tags:
  - mac
categories:
  - macos
date: 2023-06-09 23:35:49
---
## 关闭 SIP
https://zhuanlan.zhihu.com/p/360711896

## 全键盘操作
https://space.bilibili.com/394425489/channel/collectiondetail?sid=99741
- 快捷键映射
	- [Karabiner配置](https://github.com/LintaoAmons/karabiner-config/tree/main)
-  窗口管理
	- Mac 上没有炫酷的 `dwm`，我使用 [Amethyst](https://github.com/ianyh/Amethyst) 进行窗口管理，外加 [ShiftIt](https://github.com/fikovnik/ShiftIt) 辅助
### Yabai
[[Yabai|Yabai]]
## 设置 Capslock 切换输入法
https://trainspott.in/2018/12/05/macOs-%E4%B8%8B%E8%AE%BE%E7%BD%AECapslock%E5%88%87%E6%8D%A2%E8%BE%93%E5%85%A5%E6%B3%95/
## 删除 `.DS_Store` 文件
```bash
sudo find / -name ".DS_Store" -depth -exec rm {} \
```
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

# 软件
## PD Runner
Github： https://github.com/utsanjan/PD.Runner
Release Page： https://www.dopesatan.ml/2023/03/pd-runner.html
`PDPatcher_18.1.1-53328` 版本没有单独启动，直接打补丁