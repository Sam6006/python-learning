# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/7 16:48
@Auth ： Sam
@File ：03.算数_比较.py
@IDE ：PyCharm
"""

#算数运算符 +-*/ // % **
var1 = 15
var2 = 5

res = var1 + var2
res = var1- var2
res = var1 * var2
res = var1 / var2
res = var1 // var2
# 如果除数或者被除数是一个小数,那么这个结果尾巴带上.0
res = var1 // 3.0

#取余
res = var1 % 4
res = 13 % 7
res = -13 % 7  #1
res = 13 % -7  #-1
res = -13 % -7  #-6 把正确的余数算出来，前面带上负号
print(res)

#比较运算符   >< >= <= == !=
'''比较的结果只有2个，要么是真True,要么是假False'''
var1 = 15
var2 = 7
res = var1 > var2
print(res)

# >= 满足一个条件为真即可
res = 15 >= 15
print(res)
# <= 满足一个条件为真即可
res = 15 <= 15
print(res)

# == 等于,是在做比较,不是在做赋值,赋值是一个等号
res = var1 == var2
print(res)

# != 不等于
res = var1 != var2
print(res)

