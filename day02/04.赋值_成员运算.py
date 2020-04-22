# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/7 17:00
@Auth ： Sam
@File ：04.赋值_成员运算.py
@IDE ：PyCharm
"""
# ###(3)赋值运算符:  = += -= *= /= //= %= **=
var1 = 14
var2 = 3
"""
var1 = var2
print(var1)
"""

#+=
var1 += var2 # var1 = var1+var2
print(var1)
# -=
"""
var1 -= var2 # var1 = var1 -var2
print(var1)
"""
# -=
"""
var1 -= var2 # var1 = var1 -var2
print(var1)
"""
# *=
# var1 *= var2 # var1 = var1 * var2
# print(var1)

# /=
# var1 /= var2 # var1 = var1 / var2
# print(var1)

# //=
# var1 //= var2 # var1 = var1 // var2
# print(var1)

# %=
# var1 %= var2 # var1 = var1 % var2
# print(var1)

# **=
var1 **= var2 # var1 = var1 ** var2
print(var1)

# ###(4)成员运算符:  in 和 not in (针对于容器型数据)

'''判断字符串时，需要是一个连续的片段，才能返回真'''

strvar = "如果遇到你是一种错,那我宁愿一错再错"
res = '你' in strvar
res = "遇到你" in strvar
res = "错,那" in strvar
print(res)

#tuple list set
tup = ("吴波","帅乐","毕杨生","刘得元")
res = '刘得元' in tup
print(res)

lst  = ["吴波","帅乐","毕杨生","刘得元","温红杰"]
res = "温红杰" not in lst
print(res)
setvar = {"赖廷","银燕","王成全"}
res = "银燕" not in setvar
print(res)

# dict in 或not in 判断的是字典的键，不是那个值
dictvar = {"wtn":"成熟稳重","lxh":"大,头大","lsf":"温文尔雅","hh":"哈哈"}
res = "成熟稳重" in dictvar
print(res)

res = 'lsf' not in dictvar
print(res)
res = "lxh" in dictvar
print(res)

