#!/usr/bin/env python3
# coding=utf-8

import requests
import re

#获取html
url = "https://bangumi.bilibili.com/web_api/timeline_global?"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)    Chrome/95.0.4638.54 Safari/537.36"
}
resp = requests.get(url, headers=headers)
resp.encoding = 'utf-8'
result = resp.text

#初筛
first = re.compile(r'{"date":"(?P<time>.*?)",'
                   r'.*?"day_of_week":(?P<week>\d),'
                   r'"is_today":(?P<state>\d),'
                   r'"(?P<content>.*?})]}', re.S)

#筛选表里的番剧
obj = re.compile(r'{"cover":".*?"pub_index":"(?P<episode>.*?)","pub_time":"(?P<time>.*?)",'
                 r'.*?"square_cover":"(?P<image>.*?)"'
                 r'.*?"title":"(?P<name>.*?)","url":"(?P<link>.*?)"}', re.S)

#初筛
content = first.finditer(result)

#循环取内容
for iter in content:
    print(iter.group("time"))
    #取番剧
    comics = obj.finditer(iter.group("content"))
    for comic in comics:
        print(comic.group("name"), comic.group("time"), comic.group("episode"))
        #print(comic.group("image"), comic.group("link"))
        #print()
    print()


resp.close()

