---
title: Linux SSH
date: 2023-11-30 00:56:08
tags:
  - Linux
---
# 命令
```bash
ssh root@ahg-test:/root -p 10022
```

# 免密码登录
## 方法一
1. 在A机下生成公钥/私钥对：
	```bash
	# -P表示密码，-P ''就表示空密码，也可以不用-P参数，这样就要三次回车，
	# 用-P就一次回车。它在/home/ray下生成.ssh目录，.ssh下有id_rsa和id_rsa.pub两个文件。
	[ray ~]$ ssh-keygen -t rsa -P ''
	```

2. 把A机下的`id_rsa.pub`文件内容复制到B机下的`.ssh/authorized_keys`文件里，用`scp`复制。由于还没有免密码登录，所以要输入密码：
	```
	[ray ~]$ scp .ssh/id_rsa.pub root@192.168.1.181:/root/id_rsa.pub 
	root@192.168.1.181's password:
	id_rsa.pub                                    100%  223     0.2KB/s   00:00
	```

3. B机把从A机复制的`id_rsa.pub`添加到`.ssh/authorized_keys`文件里：
	```bash
	[root ~]$ cat id_rsa.pub >> .ssh/authorized_keys

	#authorized_keys 的权限要是600。
	[root ~]$ chmod 600 .ssh/authorized_keys
	```

4. A机登录B机，第一次登录时要你输入`yes`：
	```
	[ray ~]$ ssh 192.168.1.181
	The authenticity of host '192.168.1.181 (192.168.1.181)' can't be established.
	RSA key fingerprint is 00:a6:a8:87:eb:c7:40:10:39:cc:a0:eb:50:d9:6a:5b.
	Are you sure you want to continue connecting (yes/no)? yes
	Warning: Permanently added '192.168.1.181' (RSA) to the list of known hosts.
	Last login: Thu Jul 3 09:53:18 2008 from chenlb
	[root ~]$
	```
现在 A 机可以无密码登录 B 机了，反之亦然。

## 方法二
执行命令：
```bash
ssh-copy-id -i ~/.ssh/id_rsa.pub root@ahg-test
```
把本机的公钥追到ahg-test的`.ssh/authorized_keys`里。

# 配置
## 修改SSH连接数
`vim /etc/ssh/sshd_config`设置`MaxStartups 1000`

## 修改端口号
`vim /etc/ssh/sshd_config`设置`Port 1086`

## 重启SSH服务
`service ssh restart`

## 保持SSH连接不断开
### 方法一：修改客户端参数
`vi /etc/ssh/ssh_config`（如果是Mac系统则为`vi ~/.ssh/ssh_config`，注意不是`sshd_config`文件），后面添加：
```bash
ServerAliveInterval 60
ServerAliveCountMax 60
```
这表示要让所有的ssh连接自动加上此属性。
如果要指定服务端，如下：
```bash
ssh -o ServerAliveInterval=30 <IP地址>
```

### 方法二：服务端配置
编辑服务端 `/etc/ssh/sshd_config`，最后添加：
```bash
# 向客户端每60秒发一次保持连接的信号
ClientAliveInterval 60
# 如果仍要设置断开时间，设置此参数，意思是客户端60次未响应就断开连接
ClientAliveCountMax 60
```
这样，SSH Server每60秒就会自动发送一个信号给Client，而等待Client回应。

# Ubuntu 开启 SSH 远程登录
- [ubuntu开启SSH服务远程登录\_ubuntu ssh-CSDN博客](https://blog.csdn.net/jackghq/article/details/54974141)

# 常见问题
## SSH连接报错
- 报错信息：
	```
	Unable to negotiate with 59.173.19.171 port 22: no matching key exchange method found. Their offer: diffie-hellman-group-exchange-sha1,diffie-hellman-group1-sha1
	```
	解决办法：在客户端`.ssh/config`配置文件中添加：
	```bash
	Host *
		KexAlgorithms +diffie-hellman-group1-sha1
	```

- 报错信息：
	```
	Unable to negotiate with 59.173.19.171 port 22: no matching cipher found. Their offer: aes128-cbc,3des-cbc,blowfish-cbc,cast128-cbc,arcfour,aes192-cbc,aes256-cbc,rijndael-cbc@lysator.liu.se
	```
	解决办法：修改`/etc/ssh/ssh_config`配置文件，找到`# Ciphers aes128-ctr,aes192-ctr,aes256-ctr,aes128-cbc,3des-cbc`，去掉注释。

## SSH公私钥正确的情况下免密登录失败
有的时候我们经常会遇到在服务器上配置ssh公钥后，一段时间可以免密码登录，后来登录时，每次都提示要输入密码。这时我们可以删除`known_hosts`，重新把`id_rsa.pub`添加到服务器`~/.ssh/authorized_keys`下。 如果这个办法也不行，我们（首先考虑是权限问题）要查看日志。`/var/log/auth.log`日志中报错如下：
```bash
coffeeserver sshd[6761]: Authentication refused: bad ownership or modes for directory /root/.ssh
```
`/var/log/secure`日志中报错如下：
```
Authentication refused: bad ownership or modes for directory /root/.ssh
```
这些日志都告诉了我们`/root/.ssh`的目录的权限的配置出现了问题。（权限应为700）

## 解决SSH的`Write failed: Broken pipe`问题
- 方法一：如果您有多台服务器，不想在每台服务器上设置，只需在客户端的`~/.ssh/`文件夹中添加`config`文件，并添加下面的配置：
	```
	ServerAliveInterval 60
	```

- 方法二：如果您有多个人管理服务器，不想在每个客户端进行设置，只需在服务器的`/etc/ssh/sshd_config`中添加如下的配置：
	```
	ClientAliveInterval 60
	```

- 方法三：如果您只想让当前的ssh保持连接，可以使用以下的命令：
	```bash
	$ ssh -o ServerAliveInterval=60 user@sshserve
	```

## SSH链接过慢
SSH连接过程包括：
1. Server的SSHD会去DNS查找访问的Client IP的HOSTNAME，如果DNS不可用或者没有相关记录，就会消耗一段时间
2. 在authentication gssapi-with-mic有时候也会消耗一段时间

### 查找原因
- 查看debug日志
	```bash
	ssh -v root@192.168.100.10
	```
- 检测连接时间
	```bash
	time ssh root@192.168.100.10 exit
	```

### 解决办法
建议一个个设置，因为每个人连接慢的原因都不一样。修改之后记得重启sshd服务：`service sshd restart`
- **关闭DNS反向解析**
	在Linux中，默认就是开启了SSH的反向DNS解析，这个会消耗大量时间，因此需要关闭。
	```bash
	vim /etc/ssh/sshd_config

	UseDNS no
	```
	在配置文件中虽然`UseDNS yes`是被注释的，但默认开关就是yes。

- **关闭Server上的GSS认证**
	在authentication gssapi-with-mic有很大的可能出现问题，因此关闭GSS认证可以提高ssh连接速度。
	```bash
	vim /etc/ssh/sshd_config
	GSSAPIAuthentication no
	```

- **修改Server上nsswitch.conf文件**
	```bash
	vim /etc/nsswitch.conf

	#找到
	hosts: files dns
	#改为
	hosts: files
	```
	`hosts: files dns`这一行含义是对于访问的主机进行域名解析的顺序，是先访问file，也就是`/etc/hosts`文件，如果hosts中没有记录域名，则访问DNS进行域名解析，如果DNS也无法访问，就会等待访问超时后返回，因此等待时间比较长。
	如果Server需要通过域名访问其他服务器，则需要保留此行。

- **修改Server上resolv.conf文件**
	- 删除`/etc/resolv.conf`中所有不使用的IP。
	- 如果Server曾经配置过双网卡，则在该文件中会有一行目前不使用的IP地址，删除该行即可。

- **修改Server上hosts文件**
	在Server上`/etc/hosts`文件中把客户端的IP和HOSTNAME加入。

- **打开Server上的`IgnoreRhosts`参数**
	`IgnoreRhosts`参数可以忽略以前登录过主机的记录，设置为yes后可以极大的提高连接速度。
	```bash
	vim /etc/ssh/sshd_config

	IgnoreRhosts yes
	```

- **修改客户端的hosts文件**
	将目标Server的IP和域名加上去，使得本机的DNS服务能解析目标地址。
	```bash
	vim /etc/hosts

	192.168.100.11  doiido.com
	```
	hosts文件格式为目标SERVER_IP 目标SERVER_NAME。但是使用这个方法有一个弊端，需要给每台SERVER都添加一个域名解析。

- **修改客户端配置文件ssh_conf（注意，不是sshd_conf）**
	```bash
	vim /etc/ssh/ssh_conf

	#找到
	GSSAPIAuthentication yes
	#改为
	GSSAPIAuthentication no
	```

## 解决`SSH no matching host key type found`问题
如果最近升级到了`openssh 8.8-p1`版，你会发现服务器突然无法连接：
```bash
> git clone git@github.com:user/repository.git

Cloning into 'xxxx'...
Unable to negotiate with x.x.x.x port 22: no matching host key type found. Their offer: ssh-rsa,ssh-dss
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
```
或者仓库无法clone：
```bash
> git clone git@github.com:user/repository.git

Cloning into 'xxxx'...
Unable to negotiate with x.x.x.x port 22: no matching host key type found. Their offer: ssh-rsa,ssh-dss
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
```
解决办法是`ssh`命令指定算法：
```bash
ssh -o HostKeyAlgorithms=+ssh-rsa -o PubkeyAcceptedKeyTypes=+ssh-rsa user@host -p 2222
```
上面比较麻烦，可以修改ssh配置文件`~/.ssh/config`，对于无法成功连接的host增加配置项：
```shell
Host ssh.alanwei.com  
HostName ssh.alanwei.com  
User alan  
Port 22  
HostKeyAlgorithms +ssh-rsa  
PubkeyAcceptedKeyTypes +ssh-rsa
```
> `HostName`、`User`、`Port`可以省略。

或者对所有`Host`指定：
```shell
Host *
	ServerAliveInterval 10
	HostKeyAlgorithms +ssh-rsa
	PubkeyAcceptedKeyTypes +ssh-rsa
```