---
title: Linux内存和硬盘清理
tags:
  - Linux
  - docker
categories:
  - Coding
abbrlink: 3b8c769c
date: 2023-06-19 23:37:45
---

# 内存释放
```shell
echo 1 > /proc/sys/vm/drop_caches
```


# 清理日志
## 清空日志文件
```bash
cat /dev/null > nohup.out
```

## 清理 systemd-journald 产生的日志文件
在路径 `./var/log/journal` 下的文件过大时，这通常是由于系统日志引起的。您可以采取以下步骤来清理这些日志文件：

1. 停止系统日志服务：
	```shell
	sudo systemctl stop systemd-journald.service
	```

2. 清理日志文件：删除旧的或不再需要的日志文件。可以使用 `rm` 命令删除文件，例如：
	```shell
	sudo rm /var/log/journal/*.journal
	```

	上述命令将删除 `/var/log/journal` 目录下的所有 `.journal` 文件，当然日志文件不一定是 `*.journal` 格式。
	
	或者，您可以使用 `find` 命令结合 `-mtime` 选项来删除指定时间之前的日志文件。例如，下面的命令将删除 30 天之前的日志文件：
	```shell
	sudo find /var/log/journal -type f -mtime +30 -exec rm {} \;
	```

	请注意，对日志文件进行删除操作需要 root 权限，因此需要使用 `sudo` 命令或以 root 用户身份运行命令。

3. 启动系统日志服务：
	```shell
	sudo systemctl start systemd-journald.service
	```

请注意，日志文件的清理可能会导致丢失一些历史日志数据。在清理日志之前，请确保已备份重要的日志文件或确认您不再需要这些日志数据。此外，如果您希望定期自动清理日志文件，可以考虑设置日志管理策略或使用日志旋转工具来管理日志文件的大小和保留期限。具体的配置方法取决于您使用的日志服务和系统。

## 清理 Docker 日志文件
Docker 日志文件过大，例如 `/var/lib/docker/overlay2` 目录下的文件过大时，可以采取以下步骤来处理：

1. 清理无用的镜像和容器：使用 Docker 命令清理不再使用的镜像和容器。首先，列出所有停止的容器和无用的镜像：
	```shell
	docker ps -a -q --filter "status=exited" | xargs docker rm
	docker images -q --filter "dangling=true" | xargs docker rmi
	```

	上述命令将删除所有已停止的容器和无用的镜像，从而释放一些磁盘空间。

2. 清理 Docker 卷（Volumes）：Docker 会在 `/var/lib/docker/volumes` 目录下保留容器使用的卷数据。检查是否有未使用的卷并进行清理：
	```shell
	docker volume ls -qf dangling=true | xargs docker volume rm
	```

	上述命令将删除未关联到任何容器的卷。

3. 清理不再使用的镜像层：使用 `docker system prune` 命令来清理不再使用的镜像层、网络和构建缓存等：
	```shell
	docker system prune -a
	```

	此命令将删除未使用的镜像和相关资源。

4. 移动 Docker 数据目录：如果磁盘空间非常有限，您可以考虑将 Docker 的数据目录迁移到具有更大空间的磁盘。这需要一些配置步骤，请确保在进行迁移之前备份重要的数据，并按照 Docker 官方文档提供的指南进行操作。

# df
`df` 命令（磁盘空间使用情况）用于显示文件系统的磁盘空间使用情况的统计信息。

语法：
```shell
df [选项] [文件系统]
```

常用选项：
- `-h, --human-readable`：以人类可读的方式显示大小，例如使用 GB、MB 等单位。
- `-H, --si`：以基于国际单位制的方式显示大小，例如使用 GB、MB 等单位。
- `-T, --print-type`：显示文件系统类型。
- `-t <文件系统类型>, --type=<文件系统类型>`：仅显示指定类型的文件系统。
- `-i, --inodes`：显示文件系统的 inode 使用情况。
- `-a, --all`：显示所有文件系统，包括虚拟文件系统。
- `-x <文件系统类型>, --exclude-type=<文件系统类型>`：排除指定类型的文件系统。

参数：
- `文件系统`：可选参数，用于指定要显示的特定文件系统。

示例用法：
1. 显示所有文件系统的磁盘空间使用情况，以人类可读的方式：
	```shell
	df -h
	```

2. 仅显示 ext4 文件系统的磁盘空间使用情况，以基于国际单位制的方式：
	```shell
	df -H -t ext4
	```

3. 显示 `/dev/sda1` 文件系统的磁盘空间使用情况，以人类可读的方式：
	```shell
	df -h /dev/sda1
	```

4. 显示文件系统的 inode 使用情况：
	```shell
	df -i
	```

5. 显示所有文件系统的磁盘空间使用情况，包括虚拟文件系统：
	```shell
	df -a
	```

`df` 命令将输出各个文件系统的统计信息，包括文件系统的设备名称、总容量、已使用空间、可用空间、使用百分比和挂载点等。

# du
`du` 命令（磁盘使用量）用于计算文件或目录的磁盘使用量。

语法：
```shell
du [选项] [文件或目录]
```

常用选项：
- `-h, --human-readable`：以人类可读的方式显示大小，例如使用 GB、MB 等单位。
- `-H, --si`：以基于国际单位制的方式显示大小，例如使用 GB、MB 等单位。
- `-s, --summarize`：仅显示总计大小。
- `-c, --total`：显示总计大小，并包含每个文件或目录的大小。
- `-a, --all`：显示所有文件和目录的大小，而不仅仅是目录的总大小。
- `-d <深度>, --max-depth=<深度>`：指定递归的最大深度，仅显示指定深度的文件和目录。
- `-t <阈值>, --threshold=<阈值>`：仅显示大于指定阈值的文件和目录。
- `-x, --one-file-system`：仅计算指定文件或目录所在的文件系统的使用量。
- `-i, --inodes`：显示文件或目录的 inode 使用情况。
- `-L, --dereference`：对符号链接进行解引用，显示它们所指向的对象的使用量。

参数：
- `文件或目录`：要计算使用量的文件或目录路径。

示例用法：
1. 显示当前目录的磁盘使用量，以人类可读的方式：
	```shell
	du -h
	```

2. 仅显示 `/path/to/directory` 目录的总计使用量，以基于国际单位制的方式：
	```shell
	du -H -s /path/to/directory
	```

3. 显示 `/path/to/directory` 目录下所有**文件**和目录的使用量，包括子目录，以人类可读的方式：
	```shell
	du -h -a /path/to/directory
	```

4. 仅显示当前目录下直接子目录的使用量，最大深度为 1，以人类可读的方式：
	```shell
	du -h -d 1
	```
5. 显示当前目录下大于 1GB 的文件和目录的使用量，以人类可读的方式：
	```shell
	du -h -t 1G
	```

`du` 命令会计算给定文件或目录的磁盘使用量，并显示各个文件或目录的大小。如果没有指定文件或目录，默认情况下，`du` 命令将递归地计算当前目录下所有文件和目录的使用量。

排序：
`du` 命令本身不直接支持排序功能，但您可以结合其他命令，如 `sort`，来对 `du` 命令的输出进行排序。以下是几种常见的排序操作示例：
1. 按照文件/目录大小排序：
	```shell
	du -h | sort -hr
	```
	上述命令将使用 `du -h` 命令获取文件/目录大小，并将其输出通过管道传递给 `sort` 命令进行排序。`-h` 选项用于以人类可读的方式显示文件/目录大小，`-r` 选项表示以逆序（降序）排序。

2. 按照文件/目录名称排序：
	```shell
	du -h | sort
	```

3. 仅排序文件/目录大小而不显示详细信息：
	```shell
	du -h | sort -hr | awk '{print $1}'
	```
	上述命令将使用 `du -h` 命令获取文件/目录大小，并将其输出通过管道传递给 `sort` 命令进行排序，然后使用 `awk` 命令提取出仅包含文件/目录大小的部分。
