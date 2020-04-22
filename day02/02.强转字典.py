# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/3 22:56
@Auth ： Sam
@File ：02.强转字典.py
@IDE ：PyCharm
"""
#二级容器，外层是一个容器类型数据，里面元素还是一个容器类型数据
listvar = [1,2,3,4,5,(6,7,8,0)]

#二级列表
listvar = [1,2,3,4,[4,5,66]]
# 二级元组
tuplevar = (1,2,3,(4,5,6))

#二级集合 在集合里面只能放 可哈希数据 number(int float bool complex ) str tuple
setvar = {"a",1,2,(3,4,5)}
print(setvar)
# setvar = {"a",1,2,(3,4,5,[5,6,7])} error 列表不可哈希
# 二级字典
dictvar = {"a":1,"b":{"c":3,"d":4}}

# 多级容器 想要获取99
container = [1,2,3,4,5,(7,8,9,{"a":1,"b":{"c":[888,99,22]}})]
res = container[-1] # res = (7,8,9,{"a":1,"b":{"c":[888,99,22]}})
res2 = res[-1]   # res2 = {"a":1,"b":{"c":[888,99,22]}}
res3 = res2["b"] # {"c":[888,99,22]}
res4 = res3["c"] # res4 = [888,99,22]
res5 = res4[1]   # 99
print(res5)

# 简写
res = container[-1][-1]["b"]["c"][1]
print(res)

#等长的二级容器
'''
(1)里面的每一个元素都是容器类型数据
(2)容器里面放的元素的个数等长
'''
lst = [(1,2,3),(4,5,6),(8,9,10)]
tup = (["a","b"],[1,2],(4,5))

#dict 强转字典
'''
需要等长的二级容器 并且元素的总个 数是2
字符串元素个数只能是2个，多一个都不行，有局限性，不推荐使用

'''
# 外层是列表,里面是列表或者元组或者字符串(不推荐,有局限性)
lst = [["a",1],("b",2),"c3"]
res = dict(lst)
print(res)
# 外层是元组,里面是列表或者元组或者字符串(不推荐,有局限性)
tup = (["c",15],("d","sdfsdfsd"),"f8")
res = dict(tup)
print(res)
# 外层是集合,里面是元组(如果想要表达容器,在集合中只能是元组)
setvar = {("f1",3.44),("e2",3+9j)}
res = dict(setvar)
print(res)

# 外层是元组或者列表,里面是集合,从语法上来看允许,但是违背逻辑,因为集合无序,不推荐使用.
container = [{"a",15}]
res= dict(container)
print(res)
# 把列表的重复数据去掉,可以先转集合,再转列表,缺陷:顺序被打乱.
listvar = ["a","a",1,2,1,"c"]
res = list(set(listvar))
print(res)

"""
bool() int() float() complex()
str() list() tuple() set() dict()

这些强转的数据类型,在不给参数的情况下,默认返回一个该数据类型的值
这些值可以作为变量的初始化值
"""
res = tuple()
res = dict()
res = set()
res = int()
print(res)











































