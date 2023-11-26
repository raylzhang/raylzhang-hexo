---
title: Hugo
tags:
  - 建站
  - TODO
categories:
  - Coding
abbrlink: da6f84dc
ate: 2023-06-02 01:12:18
---
> ref: https://www.bilibili.com/video/BV1mg411b7Tu

# 安装
```bash
brew install hugo
hugo new site raylzhang
cd raylzhang
# 下载主题
git clone https://github.com/olOwolo/hugo-theme-even themes/even
# 应用主题配置文件
cp themes/even/exampleSite/config.toml .
```

# 创建博客
```bash
# 创建站点
hugo new post/my-fist-post.md
# 运行
hugo server
```

# 发布 Github Pages
```bash
cd ..
git clone git@github.com:raylzhang/raylzhang.github.io.git

# 软链接至hugo发布目录
cd raylzhang
rm -rf public
ln -s /Users/raylzhang/prj-ray/raylzhang.github.io /Users/raylzhang/prj-ray/raylzhang-hugo/public

# 编译并发布
hugo
cd ../raylzhang.github.io
git add *
git commit -m "first commit"
git push
```

[[Github Pages#域名绑定]]

# Vercel 部署
[[Vercel#Hugo 源码部署]]
[[Vercel#绑定域名]]

# 搜索引擎收录
常更新，尽量保持独创和高质量，搜索引擎会更快收录你的网站。

## Google
1. 访问： https://search.google.com/search-console/welcome
	![](https://static.raylzhang.com/img/202306070225742.png)
2. 下载验证文件并放入项目 `static` 目录下
	![](https://static.raylzhang.com/img/202306070225743.png)
3. 提交 Github，Vercel 会自动编译
	```bash
	hugo
	cd ../raylzhang.github.io
	git add *
	git commit -m "verify google search engine"
	git push
	```
4. 点击“验证”
	![](https://static.raylzhang.com/img/202306070225744.png)
 5. 点击“前往资源页面”，或直接访问： https://search.google.com/search-console?resource_id=https%3A%2F%2Fwww.raylzhang.com%2F
 6. 设置“站点地图”
	 ![](https://static.raylzhang.com/img/202306070225745.png)
	> 如果 `config.toml` 没有设置 `baseURL` 为域名地址，例如 `https://www.raylzhang.com/`，则无法访问 `sitemap.xml`。
	> 站点地图只用添加一次，Google 会定期爬取更新。
	> 如果网站质量没问题，Google 会在一到两周之内收录成功。

## 百度
百度和 Google 一样会自动爬取网站地图，但相对于 Google 来说，速度非常慢。

1. 进入百度收录平台：[https://ziyuan.baidu.com/site/index](https://ziyuan.baidu.com/site/index)，并添加网站（这里可能会弹出页面，需要你补充个人信息）
	![](https://static.raylzhang.com/img/202306070225746.png)
2. 设置“站点领域”
	![](https://static.raylzhang.com/img/202306070225747.png)
 3. 和 Google 类似，通过验证文件验证
	![](https://static.raylzhang.com/img/202306070225748.png)
 4. 进行“普通收录”
	![](https://static.raylzhang.com/img/202306070225749.png)
## Sogou
不支持 sitemap 形式，需要手动提交 url 列表。
## Bing
TODO
## 查询收录信息
在搜索引擎输入：`site:raylzhang.com`，点击搜索，就会显示是否收录成功。

# 广告联盟
## Google
1. 进入 https://adsense.google.com/start 并点击“开始使用”
2. 填写网站等信息
	![](https://static.raylzhang.com/img/202306070225750.png)
 3. 点击关联 Adsense
	![](https://static.raylzhang.com/img/202306070225751.png)
4. 把 Adsense 代码粘贴到 `header.html` 中
	![](https://static.raylzhang.com/img/202306070225752.png)
5. 提交至 Github 后访问网站按 F12，发现 Google Adsense 已经添加至 header 中
	![](https://static.raylzhang.com/img/202306070225753.png)
6. 设置成功后进入“下一页”“申请审核”
	![](https://static.raylzhang.com/img/202306070225754.png)
7. 这时候网站已经在“正在准备”状态，大概需要 1、2 周审核时间，期间 Google 会不断发送邮件告之你审核过程，例如不符合要求的部分，你可以针对进行改进，一般情况下常更新、尽量多的原创以及不违反法律法规会增加通过的概率
	![](https://static.raylzhang.com/img/202306070225755.png)
8. 审核通过后在“广告”中进行广告投放管理
# 插入 B 站、Youtube 视频