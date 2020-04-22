# -*- coding: utf-8 -*-
"""
@Time ： 2020/4/16 20:41
"""

#item系列 和 对象使用[]访问值有联系
# obj = {"k": "v"}
# print(obj) #字典对象
# print(obj['k'])

#在内置的模块中
#有一些特殊方法，要求对象必须实现__getitem__/__setitem__才能使用


class B():
	def __getitem__(self, item):
		return getattr(self, item)
	def __setitem__(self, key, value):
		return setattr(self,key, value)
	def __delitem__(self, key):
		delattr(self, key)

b = B()
b.k2 = 'v2'
print(b.k2)
b['k1'] = 'v1' #__setitem__
print(b['k1']) #__getitem__
del b['k1']
#print(b['k1'])

class C:
	def __init__(self, lst):
		self.lst = lst
	def __getitem__(self, item):
		return self.lst[item]
	def __setitem__(self, key, value):
		self.lst[key] = value
	def __delitem__(self, key):
		self.lst.pop(key)
c = C([1,2,3,4,5])
print(c.lst[0])
print(c[0])
c[3] = 'alex'
print(c[3])
del c[2]
print(c.lst)






















