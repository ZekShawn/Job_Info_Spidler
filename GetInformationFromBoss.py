import time
import random
import pandas as pd

from copy import deepcopy

from selenium import webdriver

template_url = "https://www.zhipin.com/c{city}/?query={description}&page={page}&ka=page-{page}"  # Boss直聘
template_city = ['101020100']  # 上海
template_description = ['数据分析实习生', '大数据开发实习生']
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


def init_driver():
    chrome_options = webdriver.ChromeOptions()
    # 不加载图片
    # chrome_options.add_argument('blink-settings=imagesEnabled=false')
    # 不出现GUI界面
    # chrome_options.add_argument('--headless')
    chrome = webdriver.Chrome(
        options=chrome_options
    )
    chrome.implicitly_wait(3)
    return chrome


def get_url_list(base_url, base_city, base_description, pages=2):
    url_list = []
    for city in base_city:
        for description in base_description:
            for page in range(1, pages + 1):
                url = deepcopy(base_url)
                url = url.replace("{city}", city).replace("{description}", description).replace("{page}", str(page))
                url_list.append(url)
    return url_list


def trans_list(source_list):
    target_list = []
    for index in range(len(source_list[0])):
        job_name = source_list[0][index]
        area = source_list[1][index]
        company = source_list[2][index].split("\n")[0]
        company_desc = source_list[2][index].split("\n")[1]
        skills = source_list[3][index]
        salary = source_list[4][index]
        job_desc = source_list[5][index]
        target_list.append([job_name, area, company, company_desc, skills, salary, job_desc])
    return target_list


def get_class_text(driver, class_list=None, xpath_list=None, mode='x', num=30):
    # assert (class_list is None and xpath_list is None)
    text_list = []
    if mode == 'x':
        for class_name in class_list:
            texts = driver.find_elements_by_class_name(class_name)
            temp_list = [text.text for text in texts]
            text_list.append(temp_list)
    else:
        for xpath in xpath_list:
            temp_list = []
            for index in range(1, num + 1):
                temp_xpath = deepcopy(xpath).replace("li[1]", f"li[{index}]")
                temp_list.append(driver.find_element_by_xpath(temp_xpath))
            text_list.append(temp_list)
    return trans_list(text_list)


def get_to_save(url, cities, descriptions, classes=None):
    driver = init_driver()
    url_list = get_url_list(base_url=url, base_city=cities, base_description=descriptions)
    data = []
    for url in url_list:
        time.sleep(random.random() * random.randint(5, 7))
        try:
            driver.get(url)
        except ConnectionError:
            print("完蛋，IP被屏蔽了")
        finally:
            print(url)
        text = get_class_text(driver, class_list=classes)
        data = data + text
    driver.close()
    data = pd.DataFrame(data, columns=template_name)
    data.to_excel('./source/job_info.xlsx', index=False, encoding='utf_8_sig')


if __name__ == "__main__":
    get_to_save(template_url, template_city, template_description, template_class)
