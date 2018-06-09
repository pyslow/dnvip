#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/5 21:32
# @Author  : Slow
# @Site    : 
# @File    : test.py
# @Software: PyCharm

import math


def foo(x):
    f, i = math.modf(x)
    a = '%d%s' % (i, str('%.3f' % f)[1:])
    return a[:4] if not a[:4].endswith('.') else a[:3]

print(foo(3.999))