# -*- coding: utf-8 -*-
"""
@Time ： 2020/4/16 23:33
"""
# 一个类
# 对象的属性 : 姓名 性别 年龄 部门
# 员工管理系统
# 内部转岗 python开发 - go开发
# 姓名 性别 年龄 新的部门

# 1000个员工
# 如果几个员工对象的姓名和性别相同,这是一个人
# 请对这1000个员工做去重
class Employee():
	def __init__(self, name, age, sex, dep):
		self.name = name
		self.age = age
		self.sex = sex
		self.dep = dep

	#自定义hash格式
	def __hash__(self):
		return hash('%s%s' %(self.name, self.sex))

	def __eq__(self, other):
		if self.name == other.name and self.sex == other.sex:
			return True

emp_lst = []
#实例化1000名员工
for i in range(300):
	emp_lst.append(Employee('erick',i, 'male', 'python'))

for i in range(300):
	emp_lst.append(Employee('sam',i, 'male', 'python'))

for i in range(300):
	emp_lst.append(Employee('nick',i, 'male', 'python'))

for i in range(100):
	emp_lst.append(Employee('alice', i, 'male', 'python'))

#print(emp_lst)

emp_set = set(emp_lst)
print(emp_set)

for person in emp_set:
	print(person.__dict__)

#set集合的去重机制，先调用hash,再调用eq,eq 不是每次都触发，只有hash值相等的时候才会触发
























