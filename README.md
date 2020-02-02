# 文泉学堂 下载器 v0.1

文泉学堂解析工具，自动生成pdf，切勿商用和广泛传播。-\_-

利用python3自动下载温泉学堂的pdf书籍（仅供测试，请24小时内删除）



## ❤免责声明

> 所发布的一切破解补丁、注册机和注册信息及软件的解密分析文章仅限用于学习和研究目的；不得将上述内容用于商业或者非法用途，否则，一切后果请用户自负。本站信息来自网络，版权争议与本站无关。您必须在下载后的24个小时之内，从您的电脑中彻底删除上述内容。如果您喜欢该程序，请支持正版软件，购买注册，得到更好的正版服务。如有侵权请邮件与我们联系处理。



## ✨ 安装

- 安装python3

- 打开命令行，使用`pip install -r requirements`安装依赖

- 按照功能运行`python main.py <book_id>`即可完成下载

- 其中，book_id是阅读界面后面的5-8位数字

  

## 🔥 功能

下载图片，生成pdf书籍

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



## ⌛️ 开发规划

无，随时关闭



## ⚡ 声明

若本应用侵犯了您的权益，或造成不利影响，请联系 lyy@iwwee.com 并提供微信号码，在确认身份后我将立即下架本应用。

欢迎 Star 和 Fork ~

如果你有什么问题请提 Issue



## 📃 LICENSE

[MIT](https://opensource.org/licenses/mit-license.php)



## 更新历史

### v0.1
- 每个页面增加1.2s间隔，防止阅读频率过快被拉黑。



## TODO

- 下载频率过高，部分页面出现空白页面检测。
- 检测下载失败的图片