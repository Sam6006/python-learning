# -*- coding: utf-8 -*-
"""
@Time ： 2020/4/11 10:04
"""
# 内置函数和类的内置方法是由奸情的
class myList():
	def __init__(self):
		self.lst = [1,2,3]

	def __len__(self):
		print('执行len了')
		return len(self.lst)

l = myList()
print(len(l)) #myList' has no len()  len(obj)相当于调用了这个对象的__len__方法
#如果一个obj对象没有__len__方法，那么len函数会报错
# __len__方法return的值就是len函数的返回值


# 练习
# 类
# self.s = ''
# len(obj) = str的长度

class MyClass():
	def __init__(self, s):
		self.s = s

	def __len__(self):

		return len(self.s)

me = MyClass('abc')
print(len(me))











