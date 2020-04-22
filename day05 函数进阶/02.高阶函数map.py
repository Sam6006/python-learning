# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/28 16:44
"""
# 高阶函数：能够把函数当成参数传递的就是高阶函数

#map
'''
map(func, iterable)
功能：把iterable里面的数据，一个一个扔到func函数中进行处理，
把处理的结果放到迭代器中，最终返回迭代器
参数：
	1.func 内置函数 或 自定义函数
	2.iterable 可迭代对象 容器类型数据， range对象，迭代器

返回值：
	迭代器
'''
# 例子1: ["1","2","3","4"] => [1,2,3,4]
lst = ["1","2","3","4"]
lst2 = []
for i in lst:
	res = int(i)
	lst2.append(res)
print(lst2)

from collections import Iterator, Iterable
it = map(int, lst)
print(isinstance(it, Iterator))
#next 调用
res = next(it)
res = next(it)
res = next(it)
res = next(it)
print(res)

#for 遍历
it = map(int, lst)
for i in range(2):
	res = next(it)
	print(res)

#用list瞬间强转成列表
it = map(int, lst) #重置迭代器
lst = list(it)
print(lst)

# 例子2 [1,2,3,4] [3,6,9,12]
lst = [1,2,3,4]
lst2 = []
for i in lst:
	res = i * 3
	lst2.append(res)
print(lst2)

'''
第一次把lst中的1拿出来,扔到func当中进行处理,返回3,放到迭代器中
第二次把lst中的2拿出来,扔到func当中进行处理,返回6,放到迭代器中
第三次把lst中的3拿出来,扔到func当中进行处理,返回9,放到迭代器中
第四次把lst中的4拿出来,扔到func当中进行处理,返回12,放到迭代器中
到此iterable中的数据已经没有,终止函数,返回迭代器.

'''
def func(n):
	return n * 3

it = map(func,lst)
print(list(it))
# 例子3 {97:"a",98:"b",99:"c"} ["a","b","c"] => [97,98,99]
dic = {97:"a",98:"b",99:"c"}
dic2 = {}
res = dic.items()
print(isinstance(res,Iterator)) # False
print(isinstance(res,Iterable)) # True

# 反转字典中的键值对
for k,v in res:
	dic2[v] = k
print(dic2)

#通过字典的键，获取值，插入到新列表中
lst = ['a','b','c']
lst2 = []
for i in lst:
	res = dic2[i]
	lst2.append(res)
print(lst2)

# map自定义函数,需要一个参数,必须写一个返回值
def func(n):
	dic = {97:"a",98:"b",99:"c"}
	#返转字典中的键值对
	for k,v in dic.items():
		dic2[v] = k
	print(dic2)
	return dic2[n]

it = map(func,['a','b','c'])
print(list(it))










