#!/usr/bin/env python3
# coding=utf-8

import requests
import re
import csv

url = "https://movie.douban.com/top250"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"
}
resp = requests.get(url, headers=headers)
page_content = resp.text

obj = re.compile(r'<li>.*?<span class="title">(?P<name>.*?)</span>'
                 r'.*?导演:\s(?P<author>.*?)&nbsp'
                 r'.*?主演:\s(?P<actor>.*?)<br>'
                 r'.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>'
                 r'.*?<span class="inq">(?P<quote>.*?)</span>', re.S)

result = obj.finditer(page_content)

#csv文件生成
file = open("data-doubanTOP.csv", mode="w")
csvwriter = csv.writer(file)

num = 1
for iter in result:
    #直接输出结果
    print("-------------------------------")
    print("No.", num)
    print(iter.group("name"), " ", iter.group("score").strip())
    print("导演：", iter.group("author").strip())
    print("主演：", iter.group("actor").strip())
    print("评语：", iter.group("quote"))
    print("-------------------------------")
    print()
    #输出结果至csv文件
    dic = iter.groupdict()
    dic['author'] = dic['author'].strip()
    dic['actor'] = dic['actor'].strip()
    csvwriter.writerow(dic.values())
    #No++
    num = num + 1

file.close()
resp.close()
