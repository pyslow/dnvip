#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/29 22:30
# @Author  : Slow
# @File    : test.py
# @Software: PyCharm

# a=[num+num for num in range(1,100,2)]
# print(a)


def fun(*ages,**kwargs):
    print(ages)
    print('**********')
    print(kwargs)
fun(11,22,111,{1:10},33,55)