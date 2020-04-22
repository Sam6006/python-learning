# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/29 17:21
"""
# 生成器表达式 generator
'''
迭代器和生成器的区别
	迭代器本身是系统内置的，重写不了，而生成器是用户自定义的，可以重写迭代逻辑
元组推导式的返回值是一个生成器对象，简称生成器，生成器本质是迭代器

生成器可以用两种方式创建
	1.生成器表达式(里面是推导式，外面用圆括号)
	2.生成器函数(用def 定义，里面含用yield)
'''
from collections import Iterator
#基本定义
gen = (i for i in range(10))
print(gen) # 返回的是生成器对象,简称生成器
print(isinstance(gen,Iterator))

#1.使用next方法调用生成器
res = next(gen)
res = next(gen)
res = next(gen)
print(res)

#2.for 配合 next 进行调用
print('========')
for i in range(5):
	res = next(gen)
	print(res)

#3.用for 循环遍历生成器
print('======')
for i in gen:
	print(i)
