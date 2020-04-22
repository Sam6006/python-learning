# -*- coding: utf-8 -*-
"""
@Time ： 2020/4/6 17:02
"""

# ### property 装饰器
'''
# 属性  : 将一个方法  伪装成一个 属性,在代码的级别上没有本质的提升,但是让其看起来跟合理.
可以把成员方法变成属性
控制成员的获取，设置，删除


@自定义名.setter 设置
@自定义名.deleter 删除
'''
# 写法一
class Myclass():
	def __init__(self, name):
		self.name = name

	@property
	def username(self):
		return self.name

	@username.setter
	def username(self,val):
		#val这个形参会自己接收alex实参
		self.name = val

	@username.deleter
	def username(self):
		#del self.name
		pass

#把方法username 变成属性 username
obj = Myclass('sam')
#获取username
print(obj.username)

#设置username
obj.username = 'alex'
print(obj.username)

#删除username
#del obj.username
#print(obj.username)

#写法二
class Myclass():

	def __init__(self, name):
		self.name = name

	def get_username(self):
		return self.name

	def set_username(self, val):
		# val这个形参会自动接收"廖萍萍"实参;
		self.name = val

	def del_username(self):
		del self.name

	#按照顺序  先获取-----设置-----删除   依次传参
	username = property(get_username, set_username, del_username)

obj = Myclass("郭艳妹")

#获取
print(obj.username)

#设置
obj.username = "尹艳姐"
print(obj.username)

#删除
del obj.username
print(obj.username)






















