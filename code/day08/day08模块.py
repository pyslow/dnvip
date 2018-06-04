#! /usr/bin/env python
# -*- coding:utf-8 -*-

'''
author :ben
date : 2018-5-xx
'''


# 包结构
# 目录和包什么区别?
# 在普通目录下边如果建立一个__init__.py脚本文件,这个目录就变成了包结构
# haha-->目录,在里面建立一个__init__.py文件,haha--->包
# 同一包下,模块名称不能相同
# 同一层次下,包名也不能相同


# python导入对象的几种方式
# 1.import 模块名
# import math
# print(math.sqrt(9))

# 2.from 模块名 import 对象
# from math import sqrt
# print(sqrt(9))

# 3.from 模块名 import *  (非私有对象)
# from math import *
# print(sqrt(9))


# 三种导入方式:
#1.import 模块名   拿到模块的引用,在使用的时候,带上模块名.对象名来使用
#2.from 模块名 import 对象      拿到对象的引用,对象名来使用,只是这一个对象
#3.from 模块名 import *  (非私有对象)     可以拿到所有非私有的对象


# 模块也是对象
# 当前模块也有一个属性__name__
# print(__name__)
# 查看__name__的名称?为什么不是day08模块这个名字呢?
# 根据该模块执行的方式而定:
# 是用解释器直接解释执行--->__name__规定为__main__
if __name__=='__main__':     # 条件成立
    print('我是解释器解释执行')


