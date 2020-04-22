# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/26 23:10
"""

# ### 匿名函数  => lambda 表达式
'''
lambda 表达式：
	用一句话来表达只有返回值的函数
好处：
	简洁，方便，定义函数数速简单
语法：
	lambda 参数 ：返回值
'''
#1.无参的lambda表达式
def func():
	return 123456

func = lambda : 123456
res = func()
print(res)

#2.有参的lambda表达式
def func(n):
	return type(n)

res = func(1234567)
print(res)

func = lambda n : type(n)
res = func('1234')
print(res)

# 3.带有条件判断的lambda表达式
def func(n):
	if n % 2 == 0:
		return '偶数'
	else:
		return '奇数'

#三目运算符：来用表达双项分支
'''
真值 if 条件表达式 else 假值
	如果条件表达式成立，执行真值
	如果条件表达式不成立，执行假值
'''
func = lambda n : '偶数' if n % 2 == 0 else '奇数'
res = func(2)
print(res)

# 计算参数中的最大值
def func(m,n):
	if m>n:
		return m
	else:
		return n
print( func(13,9) )

func = lambda m,n : m if m > n else n
res = func(1,2)
print(res)














