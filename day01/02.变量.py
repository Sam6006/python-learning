# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/2 21:40
@Auth ： Sam
@File ：02.变量.py
@IDE ：PyCharm
"""
#变量 可以改变的量，具体指的是内存的一块空间
a= 5
print(a)

#（1）变量的概念
rujia_305 = 'alex'
rujia_305 = 'alice'
rujia_305 = 'sam'
print(rujia_305)

#(2)声明变量
#声明方法1
a = 1
b = 2
print(a)
print(b)

#声明方法2
a,b = 3,5
print(a)
print(b)
#声明方法3
a = b = 99
print(a,b)
# (3)变量的命名
"""
字母数字下划线，首字符不能是数字
严格区分大小写，且不能使用关键字
变量命名有意义，且不能使用中文哦
"""

# 4234sdfsdf error
adddadfaf34345_dadf = 12
print(adddadfaf34345_dadf)

abc = 13
ABC = 14
print(abc)
print(ABC)

# print = 999
# print(1) error

#打印python所有关键字
import keyword
res = keyword.kwlist
print(res)

"""
# 如下关键字都不能作为变量名使用
[
'False', 
'None', 
'True', 
'and', 
'as', 'assert', 'break', 'class', 'continue',
 'def', 'del', 'elif', 'else', 'except', 'finally', 
 'for', 'from', 'global', 'if', 'import', 'in', 'is', 
 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 
 'try', 'while', 'with', 'yield'
 ]
"""
car = "宝马"
asdfsadfasdfsadfas = "宝马"

'''python 支持用中文命名变量，但是严禁使用
utf-8 国际通用编码（万国码) 一个中文用了3个字节表示，一个英文或者符号占用一个字节
gbk   国际编码(中国标准)   一个中文占用了2个字节，一个英文或者符号占用一个节
在编码格式不同的情况下，会乱码，为了避免乱码，不要使用中文，就执照变量命名的方法去写变量名

'''

中文 = "平头哥"
print(中文)

# (4)变量的交换
a = 21
b =22

# python特有方法
a,b = b, a
print(a,b)

#通用方法
tmp = a
a = b
b = tmp

print(a,b)


