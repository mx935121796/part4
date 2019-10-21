#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/10/21 20:37
# @funcation:
# @Author   : mx
# @File     : copy_list.py
# @Software : PyCharm
food = ['pizza', 'ice craem']
friend_food = food[:]
food.append("noodles")
friend_food.append('salad')
print(food)
print(friend_food)
###############################friend_food=food#############################p
food = ['pizza', 'ice cream']
friend_food = food
food.append("noodles")
friend_food.append('salad')
print(food)
print(friend_food)
