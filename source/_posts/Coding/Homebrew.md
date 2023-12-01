---
title: Homebrew
date: 2023-07-25 10:25:35
tags:
 - Homebrew
---
# 技巧
- cask 安装助手：[brew cu](https://github.com/buo/homebrew-cask-upgrade)
* 显示已安装程序包依赖关系：`brew deps --tree --installed`
- shows you all top-level packages, packages that are not dependencies：`brew leaves | xargs -n1 brew desc --eval-all`
- 删除所有未使用的依赖项：`brew autoremove`

# 问题
* 出现错误：
	```bash
	Error: Cask adoptopenjdk8 exists in multiple taps:
	  caskroom/versions/adoptopenjdk8
	  adoptopenjdk/openjdk/adoptopenjdk8
	```
	解决方式：
	```bash
	rm /opt/homebrew/Library/Taps/homebrew/homebrew-cask-versions/Casks/adoptopenjdk8.rb
	```
- 软件无法正常卸载或提示“does not exist”
	1. `brew uninstall --cask --force`
	2. `brew install --cask`