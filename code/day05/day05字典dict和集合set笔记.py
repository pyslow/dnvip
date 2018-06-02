#! /usr/bin/env python
# -*- coding:utf-8 -*-

'''
author :ben
date : 2018-5-xx
'''

# 1.字典数数据类型dict   (这节课的重点)
# 2.集合数据类型set
# 3.两种数据类型的分析


# 1.字典dict
# 数据项:key:value
# 例子:key:学号(3号学员)---->value:学员(华慧同学):通过学号--->找到学生
# 映射关系表:key------>value(这两部分组成一个数据项)
# 数据项:(key:value)

# list,tuple
# 字典?
# a_list = [1, 2, 3]
# 如果存放某个学员的信息:
# 华慧:这个同学是不是名字,有没有年龄,性别,手机号码,地址
# b_list = ['华慧', 19, '女', 138888888, '北京大街']

# 怎么定义一个字典存放学员的信息:
# a_dict = {'name': '华慧', 'age': 19, 'sex': '女', 'phone': 1388888, 'address': '北京大街'}
# b_dict = {}  # 空字典
# print(type(b_dict))
#
# # list,tuple--->通过索引来访问元素
# # key--->找value
# c_dict = {'name':'haha','name':'hehe'}     # 不可能同时存在两个相同的key
# print(c_dict)
# print(c_dict['name'])   # 注意点

# a_dict = {'name': '华慧', 'age': 19, 'sex': '女', 'phone': 1388888}

# 构造字典对象
# b_dict = dict(name='jim', age=24)
# print(b_dict)
# print(type(b_dict))


# 如何来获取字典里面的元素?
# print(a_dict['name'])
# print(a_dict['phone'])

# 问题:假如取的key不存在怎么办?  会报错
# print(a_dict['address'])

# 怎么增加字典的数据项:
# 原有字典里面没有key:address

# 添加数据项:
# key不存在的时候是---->添加
# a_dict = {'name': '华慧', 'age': 19, 'sex': '女', 'phone': 1388888}
# # a_dict['address'] = '北京大街'   # 添加了一个不存在的key--value
# # print(a_dict)
#
# # key存在---->修改处理
# a_dict['age'] = 26
# print(a_dict)

# list不能作为字典的key?

# 字典key包含的判断 关键字in
# a_dict = {'name': '华慧', 'age': 19, 'sex': '女', 'phone': 1388888}
# print('name' in a_dict)
# print('address' in a_dict)

# py2:内置方法has_key函数
# a_dict = {'name': '华慧', 'age': 19, 'sex': '女', 'phone': 1388888}
# print(a_dict.has_key('name'))

# py3里面没有这个函数


# a_dict = {'name': '华慧', 'age': 19, 'sex': '女', 'phone': 1388888}
# print(a_dict['ass'])  # 会报错--->脚本程序退出了,后面的代码不会被执行

# get方法
# print(a_dict.get('name'))   # get--->获取
# print(a_dict.get('ass'))    # 获取一个不存在的key,没有报错,返回None(找不到这个key)
# get--->即使访问了不存在的key,也不会报错,代码的健壮性(重要)

# print(1111111)

# 如果获取一个字典的value,假如key不存在,返回一个默认的值(None)
# a_dict = {'name': '华慧', 'age': 19, 'sex': '女', 'phone': 1388888}
# print(a_dict.get('ass', '这个key不存在'))  # get函数第一个key,第二个参数是默认值(可以灵活来指定)


# 字典里面数据项的操作:
# a_dict = {'name': '华慧', 'age': 19, 'sex': '女', 'phone': 1388888}
# list中pop方法--->弹出元素
# b = a_dict.pop('name')   # 返回值--->value
# # print(b)
# print(a_dict)
# 字典里面pop方法-->删除字典数据项(key:value都会被干掉# )
# pop方法(参数:key)

# 假设这个key不存在怎么办?
# a_dict.pop('ass')  # 会报错--->key(ass)不存在
# print(a_dict)

# 修改上面的代码:
# b = a_dict.pop('ass', '哈哈,不存在的key')  # 添加了第二个参数(默认值)之后,没有报错
# print(b)
# print(a_dict)  # 避免报错问题
# 需要关注的一些细节问题

# 字典随机删除数据项
# a_dict = {'name': '华慧', 'age': 19, 'sex': '女', 'phone': 1388888}
# # 删除数据项
# a_dict.popitem()    # 字典删除数据项
# # a_dict.popitem()
# # a_dict.popitem()
# print(a_dict)


# 字典数据清空
# 一次数据项全部删除掉
# a_dict = {'name': '华慧', 'age': 19, 'sex': '女', 'phone': 1388888}
# a_dict.clear()
# print(a_dict)   # {}:变成了一个空的字典


# 字典的遍历:
# a_dict = {'name': '华慧', 'age': 19, 'sex': '女', 'phone': 1388888}
# 需求1:遍历字典所有数据项
# for item in a_dict.items():  # 条目--->数据项
#     print(item)
# 需求2:遍历所有的key
# for key in a_dict.keys():  # 条目--->数据项
#     print(key)
# 需求3:遍历所有的value
# for value in a_dict.values():  # 条目--->数据项
#     print(value)


# 有趣的方法
# 1.key存在的情况
# a_dict = {'name': '华慧', 'age': 19, 'sex': '女', 'phone': 1388888}
# b = a_dict.setdefault('name', 'ben')  # 第一个参数是key,第二个参数是默认值()
# print(b)
# print(a_dict)
# setdefault在执行的过程中,如果key存在,就获取对应的value

# 2.key不存在的情况
# a_dict = {'name': '华慧', 'age': 19, 'sex': '女', 'phone': 1388888}
# b = a_dict.setdefault('assss', 'ben')  # 第一个参数是key,第二个参数是默认值()
# print(b)
# print(a_dict)
# setdefault在执行的过程中,如果key不存在,就添加一个数据项


# 字典的更新:
# a_dict = {'name': '华慧', 'age': 19}
# b_dict = {'sex': '女', 'name': 'haha'}
# # # 把第二个字典里面的数据更新到第一个字典里面
# a_dict.update(b_dict)   # 更新了a_dict里面的数据
# print(a_dict)
# print(b_dict)  #  被覆盖掉



# 集合set数据类型
# 容器:不同的对象--->对象不能相同
# 集合set--->重要的特性:对象之间不能相同--->去重复的功能
# a_list = [1, 2, 3, 2, 1]   # 可以出现重复元素
# print(a_list)  # 允许存在重复元素

# 定义set?
# a_set = {}  # 空字典
# print('到底是dict还是set?')

# 空集合set怎么表示?
# b_set = set()   # 定义空的集合set
# print(type(b_set))
# print(b_set)  # <class 'set'>

# c_set = set([])  # 空的集合set
# print(type(c_set))
# print(c_set)


# 集合set元素
# a_set = {1, 2, 3}
# print(type(a_set))

# 去重复的功能
# a_set = {1, 2, 3, 2, 1}
# b_set = set([1, 2, 3, 4, 5, 2, 4])
# # print(type(a_set))
# print(a_set)  # 集合set自动去重复


# 集合set添加元素
# a_set = {1, 2, 3}
# a_set.add(2)   # 已经存在
# print(a_set)

# a_set.add(4)
# print(a_set)

# a_set = {1, 2, 3}
# b_set = {4, 5, 6}
# a_set.update(b_set)   #  和dict一样的
# print(a_set)
# print(b_set)


# 删除元素
# a_set = {1, 2, 3}
# # a_set.remove(3) #z
# # print(a_set)
# # 如何传入的参数不存在怎么办?
# a_set.remove(9)    # 报错:注意点
# print(a_set)


# 清空set
# a_set = {1, 2, 3}
# a_set.clear()  #
# print(a_set)


# 以上删除,清空,添加,更新--->set是可以改变

# 不可改变的set  :frozenset--->不同于刚才的set(改变)
# a_set = frozenset({1, 2, 3})  # 不可改变(重要点)
# 验证下:
# a_set.add(6)   # 会报错


# 判断元素是否存在
# print(8 in a_set)

# 如何删除set本身(区别元素)
# del a_set  #  删除对象

# 集合set的拷贝
# a_set = {1,2,3}
# b_set = a_set.copy()  # copy方法是集合set的方法
# print(b_set)


# 集合之间的运算
# a_set = {1, 2, 3}
# b_set = {4, 5, 6}
# in判断存不存在
# 是否相等
# print(a_set == b_set)
# print(a_set != b_set)

# 包含关系,大小的判断
# a_set = {1, 2, 3}
# b_set = {1, 2, 3, 4, 5}
# print(a_set < b_set)  # <--->包含与被包含
# print(a_set <= b_set)
# # 反过来
# print(a_set > b_set)  # <--->包含与被包含
# print(a_set >= b_set)


# 集合之间的其他运算
# a_set = {1, 2, 3}
# b_set = {1, 2, 3, 4, 5}
# print(a_set & b_set)  # 交集:
# print(a_set | b_set)    # 并集:

# print(b_set - a_set)   # 差集

# 异或运算
# print(a_set ^ b_set)
# print(b_set ^ a_set)


# 两种数据类型的分析:
# list--->单个元素
# dict--->数据项(key:value)

# 内存:
# list--->内存小(1个元素)
# dict--->内存大(key:value)

# list--->可以重复
# dict--->key不能重复,重复的会覆盖,key--->不可改变的对象
# set--->自动去重复,key--->不可改变的对象(相当于字典里面的key)

a_list = [1,2,3,2,1]
print(list(set(a_list)))  # 去掉list重复元素

