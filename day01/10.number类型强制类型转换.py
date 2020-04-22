# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/3 22:39
@Auth ： Sam
@File ：10.number类型强制类型转换.py
@IDE ：PyCharm
"""

#把number部分强制转换 int float bool complex
var1 = 23
var2 = 6.78
var3 = True
var4 = 3+2j
var5 = "1234"
var6 = "abcd121"
# 强制转换成int
res = int(var2)
res = int(var3)
#res = int(var4)
res = int(var5)
print(res)

#强制转换成float
res = float(var1)
res = float(var3)
# res = float(var4)
res = float(var5)
print(res)

#强制转换成complex
res = complex(var1)
res = complex(var2)
res = complex(var3)
res = complex(var5)
print(res)

# 4.强制转换成bool 要么返回True 真的 要么返回False 假的
res = bool(var4)
res = bool(var6)
res = bool(None)
print(res)

'''
布尔类型 为假的10种情况
0 0.0 False 0j ''  [] () set() {} None
None 代表空的， 什么也没有， 一般用在变量初始化的时候

# 初始化变量的时候用
ab = None

'''


















