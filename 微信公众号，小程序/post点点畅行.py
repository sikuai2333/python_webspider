'''
Descripttion: 
version: 
Author: sikuai
Date: 2022-09-19 13:22:27
LastEditors: sikuai
LastEditTime: 2022-09-19 13:36:59
'''
import requests
import json

url = 'https://api.hzchaoxiang.cn/api-device/api/v1/Home/AppRecentlyOnlineStation'
headers={
    'Header':'application/x-www-form-urlencoded;charset=UTF-8',
    'Longitude':'116.80847981770833',
    'Latitude':'33.984828287760415',
    'deviceTypeParam':'1'
}
res = requests.post(url,headers)
# print(res.text)
data = json.loads(res.text, strict=False)
all_data = data['data']
# print(data)
for i in range(1,10):
    TotalWays = all_data[i]['TotalWays']
    OccupyWays = all_data[i]['OccupyWays']
    Name = all_data[i]['Name']
    if TotalWays-OccupyWays > 0:
        print(Name+"有"+str(TotalWays-OccupyWays)+"个空")