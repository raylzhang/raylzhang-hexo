---
title: Vercel
tags:
  - 建站
  - TODO
categories:
  - Coding
abbrlink: edee1d8b
date: 2023-06-10 00:34:43
---

# 部署
当我们提交代码至 Github 上后，Vercel 会自动编译，因此我们只需要配置一次即可。

## Github Pages 部署（推荐）
直接 `import` 即可。

## Hugo 源码部署
![](https://static.raylzhang.com/img/202306070225740.png)

注意事项：
1. `public` 文件夹添加到 `.gitignore` 中（不上传 `public` 文件夹）
2. 删除 `themes/even` 中的 `.git` 文件

# 绑定域名 
![](https://static.raylzhang.com/img/202306070225741.png)

# 解决国内无法访问问题
官方说明：
> 我们进行了更改，以确保 vercel.com 和 vercel.app 域可以在中国境内被屏蔽后再次从中国访问。
> 对于在 Vercel 上使用自定义域的受影响用户，可以通过将指向 Vercel 的 A 记录值从 76.76.21.21 更改为 76.223.126.88 来缓解该问题。
> 虽然我们已经解决了影响 CNAME 记录的问题，但我们仍然建议将 cname.vercel-dns.com 更改为 cname-china.vercel-dns.com 以获得额外的冗余。

按照官方说明修改即可。

==TODO== 目前无法解决国内访问的问题，可以使用 Nginx 本地部署，通过 Cloudflare 实现代理和 SSL [[Cloudflare搭配Nginx实现SSL]]