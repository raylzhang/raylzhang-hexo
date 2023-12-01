---
title: Nginx安装
date: 2023-12-01 17:12:25
tags:
  - Nginx
---
# ubuntu 20.4
1. 下载
	```Bash
	wget http://nginx.org/download/nginx-1.19.0.tar.gz
	```
2. 安装依赖
	```Bash
	sudo apt install openssl libssl-dev libpcre3 libpcre3-dev zlib1g-dev make
	```
3. 解压进入
	```Bash
	tar -zxvf nginx-1.19.0.tar.gz
	cd nginx-1.19.0
	```
4. 编译
	```Bash
	./configure --prefix=/opt/nginx/nginx-1.19.0 \
	    --with-http_ssl_module  \
	    --with-http_gzip_static_module \
	    --http-client-body-temp-path=/opt/nginx/nginx-1.19.0/temp/client_body_temp   \
	    --http-proxy-temp-path=/opt/nginx/nginx-1.19.0/temp/proxy_temp   \
	    --http-fastcgi-temp-path=/opt/nginx/nginx-1.19.0/temp/fastcgi_temp   \
	    --http-uwsgi-temp-path=/opt/nginx/nginx-1.19.0/temp/uwsgi_temp   \
	    --http-scgi-temp-path=/opt/nginx/nginx-1.19.0/temp/scgi_temp 
	```
5. 安装
	```Bash
	make && make install
	```
6. 检测
	```Bash
	/opt/nginx/nginx-1.19.0/sbin/nginx -t
	```

## 设置开机启动
1. 创建 nginx.service 服务
	```Bash
 	> sudo vim /usr/lib/systemd/system/nginx.service
	
	[Unit]
	Description=The nginx HTTP and reverse proxy server
	After=network.target remote-fs.target nss-lookup.target
	
	[Service]
	Type=forking
	PIDFile=/opt/nginx/nginx-1.19.0/logs/nginx.pid
	# Nginx will fail to start if nginx.pid already exists but has the wrong SELinux context. This might happen when running `nginx -t` from the cmdline.
	# https://bugzilla.redhat.com/show_bug.cgi?id=1268621
	ExecStartPre=/usr/bin/rm -f /opt/nginx/nginx-1.19.0/logs/nginx.pid
	ExecStartPre=/opt/nginx/nginx-1.19.0/sbin/nginx -t
	ExecStart=/opt/nginx/nginx-1.19.0/sbin/nginx
	ExecReload=/bin/kill -s HUP $MAINPID
	KillSignal=SIGQUIT
	TimeoutStopSec=5
	KillMode=process
	PrivateTmp=true
	
	[Install]
	WantedBy=multi-user.target
	```

 	> 注意 nginx.pid 必须在启动前删除，不然无法启动成功。

2. 设置开启启动
	```Bash
	sudo systemctl enable nginx.service
	sudo systemctl daemon-reload
	```

# MacOS
- 直接 HomeBrew 安装