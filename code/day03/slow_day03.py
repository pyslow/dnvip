#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/25 9:44
# @Author  : Slow
# @Site    : 
# @File    : zy_day03_slow.py
# @Software: PyCharm

# 1.两种字符串格式化的各写一例
#
name='Slow'
age=18

st_test1='我的名字叫:%s,今年:%s岁了'%(name,age)
st_test2='我的名字叫:{0},今年:{1}岁了'.format(name,age)

# 2.在你的command line中打印输出:看看会发生什么？
# print('\\\n\\')  #运行后正显示为两个"\"-----\ 换行 \
# print(r'\\\n\\\') #运行后出错，r原始字符串把最后一单引号当做了字符串，导致这个字符内少了一个单引号结束
# print('\\\t\\') #运行后正显示
# print(r'\\\t\\') #运行后正显示
#
# 3.将字符串"动脑学院"转换为bytes类型
dn='动脑学院'
by_dn=bytes(dn,encoding='utf-8')
