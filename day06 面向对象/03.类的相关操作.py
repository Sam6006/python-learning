# -*- coding: utf-8 -*-
"""
@Time ： 2020/4/4 11:44
"""
# ### 类的相关操作
"""
语法:
	类.属性
	类.方法()
"""
class Plane():
	#公有成员属性
	captain = '李祖庆'
	#私有成员属性
	__air_hostess = 20

	#普通公有方法
	def fly():
		#飞机会飞20
		print('飞机会飞', Plane.__air_hostess)
	#普通私有方法
	def __fly2():
		print('空姐数量是保密的')

obj = Plane()
#对象无法调用无参的普通方法，必须要加上self
#obj.fly() #error
#1.定义的类访问公有成员属性和方法
print(Plane.captain)

#无论是对象还是类，都无法在类外调用类中的私有成员
#print(Plane.__air_hostess)
Plane.fly()

#查看类Plane的所有成员
print(Plane.__dict__)

#2.定义的类动态添加公有成员属性和方法
Plane.engine = '烧汽油的'
print(Plane.__dict__)
print(obj.__dict__)


#添加方法
#无参方法
def bianxing():
	print('我的飞机能变成小鸟')

Plane.bianxing = bianxing
Plane.bianxing()

#有参方法
def setname(name):
	print('我的飞机名', name)

Plane.setname = setname
Plane.setname('空军一号')

#lambda 表达式
Plane.lunzi = lambda : print('我是制造飞机轮胎的方法')
Plane.lunzi()


'''
调用类中成员的时候，要么使用对象，要么使用类来调用，不能直接写
对象可以使用类中的相关公有成员，但是没有归属权
类中的成员都归当前这个类所有，但是不能使用对象中的相关成员

对象中如果有这个成员，用对象自己的
如果对象没有，用类的成员

'''








































