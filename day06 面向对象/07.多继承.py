# -*- coding: utf-8 -*-
"""
@Time ： 2020/4/6 11:19
"""
#多继承
#1.基本语法
class Father():
	f_property = "英俊潇洒,才华横溢,道貌岸然,一表人才"
	def hobby1(self):
		print("抽烟,喝酒,烫头,吃喝嫖赌抽,坑蒙拐骗偷")

class Mother():
	m_property = "一枝红情出墙来"
	def hobby(self):
		print("打麻将,蹦野迪,买包包")

class Daugther(Father, Mother):
	pass

obj = Daugther()
print(obj.f_property)
print(obj.m_property)
obj.hobby()
obj.hobby1()

#2.self 和super的区别
'''
1.super本身是一个类， super() 是一个对象，用于调用父类的绑定方法
2.super()只应用在绑定方法中，默认自动传递self对象，前提是super所在作用域中存大self
3.super用途：解决复杂的多继承调用顺序
'''


class Father():
	f_property = "英俊潇洒,才华横溢,道貌岸然,一表人才"

	def hobby1():
		print("抽烟,喝酒,烫头,吃喝嫖赌抽,坑蒙拐骗偷")


class Mother():
	m_property = "一枝红情出墙来"

	def hobby2(self):
		print("打麻将,蹦野迪,买包包")

class Son(Father,Mother):
	m_property = '一枝梨花压海棠'

	def hobby2(self):
		print("出入奇怪的场所,比如卡丁车,蹦极")

	def skill1(self):
		print(Father.f_property)

	"""
		self在调用成员的时候，如果自己本类有，优先调用自己的
		self在调用成员的时候，如果自己本类没有，调用父类的
	"""
	def skill2(self):
		print(self.m_property)
		self.hobby2()

	"""
		super在调用成员的时候，一定会调用父类的方法或者属性
		这是它与self的本质区别
	"""

	def skill3(self):
		print(super().m_property)
		super().hobby2()

print('======')
obj = Son()
obj.skill1()
obj.skill2()
obj.skill3()







