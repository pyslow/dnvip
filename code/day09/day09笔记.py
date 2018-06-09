#! /usr/bin/env python
# -*- coding:utf-8 -*-

'''
author :ben
date : 2018-6-xx
'''


# 第一步：你要先进入到指定的目录（安装虚拟环境的目录）
# 指令：在python3环境下面：python3 -m venv 虚拟环境名（python -m venv django_env）
# 问题:如果是python2下面如何来构建虚拟环境呢?
# 先下载virtualenv
# pip install virtualenv
# 在指定的目录下:进入该目录:virtualenv 虚拟环境名


# 模块的打包:
# 当前文件是打包文件设置文件
# from distutils.core import setup
#
# # 配置信息:
# setup(
#     name='my_package',
#     version='1.0.0',
#     author='ben',
#     author_email='xlhdx520@163.com',
#     url='http://www.xxxx.com',
#     description='模块的打包',
#     py_modules=['a']
# )

# 基本打包配置信息写好了
# 进入到setup.py所在的目录
# 打包指令:
# python setup.py sdist
# 执行指令之后,可以看到当前目录下多了一个dist目录,点进去看看,里面有一个压缩文件(模块打包之后的文件)

# 注意:打包之后的压缩文件的名称:配置信息里面name-version

# 你同事下载好了
# 先解压
# 进入解压之后的setup.py文件所在的目录
# 执行指令:python3 setup.py install
# 最后导入安装好的模块中对象来测试 from a import run-->



# python常用的内置函数
# 数学运算方面的:
# 何为内置?
# 直接在代码里面可以用
# print(abs(-8))  # 求绝对值

# print(max(1, 9, 20, 200))  # 最大值
# print(max([1, 2, 4]))
# print(max(['yr', 'yg', 'ykk'])) # list元素是字符串
# print(max(['21', '37', '199', '289']))  # []--->list

# print(sorted(['21', '37', '199', '289']))

# print(sum([1, 2, 8]))

# print(len('abcdf'))
# print(len({'name': 'ben', 'age': 28, 'sex': '女'}))  # 求字典的长度(多少数据项)
# print(len([1,2,3,6]))
# print(len((1,2,3,9,34)))  # (1,2,3,9,34)--->整体是一个元祖:

# print(3**2)

# print(pow(3, 2))
# print(pow(3, 2, 2))  # 3**2%2=1

# print(divmod(9,2))  # 返回的对象是一个元组(商,余数)  # (4, 1)

# print(round(3.88))
# print(round(3.59))  #?   python版本3.6.5(最新版),3.x早期版本round(3.59)-->3
# print(round(3.49))


# 类型转换的内置函数
# print(range(20))  # 2.x(返回的是list)--->3.x(返回的是对象)
# print(list(range(9)))  # range对象--->list
# print(type(int('20')))  # 整数
# print(float('9'))
# print(complex(3,4))  # (3+4j)
# print(type(str(3.14)))  # <class 'str'>
# print(tuple(range(4)))  # (0, 1, 2, 3)
# print(dict(name='haha',age=27))  # {'name': 'haha', 'age': 27}


# 字符和整数之间的转换?
# print(ord('a'))  # 通过码表找到字符对应的整数,解释器回答我
# print(ord('A'))  # 65

# 反过来?
# print(chr(65))    # 码表查找
# print(chr(97))

# 布尔?  细节
# print(bool(0))
# print(bool([]))
# print(bool(()))
# print(bool(''))   # False
# print(bool(' '))  # True
# print(False+2)  # 2

# 查看对象能否被执行的内置函数callable?
# name = 'haha'
# print(callable(name))  # False
# 什么原因?能够被执行(函数对象,方法对象)
# def run():
#     print('我在执行')
# 默认返回None

# print(callable(run()))  #  print(callable(None))  # False
# print(callable(run))  # True

# 切换功能的内置函数
# a_list = [1,2,3,4]
# print(a_list[0:3])  # 切片
# 内置函数实现这个功能
# print(a_list[slice(0,3)])  # print(a_list[0:3])
# print((1, 2, 9)[slice(0, 2)])  # (1, 2)
# print('pythonweb'[slice(1, 8, 2)])  # 三个参数和切片意义相同

# 进制转换的内置函数?
# print(oct(19))  #  --->八进制
# print(bin(19))  # 0b10011  二进制
# print(hex(19))  # 0x13  十六进制


# all,any
# print(all(['0', ' ', 99]))  # True
# print(all([0, ' ', 99]))  # False
# print(all([10, '', 99]))  # ''-->False--->最后就是False

# print(any((1,0)))  # 只要有一个为True--->True

# list.sort(list的方法,不是内置)
# 内置函数sorted(内置函数)


# 内置的反转函数
# a_list = [9,22,88,200]
# b_list = list(reversed(a_list))  # 内置的函数,返回的是一个对象
# print(b_list)


# 面向对象编程?
# def --->在定义函数
# class--->在定义类
class Person():  # name--->没有的
    def work(self):
        print('在工作')

    def eat(self):
        print('在吃饭')


# 定义类要做什么?
# 定义好的类--->创建类的实例对象
p1 = Person()
# 判断这个Person有没有属性和方法

# 有没有怎么判断?
# print(hasattr(p1, 'work'))  # True
# print(hasattr(p1, 'run'))   # False

# 怎么样获取属性对象?
# eat = getattr(p1,'eat') # 获取到的是一个方法对象
# # eat--->方法对象
# eat()  # 函数对象获取出来,并执行

# 设置属性?  # attr-->属性
# setattr(p1, 'name', 'ben')  # 先设置
# print(getattr(p1,'name'))   # 获取了


# 内置的判断 isinstance
# print(isinstance(Person,object))  #


# 其他的内置函数?
# print(str(2*3))  # 字符串
# print(type(299))
# print(eval('2*4'))  # 求解字符串表达式的值,参数类型是字符串

# import sys
# print(help(sys))
# print(dir(sys))
# print(__file__)
# print(__doc__)  # day03--->文档字符串

# name = '你是大美女'  # 全局变量
# def work():
#     age = 18
#     sex = '女'
#     print(locals())  # l
#     print(globals())  # g
# work()


# max-->其他的用法
# num_dict = {9: 12, 3: 22, 5: 9}
# print(max(num_dict))  # 字典里面key
# print(max(num_dict.values()))  # 字典的value部分

# a_list = [
#     (1, 'a'),
#     (2, 'b'),
#     (3, 'c'),
#     (4, 'd'),
# ]
# print(max(a_list))

# a_list = [
#     (1, 'a'),
#     (22, 'b'),
#     (3, 'c'),
#     (4, 'd'),
# ]
# print(max(a_list))  # (22, 'b') 如何来比较

# print(list(max(['a22', 'b99', 'c200'])))  # 打散

# 两个内置一起用,max,zip内置函数
age_dict = {'1_age': 19, '2_age': 22, '3_age': 33}
# print(list(age_dict.values()))
# print(list(age_dict.keys()))
# for item in zip(age_dict.values(),age_dict.keys()):
#     print(item)
# min---> max反过来

# (19, '1_age')
# (22, '2_age')
# (33, '3_age')
# print(list(max(zip(age_dict.values(),age_dict.keys()))))
# max--->(33, '3_age')-->list--->[33, '3_age']


