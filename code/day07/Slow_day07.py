#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/2 17:07
# @Author  : Slow
# @File    : Slow_day07.py
# @Software: PyCharm

# 1.
#
#
# def foo(x, y, z, *args, **kw):
#     sum = x + y + z
#     print(sum)
#     for i in args:
#         print(i)
#     print(kw)
#     for j in kw.items():
#         print(j)
#
#
# a_tuple = (1, 2, 3)#此处参数修改为2个会报错，因为形参是需要三个，只传了2个
# b_dict = {'name': 'jim', 'age': 28, 'add': '上海'}
# foo(*a_tuple, **b_dict)#分析这里会怎么样?
# 一、a_tuple参数传送给 x,y,z三个形参，然后b_dict传送个**kw，args没有值传送
# 2.
# 题目: 执行分析下代码
#
#
# def func(a, b, c=9, *args, **kw):
#     print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
#
#
# func(1, 2) #a = 1 b = 2 c = 9 args = () kw = {}
# func(1, 2, 3) #a = 1 b = 2 c = 3 args = () kw = {}
# func(1, 2, 3, 4)#a = 1 b = 2 c = 3 args = (4,) kw = {}
# func(1, 2, 3, 4, 5)#a = 1 b = 2 c = 3 args = (4, 5) kw = {}
# func(1, 2, 3, 4, 5, 6, name='jim')#a = 1 b = 2 c = 3 args = (4, 5, 6) kw = {'name': 'jim'}
# func(1, 2, 3, 4, 5, 6, name='tom', age=22)#a = 1 b = 2 c = 3 args = (4, 5, 6) kw = {'name': 'tom', 'age': 22}
# # 扩展: 如果把你的函数也定义成
# def get_sum(*args, **kw):
#     print(args)
#     print(kw)
# #如果定义成（可变参数和关键字参数）之后，函数可以接收任意形式的值
# get_sum(*(1,23,3,4,5,6,{'2':1}),{1,54,7,8},**{'name':'slow','age':18})
#
#
# 3.
# 写一个函数函数，计算传入字符串中的数字、字母、空格和其他的个数分别为多少?
def num_fun(num):
    number_digit = 0
    number_space = 0
    number_alpha = 0
    number_else = 0
    for i in num:
        if i.isdigit():  # 检查字符串是否只由数字组成
            number_digit += 1
        elif i.isspace():  # 检查字符串是否只由空格组成
            number_space += 1
        elif i.isalpha():  # 检查字符串是否只由字母组成
            number_alpha += 1
        else:
            number_else += 1
    return (number_digit, number_space, number_alpha, number_else)
n = num_fun("My name is slow,age 18。")
print('数字：{0}, 空格:{1}，字母:{2}，其它:{3}'.format(n[0],n[1],n[2],n[3]))


# http: // xzc.cn / XKiOoCYc6h
# day07作业提交地址