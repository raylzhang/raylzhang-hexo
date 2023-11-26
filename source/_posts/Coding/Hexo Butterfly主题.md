---
title: Hexo Butterfly主题
tags:
  - 建站/Hexo
categories:
  - Coding
abbrlink: 794d9e68
date: 2023-07-05 18:12:24
---

[GitHub地址](https://github.com/jerryc127/hexo-theme-butterfly)
# 安装

1. 进入项目根目录运行
	```shell
	git clone -b master https://github.com/jerryc127/hexo-theme-butterfly.git themes/butterfly
	```
2. 应用主题
	修改 Hexo 根目录下的 `_config.yml`，把主题改为 `butterfly`
	```yaml
	theme: butterfly
	```
3. 主题配置文件
	在 hexo 的根目录创建一个文件 `_config.butterfly.yml`，并把主题目录的 `_config.yml` 内容复制到 `_config.butterfly.yml` 去。（注意: 复制的是主题的 `_config.yml` ，而不是 hexo 的 `_config.yml`）
	以后只需要在 `_config.butterfly.yml` 进行配置就行。如果使用了 `_config.butterfly.yml`，配置主题的 `_config.yml` 将不会有效果。
> 注意：不要把主题目录的 `_config.yml` 删掉
> Hexo 会自动合併主题中的 `_config.yml` 和 `_config.butterfly.yml` 里的配置，如果存在同名配置，会使用 `_config.butterfly.yml` 的配置，其优先度较高。

# 备案
首先 [[备案#获取 ICP 备案号]]
## 方法 1（推荐）
编辑 `_config.butterfly.yml`，在 `custom_text:` 后面添加：
```html
<img src="https://static.raylzhang.com/img/gongan.png"><a href="https://beian.miit.gov.cn/" target="_blank">鄂ICP备2023003760号-1</a>
```
> 公安备案图片已经上传至自己的图片服务中。

## 方法 2
在 `themes/butterfly/layout/includes/footer.pug` 文件中添加：
```html
  if theme.footer.copyright
    .framework-info
      span= _p('footer.framework') + ' '
      a(href='https://hexo.io')= 'Hexo'
      span.footer-separator |
      span= _p('footer.theme') + ' '
      a(href='https://github.com/jerryc127/hexo-theme-butterfly')= 'Butterfly'

	<br/>
	<img src="https://static.raylzhang.com/img/gongan.png">
	<a href="https://beian.miit.gov.cn/" target="_blank">鄂ICP备2023003760号-1</a>

  if theme.footer.custom_text
    .footer_custom_text!=`${theme.footer.custom_text}`
```