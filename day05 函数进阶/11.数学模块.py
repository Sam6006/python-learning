# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/29 21:58
"""
#math 数学模块  使用： 模块.方法()
import math
#cell()  向上取整操作 （对比内置round）
res = math.ceil(3.01)
res = math.ceil(3.000000000000000000000000000000001)
res = math.ceil(3.99)
print(res)

#floor() 向下取整操作  对比内置round
res = math.floor(3.98)
res = math.floor(3.11111)
print(res)

#pow() 计算一个数值的N次方(结果为浮点数)  对比内置pow
res = math.pow(2,3)
print(res)
# res = math.pow(2,3,3) error 没有第三个参数
# print(res)

#sqrt() 开平方运算（结果浮点数）
res = math.sqrt(5)
print(res)

#fabs() 计算一个数值的绝对值 结果浮点数  对比内置abs
res = math.fabs(5.6)
print(res)

#modf() 将一数值拆分为整数和小数两部分组成元组
res = math.modf(5.12)
print(res)

#copysign() 将参数第二个数值的正负号拷贝给第一个
res = math.copysign(6,-1)
print(res)

#fsum() 将一个容器数据中的数据进行求和运算 结果为浮点数 对比内置 sum
lst = [1,2,34,5,11]
res = math.fsum(lst)
print(res)

#圆周率常数pi
res = math.pi
print(res)














