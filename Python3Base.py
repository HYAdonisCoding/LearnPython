#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
@Author: Adam
@Date: 2020-04-09 06:36:03
@LastEditTime: 2020-04-12 17:52:36
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
'''
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
'''
# ---------------------------------------- end ----------------------------------------

# set
# ---------------------------------------- start ----------------------------------------
'''
print('-----------set-----------')
# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
# 要创建一个set，需要提供一个list作为输入集合：
s = set([1, 1, 2, 2, 3, 3])
s.add(4)
s.remove(1)
print(s)
s1 = set([1, 2, 3])
print(s1)
print(s & s1)
print(s | s1)
key = ['1', '2', '3']
s2 = set(key)
print(s2)
## 再议不可变对象
# 上面我们讲了，str是不变对象，而list是可变对象。
# 对于可变对象，比如list，对list进行操作，list内部的内容是会变化的，比如：
a = ['c', 'b', 'a']
print(a)
a.sort()
print(a)
# 而对于不可变对象，比如str，对str进行操作呢：
s = 'abc'
s1 = s.replace('a', 'A')
print(s)
print(s1)

k1 = (1, 2, 3)
k2 = (1, [2, 3])
s2 = set(k1)
print(s2)
# s3 = set(k2)
# print(s3)
d = {'start' : 100}
d[k1] = "k1"
print(d)
# d[k2] = 'k2'
# print(d)
'''
# ---------------------------------------- end ----------------------------------------

# 函数
# ---------------------------------------- start ----------------------------------------

print('-----------函数-----------')
# https://docs.python.org/3/library/functions.html#abs
# 绝对值
print(abs(100))
print(abs(-20))
print(abs(12.34))
# print(abs(1,2))
# print(abs('a'))
# 最值
print(max(1,2))
print(max(1,2, 5, 8 ,-10))
print(min(1,2, 5, 8 ,-10))
# 数据类型转换
print(int('1234'))
print(int(12.34))
print(float('12.34'))
print(str(1.23))
print(str(100))
print(bool(1))
print(bool(0))
# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
a = abs
print(a(-100))

# 练习
# 请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：
a = 255
a = 1000
b = hex(a)
c = str(b)
print(b)
print(c)

# 定义函数
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-99))
# 如果你已经把my_abs()的函数定义保存为abstest.py文件了，那么，可以在该文件的当前目录下启动Python解释器，用from abstest import my_abs来导入my_abs()函数，注意abstest是文件名（不含.py扩展名）：

# 空函数
def nop():
    pass
# my_abs(1,2)
# my_abs('A')

# 返回多个值
import math

def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x)
print(y)
print(x, y)
r = move(100, 100, 60, math.pi / 6)
print(r)

# 小结

# 定义函数时，需要确定函数名和参数个数；

# 如果有必要，可以先对参数的数据类型做检查；

# 函数体内部可以用return随时返回函数结果；

# 函数执行完毕也没有return语句时，自动return None。

# 函数可以同时返回多个值，但其实就是一个tuple。

# 练习
# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax**2+bx+c=0 的两个解。
# 提示：
# 一元二次方程的求根公式为：
# 计算平方根可以调用math.sqrt()函数：
def quadratic(a, b, c):
    z1 = -b + math.sqrt(b**2-4*a*c)
    z2 = -b - math.sqrt(b**2-4*a*c)
    m = 2*a
    return z1/m, z2/m

print(quadratic(2, 3, 1))
if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')

# 函数的参数
def power(x):
    return x * x
print(power(5))
print(power(15))

def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
    
print(power(5, 2))
print(power(5, 3))

print(power(5))
# 默认参数很有用，但使用不当，也会掉坑里。默认参数有个最大的坑，演示如下：

# 先定义一个函数，传入一个list，添加一个END再返回：

def add_end(L=[]):
    L.append('END')
    return L
a = add_end([1, 2, 3])
print(a)
a = add_end()
print(a)
a = add_end()
print(a)
a = add_end()
print(a)
# 原因解释如下：
# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
a = add_end()
print(a)
a = add_end()
print(a)
a = add_end()
print(a)

# 可变参数
# 在Python函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc([1, 2, 3]))
print(calc((1, 3, 5, 7)))
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc(1, 2, 3))
print(calc(1, 3, 5, 7))
print(calc())
n = [1, 2, 3]
print(calc(*n))
# *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。

# 关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。请看示例：
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
person('Michael', 38)
person('Bob', 35, city='Beijing')
person('Adam',25, gender='Super', job='Engineer')
extra = {'city': 'Beijing', 'job': 'Engineer', 'addr': '中南海'}
person('Jack', 24, city=extra['city'], job=extra['job'])
person('Jack', 24, **extra)
# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。

# 命名关键字参数
# 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查。
def person(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:', name, 'age:', age, 'other:', kw)

# person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)
person('Jack', 24, **extra)

def person(name, age, *, city, job):
    print(name, age, city, job)
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)

# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person(name, age, *args, city, job):
    print(name, age, args, city, job)
# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错：
# person('Jack', 24, 'Beijing', 'Engineer')
person('Jack', 24, city='Engineer', job='Engineer')
person('Jack', 24, job='Engineer',city='Engineer')

def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)

person('Jack', 24, job='Engineer')

# 参数组合
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def f1(a, b, c=0, *args, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'args=', args,'kw=', kw)

def f2(a, b, c=0, *, d, **kw):
     print('a=', a, 'b=', b, 'c=', c, 'd=', d,'kw=', kw)
f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
args = (1, 2, 3)
kw = {'d': 00, 'x': '#'}
f2(*args, **kw)
# 虽然可以组合多达5种参数，但不要同时使用太多的组合，否则函数接口的可理解性很差。

# 练习
# 以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
def product(x, y):
    sum = x * y
    print(sum)
    return sum
    
product(5,10)

def product(*x):
    if len(x) <= 0:
        raise TypeError('params can\'t be none')
    sum = 1
    for num in x:
        sum = sum * num
    print(sum)
    return sum

product(5)
product(5, 6)
product(5, 6, 7)
product(5, 6, 7, 9)
# 测试
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else: 
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')
# product()
# 小结

# Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。

# 默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

# 要注意定义可变参数和关键字参数的语法：

# *args是可变参数，args接收的是一个tuple；

# **kw是关键字参数，kw接收的是一个dict。

# 以及调用函数时如何传入可变参数和关键字参数的语法：

# 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

# 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

# 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

# 命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

# 定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。


# 递归函数
# 在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print(fact(1))
print(fact(2))
print(fact(3))
print(fact(4))
print(fact(5))
print(fact(100))
# 递归函数的优点是定义简单，逻辑清晰。理论上，所有的递归函数都可以写成循环的方式，但循环的逻辑不如递归清晰。

# 使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。可以试试fact(1000)：
# print(fact(1000))

# 解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。

# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。

# 上面的fact(n)函数由于return n * fact(n - 1)引入了乘法表达式，所以就不是尾递归了。要改成尾递归方式，需要多一点代码，主要是要把每一步的乘积传入到递归函数中：

def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num-1, num * product)

print(fact_iter(5, 1))
print(fact_iter(4, 5))
print(fact_iter(3, 20))
print(fact_iter(2, 60))
print(fact_iter(1, 120))

# print(fact(1000))
print(fact_iter(100, 1))

#     尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。

# 遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。

# 小结

# 使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。

# 针对尾递归优化的语言可以通过尾递归防止栈溢出。尾递归事实上和循环是等价的，没有循环语句的编程语言只能通过尾递归实现循环。

# Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。


# 练习

# 汉诺塔的移动可以用递归函数非常简单地实现。

# 请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法，例如：

def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
        return
    
    move(n-1, a, c, b)
    print(a, '-->', c)
    move(n-1, b, a, c)

# move(3, 'A', 'B', 'C')
move(3, 'A', 'B', 'C')
# 需要5845.42亿年以上
# move(64, 'A', 'B', 'C')

# ---------------------------------------- end ----------------------------------------


print('end')