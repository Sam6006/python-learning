# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/25 23:01
"""

#闭包的特点
'''
内函数使用了外函数的局部变量，外函数的局部变量与内函数发生绑定，延长了该变量的生命周期
'''
def outer(val):
	def inner(num):
		return num + val
	return inner

func = outer(10)
res = func(5)
print(res)
'''
func = outer(10)
val 接收到10这什值， return inner
因为内函数使用了外函数的局部变量val val就与内函数发生绑定，延长了该变量的生命周期
不释放，等待下一次调用时使用

res = func(5)
num 接收到5这个值  return num + val = 5+10
'''

#闭包的意义
'''
闭包可以优先使用外部函数中的变量，并对闭包中的值起到了封装保护的作用，外部无法访问
模拟一个鼠标点击计数的功能
'''
clicknum = 0
def clickfunc():
	global clicknum
	clicknum += 1
	print(clicknum)


# 模拟点击操作,点击一次就调用一次
clickfunc()
clickfunc()
clickfunc()
clickfunc()
clickfunc()
clicknum = 100
clickfunc()

# 用闭包函数来进行改造
def clickfunc():
	x = 0
	def func():
		nonlocal x
		x += 1
		print(x)
	return func

clickfunc2 = clickfunc()
clickfunc2() # clickfunc2() = func()
clickfunc2()
clickfunc2()
clickfunc2()
clickfunc2()
x = 100
clickfunc2()


















