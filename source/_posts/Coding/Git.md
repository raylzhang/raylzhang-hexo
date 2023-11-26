---
title: Git
tags:
  - Git
categories:
  - Coding
abbrlink: 69c3279c
date: 2023-06-15 04:01:29
---

# 安装
1. [下载源码](https://mirrors.edge.kernel.org/pub/software/scm/git/)
	下载方式：[[命令行常用命令#curl]]
 
2. 安装环境
	- ubuntu
		```Bash
		sudo apt update
		sudo apt install dh-autoreconf libcurl4-gnutls-dev libexpat1-dev make gettext libz-dev libssl-dev libghc-zlib-dev libssl-dev
		```
	- centos
		```Bash
		yum -y install curl-devel expat-devel gettext-devel perl-ExtUtils-MakeMaker openssl-devel zlib-devel gcc
		```
3. 编译安装
	```shell
	tar -zxvf git-2.9.5.tar.gz
	cd git-2.9.5
	mkdir -p /opt/git/git-2.9.5
	make prefix=/opt/git/git-2.9.5 all
	make prefix=/opt/git/git-2.9.5 install
	echo "export PATH=$PATH:/opt/git/git-2.9.5/bin" >> ~/.profile
	source ~/.profile
	# 保证登录时能正常使用git命令
	ln -s /usr/local/git/bin/git /usr/local/bin/
	git --version
	```
# 配置
## 查看或修改用户名和邮箱
```bash
# 查看
git config user.name
git config user.email
# 修改
git config --global user.name "username"
git config --global user.email "email"
# 查看配置信息
git config --list
```
[[Git修改历史提交的用户名和邮箱]]
# 分支
## 查看分支
```Bash
# 查看本地和远程仓库的所有分支
git branch -a
# 查看远程仓库的分支
git branch -r
```
## 删除分支
```shell
# 删除本地分支
git branch -d <branch>
```
# 远程
## 查看远程地址
```Bash
git remote -v
```
## 变更本地远程地址
```Bash
git remote set-url <repository> <remote-url>
# example
git remote set-url origin git@1.117.41.55:carsuper/kczy.git 
```
## 推送本地分支
```Bash
git push <repository> <local-branch>:<remote-branch>
# example
git push origin develop:develop 
```
## 同步远程分支
```Bash
# 将本地分支与远程保持同步
git fetch
# 删除不存在的远程跟踪分支
# --prune -p 
# -- remove any remote tracking branches that no longer exist remotely
git fetch -p
```
## 拉取远程分支
```Bash
# 拉取远程分支，同时创建对应的本地分支
git checkout -b <local-branch> <repository>/<remote-branch>
```
## 拉取远程分支某个 Tag
```bash
git clone --branch <tag> <repository>
```
如果您想要切换到其他标签或分支，请使用 `git checkout` 命令进行切换。例如：`git checkout <标签或分支名称>`。
## 比较本地分支和远程分支
```bash
git fetch
git diff <local-branch> <remote-branch> 
```
# 撤销
未提交直接 checkout：
```bash
git checkout <文件名>
```
# 暂存
[git stash](https://www.cnblogs.com/tocy/p/git-stash-reference.html)
# 取消暂存
如果您想要取消 Git 中已暂存（staged）的内容，可以使用 `git restore` 命令。该命令可以还原文件的状态，将其从暂存区域移回工作区域。请按照以下步骤操作：
1. 确保您在您的 Git 仓库目录下。您可以使用 `cd` 命令进入该目录。
2. 运行以下命令以取消已暂存的文件更改：
	```bash
	git restore --staged <文件名>
	```
    将 `<文件名>` 替换为您想要取消暂存的文件名或路径。如果您想要取消暂存所有文件的更改，可以使用 `.` 作为文件名。
3. 运行以上命令后，文件的更改将被移出暂存区域，并且恢复到上一次提交的状态。您可以使用 `git status` 命令检查文件状态，确保它们已被正确取消暂存。

> 请注意，使用 `git restore` 命令取消暂存的文件更改不会撤销工作区中的实际更改。如果您想要撤销工作区中的更改并还原文件到最近一次提交的状态，可以使用 `git checkout` 命令。例如，`git checkout -- <文件名>`。但请注意，`git checkout` 命令在执行时会丢失未提交的更改，请谨慎使用。

# 操作
## 修改提交时间
```Bash
git commit --amend --date="commit_time"
```
`commit_time` 的格式比较难记，不过有个小技巧，我们可以先在命令行输入：
```Bash
> date -R
Sat, 24 Dec 2016 18:12:09 +0800
```
这个命令的输出格式与 `git commit –amend –date` 命令要填写的日期格式相同，自己再稍加修改一下即可。   
如果我们只是想将上次 git commit 的时间改为当前时间，可以使用以下两个命令：
```Bash
git commit --amend --date="$(date -R)"
# 或者
git commit --amend --date=`date -R`
```
## 合并两个不同仓库
1. 下载需要合并的分支：
	```bash
	git clone https://gitee.com/raylzhang/hello.git
	```
2. 添加需要合并的远程仓库：
	```bash
	git remote add hello2 https://github.com/raylzhang/hello.git
	```
	将 `hello2` 作为远程仓库，添加到 `本地仓库(origin)` 中，设置别名为 `hello2`（自定义，这里我是为了方便区分仓库名）。
3. 把 `hello2` 远程仓库中的数据抓取到本地仓库：
	```bash
	git fetch hello2
	```
4. `checkout` 到 `hello2` 分支上，命名为 `need_merge`：
	```bash
	git checkout -b need_merge hello2/master
	```
	由于我们需要把 `need_merge` 分支合并到 `dev` 分支中去，现在先切换到 `dev` 分支：
	```bash
	git checkout dev
	```
5. 合并
	```bash
	git merge need_merge
	```
 
	> 合并时出现 `fatal: refusing to merge unrelated histories` 错误
	>这个错误在 `git pull` 或者 `git push` 中都有可能会遇到，因为两个分支没有取得关系。
	>**解决方案**
	>在操作命令后面加 `--allow-unrelated-histories`：
	>```bash
	>git merge need_merge --allow-unrelated-histories
	>```
	
	合并完成之后会出现很多冲突，需要在本地代码中解决冲突，然后再提交到 `dev` 中去：
	```bash
	git push origin dev
	```
