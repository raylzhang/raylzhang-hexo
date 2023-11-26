---
title: ranger
tags:
  - CMD
categories:
  - Coding
abbrlink: 639a81f3
date: 2023-07-06 21:33:51
---

> [GitHub](https://github.com/ranger/ranger)
> [官方用户指南](https://github.com/ranger/ranger/wiki/Official-user-guide)

# 安装
## 生成配置文件（如果第一次使用）
```bash
ranger --copy-config=all
```
将会在 `~/.config/ranger` 目录输出以下文件：
- `commands.py`：包含各种函数的实现，用 Python 编写，用于修改 ranger 的行为，可自定义命令
- `commands_full.py`：更全的 `commands.py`
- `rc.conf`：选项设置和快捷键
- `rifle.conf`：不同文件默认打开程序
- `scope.sh`：一个 shell 脚本，用于生成各种文件类型的预览。当 `rc.conf` 中 `use_preview_script=true` 时，这个脚本会被调用

> 请注意，对于 `rc.conf` 和 `commands.py`， ranger 会依次读取全局配置和用户配置（按顺序）。它允许用户仅维护部分配置，该配置仅设置默认配置中未设置的内容。对于 `scope.sh` 和 `rifle.conf`，ranger 读取用户的配置或全局配置。

> 最佳实践是仅将实际想要更改的“选项/键绑定”添加到用户 `rc.conf` 配置，而不是直接拷贝默认的完整 `rc.conf`。这样未来就不需要手动更新配置，并能享受未来 Ranger 版本的新选项/键绑定。如果想保留完整的 `rc.conf`，我们需要将环境变量 `RANGER_LOAD_DEFAULT_RC` 设置为 `FALSE` 以避免*同时*加载全局配置和用户配置。

# 配置
## rc.conf

- 显示隐藏文件
	```bash
	set show_hidden true
	```
- 使用用户预览配置文件
	```bash
	# Use non-default path for file preview script?
	# ranger ships with scope.sh, a script that calls external programs (see
	# README.md for dependencies) to preview images, archives, etc.
	set preview_script ~/.config/ranger/scope.sh
	```
- 识别被版本控制的文件夹
	```bash
	# Be aware of version control systems and display information.
	set vcs_aware true
	```
- 图片预览
	```bash
	# Use one of the supported image preview protocols
	set preview_images true
	
	# 利用iterm2的图片预览支持。详见：http://iterm2.com/images.html
	set preview_images_method iterm2
	
	# Default iTerm2 font size (see: preview_images_method: iterm2)
	set iterm2_font_width 80
	set iterm2_font_height 110
	```
- 在 Tab 中显示目录名称
	```bash
	# Display the directory name in tabs?
	set dirname_in_tabs true
	```
- 给窗口起名字
	```bash
	# Set a title for the window? Updates both `WM_NAME` and `WM_ICON_NAME`
	set update_title true
	```
- titlebar 中 `$HOME` 缩略显示 `~` 符号
	```bash
	# Abbreviate $HOME with ~ in the titlebar (first line) of ranger?
	set tilde_in_titlebar true
	```
- 调大历史缓存
	```bash
	# How many directory-changes or console-commands should be kept in history?
	set max_history_size 2000
	set max_console_history_size 50
	```
- 在 `cd` 命令 tab completion 时不区分大小写
	```bash
	# Changes case sensitivity for the cd command tab completion
	set cd_tab_case insensitive
	```
- 在 `cd` 命令中使用 fuzzy tab completion
	```bash
	# Use fuzzy tab completion with the "cd" command. For example,
	# ":cd /u/lo/b<tab>" expands to ":cd /usr/local/bin".
	set cd_tab_fuzzy true
	```
- 当离开目录时清理所有存在的 `filters`
	```bash
	# Clear all existing filters when leaving a directory
	set clear_filters_on_dir_change true
	```
- 退出时保存 tabs
	```bash
	# Save tabs on exit
	set save_tabs_on_exit true
	```
- 排序
	```bash
	# One of: size, natural, basename, atime, ctime, mtime, type, random
	# 默认更新时间排序
	set sort mtime
	
	# Additional sorting options
	# 是否反序排序
	set sort_reverse false
	# 是否区分大小写
	set sort_case_insensitive true
	# 是否将目录（文件夹）排在文件之前
	set sort_directories_first false
	# 是否启用Unicode排序
	set sort_unicode false
	```
- 默认显示方式（devicons）
	```bash
	# 默认启用开发者图标的显示模式
	default_linemode devicons
	```
 
## 颜色配置
先从 https://github.com/ranger/ranger/tree/master/ranger 这里下载 colorschemes 目录放到 `~/.config/ranger` 目录下，修改 `rc.conf` 文件：
```bash
# 可选default、snow、jungle、solarized
set colorschema solarized 
```

## 将默认编辑器配置成 neovim
找到 `rifle.conf` 文件中的如下内容：
```bash
#-------------------------------------------
# Misc
#-------------------------------------------
# Define the "editor" for text files as first action
mime ^text,  label editor = ${VISUAL:-$EDITOR} -- "$@"
mime ^text,  label pager  = "$PAGER" -- "$@"
!mime ^text, label editor, ext xml|json|csv|tex|py|pl|rb|js|sh|php = ${VISUAL:-$EDITOR} -- "$@"
!mime ^text, label pager,  ext xml|json|csv|tex|py|pl|rb|js|sh|php = "$PAGER" -- "$@"
```
将上面两个 `$EDITOR` 修改成 `nvim`，如下：
```bash
#-------------------------------------------
# Misc
#-------------------------------------------
# Define the "editor" for text files as first action
mime ^text,  label editor = ${VISUAL:-nvim} -- "$@"
mime ^text,  label pager  = "$PAGER" -- "$@"
!mime ^text, label editor, ext xml|json|csv|tex|py|pl|rb|js|sh|php = ${VISUAL:-nvim} -- "$@"
!mime ^text, label pager,  ext xml|json|csv|tex|py|pl|rb|js|sh|php = "$PAGER" -- "$@"
```

## 自定义快捷键
- 定义一个快捷键 `DD` ，在 Mac 中能把文件或者目录放到回收站
	编辑 `rc.conf`，添加：
	```bash
	map DD shell mv %s ~/.Trash
	```
- 定义一个快捷键到指定的目录
	编辑 `rc.conf`，添加：
	```bash
	map gw cd ~/workspace/
	```
> 	这个功能可以快速定位到自己常用的目录，可以多定义几个

ranger 的一些常用命令：

![Pasted image 20221124202013](https://static.raylzhang.top/img/202307062136711.png)

# 快捷键
ranger 中有按键和命令两种操作方式，按键是直接键入键盘上的键完成某个操作，命令则需前输入 `:`，然后输入相应的命令。  
## 浏览文件
- `k`：向上移动
- `j`：向下移动
- `h`：向左移动（在浏览文件夹时，它表示回到上一级目录）
- `l`：向右移动（在光标处于一个文件夹上时，进入这个目录。处于一个文件上时，则打开该文件）
- `H`：后退到上一个历史记录
- `L`：前进到下一个历史记录
- `Ctrl + U`：向上翻半页
- `Ctrl + D`：向下翻半页
- `gg`：跳到页首
- `G`：跳到页尾
- `%`：跳到页中

和 vim 一样，指令之前可以指定一个数字，表示执行多少次指令。例如：
- `5(Ctrl + D)`：向下翻 5 个半页
- `3h`：向上跳 3 级目录
- `6gg` or `6G`：跳到第 6 行
- `20%`：跳到当前页的 20%处

- `cd`：跳转到目录，同 `:cd`

- `gl`：如果当前条目是一个符号链接，那么跳到它的原始位置
- `gh`：相当于 `cd ~`
- `ge`：相当于 `cd /etc`
- `gu`：相当于 `cd /usr`

- `zh`：显示隐藏文件
- `zp`：打开/关闭文件预览功能
- `zP`：打开目录预览功能

## 搜索
按下 `/` 打开搜索栏，然后输入要搜索的字符串，回车后开始搜索。
`n` 查找下一个结果，`N` 查找上一个结果。
你也可以通过其他属性来搜索文件：
- `cc`：通过 ctime 属性依次遍历
- `cm`：通过 mime type 属性依次遍历
- `cs`：通过 size 属性依次遍历
- `ct`：搜索已标记的文件

## 排序
- `os`：按大小排序
- `ob`：按名称排序
- `ot`：按文件类型排序
- `om`：按 mtime（上一次修改文件内容的时间）排序
- `or`：反向排序（ranger 默认是以升序排列文件）

## 书签
你可以设置一个书签以便快速的进入某个目录。
- `m<key>`：保存书签
- `'<key>`：跳到书签
- `um<key>`：删除书签
- `draw_bookmarks`：查看所有书签

> 1. key 可以是任意的数字或字母，和 vim 不同，书签是永久保存的
> 2. \`（键盘 1 左边的键）和 `'`（单引号）是等效的
> 3. `'` 本身也是一个书签，代表上一次跳转的位置

## 标签
ranger 支持多个标签页，可以快速地在多个标签页之间切换。
- `gn` 或 `Ctrl + N`：新建一个标签页
- `gt`：跳到下一个标签页
- `gT`：跳到上一个标签页
- `g<N>`：打开一个标签页，N 代表 1 到 9 的一个数字，如果这个标签页不存在，ranger 会自动创建
- `gc` 或 `Ctrl + W`：关闭当前标签页，最后一个标签页不能关闭

## 操作文件
### 选择文件
ranger 可以方便快速地选择多个文件。
- `space`：选择一个文件，之后光标会自动跳到下一个条目
- `v`：反选
- `V` 或 `uv`：取消所有选择
- `Ctrl + V`：从某个位置开始选择
- `u(Ctrl + V)`：取消选择到某个位置
	例如：
	- `Ctrl + V + gg`：选择从当前位置到顶部的所有条目
	- `Ctrl + V + G`：选择从当前位置到底部的所有条目
	- `u(Ctrl + V)`：用法同上
- `t`：标记/取消标记选择的条目
- `T`：取消标记选择的条目 

### 查看文件
- `i`：查看当前文件的内容（文本文件）
### 编辑文件
- `E`：调用默认编辑器编辑文件
### 处理文件
- `:mkdir`：创建文件夹
- `:touch`：创建文件
- `:rename`：重命名
- `yp`：复制文件地址
- `yn`：复制文件名
- `y.`：复制去掉文件后缀的文件名
- `cw`：同 `:rename`
- `A`：重命名，附加当前文件名
- `I`：同 `A`，但会将光标置于文件名之前
- `yy`：复制
- `dd`：剪切
- `pp`：粘贴，当存在同名文件时，会自动重命名
- `po`：粘贴，覆盖同名文件
- `pl`：创建一个被复制/剪切文件的符号链接
- `pL`：创建一个被复制/剪切文件的符号链接（相对路径）
- `:delete`：删除选定的条目
	如果删除的文件不止一个，ranger 会提示确认删除，键入 `y` 即可。也可以在输入命令时附加一个参数 `y`，跳过 ranger 的确认：`:delete y`

### 运行文件
- `l`：打开选定文件
	如果没有选定文件，则打开当前文件。ranger 根据 `rifle.conf` 里的配置打开相应文件。
	如果 ranger 不知道用什么程序打开相应文件，会出现 `:open_with` 对话框询问用户。也可以直接使用命令 `r` 打开 `:open_with` 对话框。
- `r`：用指定程序打开文件，同命令 `:open_with`
	`:open_with` 语法：
	```bash
	:open_with <program> <mode> <flags>
	```

	- `<program>`：需要在 `apps.py` 中定义，CustomApplications 中每一个以 `app_` 开头的函数会被命令 `:open_with` 用到
	- `<mode>`：ranger 以何种模式运行程序，可用的 mode 有：
		- `0`：窗口模式
		- `1`：全屏模式
	- `<flags>`：指定 ranger 以何种方式调用程序：
		- `s`：silence 模式。任何输出将被丢弃
		- `d`：分离程序（在后台运行）
		- `p`：将输入重定向到 pager
		- `w`：当程序执行完成时需要用户回车确认
		大写 `<flag>` 可以得到相反的作用，例如一个程序如果默认就在后台运行，那么可以使用 `:open_with D` 来防止其在后台运行
- `S`：在当前目录下开启一个 shell

## 任务管理
在执行某些操作（比如复制一个大文件）时不能立即完成，这在 ranger 中就是一个任务。你可以停止、启动某个任务，也可以对某个任务设置优先级。
- `w`：打开/关闭任务视图
- `dd`：终止一个任务
- `J`：降低当前任务的优先级
- `K`：l 提升当前任务的优先级

## 命令
命令以 `:` 开头。输入时可用 Tab 键补全，如果有多个匹配的，ranger 会依次遍历所有匹配项。
所有命令被定义在文件 `ranger/defaults/commands.py` 中。
可用的命令：
- `:cd <dirname>`：跳转到目录 `<dirname>`
- `:chmod <octal_number>`：设置被选条目的权限
- `:delete`：删除被选条目
- `:edit <filename>`：编辑文件
- `:filter <string>`：只显示文件名中含有给定字符串 `<string>` 的文件 
- `:find <regexp>`：查找匹配给定正则表达式的文件，并且执行第一个匹配的文件
- `:grep <string>`：在选定的条目中查找给定的字符串 `<string>`
- `:mark <regexp>`：选定匹配正则表达式的所有文件
- `:unmark <regexp>`：取消选定匹配正则表达式的所有文件
- `:mkdir <dirname>`：创建目录
- `:open_with <program< <mode> <flags>`：用给定的 `<program>`、`<mode>` 和 `<flags>` 打开文件。所有参数都是可选的，未给出任何参数的时候，等价于 `<Enter>`
- `:quit`：退出
- `:rename <newname>`：重命名当前文件
- `:search <regexp>`：搜索所有匹配正则表达式 `<regexp>` 的文件，相当与 vim 中的 `/`
- `:shell [-<flags>] <command>`：运行命令 `<command>`
- `:touch <filename>`：创建文件

所有命令（`:delete` 除外），可以不用写全，不过前提是和之匹配的命令只有一个。

## 杂项
- `z`：切换设置
- `u`：撤销操作
- `W`：打开 message log
- `du`：显示当前目录的磁盘占用情况
- `R`：刷新当前目录
- `Ctrl + R`：清空缓存并刷新目录
- `Ctrl + L`：重画当前窗口

## 命令行参数
- `--version`：打印 ranger 的版本
- `-h` / `--help`：打印帮助信息
- `-d` / `--debug`：以 debug 模式启动 ranger，当出错退出时，ranger 会输出所有信息
- `-c` / `--clean`：以 clean 模式启动 ranger，ranger 不会读取和创建配置文件
- `--copy-config <all|apps|commands|keys|options|scope>`：复制 ranger 的配置文件到 home 目录，已经存在的文件不会被覆盖
- `-r <dir>` / `--confdir=<dir>`：使用其他配置文件目录

# 问题
## nested 问题
- 问题：ranger 中默认 `S` 进入一个新目录时都会启动一个新的 shell，如果想关闭这个 shell 需要运行 `exit`，如果不关闭直接在这个 shell 中再次启动 ranger 会报 `youre in a nested ranger instance` 错误。
- [解决办法](https://stackoverflow.com/questions/57903114/how-to-recursively-exit-nested-shells)
	- 在.zshrc 文件中添加配置：
		```bash
		## ranger
		bindkey -s '^o' ranger
		# 解决 ranger 产生 nested 问题
		function ranger {
			# 定义局部变量 IFS，它控制如何解释字符串中的字段分隔符。在这里，$'\t\n' 表示使用制表符和换行符作为字段分隔符
		    local IFS=$'\t\n'
			# 创建一个临时文件，并将其路径保存在局部变量 tempfile 中。mktemp -t tmp.XXXXXX 生成一个唯一的临时文件名
		    local tempfile="$(mktemp -t tmp.XXXXXX)"
			# 定义一个名为 ranger_cmd 的数组
		    local ranger_cmd=(
				# 确保使用原始的 command 命令，而不是被函数重定义的版本
		        command
		        # 指定 Ranger 在启动时执行的命令，该命令将 Ranger 中目录路径保存到临时文件 tempfile 中，并退出 Ranger
		        ranger
		        --cmd="map Q chain shell echo %d > "$tempfile"; quitall"
		    )
			# 将 ranger_cmd 数组展开，并作为命令来执行。"$@" 代表函数 ranger 的所有参数
		    ${ranger_cmd[@]} "$@"
			# 如果 tempfile 存在 且 tempfile 中保存路径和当前工作目录路径不同
		    if [[ -f "$tempfile" ]] && [[ "$(cat -- "$tempfile")" != "$PWD" ]]; then
				# 将当前工作目录切换到临时文件中保存的路径。如果切换失败，则退出
		        cd -- "$(cat "$tempfile")" || return
		    fi
			# 删除临时文件。`2>/dev/null` 将忽略删除操作的错误输出
		    command rm -f -- "$tempfile" 2>/dev/null
		}
		```
		- 按 `Q` 退出 ranger 并自动将目录同步到 ranger 中的同一目录。
		- 按 `q` 正常退出而无需将目录同步回 shell。

## trash 命令无法执行
- 安装 [[Command Line命令#trash-cli]]
- 取代原先命令
```bash
# map dT console trash
map dT shell trash-put %s
```