**最后更新更新时间：2020-02-05 15:54**


**为保证大多数用户体验与减轻网站负担，请自觉调大 time sleep，减少并发**

**已经调节到了20-40s刷新一张图片，与人类正常阅读速度相似，请大家不要调快速度，避免对服务器造成过大的负担，也避免封掉自己的账号，请大家合理使用**

> (白天下载不正常是一个很正常的事情)，建议开发者看到后将图片扔到CDN上面



**如果下载出现异常，删除异常图片再重新执行相同的命令即可。已经下载的页面会自动跳过**

**已经根据原项目的patch1和2做了修改，首次使用请先登录网站并复制cookies中的PHPSESSID到cookies.txt中的{Here Input You Cookies}处。

# 文泉学堂 离线阅读转换器

文泉学堂解析工具自动生成pdf，**方便**用户通过离线的方式阅读文泉学堂**免费**的资源。切勿商用和广泛传播。-\_-

利用`python3`自动下载文泉学堂学堂提供的免费的pdf书籍（仅供测试，请24小时内删除）

## 🌙 有效性

| 时间             | 状态                                                         |
| ---------------- | ------------------------------------------------------------ |
| 2020-02-03 04:00 | 发布，下载丝滑流畅                                           |
| 2020-02-03 12:00 | 用户反馈，下载状态正常                                       |
| 2020-02-03 16:00 | 反馈下载超时，增加超时与自动重试，延长time sleep时间到2.5s   |
|                  | 通过正常页面阅读，发现加载速度慢                             |
| 2020-02-03 17:00 | 做个正常人，5秒看一个页面。挂着玩游戏吧……                    |
| 2020-02-03 17:27 | 下载过程中记得去img看一下有没有**没有加载**的图片，及时停掉等几分钟再重新启动。 |
|                  | 延长time sleep时间为5-10s（随机）                            |
| 2020-02-03 21:00 | 用的人太多了，卡死不动了。                                   |
| 2020-02-04 00:30 | 下载恢复，估计人都去睡觉了。                                 |
| 2020-02-04 00:50 | 下载异常，变成5k图片（估计是哪位老哥加班？）                 |
| 2020-02-04 01:08 | 修复下载异常，增加10k图片比对。没有增加5k图片比对（再次出现再说） |
| 2020-02-04 01:28 | 增加直接在命令行执行函数，直接运行`python main.py`即可       |
| 2020-02-04 02:39 | 被封IP、关了数据接口、单个ip访问上限等问题，被限制访问，访问全部定向到5k图片 |
| 2020-02-04 03:04 | 增加识别5k图片                                               |
| 2020-02-04 03:47 | 增加随机User-Agent，虽然没什么用                             |
| 2020-02-05 15:54 | 根据原项目的patch1&2进行了调整，支持新版需要登陆的情形|



## ❤免责声明

> 所发布的一切破解补丁、注册机和注册信息及软件的解密分析文章仅限用于学习和研究目的；不得将上述内容用于商业或者非法用途，否则，一切后果请用户自负。本站信息来自网络，版权争议与本站无关。您必须在下载后的24个小时之内，从您的电脑中彻底删除上述内容。如果您喜欢该程序，请支持正版软件，购买注册，得到更好的正版服务。如有侵权请邮件与我们联系处理。



## ✨ 安装

- 前期准备

	- 注册、登录 github
	- 点击右上角的 `⭐Star`
	- 想点`Fork`也可以，可以fork到自己的仓库以提交pr
	
- 下载与安装

  - 安装[GIT](https://gitforwindows.org/)
  - 安装python3   [x86-64  ](https://www.python.org/ftp/python/3.6.6/python-3.6.6-amd64.exe) [x86](https://www.python.org/ftp/python/3.6.6/python-3.6.6.exe) 
  - 使用`git clone https://github.com/kajweb/wqxuetang_downloader.git`克隆代码

- 下载依赖

  - 打开命令行，使用`pip install -r requirements`安装依赖

  - 运行`python main.py`

  - > 其中，book_id是阅读界面后面的5-8位数字

  
  
  由于网站（简称：对方）经常更新，在对方更新后我们这边也会及时更新。这时候你的电脑就需要执行更新代码操作。
  
  ```
  git pull
  ```
  
  
  
  

## 🔥 功能

下载免费的图书的图片，生成pdf书籍

- 普通下载

```
python main.py
```

- 下载整书

```ssh
python main.py <book_id>
```

- 指定页码下载
```ssh
python main.py <book_id> <start_page>  <end_page>
```

- 指定下载前N页
```ssh
python main.py <book_id> <end_page>
```



## ⌛️ 常见问题

- 不会安装依赖库

  > 直接使用pip install -r requirements安装即可

- no model named: fitz

  > 执行pip install pymupdf，安装[pymupdf](https://pymupdf.readthedocs.io/en/latest/)即可

- AttributeError: module 'jwt' has no attribute 'encode'

  > jwt库命名冲突，卸载jwt，重新安装[pyjwt](https://pyjwt.readthedocs.io/en/latest/).
  
- configparser.NoSectionError: No section: 'wqxt'

  > 路径问题，切程序目录下运行

- 其他问题

  > 大家注意更新，一般来说现阶段更新都是比较重要的更新，不更新可能会导致无法使用（git pull）

## ⚡ 声明

**邮箱不接受使用问题（妹子除外），使用存在问题请在[`Issues`](https://github.com/kajweb/wqxuetang_downloader/issues)中提出**

若本应用侵犯了您的权益，或造成不利影响，请联系 lyy@iwwee.com 并提供微信号码，在确认身份后我将立即下架本应用。

欢迎 Star 和 Fork ~

如果你有什么问题请提 Issue



## 📃 LICENSE

[MIT](https://opensource.org/licenses/mit-license.php)





## 其他渠道

> 其他渠道未尝试与验证，不保证可以正常使用

[gumblex/wqxt_pdf](https://github.com/gumblex/wqxt_pdf) (Python)

[文泉学堂pdf一键下载](https://greasyfork.org/zh-CN/scripts/396025-文泉学堂pdf下载) (油猴脚本)   [github](https://github.com/Kevin0z0/wenquan-pdf-download)

[[SweetInk](https://github.com/SweetInk)/wqxuetang-pdf-downloader](https://github.com/SweetInk/wqxuetang-pdf-downloader) (Java)

[sinceNa/wqxuetang ](https://github.com/sinceNa/wqxuetang)(NodeJS)