#!/usr/bin/python

from GetInformationFromBoss import get_to_save
from WriteMD import markdown_write_main
from MDtoHTML import transfer
from SendMailEveryday import send_mail_main

# 秘钥关键词
receivers = ['']   # 目标地址
mail_host = ""           # 服务器
mail_user = ""     # 用户名
mail_pass = ""      # 口令
sender = ''        # 邮件地址

# 抓取信息关键词
template_url = "https://www.zhipin.com/c{city}/?query={description}&page={page}&ka=page-{page}"  # Boss直聘
template_city = ['', '']  # 上海 南京
template_description = ['', '']
template_xpath = [
    '//*[@id="main"]/div/div[2]/ul/li[1]/div/div[1]/div[1]/div/div[1]/span[1]/a',
    '//*[@id="main"]/div/div[2]/ul/li[1]/div/div[1]/div[1]/div/div[1]/span[2]/span',
    '//*[@id="main"]/div/div[2]/ul/li[1]/div/div[1]/div[2]/div/h3/a',
    '//*[@id="main"]/div/div[2]/ul/li[1]/div/div[2]/div[1]',
    '//*[@id="main"]/div/div[2]/ul/li[1]/div/div[1]/div[1]/div/div[2]/span',
    '//*[@id="main"]/div/div[2]/ul/li[1]/div/div[2]/div[2]'
]
template_class = [
    "job-name",
    "job-area",
    "company-text",
    "tags",
    "red",
    "info-desc"
]
template_name = [
    'job_name',
    'area',
    'company',
    'company_desc',
    'skills',
    'salary',
    'job_desc'
]


if __name__ == "__main__":
    get_to_save(template_url, template_city, template_description, template_class)
    markdown_write_main()
    transfer()
    send_mail_main(receivers, mail_host, mail_user, mail_pass, sender)
