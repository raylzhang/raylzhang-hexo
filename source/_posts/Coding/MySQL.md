---
title: MySQL
tags:
  - MySQL
categories:
  - Coding
abbrlink: c24675b4
date: 2023-08-12 21:07:32
---
# 连接参数
```properties
spring.datasource.url=jdbc:mysql://localhost:3306/tech-mybatisplus?useSSL=false&useUnicode=true&characterEncoding=utf-8&serverTimezone=Asia/shanghai
```

1. 如果 `useSSL=true`（默认）在 Mac 系统下可能导致无法连接
2. 如果在 MySQL8 或者在 MySQL5下使用驱动 `com.mysql.cj.jdbc.Driver`（驱动向下兼容），必须设置 `serverTimezone`。当然，直接使用 MySQL5驱动（`com.mysql.jdbc.Driver`）就不用设置 `serverTimezone`
	```shell
	serverTimezone=Asia/Shanghai
	serverTimezone=GMT%2B8
	```

# Linux 下更改 MySQL5.7 数据库存储位置
1. 停止 MySQL 进程
2. 复制目录：
	```shell
	cp -R /var/lib/mysql /data/.
	```
1. 修改配置文件 `/etc/my.cnf`
	```shell
	datadir=/data/mysql
	socket=/data/mysql/mysql.sock
	```
4. 启动 MySQL

# MySQL 开启主从复制（Binlog）
在主库中开启 Binlog 功能，这样主库就可以把 Binlog 传递给从库，从库拿到 Binlog 后实现数据恢复达到主从数据一致性。

1. 创建主从数据库 mysql-master（端口 33061）和 mysql-slave（端口 33062）。
2. 在 mysql-master 中配置 slave 访问的账户：
	```mysql
	grant replication slave on *.* to 'rep1'@'%' identified by 'root';	
	```
3. 修改 master 数据库配置文件（如果是 Docker 创建的数据库，可以在宿主机创建后复制到 Docker 内）。
	```bash
	docker cp mysql-master:/etc/mysql/mysql.conf.d/mysqld.cnf .
	vim ./mysqld.cnf
	
	# 在mysqld.cnf中添加如下配置
	log-bin=/var/lib/mysql/binlog
	server-id=1
	binlog-do-db=testdb
	```
	其中：
	- `log-bin`：Binlog 的位置，理论可以放在任意位置，但需要 MySQL 对它有操作权限
	- `server-id`：在 MySQL 集群中，每一个数据库都需要有一个唯一 id
	- `binlog-do-db`：配置哪些库需要同步
	然后复制到容器内：`docker cp ./mysqld.cnf mysql-master:/etc/mysql/mysql.conf.d/`
	重启 mysql-master：`docker restart mysql-master`
4. 记录 master 配置项。
	进入 mysql-master 执行：
	```mysql
	show master status;
	```
	如果配置正确，记录 File 和 Position 的值	
	例如：File: `binlog.000001`，Position: `154`
5. 修改 slave 数据库配置文件。
	```bash
	docker cp mysql-slave:/etc/mysql/mysql.conf.d/mysqld.cnf .
	vim ./mysqld.cnf
	
	# 在mysqld.cnf中添加如下配置
	server-id=2
	```
	然后复制到容器内：`docker cp ./mysqld.cnf mysql-slave:/etc/mysql/mysql.conf.d/`
	重启 mysql-slave：`docker restart mysql-slave`
6. 配置 slave 数据库。
	进入 mysql-slave 执行：
	```mysql
	change master to master_host='172.17.0.1',master_port=33061,master_user='rep1',master_password='root',master_log_file='binlog.000001',master_log_pos=154;
	start slave;
	```
	> master_host 和 master_port 设置宿主机 IP 和端口，保证 slave 能正常连接。
7. 检查 slave 是否正常启动。
	进入 mysql-slave 执行：
	```mysql
	show slave status\G
	```
	确保 Slave_IO_Running 和 Slave_SQL_Running 的值都为 `Yes`。
	如果有问题，可以通过关闭 slave 后修改 slave 配置再开启 slave，这样反复进行检查：
	```mysql
	stop slave;
	start slave;
	show slave status\G
	```

# update 语句加锁
**当我们要执行 update 语句的时候，确保 where 条件中带上了索引列，并且在测试机确认该语句是否走的是索引扫描，防止因为扫描全表，而对表中的所有记录加上锁。**

我们可以打开 MySQL 里的 sql_safe_updates 参数，这样可以预防 update 操作时 where 条件没有带上索引列。

如果发现即使在 where 条件中带上了列索引列，优化器走的还是全标扫描，这时我们就要使用 `force index([index_name])` 可以告诉优化器使用哪个索引。


> [!NOTE] Reference
> https://www.cnblogs.com/frankyou/p/15271070.html


# 常见问题
## MySQL 删除数据库时的错误（errno: 39）
删除 `/var/lib/mysql/tablename` 下所有文件，不要删除 `tablename` 本身，然后再通过命令 `drop database` 就可以了。