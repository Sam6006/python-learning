# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/3 22:31
@Auth ： Sam
@File ：09.自动类型转换.py
@IDE ：PyCharm
"""
# 自动类型转换 number=> int bool float complex
'''
精度从低到高排
bool -> int -> float -> complex
如果两个不同类型进行运算
默认从低精度向高精度转化
'''
# True -> int 1 False -> int0
#bool + int
res = True + 13
print(res)

#bool + float 把false 转换成浮点型0.0 再加上float
res = False + 4.555
print(res)

# bool + complex 把true 转换成复数1+0j 再加上complex
res = True + 3+4j
print(res)

# int  + float 把int 转换成浮点型 再加上float
res = 7 + 3.13
print(res)

# int + complex 把int转换成复数 再加上complex
res = 3 + 9-2j
print(res)

# float + complex 把float 转换成复数 再加上complex
res = 3.13 + 11-6j
print(res)




















