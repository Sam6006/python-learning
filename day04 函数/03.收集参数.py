# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/24 21:36
"""
# 收集参数
'''
收集参数：
	1.普通收集参数 * 在函数的定义处
		专门用来收集那些多余的，没人要的普通实参，形成一个元组
		语法：def func(*args): args => arguments
def func(*args):
	print(args)  => 返回的数据类型是元组
'''
def func(a,b,c,*args):
	print(a,b,c)
	print(args)

func(1,2,3,4,5,6,7,7,8,9)
#计算任意长度的累加和
def mysum(*args):
	total = 0
	for i in args:
		total += i
	print(total)

mysum(11,22,33,44,56,1,2)

'''
收集参数：
	2.关键字收集参数 **在函数的定义处
		专门用来收集那些多余的，没人要的关键字实参，形成一个字典
		语法:def func(**kwargs): kwargs => keword arguments
def func(**kwargs):
	print(kwargs) => 返回的数据类型是字典
'''

def func(a= 1,b=2,**kwargs):
	print(a,b)
	print(kwargs)

#方法1
func(99,b=99,c=4,d=90,f=78)

#方法2
func(b=90,a=111,c=4,d=9,f=89)

#拼接任意字符串
dictvar = {"monitor"}
def func(**kwargs):
	str1 = ''
	str2 = ''
	dictvar = {'monitor':'班长','classflower':'班花'}
	for k,v in kwargs.items():
		# print(k,v)
		if k in dictvar:
			str1 += dictvar[k]+':'+v + '\n'
		else:
			str2 += v + ''
	print(str1)
	print(("吃瓜群众:",str2))


func(monitor="舒则会",classflower="郭一萌",eatgua1="黄花",eatgua2="李村海")




























