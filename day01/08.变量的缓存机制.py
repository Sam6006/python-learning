# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/3 22:22
@Auth ： Sam
@File ：08.变量的缓存机制.py
@IDE ：PyCharm
"""

#number 部分 变量的缓存机制

#1对于整型而言，-5到正无穷范围内的相同值 id一致
var1 = 5
var2 = 5
var1 = -6
var2 = -6
print(id(var1),id(var2))

#2对于浮点数而言，非负数范围内的相同值id一致
var1 = -5.66
var2 = -5.66
print(id(var1),id(var2))

# 3.布尔值而言,值相同情况下，id一致
var1 = True
var2 = True
print(id(var1),id(var2))

#4复数在 实数+ 虚数 这样的结构中永不相同，只有虚数的情况下例外
var1 = 4+2j
var2 = 4+2j
print(id(var1),id(var2))

var1 = 4j
var2 = 4j
print(id(var1),id(var2))

#5.字符串 和空元组 相同的情况下  地址相同
var1 = '你'
var2 = '你'

var1 = 4j
var2 = 4j
print(id(var1),id(var2))

var1 = ()
var2 = ()
print(id(var1) ,id(var2))

#6，列表 元组 字典 集合无论什么情况 id都不相同 空元组例外

var1 = [1,2,3]
var2 = [1,2,3]
print(id(var1),id(var2))

# res = "我爱你" * 3
# print(res)
