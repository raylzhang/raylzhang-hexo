---
title: Zsh
tags:
  - Terminal
categories:
  - Coding
abbrlink: d911b12b
date: 2023-07-06 18:33:39
---

# 安装
## Linux
CentOS：`yum -y install zsh`
Ubuntu：`sudo apt -y install zsh`
Mac：`brew install zsh`

# 配置
查看当前使用的 shell：`echo $SHELL`
查看安装的 shell：`cat /etc/shells`
切换为 zsh：`chsh -s /bin/zsh`
重启终端即可使用 zsh。

# 安装 Oh My Zsh
## 安装
```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```

如果由于被墙而无法安装，可以使用国内搬运地址：[https://blog.csdn.net/qq_35104586/article/details/103604964](https://blog.csdn.net/qq_35104586/article/details/103604964)
```bash
sh -c "$(curl -fsSL https://gitee.com/shmhlsy/oh-my-zsh-install.sh/raw/master/install.sh)"
```

## 配置
`vim ~/.zshrc`

```bash
# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH

# Path to your oh-my-zsh installation.
export ZSH="/root/.oh-my-zsh"

# Set name of the theme to load --- if set to "random", it will
# load a random theme each time oh-my-zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
ZSH_THEME="pi"

# Set list of themes to pick from when loading at random
# Setting this variable when ZSH_THEME=random will cause zsh to load
# a theme from this variable instead of looking in $ZSH/themes/
# If set to an empty array, this variable will have no effect.
# ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" )

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion.
# Case-sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment one of the following lines to change the auto-update behavior
# zstyle ':omz:update' mode disabled  # disable automatic updates
# zstyle ':omz:update' mode auto      # update automatically without asking
# zstyle ':omz:update' mode reminder  # just remind me to update when it's time

# Uncomment the following line to change how often to auto-update (in days).
zstyle ':omz:update' frequency 30

# Uncomment the following line if pasting URLs and other text is messed up.
# DISABLE_MAGIC_FUNCTIONS="true"

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# You can also set it to another string to have that shown instead of the default red dots.
# e.g. COMPLETION_WAITING_DOTS="%F{yellow}waiting...%f"
# Caution: this setting can cause issues with multiline prompts in zsh < 5.7.1 (see #5765)
COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# You can set one of the optional three formats:
# "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# or set a custom format using the strftime function format specifications,
# see 'man strftime' for details.
# HIST_STAMPS="mm/dd/yyyy"
HIST_STAMPS="yyyy-mm-dd"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load?
# Standard plugins can be found in $ZSH/plugins/
# Custom plugins may be added to $ZSH_CUSTOM/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(
	git
	vi-mod
	zsh-autosuggestions
	zsh-syntax-highlighting
	autojump
)

source $ZSH/oh-my-zsh.sh

# User configuration

# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
# if [[ -n $SSH_CONNECTION ]]; then
#   export EDITOR='vim'
# else
#   export EDITOR='mvim'
# fi

# Compilation flags
# export ARCHFLAGS="-arch x86_64"

# Set personal aliases, overriding those provided by oh-my-zsh libs,
# plugins, and themes. Aliases can be placed here, though oh-my-zsh
# users are encouraged to define aliases within the ZSH_CUSTOM folder.
# For a full list of active aliases, run `alias`.
#
# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"
```

## 主题
-   [**pi**](https://github.com/tobyjamesthomas/pi)
	```bash
	wget -O ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/themes/pi.zsh-theme https://raw.githubusercontent.com/tobyjamesthomas/pi/master/pi.zsh-theme
	```

-   [**punctual-zsh-theme**](https://github.com/dannynimmo/punctual-zsh-theme)
	```bash
	wget -O ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/themes/punctual.zsh-theme https://raw.githubusercontent.com/dannynimmo/punctual-zsh-theme/v0.1.0/punctual.zsh-theme
	```

-   [**lambda-mod-zsh-theme**](https://github.com/halfo/lambda-mod-zsh-theme/)
	```bash
	wget -O ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/themes/lambda-mod.zsh-theme https://raw.githubusercontent.com/halfo/lambda-mod-zsh-theme/master/lambda-mod.zsh-theme
	```

Mac 下载主题会出现异常：
![image](https://static.raylzhang.top/img/202307061823434.png)

这是由于使用了更新版本的 openssl 导致的，可以安装一个老版本的 openssl 解决问题：
```bash
brew install https://github.com/tebelorg/Tump/releases/download/v1.0.0/openssl.rb
```

### 安装 p10k 主题
- 下载主题
	```bash
	git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/themes/powerlevel10k
	```
- 配置主题
	`vim ~/.zshrc`
	```bash
	zsh_theme="powerlevel10k/powerlevel10k"
	```
- 安装字体（可选择其他 Nerd 字体）
	```bash
	brew install font-hack-nerd-font
	```
	然后在终端配置字体：`hack nerd font`。

- p10k 配置

	```bash
	p10k configure
	```
 
	由于上面配置了字体 `hack nerd font`，所以第一步下载字体步骤可以跳过，其他选项根据自己喜好来配置。配置完成后在根目录下生成 `~/.p10k.zsh`，并且在 ~/.zshrc 底部写入：

	```bash
	# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
	[[ ! -f ~/.P10k.zsh ]] || source ~/.p10k.zsh
	```

	如果想废除 `p10k` 的配置，只需要删除 `~/.p10k.zsh`，同时删除上面这条命令即可。

- p10k 美化
	[参考这篇文章](https://www.jianshu.com/p/8f5091f4d122)

## 插件
### git
自带大部分 git 命令的缩写，命令内容可以参考 `~/.oh-my-zsh/plugins/git/git.plugin.zsh`。

oh my zsh 提供了一套系统别名（alias）来达到相同的功能。比如 gst 作为 git status 的别名。而且 git 插件是 oh my zsh 默认启用的，相当于你使用了 oh my zsh，你就拥有了一套高效率的别名，而且还是全球通用的。

完整列表请参考： https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/git/

### vi-mod
[GitHub zsh-vi-mode](https://github.com/jeffreytse/zsh-vi-mode)

#### 配置
在 `.zshrc` 中添加：
```bash
export VI_MODE_SET_CURSOR=true
```
这样能让光标识别 Vim 不同模式。

#### 移动
- **Vim edition**
	In `Normal mode` you can use `vv` to edit current command line in an editor (e.g. `vi` / `vim` / `nvim`...), because it is bound to the `Visual mode`.
	
	You can change the editor by `ZVM_VI_EDITOR` option, by default it is `$EDITOR`.

- **Movement**
	- `$` : To the end of the line
	- `^` : To the first non-blank character of the line
	- `0` : To the first character of the line
	- `w` : [count] words forward
	- `W` : [count] WORDS forward
	- `e` : Forward to the end of word [count] inclusive
	- `E` : Forward to the end of WORD [count] inclusive
	- `b` : [count] words backward
	- `B` : [count] WORDS backward
	- `t{char}` : Till before [count]'th occurrence of {char} to the right
	- `T{char}` : Till before [count]'th occurrence of {char} to the left
	- `f{char}` : To [count]'th occurrence of {char} to the right
	- `F{char}` : To [count]'th occurrence of {char} to the left
	- `;` : Repeat latest f, t, F or T [count] times
	- `,` : Repeat latest f, t, F or T in opposite direction

- **Insertion**
	- `i` : Insert text before the cursor
	- `I` : Insert text before the first character in the line
	- `a` : Append text after the cursor
	- `A` : Append text at the end of the line
	- `o` : Insert new command line below the current one
	- `O` : Insert new command line above the current one

- **Surround**
	There are 2 kinds of keybinding mode for surround operating, default is `classic` mode, you can choose the mode by setting `ZVM_VI_SURROUND_BINDKEY` option.

	1. `classic` mode (verb->s->surround)
		- `S"` : Add `"` for visual selection
		- `ys"` : Add `"` for visual selection
		- `cs"'` : Change `"` to `'`
		- `ds"` : Delete `"`

	2. `s-prefix` mode (s->verb->surround)
		- `sa"` : Add `"` for visual selection
		- `sd"` : Delete `"`
		- `sr"'` : Change `"` to `'`

	Note that key sequences must be pressed in fairly quick succession to avoid a timeout. You may extend this timeout with the [`ZVM_KEYTIMEOUT` option](https://github.com/jeffreytse/zsh-vi-mode#readkey-engine).

	- **How to select surround text object?**

		- `vi"` : Select the text object inside the quotes
		- `va(` : Select the text object including the brackets
	
		Then you can do any operation for the selection:
	
		1. Add surrounds for text object
			- `vi"` -> `S[` or `sa[` => `"object"` -> `"[object]"`
			- `va"` -> `S[` or `sa[` => `"object"` -> `["object"]`
	
		2. Delete/Yank/Change text object
			- `di(` or `vi(` -> `d`
			- `ca(` or `va(` -> `c`
			- `yi(` or `vi(` -> `y`

### autojump

这个插件会记录进入过的文件夹，下次再进入只要输入很少的内容即可。
需要先安装 autojump：
- ubuntu：`sudo apt-get install autojump`
- mac：`brew install autojump`

使用方法：
```bash
j 目录名或目录名的一部分
```
跳转到最多访问的目录。

### zsh-autosuggestions、zsh-syntax-highlighting

fish 类的自动建议插件： https://github.com/zsh-users/zsh-autosuggestions

需要用 git 将插件 clone 到指定插件目录下：
```bash
# 自动提示插件
git clone https://github.com/zsh-users/zsh-autosuggestions.git $zsh_custom/plugins/zsh-autosuggestions
# 语法高亮插件
git clone https://github.com/zsh-users/zsh-syntax-highlighting $zsh_custom/plugins/zsh-syntax-highlighting
```

自动建议的字体颜色可能和你终端的颜色相近，你可以将其改成其它的，比如设置为 blue：
`export zsh_autosuggest_highlight_style='fg=blue'`