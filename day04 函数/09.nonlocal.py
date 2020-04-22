# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/25 22:26
"""

#nonlocal 用来修饰局部变量
'''
nonlocal 符合LEGB 原则，就近原则找变量
1.nonlocal 用来修饰局部变量
2.nonlocal 会不停的寻找上一层空间所对应的值 拿来修改
3.如果上一层找不到，继续向上寻找，再也找不到，直接报错
'''

# 1.nonlocal 只能用来修改局部变量
a = 90
def func():
	a = 80
	print(a)
func()

#nonlocal 会不停的寻找上一层空间所对应的值，拿来修改
'''
通过LEGB 原则，可以获取上一层空间的值，只能单纯的获取，不能直接修改
如果想要修改，通过nonlocal 加以修饰

'''
def outer():
	a = 20
	def inner():
		nonlocal a
		print(a)
		a += 1
		print(a)
	inner()

outer()

#3.如果上一层找不到，继续向上寻找，再也找不到了，直接报错 nonlocal 只能修饰局部变量
a = 100
def outer():
	a = 100
	def inner():
		def smaller():
			nonlocal a
			a += 10
			print(a)
		smaller()
		print(a,'====1')
	inner()
	print(a,'=====2')

outer()

#4.不通过nonlocal 是否可以改变局部变量？ 可以，，需要用列表进行操作
def outer():
	lst = [100,101,102]
	def inner():
		lst[0] += 1
	inner()
	print(lst)
outer()