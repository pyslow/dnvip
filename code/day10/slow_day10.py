#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/9 18:57
# @Author  : Slow
# @Site    : 
# @File    : slow_day10.py
# @Software: PyCharm


# 动手完成:
#   1.自定义一个异常类,当list内元素长度超过10的时候抛出异常
# class ClaError(Exception):
#     def __init__(self,le):
#         self.le = le
#     def myerror(self):
#         try:
#             if len(self.le)>10: #大于10抛异常
#                 raise ClaError('列表长度大于10')
#         except Exception as e:
#             print(e)
# if __name__=='__main__':
#     ls=[0,1,2,3,4,5,6,7,8,9,10]
#     myerror=ClaError(ls)
#     myerror.myerror()


#   2.思考如果对于多种不同的代码异常情况都要处理,又该如何去
#      处理,自己写一个小例子

# try:
#     y = 8 / int('我不是数字')
#     x = 22 / 0
#     f = open('hehe.py', 'r')
# except ZeroDivisionError as e:
#     print(e)
# except IOError as e:
#     print(e)
# except ValueError as e:
#     print(e)
# except Exception as e:
#     print(e)


#   3.try-except和try-finally有什么不同,写例子理解区别

# 3.1 try-except
# try:
#     1/0  #抛异常
# except Exception as a:
#     print(a) #打印异常
# print('我打印了')#执行
#

# # 3.2 try-finally
# try:
#     1/0  #抛异常
#     print('hhahaha') #我不执行
# finally:
#     print('我是finally') #不管有没有异常我都会执行
# print('我打印了')#执行


#   4.写函数，检查传入字典的每一个value的长度，如果大于2，
#      那么仅仅保留前两个长度的内容，并将新内容返回给调用者
#      dic = {“k1”: "v1v1","k2":[11,22,33}}
def censor_dict(dic):
    for key,value in dic.items():
        if len(value) > 2:
            dic[key]=value[:2:]


if __name__ == '__main__':
    dic = {"k1": "v1v1", "k2": [11, 22, 33]}
    censor_dict(dic)
    print(dic)
# 作业提交地址:http://xzc.cn/LAgUIhh20M
