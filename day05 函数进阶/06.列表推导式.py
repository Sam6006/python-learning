# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/28 21:32
"""
#推导式：可以实现一些简单的操作，重要是代码比较简洁
'''
通过一行循环判断，遍历出一系列数据的方式是推导式
语法：val for val in Iterable(把想要的值写在for 的左侧）
里面是一行循环判断 根据套在推导式外层的符号判断具体是什么类型的推导式

推导式种类：三种
	列表推导式： [val for val in Iterable]
	集合推导式：{val for val in Iterable}
	字典推导式：{a:b for a,b in Iterable}
'''

#lst = [1,2,3,4,5,6,7,8,9]
lst = []
for i in range(1,10):
	lst.append(i)
print(lst)

#1.普通列表推导式
lst = [i for i in range(1,10)]
print(lst)

# [1,2,3,4] => 2,4,6,8
lst = [i * 2 for i in range(1,5)]
print(lst)
# (2) 带有判断条件的列表推导式
'''
推导式的后面跟着只能是单项分支，其他的是不行的
'''
#基本写法
lst = [1,2,3,4,5,6,67,7,8,9]
lst2 = []
for i in lst:
	if i % 2 == 1:
		lst2.append(i)
print(lst2)

#推导式写法
lst = [i for i in lst if i % 2 == 1]
print(lst)

#3.双循环的列表推导式
lst1 = ['麦秸唐',"曾曼","王铁男"]
lst2 = ["舒则会","郭一萌","廖萍萍"]
# 谁♥♥谁
lst = []
for i in lst1:
	for j in lst2:
		strvar = i +'♥♥' + j
		lst.append(strvar)
print(lst)

lst = [i + '♥♥' + j for i in lst1 for j in lst2]
print(lst)

# (4) 带有判断条件的双循环列表推导式
lst1 = ['麦3唐',"曾2","王1男"]
lst2 = ["舒1会","郭2萌","廖33"]

lst = []
for i in lst1:
	for j in lst2:
		if lst1.index(i) == lst2.index(j):
			strvar = i + '♥♥' + j
			lst.append(strvar)

print(lst)

#推导式
lst = [i + '♥♥' + j for i in lst1 for j in lst2 if lst1.index(i) == lst2.index(j)]
print(lst)







