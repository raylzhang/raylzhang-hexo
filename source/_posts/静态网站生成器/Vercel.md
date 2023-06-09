---
title: Vercel
tags: [site]
categories:
  - 静态网站生成器
date: 2023-06-10 00:34:43
---
# 解决国内无法访问问题
官方说明：
> 我们进行了更改，以确保 vercel.com 和 vercel.app 域可以在中国境内被屏蔽后再次从中国访问。
> 对于在 Vercel 上使用自定义域的受影响用户，可以通过将指向 Vercel 的 A 记录值从 76.76.21.21 更改为 76.223.126.88 来缓解该问题。
> 虽然我们已经解决了影响 CNAME 记录的问题，但我们仍然建议将 cname.vercel-dns.com 更改为 cname-china.vercel-dns.com 以获得额外的冗余。

按照官方说明修改即可。