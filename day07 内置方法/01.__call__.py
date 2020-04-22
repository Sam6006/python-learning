# -*- coding: utf-8 -*-
"""
@Time ： 2020/4/9 22:31
"""
#__名字__
	#类中的 特殊方法\内置方法
	#双下方法
	#魔术方法 magic method
#类中的每一个双下方法 都有它自己的特殊意义
#__call__ 相当于 对象()  触发时机：把对象当作函数调用的时候自动触发
# __len__  len(obj)
# __new__  特别重要   开辟内存空间的 类的构造方法
    # 写一个单例类=
# __str__  str(obj),'%s'%obj,print(obj)

#所有的双下方法，没有需要你在外部直接调用的
#而是总有一些其他的 内置函数，特殊的语法，来自动触发这些 双下方法

#基本语法
'''
class A():
	def __call__(self, *args, **kwargs):
		print('执行call方法了')

class B():
	def __init__(self, cls):
		print('在实例化A之前做一些事情')
		self.a = cls()
		self.a()
		print('在实例化A之后做一些事情')
# a = A()
# a()  # 对象() == 相当于调用__call__方法
# a.call()

# A()() # 类名()() ,相当于先实例化得到一个对象,再对对象(),==>和上面的结果一样,相当于调用__call__方法

B(A)
'''

# (2) __call__ 魔术方法可以做一个统一的调用,不改变原类的情况下，实现调用
class MakeCake():

	def __call__(self,*args, **kwargs):
		self.step1()
		self.step2()
		self.step3()

	def step1(self):
		print("和面,发酵,放点糖,放点牛奶,等一天")

	def step2(self):
		print("扔进烤箱,考7749天,炼丹")

	def step3(self):
		print("拿出来,切一切吃")

class Run():
	def __init__(self, cls):
		print('开始做蛋糕了')
		self.a = cls()
		self.a()
		print('做完了')

Run(MakeCake)
