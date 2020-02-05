**最后更新更新时间：2020-02-05 22:43**



![](notice.jpeg)





> 先说明，该阅读系统结构简单，任何有编程基础的人都可以独立完成爬取任务。我不认为网站遭受恶意爬虫是指我们程序。
>
> - 本脚本模拟了人的正常阅读，在用户不修改程序时，默认6-20秒（随机）阅读一个页面。
>
> - 该阅读速度远远小于受过[量子波动速读](https://baike.baidu.com/item/量子波动速读/4641373?fr=aladdin)训练的人的一分钟10w字。所以采取了较快于普通人而远慢于受过量子波动速度的人的速度，即6-20秒。
>
> - 该速度平均速度为13秒/页，一分钟4.6页，一小时4.6页 277页。阅读完一本书约需要1-2个小时。所以我认为[@miaoshengyou](https://github.com/miaoshengyou)的观点不成立。
>
> 最后提醒一句：**网络不是法外之地,网络言行需谨慎。**



[[issues/#27]](https://github.com/kajweb/wqxuetang_downloader/issues/27)

```
清华的资源不能为全体国人所共享，
平时只能为一小部分人所享，
其实是国家教育资源不平等的体现，是一个很扯很丢脸的事。

人类之所以技术发展到现在，
就是因为知识传播与技术共享，
让越来越多的人掌握科技，
人类的整体水平才不断发展。
```





# 文泉学堂 离线阅读转换器（停止更新）

文泉学堂解析工具自动生成pdf，**方便**用户通过离线的方式阅读文泉学堂**免费**的资源。



利用`python3`自动下载文泉学堂学堂提供的免费的pdf书籍（仅供测试，请24小时内删除）



最后有效更新`commit ad0c71480c4eeaf338d09492237ed70e3d28d0be`



这个脚本的本质上就是将线上阅读转化为线下阅读。



切勿商用和广泛传播。



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
| 2020-02-04 17:45 | 网站受资源限制，需要登录使用。脚本停止更新。最后有效更新`commit ad0c71480c4eeaf338d09492237ed70e3d28d0be` |
| 2020-02-04 20:00 | 网站重新开放                                                 |
| 2020-02-04 20:35 | 制定并发布patch1，修复登录问题                               |
|                  | 制定并发布patch2，修复503问题                                |
| 2020-02-05 20:00 | 新增两个[悦读](http://yd.51zhy.cn)下载程序                   |
| 2020-02-05 22:21 | 制定并发布patch3，设置错误登录状态(`PHPSESSIONS`)的提示。    |
|                  | 增加`main_mult.py`提供多个文件下载，格式为：                 |
|                  | `python main_mult.py [<bid1>] [<bid2>] [<bid3>] [...]`       |



## ❤免责声明

> 所发布的一切破解补丁、注册机和注册信息及软件的解密分析文章仅限用于学习和研究目的；不得将上述内容用于商业或者非法用途，否则，一切后果请用户自负。本站信息来自网络，版权争议与本站无关。您必须在下载后的24个小时之内，从您的电脑中彻底删除上述内容。如果您喜欢该程序，请支持正版软件，购买注册，得到更好的正版服务。如有侵权请邮件与我们联系处理。



## ⚡ 声明

**邮箱不接受使用问题，使用存在问题请在[`Issues`](https://github.com/kajweb/wqxuetang_downloader/issues)中提出**

若本应用侵犯了您的权益，或造成不利影响，请联系 lyy@iwwee.com 并提供微信号码，在确认身份后我将立即下架本应用。

欢迎 Star 和 Fork ~

如果你有什么问题请提 Issue



## 📃 LICENSE

[MIT](https://opensource.org/licenses/mit-license.php)



## 爬虫学习

- [那些你不知道的爬虫反爬虫套路](https://blog.csdn.net/kajweb/article/details/72849852)(吹水文章)

- [Python：爬虫常用模块：requests（get、post、代理、伪装headers和session）、json、selenium](https://blog.csdn.net/weixin_43473435/article/details/84637382)

- [详解爬虫模拟登陆的三种方法](https://blog.csdn.net/zhusongziye/article/details/91353222)

- [爬虫的解析](https://blog.csdn.net/qq_36958104/article/details/81478551)

> 以上内容都是随便找的

## 其他渠道

> 其他渠道未尝试与验证，不保证可以正常使用

[gumblex/wqxt_pdf](https://github.com/gumblex/wqxt_pdf) (Python)

[文泉学堂pdf一键下载](https://greasyfork.org/zh-CN/scripts/396025-文泉学堂pdf下载) (油猴脚本)   [github](https://github.com/Kevin0z0/wenquan-pdf-download)

[SweetInk/wqxuetang-pdf-downloader](https://github.com/SweetInk/wqxuetang-pdf-downloader) (Java)

[sinceNa/wqxuetang ](https://github.com/sinceNa/wqxuetang)(NodeJS)

[kdxcxs/wqDownloader](https://github.com/kdxcxs/wqDownloader)(PY代理)

[e0r/wqxuetang_anjian](https://github.com/e0r/wqxuetang_anjian)(按键精灵)



[防控疫情宅在家 免费资源随便刷](http://www.ynart.edu.cn/info/1002/2807.htm)(云南艺术学院)