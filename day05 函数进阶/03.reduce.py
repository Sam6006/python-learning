# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/28 17:40
"""
#reduce
'''
reduce(func,iterable)
功能：计算
	先从iterable拿出2个数据，放到func中进行计算，得到的结果和iterable中的第三个元素，
	再扔到func中做计算，依次类推，最终返回计算结果
参数：1.func 内置函数 或自定函数
	2.iterable 可迭代对象（容器类型数据，range对象，迭代器）
返回值：计算出来的最终结果
	
'''

# 方法一
# lst = [5,4,8,8] => 5488
lst = [5,4,8,8]
strvar = ''
for i in lst:
	strvar += str(i)
print(strvar,type(strvar))
print(int(strvar))

# 方法二
"""
5 * 10 + 4  = 54
54 * 10 + 8 = 548
548 * 10 + 8 = 5488
"""
it = iter(lst)
res1 = next(it)
res2 = next(it)
res = res1 *10 +res2
print(res)
for i in it:
	res = res * 10 + i
print(res,type(res))

#使用reduce进行改写
print('========')
'''
首先把5和4扔到func当中 5* 10 + 4 = 54
然后把54和iterable 中的8 这两个参数扔到func中，
54 * 10 + 8
然后把548 和iterable 中的最后一个8两个参数扔到func中
548 * 10 + 8 = 5488
计算完毕后返lkd 5488 结束
'''

from functools import reduce
def func(x,y):
	return x * 10 + y

lst = [5,4,8,8]
res = reduce(func,lst)
print(res,type(res))

# "789" => 789 在不使用int强转的前提下完成
"""
"789" => [7,8,9]
list("789") = > ['7','8','9']
list("789") = > [7,8,9]
map(int,"789") error 不让用int
"""

strvar = '789'
def func1(n):
	dic = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
	return dic[n]

def func2(x,y):
	return x * 10 + y

it = map(func1,strvar)

#开始计算reduce
res = reduce(func2,it)
print(res)























