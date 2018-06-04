#! /usr/bin/env python
# -*- coding:utf-8 -*-

'''
author :ben
date : 2018-1-xx

'''

# from myapp import a  # 从myapp包里面导入模块a
#
# if __name__ == '__main__':
#     print('看看a.py执行')

# 当我解释执行b.py--->首先执行的代码是导入from myapp import a-->会先执行a模块里面的代码
# 判断a.py的执行方式,不是解释执行,而是导入执行,执行的是a模块里面else部分
# 如果用解释器直接解释执行,当前__name__--->__main__,如果是被导入执行,__name__就是模块名

# 解释执行__name__--->__main__,如果被导入执行__name__--->包名.模块名(模块名)


# from myapp import a

# 这个模块里面只是导入a而已,没有写其他代码
# 导入了a--->先要执行a里面的代码(a里面的代码被执行了)

# 假设现在重复导入多次会怎么样?

# from myapp import a
# from myapp import a
# from myapp import a
# 问题?a模块里面的代码会被执行几次呢?
# 结果只执行了一次
# 在模块被重复导入执行的时候,只有第一次会被执行,后面不会被重复执行
# 为什么会这样?设计是相关,考虑是导入模块执行的效率问题

# 问题来了,如果非要重  复导人执行怎么办?
# reload函数
# py2-->内置
# py3--->另外模块

# py3的写法
# from importlib import reload  #
# from myapp import a    # 第一次导入
# # from myapp import a   # 不会被重复导入执行
# # 使用reload函数
# reload(a)

# 总结一下:要重复导入执行,要使用reload函数,py2和py3是有改变

# 导入模块的方式import

# 特殊的方法__import__

# __import__('os').system('dir')

# import os
# print(os.system('dir'))

# 执行的效果是等价的

#
# import sys
# from importlib import reload
#
# from myapp import a   # 第一次导入执行
# __import__('a')       # 第二次导入执行
# print('!!!!!!')
# del sys.modules['a']  # 删除模块的操作
# __import__('a')       # 第三次导入执行
# __import__('a')       # ...(不会执行)
# __import__('a')       # ...(不会执行)
# reload(a)             # 第四次导入执行
# print(sys.modules['a'])  # sys.modules-->导入的模块信息




# 在python交互环境下,可以_代替上一次运算的结果

# 内置函数dir/help

# a_list= [1,2]
# # print(dir(a_list))
# # dir--->内置函数,直接使用,dir(对象名):对象-->模块里面的属性名和方法名
#
# # 拿到一个陌生的模块,可以这样去查看信息
# # print(help(a_list))
# print(a_list.__class__)  # <class 'list'>

# __class__:查看对象对应的类


# 包管理器,包的安装
# pip,easy_install  :包管理器
# 包管理怎么使用

# 下载:指令:pip install requests(库名或者模块名)
# 卸载:pip uninstall requests
# 查看已经安装的包:pip list


# 虚拟环境的使用
# 为什么要使用虚拟环境
# 同时参与两个项目的开发,项目a,项目b
# 项目a--->可能使用3.6,使用requests(2.0)
# 项目b--->可能使用3.6,使用requests(2.6)
# 两个项目安装的库和模块彼此是不相同

# 为项目a--->单独创造一个虚拟环境(),和其他虚拟环境,还有系统的python环境都是彼此独立,隔离开的
# 为项目b--->单独创造一个虚拟环境(),和其他虚拟环境,还有系统的python环境都是彼此独立,隔离开的

# 怎么样创建虚拟环境呢?
# 以python3.6
# 指令:python -m venv enva(虚拟环境名称)
# 使用pycharm创建虚拟环境


# 下载requests库,下载百度网页的源代码
# 在命令行的模式下:pip install requests
# 或者在pycharm里面直接下载安装

# 使用requests
import requests    # (模块名)
   # 想百度服务器发送了http(get请求)
# print(result.status_code)  # 200:响应码--->请求成功
# print(requests.get('http://www.hao123.com').text)
# print(requests.__class__)   # module

# python语言--->网页源代码爬取
#




