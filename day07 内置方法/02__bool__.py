# -*- coding: utf-8 -*-
"""
@Time ： 2020/4/9 23:01
"""
# ### __bool__ 魔术方法
'''
	触发时机：使用bool(对象)的时候自动触发
	功能：强转对象
	参数：一个self接受当前对象
	返回值：必须是布尔类型
'''
class Myclass():
	def __bool__(self):
		return False

#实例化对象
obj = Myclass()
res = bool(obj)
print(res)

'''
类似的还有如下等等(了解):
	__complex__(self)      被complex强转对象时调用
	__int__(self)          被int强转对象时调用
	__float__(self)        被float强转对象时调用
	...
	...
'''

# __add__ 魔术方法  (与之相关的__radd__ 反向加法)
'''
	触发时机：使用对象进行运算相加的时候自动触发
	功能：对象运算
	参数：二个对象参数
	返回值：运算后的值
'''
'''
类似的还有如下等等(了解):
	__sub__(self, other)           定义减法的行为：-
	__mul__(self, other)           定义乘法的行为：
	__truediv__(self, other)       定义真除法的行为：/
	...
	...
'''


class MyClass():
	def __init__(self, num):
		self.num = num

	# 当对象在+加号的左侧时,自动触发;
	def __add__(self, other):
		return self.num * 2 + other

	# 当对象在+加号的右侧时,自动触发
	def __radd__(self, other):
		return self.num * 3 + other


a = MyClass(3)
# self 接收到 a ,other 接收到 1 self.num * 2 + 1 = 3 * 2 +1 = 7
res = a + 1
print(res)

b = MyClass(5)
# 第一次参数永远接受的是对象,self接收的 b ,other 接受的是 2 => 5 * 3 + 2 => 17
res = 2 + b
print(res)

# a+b
"""
先触发add魔术方法 self 接收到a  other 接收到b => 3 * 2 + b => 6 +b
6+b 有触发了radd魔术方法 self 接收到 b  other 接收到6  => 5 * 3 + 6 => 21
"""
res = a + b
print(res)























