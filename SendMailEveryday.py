import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


def send_mail_main(receivers, mail_host, mail_user, mail_pass, sender):
    """
    receivers: 目标邮件地址
    """
    # 获取当前时间
    current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(int(round(time.time()*1000))/1000))
    print(f"{current_time}\t邮件正在发送中....")

    # 创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = Header("ZekShawn", 'utf-8')
    message['To'] =  Header("每日资讯通报", 'utf-8')
    subject = '邮件小管家为您带来今日实习资讯，请您查收！'
    message['Subject'] = Header(subject, 'utf-8')
    
    # 邮件正文内容
    with open("./source/info.html", 'r', encoding="utf-8") as f:
        subject = f.read()
    message.attach(MIMEText(subject, 'html', 'utf-8'))

    # 构造附件1，传送当前目录下的 info.csv 文件
    att1 = MIMEText(open('./source/info.csv', 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'

    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename="info.csv"'
    message.attach(att1)

    # 构造附件2，传送当前目录下的 info.md 文件
    att2 = MIMEText(open('./source/info.md', 'rb').read(), 'base64', 'utf-8')
    att2["Content-Type"] = 'application/octet-stream'
    att2["Content-Disposition"] = 'attachment; filename="info.md"'
    message.attach(att2)

    try:
        smtpObj = smtplib.SMTP() 
        smtpObj.connect(mail_host, 587)    # 25 为 SMTP 端口号
        smtpObj.login(mail_user,mail_pass)  
        smtpObj.sendmail(sender, receivers, message.as_string())
        current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(int(round(time.time()*1000))/1000))
        print(f"{current_time}\t邮件发送成功")
    except smtplib.SMTPException:
        print(f"{current_time}\t无法发送邮件")


if __name__ == '__main__':
    # send_mail_main(receivers, mail_host, mail_user, mail_pass, sender)
    pass
