#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Author: Adam
@Date: 2020-04-17 14:07:14
@LastEditTime: 2020-04-17 14:19:53
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /LearnPython/web/hello.py
'''
def application(environ, start_response):
    start_response('200 OK',[('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>'%(environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]