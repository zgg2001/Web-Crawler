#!/usr/bin/env python3
# coding=utf-8

import requests

#获取json
url = "https://bangumi.bilibili.com/web_api/timeline_global?"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)    Chrome/95.0.4638.54 Safari/537.36"
}
resp = requests.get(url, headers=headers)
resp.encoding = 'utf-8'
dic = resp.json()

#提取输出关键字
for comic in dic['result']:
    if comic['is_today'] == 1:
        print()
        print("今日番剧更新 -", comic['date'])
        print()
        for fan in comic['seasons']:
            name = fan['title']
            episode = fan['pub_index']
            time = fan['pub_time']
            image = fan['square_cover']
            link = fan['url']
            print(image)
            print("番名:", name)
            print("更新话:", episode)
            print("更新时间:", time)
            print("链接:", link)
            print()


resp.close()

