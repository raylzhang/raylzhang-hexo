---
title: Hexo
tags:
  - 建站/Hexo
  - TODO
categories:
  - Coding
abbrlink: b132932
date: 2023-06-07 15:58:48
---
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

# 三方主题
[[Hexo Butterfly主题]]

# 插件
https://hexo.io/plugins/
## 字数统计插件
-  https://ibruce.info/2015/04/04/busuanzi

## 评论插件
- [disqus](https://disqus.com/)（墙）
- [来必力](https://livere.com)（韩国作者，无需备案）
- [畅言](https://changyan.kuaizhan.com)（国内产品，需备案）

## 搜索插件
- 如果搜索引擎已收录，可以通过 `site:yourblogname.com search-value` 来变向解决搜索问题
> 	由于国内百度收录时效太低（文章收录不全），谷歌国内又无法使用，因此这种办法并不好。
- swifttype.com（收费）
	提交网站数据让其爬取然后提供搜索功能。
 
## 统计插件
- cnzz（目前被友盟收购）
- 百度

# 发布 Github Pages
- 和 [[Hugo#发布Github Pages]] 相同
- [[Vercel#部署]] 
- [[Github Pages#域名绑定]]

# Ref
- [文档 | Hexo](https://hexo.io/zh-cn/docs)
