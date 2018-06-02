#! /usr/bin/env python
# -*- coding:utf-8 -*-

'''
author :ben
date : 2018-1-xx
'''

# 字符串的比较
# print('abc' < 'bb')  # True
# print('ab' < 'aba')
# print('ab' <= 'abc')
# print('z' > 'w')
# print('tth' >= 'abc')
# print('hot' == 'hot')
# print('hot' != 'abc')


# 判断字符串是否存在(关键字in来判断)
# a_str = 'ben'
# print('a' in a_str)
# print('e' in a_str)
# print('be' in a_str)


# index函数(报错),find函数(-1)

# print(len('ben'))  # len内置函数求字符串的长度

# 大写和小写如何转换
# a_str = 'PYTHON'
# b_str = a_str.lower()
# print(b_str)
# c_str = b_str.upper()
# print(c_str)


# 原来大写-->小写,原来小写的--->大写
# a_str = 'PYthon'
# b_str = a_str.swapcase()
# print(b_str)

# a_str = 'python'
# b_str = a_str.title()  # 标题   首字符大写
# print(b_str)  # Python

# a_str = 'my name is haha'
# b_str = a_str.title()   # 每一个单词的首字母都大写了
# print(b_str)

# a_str = 'ben'
# a_str = 'my name is haha'
# b_str = a_str.capitalize()  # Ben
# print(b_str)
# 这两个函数的区别?

# a_str = 'person'
# b_str = a_str[::-1]  # 步长  --->颠倒
# print(b_str)


# 字符串的分割:
# a_str = 'my name is haha'
# b_list = a_str.split()  # split:切割函数-->返回结果是一个list
# print(b_list)

# a_str = 'my:name:is:ben'
# b_list = a_str.split(':')
# print(b_list)

# 字符串的拼接:+
# a_list = ['my', 'name', 'is', 'hehe']
# b_str = '8'.join(a_list)
# print(b_str)


# 字符串的对其(填充)方式:
# a_str = 'python'
# print(a_str.ljust(10, '$'))  # 第一个参数:长度  第二个参数:不够补充字符
# print(a_str.rjust(10, '$'))
# print(a_str.center(10, '9'))  # 中间


# 编码:
# encode,decode函数

# 判断字符串以什么开头,以什么结尾
# a_str = 'student'
# print(a_str.startswith('s'))
# print(a_str.startswith('stu'))
# print(a_str.startswith('sto'))

# print(a_str.endswith('tr'))
# print(a_str.endswith('ent'))


# 判断字符串是数字还是字符等等操作
# print('haha009'.isalnum()) # 数字或者字符组成
# print('123'.isalpha())  # 全字符判断
# print('hehe'.isalpha())

# 判断数字
# print('99'.isdigit())

# 判断是空格
# print(''.isspace())
# print('   '.isspace())


# 判断大写,小写
# print('hahA'.islower())
# print('haha'.islower())

# print('HEEE'.isupper())
# print('HEgE'.isupper())

# print('My Name Is BeN'.istitle())
# print('My Name Is Ben'.istitle())
# print('My name is ben'.istitle())


# 字符串中某个字符出现的次数
# a_str = 'ben like haha'
# print(a_str.count('a'))
# print(a_str.count('w'))
# print(a_str.count('ik'))


# a_str = 'my name is ben'
# print(a_str.rindex('e'))
# print(a_str.rfind('e'))



# list和tuple:列表和元组(容器:里面可以放多个元素)
# 1.list
# 2.tuple
# 3.区别
# 4.切片

# 1.
# list---->[]
# 可改变
# 怎么样定义list
# a_list = [1, 2, 3, 'ben', 3 + 4j]
# print(a_list)
# b_list = list('haha')
# print(b_list)

# list的长度
# a_list = [1, 2, 3, 'ben', 3 + 4j]
# print(len(a_list))  # 内置len函数

# 从容器里面取出某一个元素
# a_list = [1, 2, 3, 'ben', 3 + 4j]
# print(a_list[4])
# print(a_list[3])

# list获取元素的时候索引越界的问题?
# a_list = [1, 2, 3, 'ben', 3 + 4j]  # 0,1,2,3,4
# print(a_list[10])  # 索引越界


# 如何取list里面最后一个元素
# a_list = [1, 2, 3, 'ben', 3 + 4j, 44, 5, 5, 6, 67, 777]
# print(a_list[4])
# print(a_list[len(a_list)-1])  # 有点麻烦?

# 其他便捷方式:负索引
# print(a_list[-1])
# print(a_list[-2])

# 添加元素
# a_list = [1, 2, 3, 'ben', 3 + 4j, 44, 5, 5, 6, 67, 777]
# a_list.append('lucy')  # 末尾追加
# a_list.append(3.199)
# print(a_list)

# 问题:永远在最后面?如何要插入到中间的位置?
# a_list.insert(3, 'haha')  # 第一个插入的位置  第二个参数插入的元素
# print(a_list)

# 删除元素
# a_list = [1, 2, 3, 'ben', 3 + 4j, 44, 5, 5, 6, 67, 777]
# 把最后一个元素弹出来,相对于原有的列表(删除了一个元素)
# b = a_list.pop()  # 弹出最后一个元素
# print(b)
# print(a_list)

# 怎么样删除指定位置的元素?
# a_list = [1, 2, 3, 'ben', 3 + 4j, 44, 5, 5, 6, 67, 777]
# a_list.pop(-2)  # 这个-2是索引
# a_list.pop(0)
# print(a_list)

# 另外删除元素的方式
# a_list = [1, 2, 3, 'ben', 3 + 4j, 44, 5, 5, 6, 67, 777]
# a_list.remove('ben')  # 移除(参数是元素本身)
# print(a_list)

# 元素的替换
# a_list = [1, 2, 3, 'ben', 3 + 4j, 44, 5, 5, 6, 67, 777]
# a_list[3] = 'jim'  # [1, 2, 3, 'jim', (3+4j), 44, 5, 5, 6, 67, 777]
# a_list[-1] = 'hehe'   # [1, 2, 3, 'jim', (3+4j), 44, 5, 5, 6, 67, 'hehe']
# print(a_list)


# list的嵌套
# a_list = [1, 2, 3, [4, 5]]
# a_list[3][0] = 9  # [1, 2, 3, [9, 5]]
# a_list[3][1] = 0  # [1, 2, 3, [9, 5]]
# print(a_list)


# 元组tuple  ---->()  容器
# a_tuple = (1, 2)
# print(type(a_tuple))
# 求元组的长度
# print(len(a_tuple))

# 正索引
# a_tuple = (1, 2, 3, 4)
# print(a_tuple[0])
# print(a_tuple[3])
# 负索引
# print(a_tuple[-1])

# 元组特殊情况:当元组里面只有一个元素的时候
# a_tuple = (1)
# print(type(a_tuple))  # <class 'int'>
# 强制规定:当元组里面只有一个元素的时候,一定要加上,
# 正确写法:
# a_tuple = (8,)
# print(type(a_tuple))  # <class 'tuple'>


# list--->定义好之后,可以改变里面的元素
# tuple--->定义好之后,就不能改变里面的元素
# a_tuple = (1, 2, 3)  # 定义元组
# a_tuple[-1] = 9
# print(a_tuple)   # 元组里面的元素不能修改(添加,删除,修改都不能)
# 添加,删除,修改都无效
# a_tuple = ()
# print(len(a_tuple))
# print(type(a_tuple))  # <class 'tuple'>  这个元组里面没有元素而已

# 元组也可以嵌套,和list一样


# 区别:
# 相同点:容器,都可以放很多元素,都有索引的概念(顺序),通过for循环来迭代,元素的类型都可以不相同
# 都支持负索引,切片,获取元素

# 不同点:
# list定义之后可以改变你,而元组定义之后不能修改

# list:万能list,还要元组干嘛?
# 只能使用三个固定的苹果,橘子,香蕉


# list和tuple--->获取每一个元素
# a_list = [1,2,3,4]
# for i in a_list:
#     print(i)

# a_tuple = (1,2,3,4)
# for i in a_tuple:
#     print(i)


# a_list = ['haha','ben','cici']
# for index,item in enumerate(a_list,9):
#     print(index,item)


# list的排序
# a_list = [2,5,3,6]
# b = a_list.sort()  # 有没有返回值
# print(b)      # 只有排序功能,但是没有返回值
# print(a_list)

# a_list = [2,5,3,6]
# a_list.sort(reverse=True)  # 有没有返回值
#      # 只有排序功能,但是没有返回值
# print(a_list)    # [6, 5, 3, 2]   --->reverse决定


# 内置sorted函数排序
#
# list的方法,一个内置放,一个有返回值,一个没有返回值


# 切片
a_list = [1, 2, 3, 4, 5, 6, 7, 8]
# print(a_list[0:3:])  # 默认步长是1(不是-1),包左边不包右边
# print(a_list[-2:])
# print(a_list[-3:-1])  # 第三个参数没给,默认1
# print(a_list[0::2])
# print(a_list[-1:-4])   # 怎么是空的?  -1:-4:1  -1:-4(方向是右-->左)  步长:默认1(从左往右)
# 获取不到元素
# 分析出切片的三个参数:分析清楚,第一个参数起始索引,第二个参数是结束索引,第三个参数是步长
# 如果第三个参数是正数:(左-->右)  如果是负数:(右-->左)


print(a_list[-1:-4:1])   # 第三个参数没有给,默认步长1(如果是1可以不写)
# -1:-4(方向是右-->左)  步长:默认1(从左往右)
# 步长:1.看正(左-->右)   负(右-->左)
# 步长:看数值: 1-->每个都切    2:要间隔一个   3:要间隔2个