## 工作信息爬虫
这是一个爬取boss直聘网站上工作信息的Python脚本。

## 秘钥填写
它的使用方法很简单，只需要将下面的秘钥填写清楚，以及在当前目录下新建一个source文件夹即可。

```python
receivers = ['xxxxx@xxxxxxx.com']   # target e-mail
mail_host = "smtp.xx.com"           # server address
mail_user = "xxxxxxxxxx@xx.com"     # sender's e-mail
mail_pass = "mxxxxxxxxxxxxxxx"      # secret key
sender = 'xxxxxxxxxx@xx.com'        # sender
```

城市代码的获取就是自己去boss直聘网站切换城市，网址中c后面的那一串数字就是城市代码。

```python
template_city = ['101020100', '101190100']  # city_code
template_description = ['BI', 'spidler engineer'] # job descriptions
```

## 运行
剩下的就只需要运行run.py这个文件就可以了，当然，前提是你将所有的依赖都安装好了。
