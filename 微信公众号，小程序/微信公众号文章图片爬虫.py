'''
Descripttion: 
version: 
Author: sikuai
Date: 2022-09-11 16:19:27
LastEditors: sikuai
LastEditTime: 2022-09-12 10:14:16
'''
from time import sleep
import time
from lxml import etree
import requests
import os
import urllib

# url = 'https://mp.weixin.qq.com/s/MkYfT8kRy0haK7grBoPxGQ'
url = input("请输入公众号链接：")
res = requests.get(url=url)
res.encoding = "utf-8"
html = etree.HTML(res.text)


# print(html)
for j in range(1,2000):
    # /html/body/div[1]/div[2]/div[1]/div/div[1]/div[3]/p[4]/img
    # /html/body/div[1]/div[2]/div[1]/div/div[1]/div[3]/p[3]/span[2]
    # 这里其实文字的数字比图片大一，懒得改了，凑合用
    img = html.xpath("/html/body/div[1]/div[2]/div[1]/div/div[1]/div[3]/p["+str(j)+"]/img/@data-src")
    # @data-src是图片的链接的“标签”，右键检查可以看见
    text = html.xpath("/html/body/div[1]/div[2]/div[1]/div/div[1]/div[3]/p["+str(j)+"]/span[2]/text()")
    # /text()是为了获取爬取的文字内容
    # try:        
    if str(text) != "[]":
        print(text)
    if str(img) != "[]":
        # print(img)
        img = str(img)
        img = img.replace("']","")
        img = img.replace("['","")
        # 该死，这里卡了我好几分钟才排查出来['']
        headers = {
            "user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/105.0.0.0",
            "referer": url
        }
        # 下载图片
        r = requests.get(url = img, headers=headers,stream=True)
        print(r.status_code) # 返回状态码
        if r.status_code == 200:
            open('./img/img_{}.jpeg'.format(j), 'wb').write(r.content) # 将内容写入图片
            print("done")
        del r
    # except:
    #     pass

    
