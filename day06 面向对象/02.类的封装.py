# -*- coding: utf-8 -*-
"""
@Time ： 2020/4/4 10:43
"""
# ### 封装
'''
对象的使用方式
	对象.属性
	对象.方法()
'''

class MyCar():
	#公有成员属性
	pinpai = '布加迪威龙'

	#私有成员属性
	__oil = '2.5L'

	#公有成员方法
	def run(self):
		#self.pinpai ===obj.pinpai
		print('我的小车会跑',self.pinpai)

	#私有成员方法
	def __oil__info(self):
		print('油耗信息是保密的')

'''
绑定方法：
	1.绑定到对象： 系统会默认把对象当成参数进行传递，让self形参进行接收(对象.方法)
	2.绑定到类： 系统会默认把类当成参数进行传递，让形参进行接收，（对象.方法 或 类.方法 通过装饰器修饰）
'''

#实例化对象  或者 类的实例化  两个名字都可以，都是产生对象
obj = MyCar()

#1.实例化的对象访问公有成员属性和方法--绑定方法
print(obj.pinpai)
#obj.run() 系统自动把obj 这个对象当成参数传递给run方法中self这个参数进行接收
obj.run()

#2.实例化的对象动态添加公有成员属性和方法
#__dict__可以获取对象或类的内部成员， 它是魔术属性
print(obj.__dict__) #第一次为什么打印？ 因为当前对象obj,没有成员 {}

obj.color = '屎黄色'  #添加成员
print(obj.color)
print(obj.__dict__) #{'color': '屎黄色'}

#动诚添加成员方法
#1.添加无参方法

def fangxiangpan():
	print("我是制造方向盘的方法")

#让类外的函数赋值给obj对象的成员方法fangxiangpan
obj.fangxiangpan = fangxiangpan
obj.fangxiangpan()
print(obj.__dict__)

#2.添加有参方法
def func(self, something):
	print(self.pinpai, something)

#将右侧的赋值给左侧的成员属性func
obj.func = func
#需要手动把对象传进去，不如使用绑定方法
obj.func(obj, '有参方法')

#使用绑定方法自动把obj当成参数传递 依靠MethodType
import types
#MethodType(函数，要绑定在哪个对象上)
#将创建的绑定方法赋值给成员属性func2，意味着下次调用不需要手动传递该对象，系统会自动帮传递
obj.func2 = types.MethodType(func, obj)
obj.func2('有参方法')

#3.添加lambda表达式
obj.dahuangfeng = lambda : print('请叫我大黄峰')
obj.dahuangfeng()

obj.qingtianzhu = lambda n : print(n)
obj.qingtianzhu("擎天柱")

#obj.pinpai = "abc"
print(obj.pinpai)












