'''
Descripttion: 
version: 
Author: sikuai
Date: 2022-05-27 16:10:10
LastEditors: sikuai
LastEditTime: 2022-09-17 07:25:09
'''
from time import sleep
import requests
import json
from urllib import parse
import os


def address_1(address2):
    for address in address2:
        search(address,page,search_info,headers,save_name)
def search(address,page,search_info,headers,save_name):
    while page < 8:
        page = page + 1
        print(address)
        sleep(3)
        address = parse.quote(address)
        search_url = 'https://www.zoomeye.org/search?q='+search_info+'%20%2Bcountry:%22CN%22%20%2Bsubdivisions:'+address+'&t=v4&page='+str(page)+'&pageSize=50'
        print(search_url)
        r = requests.get(url=search_url,headers=headers)
        # print(r.text)
        datas = json.loads(r.text, strict=False)
        # print(datas)
        matches = datas['matches']
        for line in matches:
            ip = line['ip']
            port = line['portinfo']['port']
            # timestamp = line['timestamp']
            address = parse.unquote(address)
            result = "http://"+str(ip)+":"+str(port)
            with open(save_name+'.txt','a',encoding='utf-8') as f:
                f.write(str(result)+'\n')
                f.close()
        if page > 8:
            address_1(address2)
        else:
            continue
if __name__=="__main__":
    search_info = input("请输入q后的参数（脚本仅遍历国内地区和页数）：")
    save_name = input("请输入保存的文件名")
    print("初次使用请编辑脚本的headers，脚本很垃圾，大佬请自己写")
    headers={ 
    'Host': 'www.zoomeye.org',
    'Cookie': '__jsluid_s=343db6f08f60805b133c45bcb9ed1d3c; SECKEY_ABVK=HtAse9A+SyAimJHwbtx+BoGhfj2rrZm03azO3VnoFEo%3D; BMAP_SECKEY=AiKhuFWmNAKpuT3ptlM39HDIEh_FP1crQEpa9c-ht194pBmFpi4raRGlxehUr6CQYQqOpXMfyXoLjviuj2On7I-WnNyaHPRtFSbOSqATwNkotHQ6QB7koUssrOxpLFORUrrJ8Qce66Q2ilsdymWVZReyt0RwFwqrbZKuI3efzifY3yNc8p48Qh9btGDpeIQ3',
    'Sec-Ch-Ua': '" Not A;Brand";v="99", "Chromium";v="104"',
    'Accept': 'application/json, text/plain, */*',
    'Cube-Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Im9tVkRTd3AyVlU5QXRyOWRQaldFMnJSdnBnSFkiLCJlbWFpbCI6IjI2NDM5Mjc3MjVAcXEuY29tIiwiZXhwIjoxNjYzNDE0MTYyLjB9.CLSAKHRgBL4AkswAqf8De1hKsFt7jfZcwIOfEdBIbGE',
    'Sec-Ch-Ua-Mobile': '?0',
    'Referer': 'https://www.zoomeye.org/searchResult?q=app%3A%22Tongda%20OA%22%20%2Bafter:%222022-01-01%22%20%2Bbefore:%222023-01-01%22&t=all%20%2Bcountry:%22CN%22%20%2Bsubdivisions:%E4%B8%8A%E6%B5%B7&t=v4&page=3&pageSize=50',
    'BMAP_SECKEY':'AiKhuFWmNAKpuT3ptlM39HDIEh_FP1crQEpa9c-ht194pBmFpi4raRGlxehUr6CQYQqOpXMfyXoLjviuj2On7I-WnNyaHPRtFSbOSqATwNkotHQ6QB7koUssrOxpLFORUrrJ8Qce66Q2ilsdymWVZReyt0RwFwqrbZKuI3efzifY3yNc8p48Qh9btGDpeIQ3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',

    }
    # search_info = 'app%3A"Hikvision%20IP%20camera%20httpd"%20%2Bcountry:"CN"'
    address2 ={'北京','天津','上海','重庆','河北','山西','辽宁','吉林','江苏','浙江','安徽','福建','江西','山东','河南','湖北','湖南','广东','海南','黑龙江','四川','贵州','云南','陕西','甘肃','青海','台湾','内蒙','广西','西藏','宁夏','新疆','香港','澳门'}
    page = 0
    address_1(address2)
    print("爬取结束")