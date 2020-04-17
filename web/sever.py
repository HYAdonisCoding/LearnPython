#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Author: Adam
@Date: 2020-04-17 14:11:58
@LastEditTime: 2020-04-17 14:15:01
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /LearnPython/web/sever.py
'''
from wsgiref.simple_server import make_server
from hello import application

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求
httpd.serve_forever()