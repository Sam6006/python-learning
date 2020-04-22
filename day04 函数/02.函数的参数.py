# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/23 22:54
"""
#函数的参数：函数运算时，需要的值
'''
参数：
	形参：形式参数（在函数的定义处）
	实参：实际参数（在函数的调用处）

形参：（普通(位置)形参， 默认形参， 普通收集参数，命名关键字参数，关键字收集参数）
实参：（普通实参，关键字实参）

形参 和 实参  要一一对应
'''
#1.普通形参
#函数的定义处 hang, lie 普通形参
def small_start(hang,lie):
	i = 0
	while i < hang:
		j = 0
		while j < lie:
			#打印星星
			print('*', end='')
			j += 1
		#打印换行
		print()
		i += 1

#函数的调用处   3，8 普通实参
small_start(3,8)

#2.默认形参  hang, lie 在函数定义处给与默认值
'''
如果给与实参，那么就使用实际参数
如果没给实参，那么就使用参数的默认值

'''
def small_start(hang = 10, lie = 10):
	i = 0
	while i < hang:
		j = 0
		while j < lie:
			#打印星星
			print('*', end='')
			j += 1
		#打印换行
		print()
		i += 1

# small_start()
small_start(2,5)

#3.普能形参 + 默认形参
'''默认形参必须写在普通形参的后面，语法上有要求'''
def small_start(hang, lie = 10):
	i = 0
	while i < hang:
		j = 0
		while j < lie:
			#打印星星
			print('*', end='')
			j += 1
		#打印换行
		print()
		i += 1
#函数的调用处
small_start(3)
small_start(4,5)
# small_start() error  # 形参实参要一一匹配

#4.关键字实参
'''
1.如果使用关键字实参进行函数调用，实参的顺序无所谓
2.如果定久时是普通形参，调用时是关键字实参
那么这个参数后面的所有调用方式都需要关键字实参进行调用

'''
def small_start(hang,a, b, c, lie = 10):
	i = 0
	while i < hang:
		j = 0
		while j < lie:
			#打印星星
			print('*', end='')
			j += 1
		#打印换行
		print()
		i += 1
#关键字实参hang 和 lie
# small_start(lie=4, hang=7)
small_start(3,c=90,b=55,a=5,lie=2)


















