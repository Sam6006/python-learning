# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/22 14:15
"""

# ### 集合相关操作
set1 = {"王文","刘德华","张学友","郭富城"}
set2 = {"王文","王宝强","李宇春","蔡徐坤"}
# intersection()交集

res = set1.intersection(set2)
print(res)

#简写 &
res = set1 & set2
print(res)

#difference() 差集
res = set1.difference(set2)
print(res)
#简写-
res = set1 - set2
print(res)

#union 并集
res = set1.union(set2)
print(res)

#简写 |
res = set1 | set2
print(res)

#symmetric_difference()对称差集  补集情况涵盖在其中
res = set1.symmetric_difference(set2)
print(res)

#简写 ^
res = set1 ^ set2
print(res)

# issubset() 判断是还是否是子集
set1 = {"舒1会","郭2萌","黄瓜","孙33"}
set2 = {"舒1会","郭2萌"}
set3 = {"舒1会","郭2萌","黄瓜","孙33"}
res = set2.issubset(set1)
print(res)

# 简便写法 <
res = set2 < set1 # 真集合
print(res)

#issuperset() 判断是否是父集
set1 = {"舒1会","郭2萌","黄瓜","孙33"}
set2 = {"舒1会","郭2萌"}
res = set1.issuperset(set2)
print(res)

# 简便写法 >
res = set1 > set2
print(res)

#isdisjoint()检测两集合是不是想交
set1 = {"舒1会","郭2萌","黄瓜","孙33"}
set2 = {"舒1会","郭2萌"}
res = set1.isdisjoint(set2)
print(res) #False 代表相交

#集合相关函数
#add() 向集合中添加数据
setvar = {"赖1","银2","毕33"}
setvar.add('易烊千玺')
print(setvar)
# update() 迭代增加
'''把迭代性容器里面的数据一个一个拿出来放到setvar当中'''
setvar.update([1,2,3,4])
print(setvar)

# 删
setvar = {"a","c","ddd"}
#pop() 随机删除集合中的一个数据
res = setvar.pop()
print(res)
print(setvar)

#remove()删除集合中指定的值(不存在就报错)
# setvar.remove("aaaaa")
# print(setvar)

#discard()删除集合中指定的值（不存在的不删除，推荐使用）
setvar.discard('aaaaa')
print(setvar)


#clear()  清空集合
setvar.clear()
print(setvar)

#frozenset() 可强转容器类型数据为冰冻集合
# 冰冻集合一旦创建,不能在进行任何修改,只能做交叉并补操作
#定义一个空的冰冻集合
fz = frozenset()
print(fz)
# 强制转换为一个冰冻集合
listvar = [1,23,3,43,43]
fz = frozenset(listvar)
print(fz)

for i in fz:
	print(i)

# 只能做交叉并补
fz1 = frozenset(["李宇春","王宝强"])
fz2 = frozenset({"李宇春","王文","周杰伦"})
res = fz1 & fz2
print(res)

# 不能做增删操作 错误的
# fz1.add("郭富城") error
