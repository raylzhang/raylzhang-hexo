---
title: Backblaze B2、Cloudflare和PicGo搭建免费图床
tags:
  - 建站
  - CDN
categories:
  - Coding
abbrlink: 405faf41
date: 2023-06-23 12:04:55
---
> ref: https://zhuanlan.zhihu.com/p/604285576
> ref: https://www.coca.cc/mf/37.html
> ref: https://www.typeboom.com/archives/65/

由于国内图床方案存在备案以及费用等问题，所以我们将目光转向国外。
[Cloudflare Bandwidth Alliance宽带联盟](https://www.cloudflare.com/zh-cn/bandwidth-alliance/)中包含 Backblaze，因此 Backblaze 到 Cloudflare 的所有出口流量完全免费，再加上 Backblaze 对个人用户提供 10G 的免费存储额度，每天 1G 的下载量与无限上传量，我们可以同时使用两者达到 10G 免费额度与不限量上传下载。即使超过免费存储额度，相比其他国外主流的 OSS 服务提供商，Backblaze 的价格也较为低廉，但作为个人图床来说免费额度已经完全足够了。

在使用 Backblaze 之前需要购买一个域名，比较推荐 [NameSlio](https://www.namesilo.com/)，支持支付宝，免费 Whois 隐私保护，同时价格便宜。

# Backblaze OSS 搭建
1. [创建 Backblaze 帐号，并完善相关信息](https://www.backblaze.com/b2/cloud-storage.html)，直接从首页进入可能没有 Sign Up 选项
2. [进入控制台](https://secure.backblaze.com/b2_buckets.htm)，创建 Buckets 存储桶
3. 给桶起一个名字
	- 方便识别且不易被猜测即可，无需在意生成的图片链接长短，后续我们会 301 重定向
	- 将 `Files in Bucket are` 修改为 `Public`

	> 注意：给存储桶起名时尽量起不易被别人猜测的名字，可在其中增加部分随机字符，如 `c42rx71-example-winer-website`，因为在存储桶的模式为 Public 时，别人只需知道你的 OSS 服务提供商+存储桶名称+其中一个文件名，即可拼凑出文件真实链接，从而绕过 CDN 刷空你的免费流量，如果有绑定支付方式还会扣费。
 
	![image.png](https://static.raylzhang.com/img/202306231224661.png)
4. 点击 `上传/下载` 上传一张图片或临时文件，用于后续获取存储桶所在的服务器地址
5. 从左侧菜单栏的 `Browse Files` 进入刚刚的存储桶并找到上传的文件，点击查看详细信息，记住 `Friendly URL` 行的链接内容
	![image.png](https://static.raylzhang.com/img/202306231229276.png)
	![image.png](https://static.raylzhang.com/img/202306231233981.png)
6. 从 `Friendly URL` 的链接可以看到我们的存储桶位于 https://f005.backblazeb2.com/ ，而 `/file/example-winer-website` 则是存放文件目录的相对路径，记住这两个值后登陆 Cloudflare 进行设置

> 注意：如果上传文件路径中包含空格，在 Backblaze 存储时会将空格转换为 `+`，导致链接不正确

## 生成应用密钥
1. [申请地址](https://secure.backblaze.com/app_keys.htm)
2. 点击 `Add a New Application Key`
	- `Name of Key`：随便填
	- `Allow access to Bucket(s)`：创建的 Bucket
	- `Type of Access (Optional)`：Read and Write
	- `Allow List All Bucket Names (Optional): Allow listing all bucket names including bucket creation dates (required for S3 List Buckets API)`：勾选
	- `Duration (seconds) (Optional)`：根据需要填写。Key 的最长有效时间为 1000 天，即 86400000 秒，过期后请重新申请
3. 保存好 `keyID` 和 `applicationKey`

![image.png](https://static.raylzhang.com/img/202308022159681.png)

# Cloudflare 配置
1. 打开 [Cloudflare官网](https://www.cloudflare.com/zh-cn/)注册并登录
2. 登录你的域名注册服务商，修改 DNS 解析服务器到 Cloudflare
	![image.png](https://static.raylzhang.com/img/202306250229879.png)
3. 添加一条 CNAME 记录到 Cloudflare 中你域名的 DNS 管理中，二级域名可以根据喜好选择，但一般使用这几种：`oss`、`img`、`images`、`assets`、`static`，我选择的 `static`，这样我就可以在域名后面添加不同文件类型名称来区分，例如 `https://static.raylzhang.com/img/...` 或者 `https://static.raylzhang.com/js/...` 等
	![image.png](https://static.raylzhang.com/img/202306250234322.png)
4. 点击“**SSL/TLS - 概述**”，加密模式选择“完全”
	 ![image.png](https://static.raylzhang.com/img/202306260055210.png)
5. 等待 DNS 解析完后我们就完成了通过 Cloudflare 访问 Backblaze 的设置。可以使用浏览器的开发者工具，访问你设置的二级域名下对应的网址来查看是否命中 CDN 缓存，
	- `Cf-Cache-Status` 行 `HIT` 代表命中 CDN 缓存
	- `MISS` 代表没有命中 CDN 缓存，回源到 Backblaze，消耗下载流量
	![image.png](https://static.raylzhang.com/img/202306260106929.png)

6. 为了避免无法命中缓存或回源次数过多导致加载速度低下，我们需要回到 Backblaze 进行桶信息设置，添加 `{"cache-control":"max-age=86400"}`，意味 86400 秒（24 小时）内 Cloudflare 不再返回源站重新获取信息。
	> 注意，“回源”即为 CDN 节点回到源站重新拉取数据，然后再传递给用户，并不是将源站地址直接转给用户，所以无需担心回源过多导致免费流量配额消耗完毕。`max-age` 不用太长，如果太长，若源文件发生更改，且没有主动推送到 CDN 节点，这时会导致用户不能及时得到最新版本。
	> `{"cache-control":"max-age=43200"}` 表示默认不会进行缓冲。

	![image.png](https://static.raylzhang.com/img/202306260117451.png)
7. 缓存配置（**Rules - Page Rules**）
	![image.png](https://static.raylzhang.com/img/202308022237022.png)

8. 设置转换规则（**Rules - Transform Rules**）
	由于重定向方式会暴露桶名称，我们选择通过重写的方式进行解决，这种方式可以在链接不变的情况下改写其中的内容。
	- 匹配 `主机名` 用于确定请求来源
	- 匹配 `完整 URI` 过滤已经重写过的链接，避免出现反复重写的错误
	- 重写路径中的 `concat` 用于将两个字符串拼接，即在请求的文件路径前添加存储桶路径，而主机名 `statis.raylzhang.com` 在使用 concat 函数时无需填写，会自动添加
		- 例如：当前请求的 URI 路径是 `/example`, 则该转换规则将会生成 `/file/raylzhang-xxxx/example` 的字符串

	> 注：如果页面规则剩余不足或不想使用本方法，也可以[参考本文](https://help.backblaze.com/hc/en-us/articles/360010017893-How-to-allow-Cloudflare-to-fetch-content-from-a-Backblaze-B2-private-bucket)创建私有存储桶并使用 Cloudflare Workers 来进行访问

	![SCR-20230626-chnt.png](https://static.raylzhang.com/img/202306260154406.png)

9. 重写响应头
   Backblaze B2 会在请求的响应头中添加以下几个 header 参数：
	```javascript
	x-bz-content-sha1
	x-bz-file-id
	x-bz-file-name
	x-bz-upload-timestamp
	```
	虽然影响不大，但是一看这些参数就知道你用的 B2，并且这些参数头一般拿来也没啥用，可以通过 CloudFlare 的重写规则将其去掉。

	![image.png](https://static.raylzhang.com/img/202308022319045.png)

# PicGo 配置
[官网地址](https://molunerfinn.com/PicGo/)
1. 插件设置中安装 `s3` 插件
2. [[#生成应用密钥]]
3. 在图床设置中设置 `Amazon S3`
	![image.png](https://static.raylzhang.com/img/202307021839207.png)
4. 根据实际情况进行其他配置
	- 设置快捷键
	- 开启自启
	- 时间戳重命名
	- 开启上传提示
	- 上传后自动复制 URL

	这些是我配置的选项，日常中我只需要复制一张图片，然后执行我配置的快捷键，图片会自动上传，上传成功后自动复制图片地址。

## Obsidian 插件
在我主力笔记工具 Obsidian 中，我使用 Image auto upload 插件进行无感的图片上传体验（包括你看到的这篇文章的图片也是这样操作的），一定要开启“剪切板自动上传”。这样配置后，我截完图（或者复制图片）并复制在 Obsidian 笔记中，这个插件会自动上传并自动粘贴回传后的图片地址。
![image.png](https://static.raylzhang.com/img/202307021908338.png)
当然我们也可以把笔记中所有附件图片通过快捷方式（可自定义）全部自动上传（或全部自动下载），并全部自动转化为回传地址：
![image.png](https://static.raylzhang.com/img/202307021914092.png)

# 域名 SSL 配置
[[Cloudflare搭配Nginx实现SSL]]