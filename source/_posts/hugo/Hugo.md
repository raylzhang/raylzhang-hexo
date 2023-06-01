---
title: Hugo
tags: [todo, obsidian]
categories:
  - hugo
date: 2023-06-02 01:12:18
ref: https://www.bilibili.com/video/BV1mg411b7Tu
---

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

# 发布Github Pages
```bash
cd ..
git clone git@github.com:raylzhang/raylzhang.github.io.git

# 软链接至hugo发布目录
cd raylzhang
rm -rf public
ln -s /Users/raylzhang/prj-ray/raylzhang.github.io /Users/raylzhang/prj-ray/raylzhang/public

# 编译并发布
hugo
cd ../raylzhang.github.io
git add *
git commit -m "first commit"
git push
```

# 部署Vercel
当我们提交代码至Github上后，Vercel会自动编译，因此我们只需要配置一次即可。

## Github Pages部署（推荐）
直接`import`即可。

## Hugo源码部署
![](Hugo-20230422.png)

注意事项：
1. `public`文件夹添加到`.gitignore`中（不上传`public`文件夹）
2. 删除`themes/even`中的`.git`文件

# 绑定域名
## 绑定Github Pages
1. 域名解析添加`A`记录，主机记录为`@`，值为`ping raylzhang.github.io`
2. Github根目录添加文件`CNAME`，值为域名，例如`raylzhang.com`

## 绑定Vercel
![](Hugo-20230422-1.png)

# 搜索引擎收录
常更新，尽量保持独创和高质量，搜索引擎会更快收录你的网站。

## Google
1. 访问：https://search.google.com/search-console/welcome
	![](Hugo-20230423.png)
2. 下载验证文件并放入项目`static`目录下
	![](Hugo-20230423-1.png)
3. 提交Github，Vercel会自动编译
	```bash
	hugo
	cd ../raylzhang.github.io
	git add *
	git commit -m "verify google search engine"
	git push
	```
4. 点击“验证”
	![](Hugo-20230423-2.png)
 5. 点击“前往资源页面”，或直接访问：https://search.google.com/search-console?resource_id=https%3A%2F%2Fwww.raylzhang.com%2F
 6. 设置“站点地图”
	 ![](Hugo-20230423-3.png)
	> 如果`config.toml`没有设置`baseURL`为域名地址，例如`https://www.raylzhang.com/`，则无法访问`sitemap.xml`。
	> 站点地图只用添加一次，Google会定期爬取更新。
	> 如果网站质量没问题，Google会在一到两周之内收录成功。

## 百度
百度和Google一样会自动爬取网站地图，但相对于Google来说，速度非常慢。

1. 进入百度收录平台：[https://ziyuan.baidu.com/site/index](https://ziyuan.baidu.com/site/index)，并添加网站（这里可能会弹出页面，需要你补充个人信息）
	![](Hugo-20230423-4.png)
2. 设置“站点领域”
	![](Hugo-20230423-5.png)
 3. 和Google类似，通过验证文件验证
	![](Hugo-20230423-6.png)
 4. 进行“普通收录”
	![](Hugo-20230423-8.png)
 ## Sogou
不支持sitemap形式，需要手动提交url列表。
 ## Bing
 TODO
 ## 查询收录信息
在搜索引擎输入：`site:raylzhang.com`，点击搜索，就会显示是否收录成功。

# 广告联盟
## Google
1. 进入 https://adsense.google.com/start 并点击“开始使用”
2. 填写网站等信息
	![](Hugo-20230425-2.png)
 3. 点击关联Adsense
	![](Hugo-20230425-3.png)
4. 把Adsense代码粘贴到`header.html`中
	![](Hugo-20230425-4.png)
5. 提交至Github后访问网站按F12，发现Google Adsense已经添加至header中
	![](Hugo-20230425.png)
6. 设置成功后进入“下一页”“申请审核”
	![](Hugo-20230425-5.png)
7. 这时候网站已经在“正在准备”状态，大概需要1、2周审核时间，期间Google会不断发送邮件告之你审核过程，例如不符合要求的部分，你可以针对进行改进，一般情况下常更新、尽量多的原创以及不违反法律法规会增加通过的概率
	![](Hugo-20230425-6.png)
8. 审核通过后在“广告”中进行广告投放管理
# 插入B站、Youtube视频