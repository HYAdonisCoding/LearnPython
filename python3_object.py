#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self, name, score):
        # 实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
        self.__name = name
        self.__score = score

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

    # 数据封装
    def get_score(self):
        return '%s: %s' % (self.__name, self.__score)

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')


Adam = Student('Adam', 100)
# print(Adam.name, Adam.score)
# print_score(Adam)
Adam.get_score()
lisa = Student('Lisa', 89)
bart = Student('Bart', 59)
print(Adam.get_score(), Adam.get_grade())
print(lisa.get_score(), lisa.get_grade())
print(bart.get_score(), bart.get_grade())
Adam.set_score(90)
print(Adam.get_score())
