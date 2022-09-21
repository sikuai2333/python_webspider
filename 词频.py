import pandas as pd
import string
# from nltk.corpus import stopwords

f = open('54737593.txt',encoding="utf-8")
text = f.read()
f.close()

stop_words = ["的","是","了","1","2","4","of","3","6","to","s","com","https","app","The","热词系列","doge"] # 去掉不需要显示的词

ls = list(string.punctuation)            #要去除的英文标点符号
text = text.lower()   #统一为小写格式

for i in ls:          #将标点符号替换为空格
    text = text.replace(i," ")
lis = text.split()

ds = pd.Series(lis).value_counts()

for i in stop_words:
    try:    #处理找不到元素i时pop()方法可能出现的错误
        ds.pop(i)  
    except:
        continue #没有i这个词，跳过本次，继续下一个词
print(ds[:20])
