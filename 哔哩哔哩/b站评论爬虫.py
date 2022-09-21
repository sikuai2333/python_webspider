'''
Descripttion: 
version: 
Author: sikuai
Date: 2022-09-17 12:39:31
LastEditors: sikuai
LastEditTime: 2022-09-17 12:39:59
'''
import requests
import json
import os
import time

url = 'http://api.bilibili.com/x/v2/reply'
res_num = requests.get(url,headers = {'type':'1','oid':'54737593'})
# print(res.text)
data_num = json.loads(res_num.text, strict=False)
total = data_num['data']['page']['acount']
page = (total//49)+1
print(page)
for pn in range(1,page):
    print("循环页面"+str(pn))
    headers = {
        'type':"1",
        'oid':"54737593",
        'ps':"49",
        'sort':"1",
        'pn':str(pn)
    }
    time.sleep(3)
    res = requests.get(url,headers)
    # print(res.text)
    data = json.loads(res.text, strict=False)
    try:
        for i in range(0,49):
            message = data['data']['replies'][i]['content']['message']
            # print(message)
            # print(i)
            with open('评论.txt','a',encoding='utf-8') as f:
                f.write(message+'\n')
                f.close()
    except:
        continue