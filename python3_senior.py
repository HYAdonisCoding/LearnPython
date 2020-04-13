#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
@Author: Adam
@Date: 2020-04-13 16:48:59
@LastEditTime: 2020-04-13 21:03:15
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /LearnPython/python3_senior.py
'''
# 高级特征
# ---------------------------------------- start ----------------------------------------
'''
print('-----------高级特征-----------')
# 比如构造一个1, 3, 5, 7, ..., 99的列表，可以通过循环实现：
L = []
n = 1
while n <= 99:
    L.append(n)
    n = n + 2
print(L)
'''

# 切片
print('-----------切片-----------')
L= ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# 取前3个元素，应该怎么做？
# 笨办法
print([L[0], L[1], L[2]])
# 之所以是笨办法是因为扩展一下，取前N个元素就没辙了。
# 取前N个元素，也就是索引为0-(N-1)的元素，可以用循环：
r = []
n = 4
for i in range(n):
    r.append(L[i])
print(r)
# 对这种经常取指定索引范围的操作，用循环十分繁琐，因此，Python提供了切片（Slice）操作符，能大大简化这种操作。
# 对应上面的问题，取前3个元素，用一行代码就可以完成切片
print(L[0:3])
# L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。
# 如果第一个索引是0，还可以省略：
print(L[:3])
print(L[1:3])
print(L[-2:])
# 记住倒数第一个元素的索引是-1。
# 切片操作十分有用。我们先创建一个0-99的数列：
L = list(range(100))
print(L)
print(L[:10])
print(L[-10:])
print(L[10:20])
# 前10个数，每两个取一个：
print(L[:10:2])
# 所有数，每5个取一个：
print(L[::5])
L1 = L[:]
print(L1)
# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
print((0, 1, 2, 3, 4, 5)[:3])
# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：
S = 'ABCDEFG'
print(S[:3])
print(S[::2])
# 在很多编程语言中，针对字符串提供了很多各种截取函数（例如，substring），其实目的就是对字符串切片。Python没有针对字符串的截取函数，只需要切片一个操作就可以完成，非常简单。

# 练习
# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
def trim(s):
    # 去除首空格
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s

# 法2
def trim(s):
    for i in range(len(s)):
        if s[:1] == ' ':
            # 这个处理比较巧妙，不是每次用s[0]
            s = s[1:]
        if s[-1:] == ' ':
            # 这个处理比较巧妙，不是每次用s[-1]     
            s = s[:-1]
    return s


# 递归实现
# def trim(s):
#     if s[:1] == ' ':
#         return trim(s[1:])
#     elif s[-1:] == ' ':
#         return trim(s[:-1])
#     else:
#         return s
    
print(trim('   hello '))
# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
# ---------------------------------------- end ----------------------------------------

print('-----------End-----------')
