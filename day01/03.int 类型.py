# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/2 22:16
@Auth ： Sam
@File ：03.int 类型.py
@IDE ：PyCharm
"""

# ### 数字类型 number (int)
#整型 int（正整型 0 负整型

intvar = 156
print(intvar)

#type获取变量的类型(type())
res = type(intvar)
print(res)

#id 或者变量所指向的这个值的内存地址
res = id(intvar)
print(res)

#二进制整型0b表示
intvar = 0b1010
print(intvar)
print(type(intvar))
print(id(intvar))

#八进制整型 0o表示
intvar = 0o10
print(intvar)
print(type(intvar))
print(id(intvar))

#十六进制 0x表示
intvar = 0xff
print(intvar)
print(type(intvar))
print(id(intvar))

