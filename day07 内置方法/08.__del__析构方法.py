# -*- coding: utf-8 -*-
"""
@Time ： 2020/4/16 20:15
"""
# ### __del__ 魔术方法 (析构方法)
'''
	触发时机：当对象被内存回收的时候自动触发
		1.页面执行完成回收所有变量
		2.所有对象被del 的时候
	功能：
		对象使用完毕后资源回收
	参数：一个self接受对象
	返回值：无

'''
# 构造方法  申请一个空间
# 析构方法  释放一个空间之前执行
# 某对象借用了操作系统的资源,还要通过析构方法归还回去 : 文件资源  网络资源

class A:
	def __del__(self):
		#析构方法del A的对象，会自动触发这个方法
		print('执行我了')

a = A()
#del a 对象被del的时候
print(a) #页面执行完毕,触发析构方法

#文件读取操作
"""
fp = open("文件名",mode="r",encoding="utf-8")
res = fp.read()
fp.close()
"""
import os
class ReadFile():
	def __new__(cls, filename):
		if os.path.exists(filename):
			return object.__new__(cls)
		return print('该文件名不存在')
	def __init__(self,filename):
		self.fp = open(filename,mode='r',encoding='utf-8')

	def readcontent(self):
		res = self.fp.read()
		return res

	def __del__(self):
		self.fp.close()

obj = ReadFile('ceshi111.txt')
res = obj.readcontent()
print(res)




























