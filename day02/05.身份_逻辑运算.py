# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/7 17:08
@Auth ： Sam
@File ：05.身份_逻辑运算.py
@IDE ：PyCharm

"""

# 身份运算符   is 和 is not 检测两个数据在内存当中是否是同一个值
# int -5 到正无穷
var1 = 6
var2 = 6
#比较两个变量指向的地址是不是同一个  比较地址
res = var1 is var2
print(res)

# 比较两个变量的值是不是相等 比较值
res = var1 == var2
print(res)

#复数  在只有虚数的情况下地址相同
var1 = 6j
var2 = 6j
res = var1 is var2
print(res)

# bool 两个值相同,那么地址一样
var1 = False
var2 = True
print(var1 is not var2)

#容器类型数据， 只有空元组和相同的字符串，在值相同的情况下，地址是一样的
var1 = ()
var2 = ()
print(var1 is var2)
print(var1 is  var2)
var1 = "好"
var2 = "好"
print(var1 is  var2)
var1 = [1,2]
var2 = [1,2]
print(var1 is not var2)

#逻辑运算符 and or not

#and 逻辑与
'''全真则真，一假则假'''
res = False and False
print(res) # false
print(False and True) # false
print(True and True)  # True

# or 逻辑或
'''全假则假，一真则真'''
print(False or True)
print(False or False)
print(True or False)
print('=====')

#not 逻辑非
'''取反， 真变假 假变真'''
print(not True)
print(not False)
print('===')

#逻辑短路，后面的代码不走了
'''
（1）True or 表达式
（2）False and 表达式
'''

res = True or print(123)
print(res)
res = False and print(456)
print(res)

#print 是系统的函数 打印的值和要返回的值是两个完全不同的概念
res = print(1234)
print(res) # none print没有返回值， 是通过  return + 返回值定义的

res = True and 7
print(res)

res = False and 8
print(res)

res = True or 99
print(res)

res = False or 'abc'
print(res)
# 逻辑运算符优先级
'''
() > not > and > or
如果存在逻辑短路 优先计算短路 比如 True or 。。。。一定为True
'''

res = 5 or 6 and 7
print(res)

res = (5 or 6) and 7 # 5 and 7
print(res)

res = not (5 or 6) and 7 # not 5 and 7 => False and 7 => False
print(res)
res = 1>2 and 3<4 or 5>6 and 7>8
print(res)

'''
res = False and True or False and False
res = False or False
res = False
'''

