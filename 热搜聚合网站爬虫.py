'''
Descripttion: 
version: 
Author: sikuai
Date: 2022-09-14 22:51:03
LastEditors: sikuai
LastEditTime: 2022-09-17 09:36:49
'''
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
search_url = 'https://tophub.today/c/ent'


#去除selenium自动提示
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])
#去除selenium检测
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--disable-blink-features=AutomationControlledByDomain')
options.add_argument('--disable-blink-features=AutomationControlledByUrl')
options.add_argument('--disable-blink-features=AutomationControlledByUrlBlockList')
#去除证书
options.add_argument('-ignore-certificate-errors')
options.add_argument('-ignore -ssl-errors')
driver = webdriver.Chrome(options=options)
prefs = {"profile.default_content_setting_values.notifications": 2}
options.add_experimental_option("prefs", prefs)
driver.get(search_url)
time.sleep(5)
for i1 in range(1,100):
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(1)
    # 其实可以/html/body/div[2]/p[1]/text()检测有没有到底
num = driver.find_element(By.XPATH,r'/html/body/div[1]/div[4]/div/div[1]/div[1]/small').text
num = num.replace("个","")
num = int(num)+1
for i in range(1,num):
    # xpath点击/html/body/section/div/div/div[2]/form/div[6]/a[3]
    title1 = driver.find_element(By.XPATH,r'/html/body/div[1]/div[4]/div/div[2]/div['+str(i)+']/div/div[1]/div[1]/a/div').text
    title2 = driver.find_element(By.XPATH,r'/html/body/div[1]/div[4]/div/div[2]/div['+str(i)+']/div/div[1]/div[2]/div/span').text
    with open('热榜.txt','a',encoding='utf-8') as f:
        f.write(title1+"-------"+title2+'\n')
        f.close()
    try:
        for i2 in range(1,100):
            msg = driver.find_element(By.XPATH,r'/html/body/div[1]/div[4]/div/div[2]/div['+str(i)+']/div/div[2]/div[1]/a['+str(i2)+']/div/span[2]').text
            with open('娱乐.txt','a',encoding='utf-8') as f:
                f.write(msg+'\n')
                f.close()
    except:
        pass
