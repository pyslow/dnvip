#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/19 11:26
# @Author  : Slow
# @File    : dn_day01_Slow.py
# @Software: PyCharm

# 1.	课后在自己的电脑上安装python,配置环境,并查看python安装目录的文档结构
"""
DLLs :动态链接库
Doc：官方文档
include：C语言头文件库
Lib：内置库
libs：库
Scripts：python依赖脚本工具
tcl：图形GUI相关库
Tools：工具集
"""

# 2.	在cmd下进入python交互环境,编写你的第一个python程序然后进入IDLE编辑器,编写同样的程序,并调用python解释器执行:
# 1.	打印输出你真心喜欢的那个异性对象的名字,如:’I love xiaoming’
print('I love you!')
# 2.	使用print在屏幕上显示你的名字，年龄，最喜欢的颜色和你相关的一些事，比如：背景，兴趣，爱好
name = "Slow"
age = 18
colour = "blue"
its = "python、旅游、打球"
print("我叫%s,我今年%d岁了，我喜欢%s色，我爱好%s!" % (name, age, colour, its))

