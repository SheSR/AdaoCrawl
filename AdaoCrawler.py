# -*- coding:UTF-8 -*-
import re
import requests



url = "http://adnmb1.com/Forum"
#header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

html = requests.get(url)

src = html.content

pic_url = re.findall('<img src="(.*?)" title="开放包容 理性客观 有事说事 就事论事 顺猴者昌 逆猴者亡"/>',src)


def crawl(n):
    print "now downloading:" + str(n)
    pic = requests.get(pic_url[0])
    fp = open('images\\' +str(n) +'.jpg','wb')
    fp.write(pic.content)
    fp.close()
    print "download success"
    
print "how many pics?"
n = raw_input()

for n in range(1,int(n)+1):
    crawl(n)


