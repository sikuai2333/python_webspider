'''
Descripttion: 
version: 
Author: sikuai
Date: 2022-09-15 12:56:53
LastEditors: sikuai
LastEditTime: 2022-09-21 17:33:33
'''
import jieba
import wordcloud
# 读取文本
with open("微博评论.txt",encoding="utf-8") as f:
    s = f.read()
print(s)
ls = jieba.lcut(s) # 生成分词列表
text = ' '.join(ls) # 连接成字符串

# stopwords = set()
stopwords = ["的","是","了","视频","同学","for","of","微笑","I","to","app","The","热词系列","doge","1","2","4","of","3","6","to","s","com","https","app","The","热词系列","doge"] # 去掉不需要显示的词

wc = wordcloud.WordCloud(font_path="msyh.ttc",
                         width = 1920,
                         height = 1080,
                         background_color='white',
                         max_words=40,stopwords=s)
# msyh.ttc电脑本地字体，写可以写成绝对路径
wc.generate(text) # 加载词云文本
wc.to_file("微博评论.png") # 保存词云文件