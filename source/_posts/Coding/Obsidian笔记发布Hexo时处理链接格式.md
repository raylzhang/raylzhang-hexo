---
title: Obsidian笔记发布Hexo时处理链接格式
tags:
  - 建站/Hexo
  - Obsidian
  - TODO
categories:
  - Coding
abbrlink: e935c008
date: 2023-07-03 22:56:10
---

Obsidian 笔记直接被 Hexo 发布时会出现两个问题：
1. 笔记中的链接，包括双向链接引用（md 文件）、图片、视频等不能正确被 Hexo 转化，无法正常访问
2. 文件名如果有空格则无法正确解析
3. 链接中的锚点，例如 `[[Docker#Docker是什么？]]` 这样的锚点跳转无法正确识别。之前使用过 [hexo-backlink插件](https://github.com/Cyrusky/hexo-backlink)，这个插件能正常转化 wiki 格式的双向链接引用，但忽略了锚点跳转（看过其源代码，直接忽略了所有锚点信息）
4. Hexo 笔记 URL 的格式为：`:year/:month/:day/:title/`，这种格式有个非常大的缺点，就是当我们对笔记的日期、分类（文件夹）或文件名进行调整后，原笔记地址就失效了，这样就无法正常分享出去

为了解决上面 3 个文件，我们使用 [hexo-link-obsidian](https://github.com/moelody/hexo-link-obsidian) 插件，这个插件必须依赖 [hexo-abbrlink](https://github.com/rozbo/hexo-abbrlink)（解决 permalink 唯一不变） 和 [link-to-server](https://github.com/moelody/link-to-server)（从 Obsidian API 中获取 Wiki 链接的文件信息） 这两个插件。

# 1. 安装 [hexo-abbrlink](https://github.com/rozbo/hexo-abbrlink)
这个是 npm 的一个 package，在 Hexo 项目根目录下直接安装即可：
```bash
npm install hexo-abbrlink
```

如果出现 `npm ERR! Cannot read properties of null (reading 'pickAlgorithm')` 异常，我们需要清理一下 npm 缓存：
```bash
npm cache clear --force
```
然后再安装一次就应该正常了。

安装成功后根据官方文档在 Hexo `_config.yml` 中添加如下配置：
```yml
permalink: :abbrlink/
abbrlink:
    alg: crc32
    rep: hex
```
> 具体配置说明查看 GitHub 主页文档。

# 2. 安装 [link-to-server](https://github.com/moelody/link-to-server)
这个插件已经无法从 Obsidian 三方插件市场中查找到，我们只能下载 Release 安装包后导入至 Obsidian。
1. 下载地址： https://github.com/moelody/link-to-server/releases
2. 把文件放入 Obsidian 插件文件夹下：`<vault>/.obsidian/plugins/link-info-server`
3. 重新加载 Obsidian 即可
> 注意，如果安装时出现安全模式的提示，我们需要禁用安全模式。

==TODO 查看这个插件源码，看有没办法直接取消掉或使用别的方式达到一样的效果==

# 3. 安装 [hexo-link-obsidian](https://github.com/moelody/hexo-link-obsidian)
和第一步一样，在 Hexo 项目根目录下直接安装即可：
```bash
npm install hexo-link-obsidian
```
安装完成后无需任何配置。