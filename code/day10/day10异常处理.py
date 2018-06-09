#! /usr/bin/env python
# -*- coding:utf-8 -*-

'''
author :ben
date : 2018-6-xx
'''

# python异常处理

# 1.错误?异常?
# 2.常见的异常种类
# 3.异常处理机制
# 4.自定义异常


# 错误,异常?
# 错误:大多都是代码书写的错误,比如,违背了语法规则,掉了:或者缩进有问题,导入不存在的模块,包
# 使用了不存在的对象


# 异常:解释器解释执行代码的过程中有可能会出现的一些不正常的状态
# 异常有可能发生,也有可能不发生
# 代码里打开去读取一个不存在的文件的时候,代码会出现异常
# with open('ben.py', 'r', encoding='utf-8') as f:
#     print(f.read())   # 出现了异常状态,但是没有处理,导致后面的代码没有被执行
# print('异常之后的代码')
# 如果代码出现异常,解释器崩溃了
# 异常处理,保障代码的健壮

# # 没有异常的情况:只执行了try里面的代码
# try:
#     f = open('ben.py', 'w', encoding='utf-8')
#     print('没有发生异常')  # 如果32出现异常,那33行代码是不会被执行
# except Exception as e:  # Exception--->异常种类的基类(父类)
#     print('出现异常')
#     print(e)


# 出现异常的情况:
# try:
#     f = open('tom.py', 'r', encoding='utf-8')
#     print('没有发生异常')  # 如果32出现异常,那33行代码是不会被执行
# except Exception as e:  # Exception--->异常种类的基类(父类)
#     print('出现异常')
#     # print(e)   # [Errno 2] No such file or directory: 'tom.py'
# print(111111)  # 即使前面出现异常,也不影响后面的代码的执行

# try....except   # python里面的关键字--->异常处理的关键字
# as--->取别名(e)


# py2版本里面
# try:
#     f = open('tom.py', 'r', encoding='utf-8')
# except Exception,e:  # py2异常语法,在python3里面不兼容
#     print(e)

# Exception--->异常种类的基类(父类)
# 不管出现什么异常--->异常的基类类匹配  100%


# 异常处理结构:
# try:  # 逻辑代码
#     f = open('tom.py', 'r', encoding='utf-8')  # 会出现异常
#     print(1111)  # 不会被执行
# except Exception as e:  # 肯定匹配上
#     print(e)   # [Errno 2] No such file or directory: 'tom.py'
# else:  # 没有异常发生,else才会被执行
#     print(9999)  # 没有执行?为什么?try里面的代码没有异常,else代码块才会被执行
# finally:  # 不管异常有没有发生,finally都要执行
#     print(3333)  #  2222
# [Errno 2] No such file or directory: 'tom.py'
# 0

# try:  # 逻辑代码
#     f = open('tom.py', 'r', encoding='utf-8')  # 会出现异常
#     print(1111)  # 不会被执行
# except Exception as e:  # 肯定匹配上
#     print(e)   # [Errno 2] No such file or directory: 'tom.py'
# finally:  # 不管异常有没有发生,finally都要执行
#     print(3333)
# else:  # 没有异常发生,else才会被执行
#     print(9999)  # 没有执行?为什么?try里面的代码没有异常,else代码块才会被执行

#  如果同时出现finally和else两个代码块,finally必须放到后面
# SyntaxError--->语法错误--->违背了语法规则


# 常见的异常类型
# 1.NameError:没有定义的变量
# print(age)  # 变量没有定义,就拿来用

# 2.ZeroDivisionError:0除异常
# print(20/0)

# 3.SyntaxError:语法错误
# for num in range(20)
#     print(num)

# 4.IndexError:索引越界
# a_list = [2, 3, 4]
# print(a_list[10])

# 5.KeyError:不存在的key
# a_dict = {'name': 'ben', 'age': 28}
# print(a_dict['sex'])  # 不存在的key

# 6.FileNotFoundError:文件不存在异常
# f = open('haha.py','r')

# IOError:(文件操作相关的异常类型)--->父类---->Exception(一层层)--->object

# 7.AttributeError:属性异常
# class Student():
#     pass
# s1 = Student()  # s1对象不存在属性叫name
# print(s1.name)

# 很多时候用父类Exception(基类)


# try:
#     y = 8 / int('我不是数字')
#     x = 22 / 0
#     f= open('hehe.py','r')
# except Exception as e:  # Exception
#     print(e)   # 1
# else:  #
#     print('没有异常出现')
# finally:
#     print('不管异常有没有发生,我都要执行和')  # 1


# try:
#     f = open('hehe.py', 'r')
#     x = 22 / 0
#     y = 8 / int('我不是数字')
# except ZeroDivisionError as e:  # Exception
#     print(e)   # 1
# except IOError as e:  # Exception
#     print(e)
# except ValueError as e:  # Exception
#     print(e)    # 1
# else:  #
#     print('没有异常出现')
# finally:
#     print('不管异常有没有发生,我都要执行和')  #1


# try:
#     y = 8 / int('我不是数字')
#     x = 22 / 0
#     f = open('hehe.py', 'r')
# except (ZeroDivisionError, ValueError, IOError,Exception) as e:  # Exception
#     print(e)  # 1
# else:  #
#     print('没有异常出现')
# finally:
#     print('不管异常有没有发生,我都要执行和')


# 如果把基类(Exception)放到最前面,永远在父类异常里面处理
# 都父类吞噬掉,子类不会发生作用
# try:
#     y = 8 / int('我不是数字')
#     x = 22 / 0
#     f = open('hehe.py', 'r')
# except Exception as e:  # Exception
#     print(e)
#     print(0)
# except ZeroDivisionError as e:  # Exception
#     print(e)   # 1
#     print(1)
# except IOError as e:  # Exception
#     print(e)
#     print(2)
# except ValueError as e:  # Exception
#     print(e)    # 1
#     print(3)


# try:
#     y = 8 / int('我不是数字')
#     x = 22 / 0
#     f = open('hehe.py', 'r')
# except ZeroDivisionError as e:  # Exception
#     print(e)   # 1
#     print(1)
# except IOError as e:  # Exception
#     print(e)
#     print(2)
# except ValueError as e:  # Exception
#     print(e)    # 1
#     print(3)
# except Exception as e:  # Exception
#     print(e)
#     print(0)
# 父类异常处理放到最后面,即使前面子类异常匹配不上,还有万能的匹配


# 异常处理写到函数内
# def work():
#     try:
#         f = open('haha.py','r')
#     except Exception as e:
#         print(e)


# 如果代码出现了异常,如果不做异常处理--->解释器抛出异常---->解释器崩溃
# f = open('haha.py','r')  # line 211 定位出现异常位置
# Traceback (most recent call last):
#   File "E:/project/other/vip/vip1805/day10/day10异常处理.py", line 211, in <module>
#     f = open('haha.py','r')
# FileNotFoundError: [Errno 2] No such file or directory: 'haha.py'
# 打印是异常信息
# 堆栈错误信息--->解释器退出了
# 出现异常--->查看异常信息
# File "E:/project/other/vip/vip1805/day10/day10异常处理.py", line 211, in <module>
# 代码的位置信息
# f = open('haha.py','r')  就这个代码
# FileNotFoundError:出现的异常的种类FileNotFoundError
# [Errno 2] No such file or directory: 'haha.py'  说明信息


# 假设如果让你主动触发异常
# 如果出现了某个特殊场景,模拟抛出异常--->由程序员主动引用异常
# 解释器抛出的异常
# 由程序员(你)主动引用异常

# raise--->这个关键字

# for num in range(20):  # 不会出现--->主动触发的异常
#     if num == 9:  # 假设的一种
#         raise ValueError('小哥哥,我拿到你了')
# 形式是一样:堆栈错误(异常信息)
# 到底由谁来触发的异常:现在由我(程序员)控制


# 自定义异常
# 为什么异常?python提供给我们用的异常种类还是有限(这些异常种类以外的异常怎么办)
# 类--->控制(面向)
# 构造方法(类--->类的实例对象)--->初始化函数(添加属性(数据))---
import sys
class MyError(Exception):    # 图纸(类)--->实际存在的小汽车(实例对象)
    def __init__(self,message):
        self.message = message # 左边message是属性,右边传递进来值
def main():
    try:
        if len(sys.argv)== 1:  #
            # 不是系统提供了异常类型,而是我自己的异常类的实例对象
            raise MyError('参数的个数少了')   # 构造了我自定义异常的实例对象
    except Exception as e:
            # 直接打印对象--->自动去调用__str__魔法方法
        print(1111)
        print(e)
# 右键运行这个脚本文件: python 脚本文件名 (直接右键只有一个参数)
# python day10异常处理.py  # 参数个数是1
# python day10异常处理.py 200 300
# 当前目录下:python 脚本文件名       cmd下
if __name__=='__main__':
    main()


# class Person():  # --->object
#     def __init__(self,name):   # 初始化函数(特殊函数)
#         self.name = name
#     def __str__(self):  # 并没有显示的执行,但是被执行
#         print(22222)
#         return self.name
# p1 = Person('ben')  # 实例
# print(p1)  # 这行代码触发(直接打印这个实例)
# 设计机制:类实现了__str__魔法方法,直接打印输出实例对象的时候自己出发这个魔法方法

# 不是构造实例,而是直接打印实例对象自动调用__str__这个方法  (理解)
# 面向魔法方法比较多(设计机制)
# 构造对象(生孩子)--->再初始化数据(起名字,穿衣服)--->
# 后面内容



