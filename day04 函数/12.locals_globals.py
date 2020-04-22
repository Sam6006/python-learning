# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/26 22:47
"""
#locals 和globals

'''
locals()  获取当前作用域的所有变量

如果locals 在函数外： 所获取的是locals()，打印返回值之前的所有内容
如果locals 在函数内： 所获取的是locals(), 调用之前所有内容
'''
#当前作用域在全局范围
'''
a = 1
b = 2
res = locals()
c = 3
print(res)
'''

#当前作用域在局部范围
'''
zz = 88
def func():
	d = 4
	f = 5
	res = locals()
	g = 6
	print(res)

func()
'''

"""
globals 无论在函数内外，都只获取全局作用域当中的所有内容

如果globals 在函数外，所获取的是globals(),打印返回值之前的所有内容
如果globals 在函数内，所获取的是globals(),调用之前所有内容
"""
# 当前作用域在全局范围
# a = 1
# b = 2
# res = globals()
# c  = 3
# print(res)

#当前作用域在局部范围
'''
aa = 11
bb = 22
def func():
	d = 1
	f = 2
	res = globals()
	z = 3
	print(res)

cc = 33
func()
'''

#globals 动态的创建全局变量
'''
globals() 返回的是系统的字典 ，只需要在字典里面添加键值对，就可以创建变量
字典中的键 就是变量名
字典中的值 就是变量所指代的值

'''
dic = globals()
print(dic)

dic['wangwen'] = 'sb'
print(wangwen)

#globals 批量创建全局变量
# 创建 p1-p5 个全局变量
def func():
	dic = globals()
	for i in range(1,6):
		dic['p%d' %(i)] = i
func()
print(p1)
print(p2)
print(p3)
print(p4)
print(p5)



