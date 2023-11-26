---
title: Maven
tags:
  - Maven
categories:
  - Coding
abbrlink: 7273cdc
date: 2023-06-18 02:49:16
---

# 安装
```bash
tar -xvzf apache-maven-3.6.0-bin.tar.gz mkdir /opt/maven mv apache-maven-3.6.0 /opt/maven
```
增加配置：
```bash
export MAVEN_HOME=/opt/maven/apache-maven-3.6.0 export PATH=$PATH:$MAVEN_HOME/bin
```

测试：`mvn -v`

# 配置
## 阿里云镜像配置
[阿里云镜像配置](https://help.aliyun.com/document_detail/102512.html?spm=a2c40.aliyun_maven_repo.0.0.36183054eGk3vS)

# 命令
## 依赖
### `-pl`
全称：`--projects`
选项后可跟随`{groupId}:{artifactId}`或者所选模块的相对路径（多个模块以逗号分隔）。

### `-am`
全称：`--also-make`
表示同时处理选定模块所依赖的模块。

### `-amd`
全称：`--also-make-dependents`
表示同时处理依赖选定模块的模块。

### `-N`
全称：`--Non-recursive`
表示不递归子模块。

### `-rf`
全称：`--resume-from`
表示从指定模块开始继续处理。

## 跳过 Test
`mvn package -DskipTests`

# Maven Bom
[[Maven Bom|Maven Bom]]