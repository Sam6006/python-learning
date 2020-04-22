# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/28 18:10
"""
# sorted
'''
sorted(iterable,reverse = False, key=函数)
功能：
	排序
参数：
	iterable 可迭代对象（容器类型数据，range对象，迭代器）
	reverse 控制正序或者顺序 reverse = True 倒序
	key:可自定义排序的规则
返回值：
	排序后的结果使用
'''
# 默认从小到大排序
lst = [88,31,-90,0]
res = sorted(lst)
print(res)

#从大到小排序
lst = [88,31,-90,0]
res = sorted(lst,reverse = True)
print(res)

#按照绝对值排序（使用内置函数）
lst = [-99,-2,45,1]
res = sorted(lst,key=abs)
print(res)
"""
1   => 1
-2  => 2
45  => 45
-99 => 99
"""
"""
abs 获取一个数的绝对值
print(abs(-80.34))
print(abs(90))
"""

#按照余数排序 使用自定义函数
def func(n):
	return n % 10

lst = (19,24,91,36)
"""
91 % 10 => 1
24 % 10 => 4
36 % 10 => 6
19 % 10 => 9 
"""
res = sorted(lst, key= func)
print(res)
print(lst)


#如果排序字符串，按照ascii编码来排序
strvar = 'cba'
res = sorted(strvar)
print(res)

'''
sort 基于原有列表进行修改
sorted 会产生一个新列表，原来的数据不动，
其余的用法一模一样
只不过sort 只能用在列表中
sorted 可以用在所有容器类型数据中
'''









































