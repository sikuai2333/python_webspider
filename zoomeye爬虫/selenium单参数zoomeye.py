'''
Descripttion: 
version: 
Author: sikuai
Date: 2022-07-05 12:07:29
LastEditors: sikuai
LastEditTime: 2022-09-16 19:33:11
Tips: 
作者连个python菜鸡都算不上, 所以代码写的很烂, 直接写的延迟而不是检测元素存在, 还请大佬们见谅
由于是用的selenium, 所以需要安装chrome浏览器, 以及对应的驱动
版本 104.0.5112.81, 如有不同, 还请自行下载对应版本的驱动, 或修改代码为edge或firefox
不会带cookie登录, 所以采用github登录, (如果有大佬会还请不吝赐教) 

'''
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

i = 2
page = 1
github_username = "sikuai2333"
github_password = "zymjhk0417"
print(
    '''
                                                            _     _           
 _______   ___  _ __ ___   ___ _   _  ___     ___ _ __ (_) __| | ___ _ __ 
|_  / _ \ / _ \| '_ ` _ \ / _ \ | | |/ _ \   / __| '_ \| |/ _` |/ _ \ '__|
 / / (_) | (_) | | | | | |  __/ |_| |  __/   \__ \ |_) | | (_| |  __/ |   
/___\___/ \___/|_| |_| |_|\___|\__, |\___|___|___/ .__/|_|\__,_|\___|_|   
                               |___/    |_____|  |_|                      
    '''
)
print("不会带cookie登录, 这里我用的是微信扫码登录(如果有大佬会还请不吝赐教) ")
search_info = input("请输入搜索关键字(关键词较多您可以修改代码search_url):")
search_url = 'https://www.zoomeye.org/searchResult?q='+search_info+'&page='+str(page)+'&pageSize=50'
save_name = input("请输入保存文件名:")

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
time.sleep(2)
# xpath点击/html/body/section/div/div/div[2]/form/div[6]/a[3]
# github_login = driver.find_element(By.XPATH,r'/html/body/section/div/div/div[2]/form/div[6]/a[3]')
# github_login.click()
# github_username_box = driver.find_element(By.XPATH,r'/html/body/div[3]/main/div/div[3]/form/input[2]')
# github_password_box = driver.find_element(By.XPATH,r'/html/body/div[3]/main/div/div[3]/form/div/input[1]')
# #输入账号密码
# github_username_box.send_keys(github_username)
# github_password_box.send_keys(github_password)
# #点击登录/html/body/div[3]/main/div/div[3]/form/div/input[12]
# github_login_button = driver.find_element(By.XPATH,r'/html/body/div[3]/main/div/div[3]/form/div/input[12]')
# github_login_button.click()
time.sleep(15)

while page <= 8:
    # 打印当前页数
    print('第'+str(page)+'页')
    # 随机休息时间,访问过多或过快会有检测,页面响应不正常,修改url可以解决,暂时没有修改
    time.sleep(random.randint(3,10))
    for i in range(2,51):
        try:
            # 此处是记录ip和端口,可以修改xpath,获取其他信息
            ip_result = driver.find_element(By.XPATH,r'/html/body/div/div/div/div[2]/div[3]/div[1]/div/div['+str(i)+']/div/div[1]/h3').text
            port_result = driver.find_element(By.XPATH,r'/html/body/div/div/div/div[2]/div[3]/div[1]/div/div['+str(i)+']/div/div[1]/div/a/button').text
            all_result = ip_result + ':' + port_result
            print(all_result)
            # 写入文件
            with open(save_name+'.txt','a') as f:
                # 此处是因为其他扫描器需要http://, 所以加上,自行修改
                f.write('http://'+all_result+'\n')
                f.close()
        except:
            time.sleep(1)
    # 页面循环的我有点懵，整个也是靠试出来的，不知道有没有更好的方法
    page = page + 1
    driver.get('https://www.zoomeye.org/searchResult?q='+search_info+'&page='+str(page)+'&pageSize=50')
    time.sleep(3)
    #等待页面加载完成
    # driver.implicitly_wait(10)

print('扫描完成')
# driver.quit()
