#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/26 11:00
# @Author  : Slow
# @File    : dn_day04_Slow.py
# @Software: PyCharm

# 第一题:
num_list = [[1,2],['tom','jim'],(3,4),['ben']]
#  1. 在’ben’后面添加’kity’
# num_list[3].append('kity')
#  2. 获取包含’ben’的list的元素
# for ite in num_list:
#     if 'ben' in ite:
#         print(ite)

#  3. 把’jim’修改为’lucy’
# num_list[1][1]='lucy'
# print(num_list)
#  4. 尝试修改3为5,看看
# num_list[2][0]=5 因为是元组不能修改

#  5. 把[6,7]添加到[‘tom’,’jim’]中作为第三个元素
# num_list[1].append([6,7])
# print(num_list)
#  6.把num_list切片操作:
#       num_list[-1::-1]
print(num_list[0::2])
print(num_list[-1::-1])


# 第二题:
numbers = [1,3,5,7,8,25,4,20,29]
# 1.对list所有的元素按从小到大的顺序排序
numbers.sort()
print(numbers)
# 2.求list所有元素之和
numsum=0
for num in numbers:
    numsum+=num
print(numsum)
# 3.将所有元素倒序排列
numbers[-1::-1]