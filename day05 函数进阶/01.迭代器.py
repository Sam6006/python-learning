# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/28 15:24
"""
# 迭代器
'''
能被next调用，并不断返回下一个值的对象
特征：
迭代器会生成惰性序列，它通过计算把值依次的返回，一边循环一边计算而不是一次性得到所有数据
优点：需要数据的时候，一次取一个，可以大大节省内存空间，而不是一股脑的把有数据放进内存
'''
#1.可迭代对象
'''
如果一个数据类型其中的成员包含__iter__方法，这个数据类型就是可迭代对象
dir 这个函数可以获取该数据类型的成员结构
'''
setvar = {1,2,'a'}
print(setvar)
for i in setvar:
	print(i)

res = dir(setvar)
print(res)

#2.迭代器
'''
for 循环在迭代器数据的时候，内部先转化成迭代器，然后通过next方法来进行调用，形成迭代效果
可迭代对象--> 迭代器 从不可被直接调用 --> 可被直接调用的过程

变成迭代器：
	1.iter()   2 __iter__()
遍历迭代器：
	1.next    2.__next__()
	
判断迭代器：
	1.该数据含有__iter__ 和 __next__两个方法
	就说该数据类型是迭代器
	2.from collections import Iterator, Iterable
如果是一个迭代器，一定是一个可迭代对象
如果是一个可迭代对象，不一定是迭代器
'''

#变成迭代器
res1 = iter(setvar)
print(res1)

res2 = setvar.__iter__()
print(res2)
#遍历迭代器
res = next(res2)
res = next(res2)
res = next(res2)
print(res)

lst = dir(res2)
print(lst)

#判断可迭代对象
print('__iter__' in dir(setvar))
#判断迭代器  1
print('__iter__' in dir(res2) and '__next__' in dir(res2))

#判断迭代器 2
# from 从哪里.. collections模块 import 引入 Iterator迭代器 Iterable可迭代对象
from collections import Iterator,Iterable
lst = [1,2,3,4,5]
#lst 是否是一个迭代器
res = isinstance(lst, Iterator)
print(res) #False

#lst 是否是一个可迭代对象
print(isinstance(lst,Iterable))

#判断range的可迭代属性
res = isinstance(range(10), Iterator)
print(res) #False

print(isinstance(range(10), Iterable)) #True

#遍历range对象
for i in range(10):
	print(i)

#通被next调用的，一定是一个迭代器
#next(range(10)) #TypeError: 'range' object is not an iterator

#变成迭代器
it = iter(range(10))
print(it) #<range_iterator object at 0x0000023298CDF630>

#判断类型： isinstance
print(isinstance(it, Iterator))

#调用range转换的迭代器
'''
如果在调用时，超出了原有的数据个数，直接越界报错
next在调用数据时，是单向不可逆的(一条路走到黑，一次性）

'''
res = next(it)
res = next(it)
res = next(it)
res = next(it)
res = next(it)
res = next(it)
res = next(it)
res = next(it)
res = next(it)
res = next(it)
#res = next(it) #StopIteration 越界报错
print(res)

print('====')
#重置迭代器
it = iter(range(10))
#遍历方式二，通过for 和next 配合调用
for i in range(10):
	res = next(it)
	print(res)

#遍历方法三  也可以通过for, 一次性遍历所有迭代器中数据
print('========')
it = iter(range(10))
for i in it:
	print(i)
# next(it) error

'''
用法1:isinstance(要判断的数据，数据类型) 返回True或者返回False
用法2:isinstance(要判断的数据,(数据类型1，数据类型2，....))
如果有一个条件满足，就返回真
int float bool complex str list tuple dict set
lst = [1,2,3]
res = isinstance(lst,list)
res = isinstance(lst,tuple)
# 有一个数据类型满足条件,就返回真
res = isinstance(lst, (list,tuple,set,str) )
print(res)
'''




















