#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 此程序仅供学习交流使用。

import urllib.request
import json
import re
import urllib.parse
from urllib import parse

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

name = input("输入你想听的歌名or歌名+歌手:")
name = urllib.parse.quote(name)
url = "https://y.qq.com/portal/search.html#page=1&searchid=1&remoteplace=txt.yqq.top&t=song&w=" + name

headers = {
    'Referer': 'https://y.qq.com/portal/search.html',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
}


def network(url):
    request_url = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request_url).read().decode('utf-8')
    return response


def download(songmid, music_name):
    # json数据
    json_url = "https://c.y.qq.com/base/fcgi-bin/fcg_music_express_mobile3.fcg?g_tk=5381&jsonpCallback=MusicJsonCallback8796342823761736&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&cid=205361747&callback=MusicJsonCallback8796342823761736&uin=0&" \
               "songmid=" + songmid + "&filename=C400" + songmid + ".m4a&guid=4626869183"
    html = network(json_url)
    # 找到json中music的信息
    music_json = json.loads(re.findall(r'^\w+\((.*)\)$', html)[0])
    filename = music_json['data']['items'][0]['filename']
    vkey = music_json['data']['items'][0]['vkey']
    # 歌曲的下载链接
    download_url = "http://dl.stream.qqmusic.qq.com/" + filename + "?vkey=" + vkey + "&guid=4626869183&uin=0&fromtag=66"
    # 构造POST表格
    dict = {
        'format': 'jsonp',
        'g_tk_new_20200303': '5381',
        'jsonpCallback': 'MusicJsonCallback',
        'loginUin': '0',
        'hostUin': '0',
        'format': 'jsonp',
        'inCharset': 'utf8',
        'outCharset': 'utf-8',
        'notice': '0',
        'platform': 'yqq',
        'needNewCode': '0'
    }
    data = bytes(parse.urlencode(dict), encoding='utf8')
    ret_url = urllib.request.Request(download_url, data=data, headers=headers)
    print('download_url', download_url)
    music_url = urllib.request.urlopen(ret_url).read()
    with open("./" + music_name + ".m4a", "wb") as fb:
        fb.write(music_url)


def get():
    print('url', url)
    # 加载Chromedriver,百度chromedriver.exe，下载与自己chrome版本一致的。
    option = webdriver.ChromeOptions()
    option.add_argument('headless')  # 添加无头浏览
    driver = webdriver.Chrome(options=option)

    # driver = webdriver.Chrome()

    # 请自行修改加载的路径
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "js_song")))
    music = driver.find_element_by_class_name('js_song')
    href = music.get_attribute('href')
    music_name = music.get_attribute('title')
    # 匹配到歌曲的id
    songmid = re.findall(r'https://y.qq.com/n/yqq/song/(\S+).html', href)[0]
    download(songmid, music_name)


if __name__ == '__main__':
    get()