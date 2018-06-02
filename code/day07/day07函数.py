#! /usr/bin/env python
# -*- coding:utf-8 -*-

'''
author :ben
date : 2018-5-xx
'''


# 为什么要使用函数?
# 小明的妈妈会做红烧鱼
# 小明要吃红烧鱼?--->自己按照菜谱一步步的去做红烧鱼
# 后天,小明又想吃红烧鱼?---->自己按照菜谱一步步的去做红烧鱼(再来一次)

# 做红烧鱼--->一段代码块,写一次
# 再写一次(把之前的代码复制一次)

# 做红烧鱼的功能---->封装到一个对象里面
# 每一次要去红烧鱼的时候,给这个对象发信息,告诉他要吃红烧鱼

# 功能代码组织到一个对象里面(函数)   20行代码-->复制,不是重复写,封装到函数里面
# 下次,不再重复写代码,给这个函数发信息,给我执行这个功能


# 功能的封装--->提高了代码的复用性

# 怎么定义一个函数?
# def--->专门定义函数

# def 函数名(参数):
#     # 函数内的逻辑代码

# 定义函数
# def run():
#     #pass    # 代码块内什么都不做,我们需要使用占位符
#
# # 执行函数:函数名()
# run()

# def fun():
#     print(1)
#     print(2)
# a = fun()   # 有没有返回值?如何验证
# print(a)     # 本质上是有返回值:None
# 函数定义没有显示的return,默认返回None

# def fun(x, y):
#     return x * y
# a = fun(2, 3)  # 有没有返回值?如何验证
# print(a)

# 这样定义函数能不能?
# def run(x,(y,z)):   #
#     pass
# run()
# 这样定义函数在python3.x是不行?
# 在3.x去掉了元组参数的解包
# 在python2.x是可行
# 不同版本之间的兼容性-->调整

# 标识符
# 定义函数,函数名的定义:
# 对于函数名要规范
# 函数名是小写

# def fun():  # 函数名是fun,  全是小写
#     pass

# def get_age():  # 函数名有两部分,都小写,中间以下划线连接
#     pass

# def FUN():   # 非要全大写,虽然可以执行
#     print(111)
# FUN()  # 也可以


# 默认是None
# 函数执行之后能不能返回多个对象(多个值)?

# def get_numbers(x, y):
#     a = x + 2
#     b = y * 2
#     return (a, b)  # 将多个值(对象)--->打包进一个元组作为返回
#
#
# # num = get_numbers(2,3)
# # print(type(num))   # <class 'tuple'> 元组数据类型
# # print(num)  # (4, 6)--->打包返回
# # 解包
# c, d = get_numbers(2, 3)
# print(c)
# print(d)


# def fun(x, y, z):
#     return x + 1, y * 2, z + 3  # ?  并没有显示打包成元组


# result = fun(2, 3, 4)
# print(type(result))   # <class 'tuple'>
# a, b, c = fun(2, 3, 4)
# print(a)
# # print(b)
# print(c)
# 需求:如果只需要其中某部分数据怎么办?
# 注意写法:
# a, b, _ = fun(2, 3, 4)
# print(a)
# print(b)

# 1和3怎么办?
# a, _, c = fun(2, 3, 4)
# print(a)
# print(c)
# 返回多个对象,可以只接收部分数据


# 函数的参数的类型和个数?
# def fun(x):   # 参数的个数
#     if isinstance(x,int):    # 传递进来的参数的类型是不是整数
#         print('整数')
#     elif isinstance(x,float):
#         print('小数')
# # fun(2,3)  # 执行的时候参数个数要对应
# # fun() takes 1 positional argument but 2 were given
# # fun(9)
# fun(3.14)  #
# 两个知识点:1.参数个数要对应    2.判断传入的参数的类型

# isinstance:内置函数:对类型的判断


# 全局变量和局部变量
# num = 9     # 全局变量,在函数外
# def run():    # 只是定义了函数,但是并没有执行函数
#     # num = 100    # 局部变量,是在函数体内部(局部范围)
#     print(num)   # ? 100    这个打印语句是在函数内-->执行函数
# # print(num)   # ?         9  全局变量num
# run()   # 开始执行函数


# 休息十分钟

# 变量作用域legb
# locals:局部的变量
# enclosing function:外部函数空间中的变量
# globals:全局变量
# __builtings__:内置中
# max = '全局'              # g
# def run():
#     # max = '外层中'        # e
#     def fun():
#         # max = '内层中'    # l
#         print(max)
#     return fun
# run()()
# 内层中
# 注释153行后,外层中
# 注释151行后,全局
# 注释149行后,使用内置函数max对象  <built-in function max>
# 检索变量的顺序:l--->e---->g----->b (重点)



# 看一个例子:
# def fun(s=[]):  # 定义的时候是空的list
#     print(id(s))
#     s.append('王八蛋')
#     return s

# print(fun([1,2,3]))  # 执行正常  [1,2,3]-->'王八蛋'
# # [1, 2, 3, '王八蛋']
# print(fun([1, 2, 3]))   # [1, 2, 3, '王八蛋']
# print(fun([4, 5, 6]))  # [4, 5, 6, '王八蛋']
# 特殊情况:
# print(fun())   # []-->追加'王八蛋'  ['王八蛋']
# # 内存地址值:41278920
# print(fun())   # []-->追加'王八蛋'  ['王八蛋'] ?为什么['王八蛋','王八蛋']这个结果?
# 内存地址值:41278920
# 指向的同一个list对象
# 定义fun函数,默认参数是一个可变的对象([]--->是可变对象)

# 定义函数的时候参数是可变对象的情况(注意点)


# python默认参数
# def fun(x, y=9):  # 定义函数的时候出现默认值
#     return x + y
# print(fun(1))  # 可以只传入一个参数  x = 1 y=9(默认值)
# print(fun(2, 3))      # x = 2 ,y = 3会覆盖默认值9

# def fun(y=9,x):  # 定义函数的时候出现默认值
#     return x + y
# print(fun(1))  # 可以只传入一个参数  x = 1 y=9(默认值)
# print(fun(2, 3))
# 默认参数情况下:位置参数在前,默认参数在后 (重点)

# 关键字参数:
# def fun(x, y, z=8):
#     return x + y + z
# # print(fun(2,3))   #  会使用默认值8
# # print(fun(2,3,4))
# # 关键字参数用法
# print(fun(z=2, x=3, y=4))  # 执行的时候参数打乱了,不用担心调用的参数顺序



# 动态收集参数
# def say_hello(message, *name_list):  # message-->说话的内容
#     for name in name_list:
#         print(message, name)
# say_hello('我喜欢你', 'tom', 'jim', 'lucy', 'ben', 'haha', 'hehe')
# 动态收集参数


# 特殊的语法:一个星号:对象就是元组
# def fun(*nums):  # 定义了一次
#     # print(type(nums))  #<class 'tuple'>
#     sum = 0
#     for i in nums:  # 遍历出元组里面每一个元素
#         sum += i
#     print(sum)
#     return sum
#
# fun(1, 2, 3)  # 个数可以不限
# fun(1, 2)
# fun(1, 2, 3, 4, 5, 6)


# 两个星号:
# def fun(**kwargs):  # 两个星号之后的kwargs--->字典对象
#     if 'name' in kwargs:
#         print('haha存在')
#     if 'age' in kwargs:
#         print('22存在')
# fun(name='haha', age=22)  # 所有的数据项-->收集进一个字典里面
# fun(name='haha', age=22, sex='男')


# 匿名函数:
# 就是没有名字的函数--->本质上还是一个函数对象
# def run():  # 函数名(函数引用--->拿到函数的对象)
#     pass
# 没有的名字的函数--->没有函数引用--->不能多次使用函数对象,一般在定义的地方使用一次

# 关键字lambda--->定义匿名函数
# lambda
# a = lambda x, y: x + y
# print(type(a))   # <class 'function'> 方法对象
# 当然可以执行
# print((lambda x, y: x * y)(2, 3))
# (lambda x, y: x * y)--->函数(2,3)

def run(func, x, y):  # func--->方法对象
    return func(x, y)

# 执行之前要先定义一个函数对象进行传递
print(run(lambda x, y: x + y, 3, 4))  # lambda x,y:x+y--->func

# 注意点:
# 1.匿名函数--->没有名字
# 2.关键字lambda
# 3.匿名函数返回的对象--->方法
# 4.匿名函数的用法

# 都可以使用匿名:没有函数的引用而已


# 一个星号--->元组
# 两个星号--->字典


# 关键字def
# 函数名命名的规则
# 参数的个数对应,类型
# 占位符pass
# 默认的返回值,返回多个值
# 默认参数,关键字参数,动态收集参数    (重点)
#
