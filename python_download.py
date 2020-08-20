#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests                                                                                                             
print 'start'
 
url = 'https://1252524126.vod2.myqcloud.com/9764a7a5vodtransgzp1252524126/b759cfc05285890804762869866/drm/v.f230.ts?start=5666928&end=6902287&type=mpegts'
r = requests.get(url, stream=True)
 
with open('这是什么 第一集月亮.mp4', "wb") as mp4:
    for chunk in r.iter_content(chunk_size=1024*1024):
        if chunk:
            mp4.write(chunk)
            
print "dowload over"

