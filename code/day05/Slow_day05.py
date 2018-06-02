#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/27 17:46
# @Author  : Slow
# @File    : dn_day05_Slow.py
# @Software: PyCharm

# 1.自己写一个字典:
name_dict = {'name': 'ben', 'age': 22, 'sex': '男'}
#     添加,删除,更新,清空操作
name_dict['address'] = '广西'  # 添加
name_dict.pop('name')  # 删除
xq_dict = {
    'love': '游泳',
    'friend': '小丽'
}
name_dict.update(xq_dict)  # 更新
name_dict['age'] = 18  # 更新
name_dict.clear()  # 清空操作

#
# 2.写两个集合:
num1_set = {3, 5, 1, 2, 7}
num2_set = {1, 2, 3, 11}
#     并分别进行&,|,^,-运算
print(num1_set & num2_set)
print(num1_set | num2_set)
print(num1_set ^ num2_set)
print(num1_set - num2_set)
#
# 3.整数字典:
num_dict = {'a':13,'b':22,'c':18,'d':24}
#     按照dict中value从小到大的顺序排序
# num_list= {value:key for key,value in num_dict.items() }
num_dict=sorted(num_dict.items(),key = lambda x:x[1],reverse = False)
print(num_dict)