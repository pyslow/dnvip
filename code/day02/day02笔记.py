#! /usr/bin/env python
# -*- coding:utf-8 -*-

'''
author :ben
date : 2018-5-xx
'''

# 基本数据类型之Number
# 运算符
# 标准输入和输出
# 字符串

# 标识符:
# 中画线:-      下画线:_
# 数字,字母,下画线
# 数字不能开头
# 数字,字母,下画线以外的特殊字符   #  $ @
# 不能使用python关键字
# 类名:      class Person():   pass    首字母大写
# 函数名:     def work():  pass       小写:如果两个单词,可以my_fun():  myfun()




# 基本数据类型之Number
# 1.整数
# 早期版本:长整数(long):理论上可以无限大,受限于电脑的内存大小,虚拟内存大小
# 在py3--->没有长整数一说,都是整数int
# num = 9
# print(type(num))    # 类型:int
# 内置函数type:---->查看对象的类型
# print(type('ben'))   # 类型:str
# 经常使用这个type内置函数

# 十进制的表示方式:
# 十六进制的方式:0xff00:以0x(不是ox)
# 八进制方式:0off00:以0o开头(不是两个0)
# 二进制:0b1000:以0b开头(不是字母ob)
# python--->内置进制转换函数
# a = hex(16)
# print(a)     # 十六进制
#
# b = oct(16)
# print(b)   # 八进制
#
# c = bin(16)  # 二进制
# print(c)

# 八进制的表示方式:
# 2.x--->有两种表示方式:  01000,0o1000
# 3.x--->只有一种形式:0o1000

# 学习py3

# print(1000000)
# print(2+3)


# 2.浮点数据:小数
# print(3.14)
# print(type(5.66))   # 类型:float


# py3下面:
# print(10/3)    # 3.3333333333333335
# print(type(10/3))

# print(9/3)    # 3.0
# print(type(9/3))  # float
# py3下面的调整:结果是浮点小数(除法运算:/)    注意点:print(3/3)
# print(type(3/3))

# print(10//3)  # 地板除:取整
# print(type(10//3))   # 类型:int
#
# print(9//3)

# 除法和地板除的区别:

# print(20 % 5)    # 求余数--->商是4,但是余数是0(%--->求余运算)
# print(20 % 6)      # 求余数--->商是3,但是余数是2(%--->求余运算)

# 科学计数法:
# print(3.14e9)   # 3.14乘以10的9次方
# print(type(3e8))  # 3乘以10的8次方--->应该是整数 (都是浮点)
# float
# print(type(3))   # int
# print(type(3.))  # float


# 复数数据类型:(用得很少:科学计算,工程学)
# a = 3 + 4j
# print(type(a))   # complex:实部和虚部

# b = complex(2, 5)   #
# print(type(b))   # complex
#
# print(b.real)  # complex对象的实部
# print(b.imag)  # complex对象的虚部


# 布尔数据类型:只有两个值:True(正确),False(错误)
# 书写的时候要首字母大写 (错误的写法:true,false)

# 条件表达式:and  or not

# if 2 and 3:   # 2 and 3-->这部分是条件表达式,如果为True:执行后面的代码
#     print(111)

# if 2 and 0:   # 2 and 3-->这部分是条件表达式,如果为False:不执行后面的代码
#     print(222)

# or:只有一个条件成立,最终的结果就为True
# 0--->False     非0---->True  (2,3,5,6,1)


# 运算符:
# /
# //
# %


# 不等于的运算符:
# py2:第一种:<>--->2<>3       2!=3
# py3:只有一种:2!=3
# print(2<>3)  # 在py3下语法不通过
# print(2!=3)

# 其他:
# print(2+3)
# print(9-4)
# print(2*3)  # 乘法运算符:星号表示

# 幂次方运算
# print(3**3)  # 幂次方:两个星号连写
# print(pow(2, 3))   # 内置函数求
# print(pow(3, 3))


# 比较运算符:
# print(2 > 3)
# print(5 > 3)
# print(3 <= 3)
# print(3 <= 5)
# print(5 >= 3)
# print(3 == 3)  # 不等于  2!=3
# 问题:一个=和==什么区别?  一个=是赋值运算符

# 问题2:
# print(3 < b)

# 问题3:
# print(4 < 'b')   # 数据类型不兼容    字符串和整数是不能比较的

# 问题4:
# print(4 < 'b')  # 在2.x版本下面去执行又会怎么样?   True


# 其他运算符
# =
# ==
# +=
a = 3
# a +=2
# print(a)  # +=--->先加再赋值

# -=---->先减再赋值
# a-=1
# print(a)

# *=     /=    //=    **   %=  都是一样的道理
# a **= 2
# print(a)


# 成员运算符
# in--->存在于(是成员之一)
# not in---->不存在于(不是成员之一)
# a_list = [1, 2, 3, 4]
# print(1 in a_list)  # 成立
# print(1 not in a_list)  # 加上否定-->不成立
# 容器--->可以存放很多个元素(对象)


# 逻辑运算符
# not/and/or
# print(not 1)  # 1--->True
# print(not False)
# print(1 and 0)
# print(True and True)
# print(True and False)  # and:连接的两个条件表达式都是True,最终的结果才为True
#
# print(True or False)   # or:连接的两个条件表达式只要其中有一个为True,最终的结果就为True
# print(False or True)

# if -3:     # 看是不是0:-3不是0--->True
#     print(1111)

# if 0:     # 看是不是0:-3不是0--->True
#     print(1111)

# if False:     # 看是不是0:-3不是0--->True
#     print(1111)

# print(~3)   # -(3+1)=-4
# print(~-4)  # -(-4+1)=-(-3)=3

# print(2 ^ 3)
# print(2 & 3)    #底层算法
#                   # 0010
#                   # 0011
#                   # 0010  --->2
#
# print(2 | 3)
# 0010
# 0011
# 0011  ---> 3

# print(5 & 7)   # 位运算

# print(2 << 2)  # 2 * 2**2= 2*4 =8

# print(2 >> 2)    # 2 / 2**2 = 2/4=(取整处理,截取整数)



# 标准输入和输出
# 输出
# print('我是小明')
# print('我是haha', 2, 'ben')

# 输入函数input的用法
# 以py3为例:  # input内置函数
# 什么叫内置:安装好python之后就可以直接在代码使用
# num = input('请输入一个整数:') # 括号里面的参数:友好的提示作用,提示信息
# print(type(num))   # 字符串str
# print(num)
# python3--->input内置函数返回值都是字符串

# num = input('请输入你的年龄:') or '28'
# print(num)
# 当什么都不输入的时候--->返回默认值or后面的默认值

# num = input('请输入你的年龄:') or '28'
# num = int(num)  # 类型强转
# print(type(num))


# num = int(input('请输入你的年龄:') or '28')
# print(type(num))
# print(num)
# input--->返回的永远是字符串


# 问题:
# num = int(input('请输入你的年龄:'))
# print(num)   # input-->字符串--->整数的过程中('9')   'abc'--->整数(不行)

# py3--->
# py2--->input/raw_input(返回也是字符串)两个函数

# 类型问题:
# print('abc' + 9)   # 字符串不能和整数做+运算
# print('ab' * 3)  # 重复几次


# 字符串
# 如何定义字符串
# 多种形式:
# 单引号:
# print('我是大笨蛋', 'ben')

# 双引号:
# print("我是双引号")

# 有单引号?为什么又双引号?
# print("tom is 'cool'")  # 字符串的嵌套

# 三引号:
# a = '''
# 'my name is ben',
# "haha",
# 'hehe'
# '''
# print(type(a))  # 也是字符串
# print(a)

# 三引号字符串有什么用?
# 优势:保持原样输出;嵌套单,双引号
# 原样输出?
# a = '''
#       'my name is ben',
#            "haha",
#                  'hehe'
# '''
# print(a)

# 单,双,三引号都可以定义字符串

# 三引号其他用法?
# 三引号--->解释说明
# 脚本文件的文档字符串
# print(__doc__)  # 内置__doc__属性:当前脚本文件的注释说明(文档字符串--->解释说明)


# class Person():
#     '''
#         定义一个人的模型类
#     '''
# print(Person.__doc__)  # 类的文档字符串(说明这个类是干什么用的)


# 函数的文档字符串
# def run():
#     '''
#         求最大值
#     :return:
#     '''
# print(run.__doc__)  # 函数的文档字符串--->对函数功能的解释说明
# 文档字符串---->三引号字符串(解释说明的功能)
