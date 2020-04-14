#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
@Author: Adam
@Date: 2020-04-13 16:48:59
@LastEditTime: 2020-04-14 21:54:46
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
'''
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
'''
# ---------------------------------------- end ----------------------------------------

# 迭代
# ---------------------------------------- start ----------------------------------------
'''
print('-----------迭代-----------')
# 如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。
# 在Python中，迭代是通过for ... in来完成的，而很多语言比如C语言，迭代list是通过下标完成的，比如Java代码：
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
# 默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()。
for value in d.values():
    print(value)
for key, value in d.items():
    print(key, ':', value)
# 由于字符串也是可迭代对象，因此，也可以作用于for循环：
for ch in 'ABCDEFG':
    print(ch)
# 所以，当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，而我们不太关心该对象究竟是list还是其他数据类型。
# 那么，如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：
from collections import Iterable
print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))

# 最后一个小问题，如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
# 上面的for循环里，同时引用了两个变量，在Python里是很常见的，比如下面的代码：
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

# 练习
# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
    "寻找列表中的最大值和最小值，空列表返回None，不用list.sort，不用max、min"
    if len(L) == 0 or not isinstance(L, list):
        return (None, None)
    min = L[0]
    max = L[0]
    try:
        for i in L:
            if min > i:
                min = i
            elif max < i:
                max = i
    except TypeError:
        print(r"can't compare different types")
        return (None, None)
    else:
        return (min, max)
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
print(findMinAndMax('abc'))

print(findMinAndMax(['a','b',1]))
# ---------------------------------------- end ----------------------------------------

'''
# 列表生成式
# ---------------------------------------- start ----------------------------------------
print('-----------列表生成式-----------')
# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
L = list(range(1, 11))
print(L)
# 但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环：
L = []
for x in range(1, 11):
    L.append(x ** 2)
print(L)

# 但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list：
L = [x ** 2 for x in range(1, 11)]
print(L)

# 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来，十分有用，多写几次，很快就可以熟悉这种语法。
# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
L = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print(L)
# 还可以使用两层循环，可以生成全排列：
L = [m + n for m in 'ABC' for n in 'XYZ']
print(L)
# 三层和三层以上的循环就很少用到了。

# 运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现
import os 
L = [d for d in os.listdir('.')]
print(L)

# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.items():
    print(k, '=', v)

# 因此，列表生成式也可以使用两个变量来生成list：
L = [k + '=' + v for k, v in d.items()]
print(L)

# 最后把一个list中所有的字符串变成小写：
L = ['HELLO', 'WORLD', 'IBM', 'Apple']
L1 = [s.lower() for s in L]
print(L1)

# if ... else

# 使用列表生成式的时候，有些童鞋经常搞不清楚if...else的用法。

# 例如，以下代码正常输出偶数：
L = [x for x in range(1, 11) if x % 2 == 0]
print(L)
# 但是，我们不能在最后的if加上else：
# L = [x for x in range(1, 11) if x % 2 == 0 else 0]
# 这是因为跟在for后面的if是一个筛选条件，不能带else，否则如何筛选？

# 另一些童鞋发现把if写在for前面必须加else，否则报错：
# L = [x if x % 2 == 0 for x in range(1, 11)]
# 这是因为for前面的部分是一个表达式，它必须根据x计算出一个结果。因此，考察表达式：x if x % 2 == 0，它无法根据x计算出结果，因为缺少else，必须加上else：
L = [x if x % 2 == 0 else -x for x in range(1, 11)]
print(L)

# 上述for前面的表达式x if x % 2 == 0 else -x才能根据x计算出确定的结果。

# 可见，在一个列表生成式中，for前面的if ... else是表达式，而for后面的if是过滤条件，不能带else。

# 练习
# 如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：
L = ['Hello', 'World', 18, 'Apple', None]
# L1 = [s.lower() for s in L]
print(L)
L2 = [s.lower() for s in L if isinstance(s, str)]
# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
# ---------------------------------------- end ----------------------------------------
print('-----------End-----------')
