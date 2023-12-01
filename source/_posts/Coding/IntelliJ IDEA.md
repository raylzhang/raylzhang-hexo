---
title: IntelliJ IDEA
date: 2023-12-01 17:01:23
tags:
  - IDEA
---
# 安装
除了使用激活工具外，可以下载 JetBrains Toolbox 然后安装 EAP 版本，可以无限免费使用。

# 激活
[[资源#JetBrains]]

# 设置
>设置基于 2021.2 版本
## 修改 vm 参数
- **Help - Edit Custom VM Options...**
	- **-Xms128m**：JVM 初始分配的堆内存，16G 内存的机器可尝试设置为：`-Xms512m`
	- **-Xmx750m**：JVM 最大允许分配的堆内存，16G 内存的机器可尝试设置为：`-Xmx1500m`
	- **-XX:PermSize=128m**：JVM 初始分配的非堆内存，16G 内存的机器可尝试设置为：`-XX:PermSize=250m`
	- **-XX:MaxPermSize=350m**：JVM 最大允许分配的非堆内存，16G 内存的机器可尝试设置为：`-XX:MaxPermSize=500m`
	- **-XX:ReservedCodeCacheSize=225m**：16G 内存的机器可尝试设置为：`-XX:ReservedCodeCacheSize=500m`

## 设置（必要）
- **Help - Change Memory Settings**：根据机器配置情况设置 `Maximum Heap Size`，我设置的1500MiB，这个相当于 [[IntelliJ IDEA#修改vm参数]]的 `-Xmx`
- **View - Appearance**
	- **Tool Window Bars**：开启
	- **Compact Mode**：开启。紧凑模式
- 开启**Project**设置中的**Tree Appearance - Compact Middle Packages**
- **Preferences**
	- **Appearance & Behavior**
		- **Appearance - UI Options**
			- **Show tree indent guides**：开启。左侧菜单显示树形缩进线
			- **Use smaller indents in trees**：开启。减少左侧菜单树缩进距离
		- **System Settings**
			- **Project**
				- **Reopen projects on startup**：关闭。IntelliJ IDEA 启动默认打开上次项目设定
				- **Open project in**：设置为 `New window`。在新窗口中打开项目
			- **Updates - Check IDE updates for**：关闭。关闭 IDE 自动更新
	- **Editor**
		- **General**
			- **Mouse Control - Move code fragments with drag-and-drag**：关闭。关闭鼠标代码拖拽功能
			- **Appearance**
				- **Show method separators**：开启。显示方法线
				- **Show whitespaces**：全部开启。显示空格
				- **Show indent guides**：开启。显示缩进辅助线
			- **Code Completion - Match case**：关闭。智能提示忽略大小写
			- **Editor Tabs - Show tabs in one row**：`Multiple rows`。使用多行显示文件，效率比单行高，因为单行会隐藏超过界面部分
		- **Font**
			- 方案 1
				- **Font**：修改为 [[开发字体与样式#Fira Code|FiraCode Nerd Font Mono]]
				- **Size**：修改为 `17.5`
				- **Line height**：修改为 `1.1`
			- 方案 2
				- **Font**：修改为 [[开发字体与样式#Sarasa-Gothic|Sarasa Mono SC]]
				- **Size**：修改为 `19`
				- **Line height**：修改为 `1.2`
		- ==**Code Scheme**==
			- **General**：Duplicate Darcula as name "Darcula by Ray"
				- **Code - Identifier under caret - Background**：设置为 `286B28`（暗黑）、`82E782`（明亮）
				- **Code - Identifier under caret (write) - Background**：设置为 `65406E`（暗黑）、`DF93F2`（明亮）
		- **Code Style**
			- 所有语言
				- 取消 `Line comment at first column`
				- 开启 `Add a space at line comment start`
					- 开启 `Enforce on reformat`
				- 取消 `Block comment at first column`
				- 开启 `Add spaces around block comments`
			- **JavaScript - Punctuation**
				- 不适用分号：`Dont's use` semicolon to terminate statements in new code
				- 设置单引号：Use `single` quotes in new code
				
			>在 Code Style 下可以选择你想调整的单行注释的其他语言
		- **Inspections - JVM languages - Serializable class without 'serialVersionUID'**：开启。默认 IntelliJ IDEA 是没有开启生成 serialVersionUID 功能的，开启后，我们可以在已经继承了 Serializable 接口的类名上，把光标放在类名上（必须这样做），按 cmd+Enter，即可提示帮你生成 serialVersionUID 功能
		- **File Encodings - Default encoding for properties files: UTF-8 - Transparent native-to-ascii conversion**：开启。此选项主要用于转换 ascii，一般都要勾选，不然 Properties 文件中的注释显示的都不会是中文
		- **File Types - Ignored Files and Folders**：去掉里面的 `.idea`。如果忽略此文件夹会导致 IDEA Http Client 无法正常使用 cookies 和 session
	- **Version Control - Confirmation - Changes - Highlight directories that contain modified files in the Project tree**：开启
	- **Build, Execution, Deployment**
		- **Build Tools - Maven - Maven home path**：指定正确的 maven 路径
		- **Compiler**
			- **Build project automatically**：开启
			- **Shared build process heap size (Mbytes) (Default: 700)**：设置为 1500+
	- **Languages & Frameworks - Markdown - Show problems in code fences**：关闭
	- **Tools - Terminal - Cursor shape(Default: Block)**：修改为 `Vertical`。设置 Terminal 中光标样式
	- **Advanced Settings - Project View - Increase font size in Project view**：开启。增加左侧项目目录字体大小，需要重启 IDE
- **File - New Projects Setup - Preferences for New Projects...**：设置新建项目的默认配置
	- **File Encodings - Transparent native-to-ascii conversion**：开启。此选项主要用于转换 ascii，一般都要勾选，不然 Properties 文件中的注释显示的都不会是中文
	- **Version Control - Confirmation - Changes - Highlight directories that contain modified files in the Project tree**：开启
	- **Build, Execution, Deployment - Build Tools - Maven - Maven home path**：指定正确的 maven 路径
- 使用**Settings Repository**插件
	1. 开启插件
	2. Github 上新建一个 Repository（例如取名叫：jetbrains-settings）用来同步 IntelliJ IDEA 的 Settings
	3. 点击**File - Manage IDE Settings - Settings Repository...**，输入上一步新建的 Github 仓库地址，并选择**Overwrite Remote**上传本地配置。

	详细设置位置：**Preferences - Tools - Settings Repository**。如果选中**Auto Sync**的话，那么每次打开/关闭 IntelliJ IDEA 时系统会自动同步设置。
## 功能
- 删除版本升级后剩余的老版本配置目录（适用于所有 Jetbrains 产品）
	**Help - Delete Leftover IDE Directories**

# 插件
## IdeaVimExtension
https://www.v2ex.com/t/546621

# 问题
- [RMI TCP connection error when starting Spring Boot application - Stack Overflow](https://stackoverflow.com/questions/47283504/rmi-tcp-connection-error-when-starting-spring-boot-application)