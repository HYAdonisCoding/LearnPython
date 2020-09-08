# /usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
import urllib.parse
import json
import re


# 爬取代理ip
def get_ip_address():
    url = 'http://31f.cn/'
    head = {}
    head[
        'User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
    response = urllib.request.urlopen(url)
    html_document = response.read().decode('utf-8')
    pattern_ip = re.compile(r'<td>(\d+\.\d+\.\d+\.\d+)</td>[\s\S]*?<td>(\d{2,4})</td>')
    ip_list = pattern_ip.findall(html_document)
    print(len(ip_list))
    for item in ip_list:
        print("ip地址是:%s 端口号是:%s" % (item[0], item[1]))


# 爬取代理ip 119.27.170.46 端口号是:8888
# get_ip_address()


def resemble_data(content, index):
    data = {}
    data['types'] = 'search'
    data['count'] = '30'
    data['source'] = 'netease'
    data['pages'] = index
    data['name'] = content
    data = urllib.parse.urlencode(data).encode('utf-8')
    return data


def request_music(url, content):
    # set proxy agent
    proxy_support = urllib.request.ProxyHandler({'http:': '119.27.170.46:8888'})
    opener = urllib.request.build_opener(proxy_support)
    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36')]
    urllib.request.install_opener(opener)
    # set proxy agent
    total = []
    pattern = re.compile(r'\(([\s\S]*)\)')
    for i in range(1, 10):
        data = resemble_data(content, str(i))
        response = urllib.request.urlopen(url, data)
        result = response.read().decode('unicode_escape')
        json_result = pattern.findall(result)
        total.append(json_result)
    return total


def save_music_file(id, name):
    save_path = '/Users/Adam/Developer/MyGithubCode/Music'
    pattern = re.compile('http.*?mp3')
    url = 'http://www.gequdaquan.net/gqss/api.php?callback=jQuery111307210973120745481_1533280033798'
    data = {}
    data['types'] = 'url'
    data['id'] = id
    data['source'] = 'netease'
    data = urllib.parse.urlencode(data).encode('utf-8')
    response = urllib.request.urlopen(url, data)
    music_url_str = response.read().decode('utf-8')
    music_url = pattern.findall(music_url_str)
    print('music_url', music_url)
    result = urllib.request.urlopen(music_url[0])
    file = open(save_path + name + '.mp3', 'wb')
    file.write(result.read())
    file.flush()
    file.close()


def main():
    url = 'http://www.gequdaquan.net/gqss/api.php?callback=jQuery11130967955054499249_1533275477385'
    content = input('please input the artist name:')
    result = request_music(url, content)
    for group in result[0]:
        target = json.loads(group)
        for item in target:
            print('item', item)
            save_music_file(str(item['id']), str(item['name']))


# main()

import requests
from multiprocessing import Pool

headers = {
    'Referer': 'http://music.163.com/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
}


def get_page(url):
    res = requests.get(url, headers=headers)
    data = re.findall('<a title="(.*?)" href="/playlist\?id=(\d+)" class="msk"></a>', res.text)

    pool = Pool(processes=4)
    pool.map(get_songs, data[:3])
    print('下载完毕')


def get_songs(data):
    playlist_url = "https://music.163.com/playlist?id=%s" % data[1]
    res = requests.get(playlist_url, headers=headers)
    for i in re.findall(r'<a href="/song\?id=(\d+)">(.*?)</a>', res.text):
        download_url = "http://music.163.com/song/media/outer/url?id=%s" % i[0]
        try:
            with open('music/' + i[1] + '.mp3', 'wb') as f:
                f.write(requests.get(download_url, headers=headers).content)
        except FileNotFoundError:
            pass
        except OSError:
            pass


if __name__ == '__main__':
    # hot_url = "https://music.163.com/discover/playlist/?order=hot"
    # hot_url = "https://music.163.com/discover/playlist/?cat=%E5%8D%8E%E8%AF%AD"
    hot_url = 'https://music.163.com/weapi/pl/count?csrf_token=597f8a3d25e829f078a4e9fca7ed825b'
        # "https://music.163.com/discover/toplist?id=3778678"
    get_page(hot_url)

