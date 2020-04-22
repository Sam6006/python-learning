# -*- coding: utf-8 -*-
"""
@Time ： 2020/4/11 10:40
"""
# __new__ 魔术方法
'''
	触发时机：实例化类生成对象的时候触发(触发时机在__init__之前)
	功能：控制对象的创建过程
	参数:至少一个cls接受当前的类,其他根据情况决定
	返回值：通常返回对象或None
'''
#__new__   构造方法
#__init__  初始化方法

class Single:
	def __new__(cls, *args, **kwargs):
		print('在new方法里')
		obj = object.__new__(cls)
		print('在new方法里',obj)
		return obj
	def __init__(self):
		print('在init方法里', self)


'''
1.开辟一个空间，属性对象
2.把对象的空间传给self,执行init
3.将这个对象的空间返回给调用者

'''
obj =Single()
#Single的new, singal没有，只能调用object的new 方法
#new方法在什么时候执行？？
	#在实例化之后, __init__之前先执行new来创建一块空间

# 可以通过__new__ 来控制对象创建的过程
class MyClass2():
	def __new__(cls):
		print(cls)
		# 通过父类object 中的 __new__ 魔术方法 ,返回该类的对象,参数是类.
		# obj = object.__new__(cls)

		# 返回本类对象,只能通过父类创建.
		# return obj
		# 可以返回None
		# return None
		# 也可以返回别人的对象
		return obj2

#
# obj = MyClass2()
# print(obj)
# print(obj.a)

# 2 .对比__new__ 和 __init__ 之间的区别
"""
__new__  负责创建对象
__init__ 负责初始化对象
__new__ 在 __init__ 触发时机之前.
"""


class MyClass3():
	def __new__(cls,name):
		print(1)
		return object.__new__(cls)

	def __init__(self, name):
		print(2)
		self.name = name


obj = MyClass3("廖平平")
print(obj.name)


#升级版
class MyClass3():
	#用收集参数，一劳永逸
	def __new__(cls, *args, **kwargs):
		print(1)
		return object.__new__(cls)
	def __init__(self,name, age, sex):
		print(2)
		self.name = name
		self.age = age
		self.sex = sex

obj = MyClass3("廖平平",98,"未知")
print(obj.name)
print(obj.age)
print(obj.sex)


# (3) 注意点.__init__ 只能初始化自己本类的对象

class MyClass4():
	def __new__(cls):
		print(1)
		return obj

	# 不会调用init方法,因为返回的对象不是MyClass4本身的,不调用;
	def __init__(self):
		print(2)


obj = MyClass4()
print(obj)
