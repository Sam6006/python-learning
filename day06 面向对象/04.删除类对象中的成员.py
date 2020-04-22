# -*- coding: utf-8 -*-
"""
@Time ： 2020/4/4 21:01
"""
#删除类对象中的成员
class MyCar():
	price = '100元'
	__oil = '百公里1升'

	#普通方法
	def bianxing_cat1():
		print('车会变形成猫', MyCar.price)

	#绑定到对象方法
	def bianxing_cat2(self):
		print('车会变成猫', self.price)

	#普通私有方法
	def __oil_info1():
		print('油耗信息保密')

	#私有绑定方法
	def __oil_info2(self):
		print('油耗信息保密')

	#定义公有绑定方法
	def pub_func(self):
		print(self.__oil)
		self.__oil_info2()

	#定义公有普通方法
	def pub_func2():
		print(MyCar.__oil)
		MyCar.__oil_info1()

#实例化对象
obj = MyCar()
print(obj.__dict__)
print(MyCar.__dict__)

#1.实例化的对象删除公有成员属性和方法
obj.price = '2元' #动态为该对象成员属性price
print(obj.price)
del obj.price
print(obj.price)

#func这个成员是一个静态方法，无论是类还是对象都能当成普通方法调用
'''
在类外动态添加成员方法，返回的是静态方法
'''
obj.func = lambda n : print('我是func函数', n)
obj.func(11)
del obj.func #删除方法
#obj.func(123) #删除之后无法调用

#2.定义的类删除公有成员属性和方法
#del MyCar.price
#print(MyCar.price) #类无法调用
#print(obj.price) # 对象无法调用
#MyCar.func(123)  #类无法调用对象中的成员
#
# del MyCar.bianxing_cat1
# MyCar.bianxing_cat1()

#3.可否在类外调用私有成员？
'''
改名策略
	_类名 + 私有成员：比如
	__oil ===_MyCar__oil
	__oil_info1 ===_MyCar__oil_info1

'''
#对象的调用
print(obj._MyCar__oil)
obj._MyCar__oil_info2()

#类的调用
print(MyCar._MyCar__oil)
MyCar._MyCar__oil_info1()

obj.bianxing_cat2()

print('======')

#4.通过公有方法，调用私有成员
obj.pub_func()
MyCar.pub_func2()



