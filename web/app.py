#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Author: Adam
@Date: 2020-04-17 14:50:20
@LastEditTime: 2020-04-17 15:07:16
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /LearnPython/web/app.py
'''
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin', methods=['POST'])
def sigin():
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'

if __name__ == '__main__':
    app.run()