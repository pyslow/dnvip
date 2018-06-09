#! /usr/bin/env python
# -*- coding:utf-8 -*-

'''
author :ben
date : 2018-1-xx


'''

# 本节课知识点:
# 1.字符串的连接
# 2.转义字符
# 3.原始字符串
# 4.如何来注释代码
# 5.字符串的格式化
# 6.编码问题
# 7.python2和python3字符串的区别
# 8.编码和解码问题
# 9.str--->bytes区别
# 10.字符串的长度
# 11.字符串的基本处理




# 具体知识点:
# 1.# 1.字符串的连接
# print('tom', 1, 3.14, 'boy')
# a_str = 'tom' ' is' ' good' ' boy'
# print(a_str)

# b_str = 'jim' + ' is' + ' good' + ' boy' + '\n' + 'and' + ' you'  # 加号--->字符串的拼接处理
# print(b_str)
# \n:换行符  (注意点)

# c_str = 'my name' \
#         'is ben'
# print(c_str)
# \:这个用法是续行符:当前第一字符串还没有完   (注意点)

# +:字符串拼接处理
# 换行符和续行符



# 2.转义字符
# print('what's your name')  # 报错了(语法不通过)  单引号中嵌套单引号
# 原因?
# 怎么解决?
# 方案1:字符串的嵌套
# print("what's your name")  # 双引号中间嵌套单引号
# 方案2:转义字符
# print('what\'s your name')  # 去特殊化处理
# 转义字符有什么用?
# path = 'f:\py\now'   # 电脑上文件夹路径
# print(path)  # 打印出来不是我们想要的效果,完整的路径
# 完整路径怎么弄?
# path = 'f:\py\\now'  # 增加一个转义字符:去特殊化(特殊的换行符) \\n--->后面的\n去特殊化
# print(path)    # f:\py\now  ---->这个才是我们的要的路径

# print(r'what \n your name')  # 原始字符串  转义字符串去特殊化


# 3.原始字符串
# content = 'i\'m study \\n python' # 换行符   \\n--->后面的\n去特殊化
# print(content)
# 这种写法有点不优雅,可读性不好
# 原始字符串--->
# content = r"i'm study \n py\n thon"  # r'':告诉你这个原始字符串
# # 原始字符串:转义字符串\--->不具有特殊化(\不再具有特殊化:变成一个普通的\)
# print(content)

# 最流行的pythonweb 网络框架   django:路由的配置大量的使用原始字符串


# 4.如何来注释代码
# 注释代码的符号:#
# print(111111)   #--->之后的代码不再被解释执行
# java里面多行注释:/*.........*/(这是java里面,不是python)

# print(111)
# print(222)
# print(333)
# 注释快捷键:ctrl+/    ()

# '''
#     多行注释
# '''

# 还有一些特殊的注释:
# ! /usr/bin/env python   解释说明的功能  linux下面python解释器的路径,win下没说明用,做预准备
# -*- coding:utf-8 -*-     # 当前脚本文件--->编码格式为utf-8


# 5.字符串的格式化:更加灵活
# name = 'ben'
# age = 28
# # 字符串格式化的第一种方式: 占位符:%s  可读性稍好
# text = '%s is %s years old' % ('tom', 29)  # % 后面传入参数
# # 字符串里面使用了占位符--->根据参数
# print(text)

# 第二种方式:  占位符:{}   稍高一点点
# text = '{0} is {1} years old'.format('tom', 22222)  # 索引从0开始
# print(text)

# print('ben is 28')



# 6.编码问题(了解)
# 一串二进制的序列
# ASCII编码:外国人--->大小写英文字母,数字,一些符号,一共127个字符
# a,z,A,Z,=....  127
# 一个字节(byte)--->8位--->127个字符,全部表示完   a

# 其他国家:以中国为例:ASCII编码:我,这个问题怎么解决?  (万国码)
# unicode编码:全世界所有语言统一到一套码表
# unicode编码:2-4个字节(最少2个字节)

# 原有ASCII编码中127个字符,原来一个字节表示的,unicode编码要用2个字节表示?浪费了内存

# 怎么解决?

# utf-8编码表:unicode编码切一刀,一分为2,能够用一个字节表示的就用一个字节,不能一个的用多个字节表示

# gbk编码:gb2312的扩展,中文不能一个字节表示


# 7.python2和python3字符串的区别
# python2--->str,unicode字符串
# 演示之前,切换到python2.7下面了
# a_str = '哈哈'       # str字符串
# print(len(a_str))   # 长度是6     求长度字节数(3*2=6个字节)
#
# b_str = u'哈哈'        # unicode字符串  (注意2.x  u标记:unicode字符串)
# print(len(b_str))    # 长度是2   求长度是字数

# 切换回3.6下面
# python3.x--->只有一种字符串:unicode字符串
# a_str = '哈哈'  # unicode字符串
# 不同版本之间的差异,不要混为一团


# 为什么要转换编码:内存是unicode编码,保存到硬盘或者需要传输的时候---->比如:转换为utf-8编码
# 编码转换函数:encode,decode
# python项目--->utf-8编码

# a_str = '我是中国人'
# b_str = a_str.encode('utf-8')  # 编码过程:unicode字符串---->bytes数据类型
# print(b_str)  # python二进制:b'\xe6\x88\x91\xe6\x98\xaf\xe4\xb8\xad\xe5\x9b\xbd\xe4\xba\xba'
# # b标记--->byte
# print(b_str.decode('utf-8'))   # 解码过程:



# 9.str--->bytes区别
# str:文本字符串         ''
# bytes:二进制类型      b''
# a_byte = bytes([1, 2, 3])
# print(a_byte)  # b'\x01\x02\x03'
# print(type(a_byte))  # bytes

# b_byte = bytes('ben', 'ascii')
# print(type(b_byte))  # bytes
# print(b_byte)
#
# # 普通文本字符串:str
# a_str = 'ben'
# print(a_str)


# 字符和整数的转换:
# ord内置函数
# print(ord('A'))   # A--->对应的整数  65    65---- A
# print(ord('a'))   # 97    97----a
# 按照什么规则:ascii编码

# 整数--->字符  ,和上面反的
# print(chr(65))
# print(chr(97))


# python内置len函数:个数
# print(len('ben'))
# print(len('我是大坏蛋'))

# print(len('聪明'.encode('utf-8')))   # 在bytes中是字节个数


# 字符串的赋值的过程
# a_str = 'ben'
# b_str = a_str
# print(b_str)


# 字符串的截取:
# a_str = 'pythonweb'   # 索引是从0开始,-1就是从右边倒过来数
# print(a_str[-1])  # 按照索引取值
# print(a_str[0])
# print(a_str[1:3])  # y--1  t--2 h--3 :包左不包右  yt
# print(a_str[-1:-2:1])  # 步长方向的原因  切片后面会讲
# 切片的范围:[-1:]  从右往左切,再看步长方向(如果为负:右边-->左边)

# 后面会专门讲


# 去掉两端空格:
# a_str = '     pythonnweb          '  # 两边都有空格
# print(a_str)
# # 去掉两端空格:
# print(a_str.strip())  #  strip:去掉两端空格
# # 只去掉左边空格怎么办?
# print(a_str.lstrip())  # 去左边空格
# # 只去掉右边空格?
# print(a_str.rstrip())  # 去右边空格


# a_str = ',ben.'
# print(a_str.lstrip(','))  #  l:left(左边)
# print(a_str.rstrip('.'))  #  r:right(右边)

# b_str = '.@cici#!'  # 去掉指定字符
# c_str = b_str.lstrip('.@').rstrip('#!')
# print(c_str)


# 拼接+
# 字符串的重复
# print('=%'*10)  #


# 字符串的替换:replace
# a_str = 'my name is ben'
# b_str = a_str.replace('ben', 'cici')  # my name is cici
# print(b_str)


# 字符串的查找,建议使用find来
# a_str = 'my name is ben'
# print(a_str.index('ben'))  # 起始索引
# print(a_str.index('cici'))  # 如果不存在,会报错
#
# print(a_str.find('ben'))  # 如果存在,结果就是起始索引
# print(a_str.find('cici'))  # 如果不存在,返回-1,不会报错

