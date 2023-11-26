---
title: Git修改历史提交的用户名和邮箱
tags:
  - Git
categories:
  - Coding
abbrlink: f63c9fb5
date: 2023-06-15 18:45:56
---
> ref: [[Git#查看或修改用户名和邮箱]]

# 方法一
此方法只能修改最近一次提交。
```bash
git commit --amend --author="userName <userEmail>"
```
注意不能缺少`<` `>`。

# 方法二
此方法可以批量修改。
1. 首先配置用户名和邮箱：
	```bash
	git config user.name 'username'
	git config user.email 'email'
	```

2. 创建脚本：
	```bash
	#!/bin/sh

	git filter-branch --env-filter '

	OLD_NAME="old_email@email.com"
	CORRECT_NAME="new_name"
	CORRECT_EMAIL="new_email"

	if [ "$GIT_COMMITTER_NAME" = "$OLD_NAME" ]
	then
		export GIT_COMMITTER_NAME="$CORRECT_NAME"
		export GIT_COMMITTER_EMAIL="$CORRECT_EMAIL"
	fi
	if [ "$GIT_AUTHOR_NAME" = "$OLD_NAME" ]
	then
		export GIT_AUTHOR_NAME="$CORRECT_NAME"
		export GIT_AUTHOR_EMAIL="$CORRECT_EMAIL"
	fi
	' --tag-name-filter cat -- --branches --tags
	```
	>其中`OLD_NAME`可以换成`OLD_EMAIL`用来替换邮箱。

3. 如果执行失败的话，执行一下这段命令：
	```bash
	git filter-branch -f --index-filter 'git rm --cached --ignore-unmatch Rakefile' HEAD
	```
	然后再运行脚本。

4. 推送至远程：
	```bash
	git push origin --force --all
	```