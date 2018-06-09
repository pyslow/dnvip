#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/7 20:31
# @Author  : Slow
# @Site    : 
# @File    : slow_day09.py
# @Software: PyCharm

# 1.a_list = [1,2,3,2,2]
#    删除a_list中所有的2,注意是所有的2
# a_list = [1,2,3,2,2]
# while 2 in a_list:
#     a_list.remove(2)
# print(a_list)
#
# 2.写一个猜数字的游戏,给5次机会,每次随机生成一个整数,然后由控制台输入一个
#    数字,比较大小.大了提示猜大了,小了提示猜小了.猜对了提示恭喜你,猜对了.
#     退出程序,如果猜错了,一共给5次机会,5次机会用完程序退出.
#
import random

number=random.randint(1,50)
print(number)
for i in range(1,6):
    in_num=int(input('请输入你猜测的数字1-50：'))
    if in_num < number:
        print('您猜小了。')

    elif in_num > number:
        print('您猜大了。')
    else:
        print('恭喜你,猜对了')
        break
    if i==5:
        print('您的五次机会已经用完了。')
    else:
        print('您还有%d次机会'%(5-i))
print('游戏结束，程序退出！')



# day09作业提交地址：http://xzc.cn/le1tjnnNuY
