#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
@Author: Adam
@Date: 2020-04-09 06:36:03
@LastEditTime: 2020-04-12 14:54:45
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /undefined/Users/adonis/Developer/MyGithubCode/LearnPython/Python3Base.py
'''


# print absolute value of an integer:
# a = 100
# if a >=100:
#     print(a)
# else:
#     print(-a)
# #ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
# b = ord('A')
# print(b)
# c = ord('中')
# print(c)
# d = chr(66)
# print(d)
# e = chr(25991)
# print(e)

# #两种写法完全是等价的。
# # '\u4e2d\u6587'
# # '中文'

# #Python对bytes类型的数据用带b前缀的单引号或双引号表示：
# x = b'ABC'

# # 'ABC'.encode('ascii')
# # b'ABC'
# # '中文'.encode('utf-8')
# # b'\xe4\xb8\xad\xe6\x96\x87'
# # '中文'.encode('ascii') # UnicodeEncodeError

# # 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节：
# # print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))
# # '中'

# # 计算str包含多少个字符
# len('Abc')
# len('中文')
# # len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数：
# len(b'ABc')
# len(b'\xe4\xb8\xad\xe6\x96\x87')
# len('中文'.encode('utf-8'))

# # 在Python中，采用的格式化方式和C语言是一致的，用%实现
# 'Hello, %s' % 'world'
# 'Hi, %s, you have $%d.' % ('Michael', 1000000)

# #常见的占位符有：
# # 占位符	替换内容
# # %d	整数
# # %f	浮点数
# # %s	字符串
# # %x	十六进制整数
# # 其中，格式化整数和浮点数还可以指定是否补0和整数与小数的位数：
# print('%2d-%02d' % (3, 1))
# print('%.2f' % 3.1415926)
# # 如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串：
# print('Age: %s. Gender: %s' % (25, True))
# # 有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%：
# print('growth rate: %d %%' % 7)
# # format()
# # 另一种格式化字符串的方法是使用字符串的format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}……，不过这种方式写起来比%要麻烦得多：
# print('Hellow, {0}, 成绩提升了 {1:.1f}%'.format('Adam', 17.125))

# classmates = ['Michael', 'Bob', 'Adam']
# len(classmates)
# classmates[0]
# classmates[1]
# classmates[2]
# # 索引超出了范围时，Python会报一个IndexError错误，所以，要确保索引不要越界，记得最后一个元素的索引是len(classmates) - 1。
# # 如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素：
# classmates[-1]
# classmates.append('Tom')
# # 也可以把元素插入到指定的位置，比如索引号为1的位置：
# classmates.insert(1, 'Jack')
# # 要删除list末尾的元素，用pop()方法：
# classmates.pop()
# # 要删除指定位置的元素，用pop(i)方法，其中i是索引位置：
# classmates.pop(1)
# # 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
# classmates[1] = 'Sarah'
# # list里面的元素的数据类型也可以不同
# L = ['Apple', 123, True]
# # list元素也可以是另一个list
# p = ['Asp', 'Php']
# s = ['Python', 'Java', p, 'Scheme']
# # tuple
# # 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：
# classmates = ('Michael', 'Bob', 'Adam')
# # 如果要定义一个空的tuple，可以写成()：
# t = ()
# # Python在显示只有1个元素的tuple时，也会加一个逗号,，以免你误解成数学计算意义上的括号。
# t = ('a', 'b', ['A', 'B'])
# t[2][0] = 'X'
# t[2][1] = 'Y'
# # 练习
# l = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]
# print(l[0][0])
# print(l[1][1])
# print(l[2][2])

# 条件判断
# ---------------------------------------- start ----------------------------------------
'''
age = 22
if age >= 18:
    print('your age is', age)
    print('adult')
elif age > 10:
    print('your age is', age)
    print('teenager')
else:
    print('your age is', age)
    print('child')

# input()读取用户的输入
# s = input('birth:')
# birth = int(s)
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')
'''

'''
练习

小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
'''
'''
height = 1.75
weight = 80.8
bmi = weight / (height**2)
if bmi < 1.85:
    print('过轻', bmi)
elif bmi < 25:
    print('正常', bmi)
elif bmi < 28:
    print('过重', bmi)
elif bmi < 32:
    print('肥胖', bmi)
else:
    print('严重肥胖', bmi)

'''
# ---------------------------------------- end ----------------------------------------

# 循环
# ---------------------------------------- start ----------------------------------------
'''
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum, list(range(5)))
sum = 0
for x in range(101):
    sum = sum + x
print(sum)

print('-----------while循环-----------')
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

# 练习
# 请利用循环依次对list中的每个名字打印出Hello, xxx!：

L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print('Hello, '+name+'!')
print('-----------break-----------')
n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n + 1
print('-----------continue-----------')
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)
    
    
'''
# ---------------------------------------- end ----------------------------------------

# dict
# ---------------------------------------- start ----------------------------------------
print('-----------dict-----------')
names = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
d['Adam'] = 78
print(d['Adam'])
# 要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
print('Alice' in d)
# 二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
print(d.get('Alice'))
print(d.get('Alice', -1))
print(d.get('Adam'))
print(d.get('Adam', -1))
# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
print(d.pop('Bob'))
print(d)
# 请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。
# 和list比较，dict有以下几个特点：
# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。
# 而list相反：
# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少。
# 所以，dict是用空间来换取时间的一种方法。
# dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。
# 这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。
# 要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key：
key = [1, 2, 3]
# d[key] = 'a list' TypeError: unhashable type: 'list'

# ---------------------------------------- end ----------------------------------------

# set
# ---------------------------------------- start ----------------------------------------
# print('-----------set-----------')
# ---------------------------------------- end ----------------------------------------
print('end')