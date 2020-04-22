# -*- coding: utf-8 -*-
"""
@Time ： 2020/4/4 23:08
"""
#构造方法 __init__
#__init__魔术方法（构造方法）
'''
	触发时机：实例化对象，初始化的时候触发
	功能：为对象添加成员
	参数：参数不固定，至少一个self参数
	返回值：无
'''
#1.基本语法
class MyClass():
	def __init__(self):
		self.name = 'alex'

#实例化对象
obj = MyClass()
print(obj.name)

#2.多个参数的__init__
class MyClass():
	def __init__(self, name):
		#self.name(成员属性name) = name(参数name)
		self.name = name

#实例化对象的同时，在括号中加上对应的参数，self是系统自己传递的，name需要手动传递，郭一萌会被name形参接收走,在实例化的时进行赋值.
obj = MyClass('郭一萌')
print(obj.name)

#综合实例：类可以有一个，对象可以有多个，不同的对象之间彼此数据隔离
class Children():
	def __init__(self,name, skin):
		self.name = name
		self.skin = skin

	def cry(self):
		print('小孩一生下就哭')

	def eat(self):
		print('小孩饿了喝奶奶')

	def sleep(self):
		print("小孩一天23个小时睡觉,还有一个小时上厕所")

	def child_info(self):
		print('该对象姓名:{}, 肤色是：{}'.format(self.name, self.skin))

#实例化对象1
child1 = Children('王铁男', '黑色')
child1.cry()
child1.child_info()

#实例化对象2
child2 = Children('康哥', '屎黄色')
child2.eat()
child2.child_info()

#实例化对象3
child3 = Children('王宝强', '绿色的')
child3.sleep()
child3.child_info()










