# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/28 21:02
"""
# filter

'''
filter(func, iterable)
功能：过滤
	在自定义的函数中，如果
		:return True  代表保留该数据
		:return False 代表舍弃该数据
参数：
	1.func 自定义函数
	2.iterable 可迭代对象（容器类型数据 range对象 迭代器）
返回值：
	迭代器
'''

#基本写法
lst = [24,234,23,423,4,234,1,23,12,31,231,2,3]
for i in lst:
	if i % 2 == 0:
		print(i)
	else:
		pass

print('=========')

#2.filter 写法
def func(n):
	if n % 2 == 0:
		#保留该数据
		return True
	else:
		return False

it = filter(func, lst)
print(list(it))


print('=======')
#优化变lambda
func = lambda n : True if n % 2 == 0 else False
it = filter(func, lst)
print(list(it))































