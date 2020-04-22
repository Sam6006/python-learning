# -*- coding: utf-8 -*-
"""
@Time ： 2020/4/4 9:11
"""
#面向对象 oop
'''
用几大特征表达一类事物称为一个类，类更像是一张图纸，表达的是一个抽象概念

对象是类的具体实现，更像是由这个图纸产出的具体物品，类只有一个，但对象可以通过这个类实例化出多个


'''
#类的定义
class MyClass:
	pass

#推荐写法
class MyClass():
	pass

class MyClass(object):
	pass

#类的实例化
class Car():
	color = '蓝色'

#类的实例化，产生的是对象
obj = Car()
print(obj)


#类的基本结构
'''
类中只有两样东西
	1.成员属性
	2.成员方法
'''

#标准写法
class MyCar():
	#成员属性
	color = '红色'
	#成员方法
	def run(self):
		pass

#例外不标准写法，不推荐使用
'''
类中的逻辑，在定义类的时候，直接执行，这个写法语法上不报错，但是严令禁止使用
'''
class MyCar():
	if 5 == 5:
		print(1233)

#改造
class MyCar():
	def func(self):
		if 5 == 5:
			print(1233)

# (4)类的命名
"""
推荐使用驼峰命名法:
	每个单词首字符大写;
	myclass => MyClass
	mycar => MyCar
	iloveboy => ILoveBoy
"""


























