#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/31 22:01
# @Author  : Slow
# @File    : yesy.py
# @Software: PyCharm

# def a():
#     def b():
#         print('a')
#     return b
# print(a())

# def foo(x, y, z, *args, **kw):
#     sum = x + y + z
#     print(sum)
#     for i in args:
#         print(i)
#     print(kw)
#     for j in kw.items():
#         print(j)
# a_tuple = (1,2,3) #    此处参数修改为2个看看会怎么样?
# b_dict = {'name': 'jim', 'age': 28, 'add': '上海'}
# foo(*a_tuple, **b_dict)   # 分析这里会怎么样?

# 2.题目:执行分析下代码
def func(a, b, c=9, *args, **kw):
     print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
func(1,2)
func(1,2,3)
func(1,2,3,4)
func(1,2,3,4,5)
func(1,2,3,4,5,6,name='jim')
func(1,2,3,4,5,6,name='tom',age=22)
    # 扩展: 如果把你的函数也定义成  def  get_sum(*args,**kw):pass