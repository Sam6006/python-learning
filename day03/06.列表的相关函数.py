# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/22 12:02
"""
#列表的相关函数
lst = [22,33,44]
#增
#1.append 向列表的末尾添加新的元素
res = lst.append(16)
print(lst)
#2.insert 在指定索引之前插入元素
lst =['sam','alex']
lst.insert(1,'nick')
print(lst)

#删
listvar = ["邓良辉","李祖清","舒则会","郭一萌","黄花"]
# 1. pop 通过指定索引删除元素,若没有索引移除最后那个 (推荐使用)
listvar.pop()
print(listvar)
listvar.pop(0)
print(listvar)

#2.remove 通过给予的值来删除，如果多个相同元素，默认删除第一个
listvar = ["邓良辉","李祖清","舒则会","郭一萌","舒则会","黄花"]
listvar.remove('舒则会')
print(listvar)

#3.clear 清空列表
listvar.clear()
print(listvar)

# 其他相关函数
listvar = ["邓良辉","李祖清","舒则会","郭一萌","舒则会","黄花","郭一萌","郭一萌"]
# 1.index 获取某个值在列表中的索引
"""index(要搜索的值,[开始索引,结束索引])"""
res = listvar.index('郭一萌')
print(res)

res = listvar.index('郭一萌',4)
print(res)
res = listvar.index("郭一萌",6,7)
print(res)

# count() 计算某个元素出现的次数
res = listvar.count("郭一萌")
print(res)

#sort()列表排序（默认从小到大）
"""如果是字母,按照ascii编码进行排序"""
listvar = ["james","jand","qz","davis","smallkl"]
listvar.sort()
print(listvar)

#sort(reverse = True) (从大到小排序)
listvar = [-90,67,11,1000]
listvar.sort()
print(listvar)
listvar.sort(reverse=True)
print(listvar)

#reverse列表反转操作
listvar = [1,88,-90,"a"]
listvar.reverse()
print(listvar)
"""
tuple 里面只有index和count两个函数可以用.剩下的基本操作和列表一样
"""
