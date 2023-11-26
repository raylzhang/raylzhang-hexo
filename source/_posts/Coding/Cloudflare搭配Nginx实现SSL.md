---
title: Cloudflare搭配Nginx实现SSL
tags:
  - CDN
categories:
  - Coding
abbrlink: ad10a44d
date: 2023-06-14 15:46:02
---
> ref: https://www.digitalocean.com/community/tutorials/how-to-host-a-website-using-cloudflare-and-nginx-on-ubuntu-20-04

前置参考： [[Backblaze B2、Cloudflare和PicGo搭建免费图床]]

# 1. 确保 Cloudflare 中网站 DNS 配置开启代理
![image.png](https://static.raylzhang.top/img/202306141609667.png)
# 2. 生成 Origin CA TLS 证书
![image.png](https://static.raylzhang.top/img/202306141551078.png)
![image.png](https://static.raylzhang.top/img/202306141552256.png)
> 能建 15 年全域名证书！

![image.png](https://static.raylzhang.top/img/202306141554331.png)
生成 `PEM` 格式证书，复制分别保存至本地文件 `example.com.pem` 和 `example.com-key.pem` 文件。
> 注意
> 1. 这里 key 也需要保存为 `pem` 格式文件
> 2. 私钥只在此刻展示，之后不会再出现 

![image.png](https://static.raylzhang.top/img/202306141558372.png)
之后可以在这里通过 `下载` 查看证书，但无法查看私钥，如果忘记，请 `吊销` 后重新 `创建证书`。
# 3. Nginx 配置
```nginx
server {
    listen 80;
    server_name example.com www.example.com;
	# http强制跳转至https
    return 301 https://$host$request_uri;
}
server {
    listen 443 ssl http2;
    ssl_certificate /etc/nginx/ssl/cloudflare/example.com.pem;
    ssl_certificate_key /etc/nginx/ssl/cloudflare/example.com-key.pem;
    server_name example.com www.example.com;
    root /usr/share/nginx/html;
    index index.html index.htm;
    location / {
        try_files $uri $uri/ =404;
    }
}
```
在 Cloudflare 中设置加密模式为 `完全（严格）`
![image.png](https://static.raylzhang.top/img/202306141606720.png)
# 4. 设置 Authenticated Origin Pull
我们可以通过 TLS 客户端身份验证来验证我们的 Nginx 服务器是否正在与 Cloudflare 通信。
客户端身份验证的 TLS 握手中，双方都提供要验证的证书。服务器配置成为仅接受使用 Cloudflare 的有效客户端证书的请求才能通过，未通过 Cloudflare 的请求将被丢弃，因为它们没有 Cloudflare 证书。这样可以防止攻击者无法绕过 Cloudflare 的安全措施，直接连接到 Nginx 服务器。
我没有配置，具体配置参考： https://www.digitalocean.com/community/tutorials/how-to-host-a-website-using-cloudflare-and-nginx-on-ubuntu-20-04#step-3-setting-up-authenticated-origin-pulls