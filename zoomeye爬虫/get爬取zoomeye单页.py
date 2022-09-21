'''
Descripttion: 
version: 
Author: sikuai
Date: 2022-05-27 16:10:10
LastEditors: sikuai
LastEditTime: 2022-08-30 19:51:41
'''
from urllib import response
import urllib3
import requests
import json
import os
url='https://www.zoomeye.org/searchResult?q=camera%20+country:%22CN%22%20+subdivisions:%22%E5%AE%89%E5%BE%BD%22%20+city:%22%E6%B7%AE%E5%8C%97%22%20+after:%222020-01-01%22%20+before:%222020-12-31%22%20%2Btitle:%22index%22&t=all'
# url = 'https://www.baidu.com'

# Cube-Authorization,Content-Type,Content-Disposition,Authorization

headers={ 
'Host': 'www.zoomeye.org',
'Cookie': '__jsluid_s=343db6f08f60805b133c45bcb9ed1d3c; SECKEY_ABVK=HtAse9A+SyAimJHwbtx+BoGhfj2rrZm03azO3VnoFEo%3D; BMAP_SECKEY=AiKhuFWmNAKpuT3ptlM39HDIEh_FP1crQEpa9c-ht194pBmFpi4raRGlxehUr6CQYQqOpXMfyXoLjviuj2On7I-WnNyaHPRtFSbOSqATwNkotHQ6QB7koUssrOxpLFORUrrJ8Qce66Q2ilsdymWVZReyt0RwFwqrbZKuI3efzifY3yNc8p48Qh9btGDpeIQ3',
'Sec-Ch-Ua': '" Not A;Brand";v="99", "Chromium";v="104"',
'Accept': 'application/json, text/plain, */*',
'Cube-Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Im9tVkRTd3AyVlU5QXRyOWRQaldFMnJSdnBnSFkiLCJlbWFpbCI6IjI2NDM5Mjc3MjVAcXEuY29tIiwiZXhwIjoxNjYzNDE0MTYyLjB9.CLSAKHRgBL4AkswAqf8De1hKsFt7jfZcwIOfEdBIbGE',
'Sec-Ch-Ua-Mobile': '?0',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36',
'Sec-Ch-Ua-Platform': '"Windows"',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Dest': 'empty',

}


r = requests.get(url=url,headers=headers)
print(r.json)
datas = json.loads(r.text, strict=False)
matches = datas['matches']
for line in matches:
    ip = line['ip']
    port = line['portinfo']['port']
    # timestamp = line['timestamp']
    result = str(ip)+":"+str(port)
    with open('test.txt','a',encoding='utf-8') as f:
        # 此处是因为其他扫描器需要http://, 所以加上,自行修改
        f.write(str(result)+'\n')
        f.close()