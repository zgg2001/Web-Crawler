#!/usr/bin/env python3
# encoding: utf-8

import requests
import re

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"
}
url = "https://www.zhihu.com/billboard"
resp = requests.get(url, headers=headers)
page_content = resp.text

#print(page_content)

obj = re.compile(r'"target":{"titleArea":{"text":"(?P<name>.*?)"},"excerptArea":{"text":"(?P<text>.*?)"},"imageArea'
                 r'.*?metricsArea":{"text":"(?P<hot>.*?)"},"labelArea"'
                 r'.*?link":{"url":"(?P<link>.*?)"}', re.S)

result = obj.finditer(page_content)

num = 1
for iter in result:
    #直接输出结果
    print("-------------------------------")
    print("No.", num)
    print("问题:", iter.group("name"))
    print("详情:", iter.group("text"))
    print("热度:", iter.group("hot"))
    str = iter.group("link")
    str = str.replace(r'\u002F', '/')
    print("链接:", str)
    print("-------------------------------")
    print()
    #No++
    num = num + 1

resp.close()
