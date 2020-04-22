# -*- coding: utf-8 -*-
"""
@Time ： 2020/4/11 12:26
"""
#__str__ 魔术方法
'''
	触发时机: 使用print(对象)或者str(对象)的时候触发
	功能:     查看对象
	参数:     一个self接受当前对象
	返回值:   必须返回字符串类型
'''
#__str__
#l = [1,2,3] 实例化一个list的对象
# l是个对象
#print(l)

class Student():

	def __str__(self):
		return self.name

	def __init__(self,name, age):
		self.name = name
		self.age = age

s = Student('alex', 30)

# 方式一:打印对象时触发
print(s)    # 内置的数据类型,内置的类,相当于执行__str__
# 方式二:强转对象为字符串时触发

res = str(s)
print(res) # str(obj),相当于执行obj.__str__方法

# __repr__ 魔术方法
'''
	触发时机: 使用repr(对象)的时候触发
	功能:     查看对象,与魔术方法__str__相似
	参数:     一个self接受当前对象
	返回值:   必须返回字符串类型
'''


class Mouse():
	gift = "会打洞"
	def __init__(self, name):
		self.name = name

	def obj_info(self):
		return "该对象名字{},该对象属性:龙生龙,凤生凤,老鼠的儿子{}".format(self.name, self.gift)

	def __repr__(self):
		return self.obj_info()

	# 系统底层,自动加了一句话,如果存在__repr__魔术方法,自动把这个方法赋值给__str__方法,所以即使在print打印或者强转对象为字符串,也仍然触发.
	__str__ = __repr__


jerry = Mouse("杰瑞")
# res = repr(jerry)
# print(res)

print(jerry)
res = str(jerry)
print(res)

