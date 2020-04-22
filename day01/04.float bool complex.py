# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/2 22:44
@Auth ： Sam
@File ：04.float bool complex.py
@IDE ：PyCharm
"""

#数字类型Number(float bool complex)
# (1)float浮点型 就是小数
#表示方法1
floatvar = 3.14
print(floatvar)
print(type(floatvar))
print(id(floatvar))

# (2)表示方法2 科学计数法
floatvar = 5.12e4 #小数点向右移动
floatvar = 5.12e-2 #小数点向右移动
print(floatvar)


# (2) bool 布尔型 ( True 真的  False 假的)
boolvar = True
boolvar = False
print(boolvar)
print(type(boolvar))
print(id(boolvar))


#complex复数
"""
复数：实数 + 虚数
比如: 3+4j
3是实数
4j是虚数
什么是j?
如果有一个数,它的平方是-1,那么这个数就是j
科学家认为有,表达高精度类型.
"""

# 表达方法1
complexvar = 3-8j
complexvar = 5j
print(complexvar)
print(type(complexvar))
print(id(complexvar))

# 表达方法2 complex 函数,转换成复数
"""
语法:
complex(实数,虚数)

"""

complexvar = complex(2,2)
complexvar = complex(2,-2)
print(complexvar)