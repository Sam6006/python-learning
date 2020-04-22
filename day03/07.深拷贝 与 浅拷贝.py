# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/22 12:33
"""
"""
#深拷贝 与 浅拷贝
a = 7
b = a
a = 9
print(b)

#列表赋值出现的问题，两个不同的变量指向同一个列表
lst1 =[1,2,3]
lst2 = lst1
lst1.append(4)
print(lst2)
"""
#浅拷贝 copy 两个列表之间彼此独立，拷贝一个新副本
lst1 = [1,2,3]
lst2 = lst1.copy()
lst1.append(4)
print(lst1)
print(lst2)

#import 引入copy模块下的copy方法
import copy
lst1 = [1,2,3]
lst2 = copy.copy(lst1)
lst1.append(4)
print(lst1)
print(lst2)

# 深拷贝

'''
浅拷贝只是单独复制一级列表里面所有元素
深拷贝可以复制所有级别的列表元素，都单独拷贝一份，
都形成独立的副本，彼此不受干扰
'''
# 出现的问题:
print('========')
lst1 = [1,2,3,[4,5,6]]
lst2 = lst1.copy()
lst1[-1].append(7)
lst1.insert(2,666)
print(lst1)
print(lst2)
print('========')
lst1 = [1,2,3,[4,5,6]]
lst2 = copy.deepcopy(lst1)
lst1[-1].append(999)
#print(lst1)
print(lst2)

"""
看需求而定
浅拷贝的执行时间,要比深拷贝执行时间要快
而深拷贝是所有级别的列表都单独拷贝出来,形成独立副本
而浅拷贝仅仅只是拷贝一级的所有元素,二级的不考虑.
"""

container = [1,2,3,{"a":[4,5,6]}]
container2 = copy.deepcopy(container)
container[-1]['a'].append(888)
print(container)
print(container2)