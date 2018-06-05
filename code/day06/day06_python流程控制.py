#! /usr/bin/env python
# -*- coding:utf-8 -*-

'''
author :ben
date : 2018-5-xx
'''

# python流程控制
# 1.程序块,作用域
# 2.条件控制语句
# 3.循环控制语句
# 4.循环跳出
# 5.语句的嵌套

# 1.程序块,作用域
# 程序块:组织代码结构的一种形式--->提高代码的可读性
# if 1:
#     print(1)
#     print(2)
#     print(3)
#     print(4)  # 假设100行代码
#     if 2:
#         print(5)
#         print(6)

# 作用域:
# age = 19    # 全局变量
# def run():
#     age = 22     # 函数内的局部变量
#     print(age)
# # print(age)  # 19?22?
# run()   #但是没有执行函数   执行函数--->会执行函数内部的代码块里面的代码


# 缩进是非常重要

# if 1:   #  什么都不干
#     pass    # 什么都不做,使用占位符pass

# def run():
#     pass
# run()


# 条件控制语句?
# 如果明天不下雨,我们去打篮球,如果明天下雨,我们就去看电影
# 判断的条件是:明天到底下不下雨
# 第一种可能性:明天下雨---->看电影
# 第二种可能性:明天不下雨--->打篮球
# 代码表示(伪代码)
# if 明天下雨:  # 明天下雨(判断的条件)
#     看电影
# else:
#     打篮球


# name = input('哥们,请告诉我你的名字:')
# if name == 'jim':
#     print('你是吉姆')
# else:
#     print('我知道你的名字是%s' % name)


# 几种特殊情况:
# if False:
#     print(1)

# if 200:
#     print(2)
# 原因--->非0--->True       0--->False

# if ' ':
#     print(1)
# 为什么能?  是带有空格的字符串,而不是空字符串
# ' '--->True   空格的字符串--->True

# if '':
#     print(2)
# 原因:# ''--->True   空字符串--->False

#
# if {}:
#     print(3)

# if []:
#     print(3)
# 原因:空字典--->空容器--->False

# if 后面的条件:代码块

# 后面的条件---->
# [],(),{}.None,'',0:False

# if/elif/elif/else
# num = int(input('请输入一个整数:'))
# if num >= 90:    # num >= 90---->条件表达式
#     print('成绩优秀')
# elif 80 <= num < 90:
#     print('成绩良好')
# elif 70 <= num < 80:
#     print('成绩良好')
# elif 60 <= num < 70:
#     print('成绩良好')
# else:
#     print('成绩不合格')



# 特殊情况:
# num = int(input('请输入一个整数:'))
# if num > 60:  # num >= 90---->条件表达式
#     print('成绩优秀')
#     print(2222222)
# elif num > 90:
#     print('成绩良好')
# else:
#     print('成绩不合格')
# 输入98?



# 三元运算符
# x, y, z = 2, 6, 9  # 定义多个变量
# print(x)
# print(y)
# print(z)

# x, y = 2, 7
# x, y = y, x   # 交换了两个变量的值,没有借助中间第三个变量
# print(x)
# print(y)

# x, y = 30, 20
# if x < y:
#     print('小于')
# else:
#     print('大于')

# x, y = 20, 7
# print('小于' if x < y else '大于')


# 循环结构:
# while --->for(常见)
# while:循环
# while 后面是条件表达式
# while 1:    # 1--->True
#     print('哈哈')
#     print('0000')   # 无线循环的效果


# num = 1
# while num < 100:     #   循环的条件判断:num < 100这个条件成不成立
#     num += 1   # 2  5
#     print(num)
#     num = pow(num, 2)  # 4 25
#     print(num)


# 需求:1+2+3+....+99+100   求和
# while循环来实现
# result = 0  # 存放最终结果的变量
# num = 1  # 从1开始
# while num <= 100:
#     # result += num   # ?  第一次循环:  result = 1 + 0 =1+2=3+3
#     result = result + num
#     num += 1  # 间隔处理 2 3 4
# print(result)   # 5050


# 求1,,3,5,7...97+99
# result = 0
# num = 99  # 最大的值
# while num > 0:
#     result += num
#     num -= 2  # 间隔为2 97 95 .... 1>0
# print(result)



# 以上2个求和换成for怎么办?
# 需求:1+2+3+....+99+100   求和
# result = 0
# for num in range(1, 101):  # 包左不包右
#     result += num  # num = 1
# print(result)   # 5050


# 求1+3+5,7...97+99
# result = 0
# for num in range(1, 100, 2):  # 包左不包右
#     result += num  # num = 1
# print(result)   # 2500

# 遍历容器里面的元素的时候for
# range函数不用讲了
# 可迭代对象,迭代器

# for循环代码简洁

# a_dict = {'name': 'ben', 'age': 28}
# for item in a_dict.items():
#     print(item)
# 循环过程中将数据项进行解包
# for key, value in a_dict.items():
#     print(key, value)


# break
# num = 1
# while 1:
#     print(num)  # 1
#     num += 1    # 2,3,4,5,6,7,8
#     if num >= 8:
#         break
# break结束当前循环体,不会再继续判断了


# for num in range(1,9):  # 1,2,3,4,5,6,7,8
#     if num % 2 == 0:     # num是偶数,条件成立--->continue:结束本次循环
#         continue   # 结束本次循环,后面内容不会被执行
#     print(num)  # 1 3 5 7


# 总结:
# break:--->一旦触发,结束整个循环体
# continue--->一旦触发,只是结束了一次循环而已,直接进入到下一次循环继续执行

# 语句的嵌套 (理解一下)
# 伪代码
# if 1:
#     if 2:

# for i in range(9):
#     for j in range(8):

