# -*- coding: utf-8 -*-
"""
@Time ： 2020/4/6 11:09
"""

#继承
'''
1.单继承 2.多继承
到少2个类，子类和父类
一个类继承另外一个类，当前类是子类（衍生类）
被继承的这个类是父类（基类，超类）

python 所有类的父类都是object
'''
#1.子父继承后，子类可以使用父类的公有方法
class Father():
	skin = '黑色的'
	__sex = '男性'

	def hobby(self):
		print('爱好喜欢打篮球')

	def __smoke(self):
		print('老爸喜欢抽大麻')

class Daughter(Father):
	pass


obj = Daughter()
print(obj.skin)
obj.hobby()

#2.子父继承后，子类不能调用父类的私有方法
class Son(Father):
	def pub_func(self):
		print(self.__sex) #error

obj = Son()
#print(obj.__sex)
#obj.pub_func()

#3.子父继承后，子类可以改写父类方法
class n_seflchild(Father):
	skin = '白色的'
	def hobby(self):
		print('白种人喜欢种大麻')

obj = n_seflchild()
obj.hobby()
print(obj.skin)





























