---
title: Yabai
tags: [mac]
categories:
  - macos
date: 2023-06-09 13:08:51
---
# 安装
GitHub 地址： https://github.com/koekeishiya/yabai
## 1. 关闭 SIP
[[macOS#关闭 SIP|macOS > 关闭 SIP]]
## 2. 安装 yabai
```bash
brew install koekeishiya/formulae/yabai
```
## 3. 赋予 Yabai root 权限
官方文档：[Configure scripting addition]( https://github.com/koekeishiya/yabai/wiki/Installing-yabai- (latest-release))
1. 获取 Yabai hash 值
	```bash
	shasum -a 256 $(which yabai)
	```
	得到 hash 值：`0c054aec0f8eeb0ba2328aa91654f5354eeacc53e9e679250afb7db1eaf062b3`
2. 编辑 `/etc/sudoers` 文件
	```bash
	sudo vim /etc/sudoers
	# 格式：<user> ALL=(root) NOPASSWD: sha256:<hash> <yabai> --load-sa
	raylzhang ALL=(root) NOPASSWD: sha256:0c054aec0f8eeb0ba2328aa91654f5354eeacc53e9e679250afb7db1eaf062b3 /opt/homebrew/bin/yabai --load-sa
	```
3. Yabai 配置文件头部添加：
	```bash
	yabai -m signal --add event=dock_did_restart action="sudo yabai --load-sa"
	sudo yabai --load-sa
	```
## 4. 设置 boot-args（可选）
先执行第 5 步，再根据第 5 步错误提示选择执行。
```bash
# 检查 boot-args 值
nvram boot-args
# 如果结果不是 -arm64e_preview_abi
sudo nvram boot-args=-arm64e_preview_abi
```
> 需要重启。
## 5. 注入 Yabai 脚本
```bash
sudo yabai --load-sa
```
确保执行后没有任何错误。
## 6. 安装 skhd
Github 地址： https://github.com/koekeishiya/skhd
skhd 是 Yabai 作者自己写的一个系统快捷键映射程序。
```bash
brew install koekeishiya/formulae/skhd
```
## 7. 添加配置文件
[[Yabai#配置|Yabai 配置]]
## 8. 启动
```bash
yabai --start-service
skhd --start-service
```
启动时会提示是否允许访问辅助功能，勾选允许即可。

# 配置
## Yabai 配置
官方文档： https://github.com/koekeishiya/yabai/wiki/Configuration#configuration-file
Yabai 配置文件可以存放的位置：
- `$HOME/.config/yabai/yabairc` 
- `$HOME/.yabairc`
可以复制推荐配置：
```bash
cp /opt/homebrew/Cellar/yabai/5.0.6/share/yabai/examples/yabairc ~/.config/yabai
```
配置文件参考： https://raw.githubusercontent.com/raylzhang/dotfiles/main/yabai/.config/yabai/yabairc
## skhd 配置
可以复制推荐配置：
```bash
cp /opt/homebrew/Cellar/yabai/5.0.6/share/yabai/examples/skhdrc ~/.skhdrc
```
配置文件参考： https://raw.githubusercontent.com/raylzhang/dotfiles/main/skhd/.skhdrc

# 操作
## Yabai
启动：`yabai --start-service`
重启：`yabai --restart-service`