# -*- coding: utf-8 -*-
"""
@Time ： 2020/4/6 12:08
"""
'''
新式类：继承object类的都叫新式类，python3.x中所有的类默认都继承object，python3x中全部都是新式类
	广度优先
经典类：不继承object类就是经典类，python2.x默认是经典类，可以让其继承object变成新式类
	深度优先
	深度优先，广度优先，只能是继承两个类的情况----mro算法（继承三个类的顺序）
'''

#菱形继承（钻石继承）
'''
	Human
Man			Woman
	Children
'''
class Human():
	pty = 4
	def feelT(self):
		print("古代人类,天冷了,穿动物的毛1")
		print(self.pty)
		print('古代人类,天热了,啃树皮2')

class Man(Human):
	pty = 3
	def feelT(self):
		print("现代人类,天热了,喝啤酒,吃西瓜,撸串3")
		super().feelT()
		print("现代人类,天冷了,把火罐,开空调,吃炸鸡4")

class Woman(Human):
	pty = 2
	def feelT(self):
		print("现代女性,天热了,光膀子,穿裙子,买包包5")
		super().feelT()
		print("现代女性,天冷了,穿动物的毛,貂皮大衣6")
class Children(Man,Woman):
	pty = 1
	def feelT(self):
		print("现代小孩,天热了,吃冰棍,游泳7")
		super().feelT()
		print("现代小孩,天冷了,喝热水,玩农药8")

obj = Children()
obj.feelT()

'''
super遵循mro列表中出现的顺序，依次进行调用
类.mro

super在调用方法时，默认传递本对象
'''
lst =Children.mro()
print(lst)











