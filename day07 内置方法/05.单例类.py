# -*- coding: utf-8 -*-
"""
@Time ： 2020/4/11 12:13
"""

#如果一个类，从头到尾只能有一个实例，说明从头到尾只开辟了一块属于对象的空间,那么这个类就是一个单例类

class Single():
	# 防止类外调用__obj,形成封装保护.
	__ISINCTANCE = None
	def __new__(cls, *args, **kwargs):
		if not cls.__ISINCTANCE:
			cls.__ISINCTANCE = object.__new__(cls)
		return cls.__ISINCTANCE

	def __init__(self, name, age):
		self.name = name
		self.age = age

s1 = Single('alex', 99)
s2 = Single('taibai', 40)

print(s1.name)
print(s2.name)
print(s1, s2)

"""
class A:
	__OBJ = None
	def __new__(cls, *args, **kwargs):
		if not cls.__OBJ:
			cls.__OBJ = object.__new__(cls)
		return cls.__OBJ
"""


# 2. 有且只有一个对象
class SingleTon():
	# 防止类外调用__obj,形成封装保护.
	__obj = None

	def __new__(cls, *args, **kwargs):
		if cls.__obj is None:
			cls.__obj = object.__new__(cls)
		return cls.__obj

	def __init__(self, name):
		self.name = name


obj1 = SingleTon("郭一萌")
print(obj1.name)
obj2 = SingleTon("舒则会")
print(obj1.name)
print(obj2.name)
obj3 = SingleTon("银燕")
print(obj1.name)
print(obj2.name)
print(obj3.name)
"""
obj1.name = 郭一萌
obj2.name = 舒则会
"""


















