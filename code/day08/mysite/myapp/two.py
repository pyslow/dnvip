#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/4 15:12
# @Author  : Slow
# @Site    : 
# @File    : two.py
# @Software: PyCharm

import one
from importlib import reload

def fun1():
    print(one.name)


if __name__ == "__main__":
    fun1()
    reload(one)
    print('我是two模块')
else:
    print('我是导入模块two')
    print(__name__)

#2.写函数，判断用户传入的对象（字符串、列表、元组）
# 长度是否大于6, 如果大于6, 截取前4位, 否则直接打印输出
