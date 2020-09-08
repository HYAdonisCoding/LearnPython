#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# import os
# from os import path
# def file_walker(path):
#     file_list = []
#     for root, dirs, files in os.walk(path): # 生成器
#         for fn in files:
#             p = str(root+'/'+fn)
#             file_list.append(p)

#     print(file_list)
#     return file_list

# def combine(ts_path, combine_path, file_name):
#     file_list = file_walker(ts_path)
#     file_path = combine_path + file_name + '.ts'
#     with open(file_path, 'wb+') as fw:
#         for i in range(len(file_list)):

#             fw.write(open(file_list[i], 'rb').read())

import datetime
import requests
# m3u8是本地的文件路径
def get_ts_urls(m3u8_path,base_url):  
    urls = []
    with open(m3u8_path,"r") as file:
        lines = file.readlines()
        
        for line in lines:
            print('line', line)
            print('strip', line.strip("\n"))
            if line.endswith(".ts\n"):
                urls.append(base_url+line.strip("\n"))

    return urls

if __name__ == '__main__':
    urls = get_ts_urls('../Videos/voddrm.token.Mjg1ZjhmYTRhNDU1YmI2Y2VPU011WC9DNk5aa1JIakpPdnpKMDM0T2k0WGE2RTcyYU1XN1lmcktESnoxUi9pSw.v.f230.m3u8','https://1252524126.vod2.myqcloud.com/9764a7a5vodtransgzp1252524126/b759cfc05285890804762869866/drm/voddrm.token.Mjg1ZjhmYTRhNDU1YmI2Y2VPU011WC9DNk5aa1JIakpPdnpKMDM0T2k0WGE2RTcyYU1XN1lmcktESnoxUi9pSw.v.f230.m3u8?time=1598171724621')
    print('urls', urls)
    # download(urls,'../Videos')
    # combine('../Videos', '../Videos/*.ts', '这是什么 第一集月亮.mp4')