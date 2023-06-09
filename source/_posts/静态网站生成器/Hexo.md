---
title: Hexo
tags: []
categories:
  - 静态网站生成器
abbrlink: b132932
date: 2023-06-07 15:58:48
---

> ref: https://hexo.io/zh-cn/docs

# 安装
```shell
# 安装
npm install hexo-cli -g
# 当前目录创建hexo项目
hexo init blog
cd blog
npm install
# 启动hexo
hexo server
```

安装完成后目录结构如下：
```text
. 
├── _config.yml # 网站的基础配置，文档：https://hexo.io/zh-cn/docs/configuration  
├── package.json  
├── scaffolds # 文章模板  
├── source  
|   ├── _drafts  
|   └── _posts # 你的 markdown 文章就需要存放在此目录下  
└── themes # 存放主题源码
```

# 命令
## 生成静态文件
```shell
hexo generate
# 简写
hexo g
```
生成 public 文件夹。

# 安装三方主题
例如 [butterfly](https://github.com/jerryc127/hexo-theme-butterfly)
1. 进入项目根目录运行
	```shell
	git clone -b master https://github.com/jerryc127/hexo-theme-butterfly.git themes/butterfly
	```
2. 应用主题
	修改 Hexo 根目录下的 `_config.yml`，把主题改为 `butterfly`
	```yaml
	theme: butterfly
	```
3. 主题配置文件
	在 hexo 的根目录创建一个文件 `_config.butterfly.yml`，并把主题目录的 `_config.yml` 内容复制到 `_config.butterfly.yml` 去。（注意: 复制的是主题的 `_config.yml` ，而不是 hexo 的 `_config.yml`）
	以后只需要在 `_config.butterfly.yml` 进行配置就行。如果使用了 `_config.butterfly.yml`，配置主题的 `_config.yml` 将不会有效果。
> 注意：不要把主题目录的 `_config.yml` 删掉
> Hexo 会自动合併主题中的 `_config.yml` 和 `_config.butterfly.yml` 里的配置，如果存在同名配置，会使用 `_config.butterfly.yml` 的配置，其优先度较高。

# 发布 Github Pages
和 [[Hugo#发布Github Pages]] 相同，包括 Vercel 配置。

## Front-matter
https://hexo.io/zh-cn/docs/front-matter

## 代码块
https://hexo.io/zh-cn/docs/tag-plugins#%E4%BB%A3%E7%A0%81%E5%9D%97
然后在主题目录下 `layout/_partial/head.ejs` 文件中添加里想要的主题样式，例如：
```html
<link rel="stylesheet" href="https://oindk07nf.qnssl.com/atom-one-dark.css" media="screen" type="text/css">
```

# 插件
https://hexo.io/plugins/
## 字数统计插件
-  https://ibruce.info/2015/04/04/busuanzi
## 评论
- [disqus](https://disqus.com/)（墙）
- [来必力](https://livere.com)（韩国作者，无需备案）
- [畅言](https://changyan.kuaizhan.com)（国内产品，需备案）
## 搜索
- 如果搜索引擎已收录，可以通过 `site:yourblogname.com search-value` 来变向解决搜索问题
> 	由于国内百度收录时效太低（文章收录不全），谷歌国内又无法使用，因此这种办法并不好。
- swifttype.com（收费）
	提交网站数据让其爬取然后提供搜索功能。
## 统计
- cnzz（目前被友盟收购）
- 百度

# 发布
## Github Pages
[[Github Pages]]

# 功能
## 使用 Markdown 嵌入图片
https://hexo.io/zh-cn/docs/asset-folders.html#%E4%BD%BF%E7%94%A8-Markdown-%E5%B5%8C%E5%85%A5%E5%9B%BE%E7%89%87