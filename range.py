#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/10/21 19:48
# @funcation:
# @Author   : mx
# @File     : range.py
# @Software : PyCharm
for i in range(1,5):
    print(i)
squares=[]
for value in range(1,11):
    squares.append(value**2)
    print(value**2)
print(min(squares))
print(max(squares))
print(sum(squares))
squares=[value**2 for value in range(1,11)]
print(squares)