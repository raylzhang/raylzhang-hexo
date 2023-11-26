---
title: nvm
tags:
  - NodeJS
categories:
  - Coding
abbrlink: f76efcad
date: 2023-06-18 22:54:55
---
> ref: [nvm github](https://github.com/nvm-sh/nvm)

nvm 是一个 nodejs 版本管理工具。

# 安装
## Linux
### 方法 1
```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash
# 或者
wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash
```
Running either of the above commands downloads a script and runs it. The script clones the nvm repository to `~/.nvm`, and attempts to add the source lines from the snippet below to the correct profile file (`~/.bash_profile`, `~/.zshrc`, `~/.profile`, or `~/.bashrc`).
```bash
export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm
```
### 方法 2
如果[[nvm#方法1|方法1]] 无法连接 github，可以直接本地下载：
```bash
wget -O nvm-0.39.3.tar.gz https://github.com/nvm-sh/nvm/archive/refs/tags/v0.39.3.tar.gz
```
然后上传到服务器，之后登录服务器执行：
```bash
mkdir /root/.nvm
tar -zxvf nvm-0.39.3.tar.gz -C /root/.nvm
```
配置环境变量：
```bash
vim ~/.zshrc

export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm/nvm-0.39.3" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm
```

## Mac
```shell
brew install nvm
```
`.zshrc` 配置文件中添加：
```shell
## nvm
export NVM_DIR="$HOME/.nvm"
  [ -s "/opt/homebrew/opt/nvm/nvm.sh" ] && \. "/opt/homebrew/opt/nvm/nvm.sh"  # This loads nvm
  [ -s "/opt/homebrew/opt/nvm/etc/bash_completion.d/nvm" ] && \. "/opt/homebrew/opt/nvm/etc/bash_completion.d/nvm"  # This loads nvm bash_completion
```
`source ~/.zshrc` 后生效，可通过 `nvm --version` 查看版本。

# 命令
## 查看
- 查看本地所有版本：`nvm list`
- 查看所有远程服务器的版本（官方 node version list）：`nvm ls-remote`
- 显示当前版本：`nvm current`
## 安装
- 安装指定版本：`nvm install <version>`
- 安装最新稳定版：`nvm install --lts`
## 使用
- 切换到指定版本：`nvm use <version>`
- 使用指定版本执行文件：`nvm exec <version> node <file-path>`
## 别名
- 给不同版本添加别名：`nvm alias <name> <version>`
- 删除已设置别名：`nvm unalias <name>`
- 设置默认版本：`nvm alias default <version>`
## 卸载与清理
- 卸载指定版本：`nvm uninstall <version>`
- 在当前版本 node 环境下，重新全局安装指定版本号的 npm 包：`nvm reinstall-packages <version>`
- 查看缓存路径：`nvm cache dir`（可以进入目录自行删除缓存）