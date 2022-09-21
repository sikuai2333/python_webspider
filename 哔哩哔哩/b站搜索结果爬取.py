import requests

if __name__ == "__main__":
    url = "https://search.bilibili.com/all"
    kw = input("what do you want to search:")
    param = {
        "keyword":kw
    }
    headers = {
        "user agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36 Edg/92.0.902.78",
    }
    response = requests.get(url=url,params=param,headers=headers)
    page_text = response.text
    filename = kw+".html"
    with open(filename,"w",encoding="utf-8") as fp:
        fp.write(page_text)
    print(filename,"保存成功。")