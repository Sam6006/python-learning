# -*- coding: utf-8 -*-
"""
@Time ： 2020/4/6 16:44
"""
#类中方法
"""
普通方法：
	没有任何参数，只能类来调用
绑定方法：
	1.绑定到对象
	2.绑定到类
静态方法：
	无论对象还是类都能调用
"""
class Dog():
	#普通方法
	def jiao():
		print('小狗喜欢叫')

	#绑定方法(绑定到对象)
	def run(self):
		print('running')

	#绑定方法（绑定到类）
	@classmethod
	def tail(cls):
		print(cls)
		print("小狗看见主人会摇尾巴")

	#静态方法
	@staticmethod
	def tian(a):
		print("小狗看见骨头喜欢舔一舔")

#实例化对象
obj = Dog()
#普通方法
Dog.jiao()

#2.绑定方法（绑定到对象)
obj.run()
Dog.run(1) # 手动传参

#3.绑定方法(绑定到类)
'''无论是类还是对象都可调用，只不过默认传递的参数是类'''
Dog.tail() # 推荐
obj.tail()

#静态方法
obj.tian(2)
Dog.tian(3)


# 默认在类外,动态添加的方法时静态方法;
obj.func = lambda  : print(1233)
obj.func()





























