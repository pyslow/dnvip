#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/4 15:33
# @Author  : Slow
# @Site    : 
# @File    : slow_day08.py
# @Software: PyCharm

# 2.写函数，判断用户传入的对象（字符串、列表、元组）
# 长度是否大于6, 如果大于6, 截取前4位, 否则直接打印输出

def fun(ages):
    if isinstance(ages, (str, list, tuple)):
        if len(ages) < 6:
            print(ages)
        else:
            print(ages[:4])


if __name__ == '__main__':
    st = '我是要截取'
    li = ['tom', 'boss', 'gie', 'san', 'slow', [22, 33, 44, 55, 77]]
    tup = (1, 7, 8, 0, 66, 88)
    fun(st)
    fun(li)
    fun(tup)