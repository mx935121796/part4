#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/10/21 20:10
# @funcation:
# @Author   : mx
# @File     : test.py
# @Software : PyCharm
num=[value for value in range(1,1000001)]
print(num)
print(sum(num))
num=[value for value in range(1,21,2)]
print(num)
for value in range(3,31,3):
    print(value)
    list=[]
for value in range(1,11):
    print(value**3)
    list.append(value**3)
print(list)
num=[1,2,3,4,5]
print(num[:3])
print(num[-3:])
print(num[1:2])
indexes=range(1,len(num),2)
print(len(num))
for index in indexes:
    print(num[index])

