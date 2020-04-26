# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/2 23:05
@Auth ： Sam
@File ：06.list tuple.py
@IDE ：PyCharm
"""

# 容器类型数据(列表 list 元组 tuple)
"""list 列表  可获取 可修改，有序"""
#定放一个空列表
listvar = []
print(listvar)
print(type(listvar))

#2获取列表元素
#          0    1    2    3    4  正向索引
listvar = [55,3.14,True,2+9j, "abcada123"]
#          -5   -4  -3    -2   -1  逆向索引

res = listvar[2]
print(res)

#瞬间拿到列表最后一个元素
res = listvar[-1]
print(res)

#通用方法 用len
'''len 可以获取容器类型数据的长度 元素总个数'''
res = listvar[4]
print(res)

res = len(listvar)
print(res) # 5

#                   5       -  1 = 4
res = listvar[    len(listvar)-1    ]
print(res)

# 3.修改列表元素
listvar[0] = "abc"
print(listvar)


# tuple 元组 可获取 不可修改  有序
#定义一个空元组
tuplevar = ()
print(tuplevar)
print(type(tuplevar))

#判断它是否是元组，在于，逗号
tuplevar = ('abc',)
tuplevar = 1,2
print(tuplevar,type(tuplevar))

# 定义一个元组
tuplevar = ("aaa","bbb","ccc","ddd","eee")

#获取元组当中的值
res = tuplevar[2]
print(res)

# 修改元组中的值? 不可以
# tuplevar[0] = 123 error

#str 可获取 不可修改 有序
# 字符串可以通过索引下标取值

# 可获取
#          0 1 2 3 45 6 7 9  正向索引
strvar = "瞅你一眼,浑身哆嗦"
#         -9-8-7-6-5-4-3-2-1 逆向索引
# 获取"眼"字
res = strvar[3]
res = strvar[-6]
print(res)

# 可以修改么? 不可修改
# strvar[3] = 123 error
