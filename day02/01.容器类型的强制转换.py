# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/3 22:47
@Auth ： Sam
@File ：01.容器类型的强制转换.py
@IDE ：PyCharm
"""
#容器类型的强制转换   str list tuple set dict

var1 = "今天天气好晴朗朗"
var2 = ["刘璐","王钊","王华振","罗淞峰"]
var3 = ("刘璐1","王钊1","王华振1","罗淞峰1")
var4 = {"王文贤","庄哲浩","王铁男"}
var5 = {"a":1,"b":2}
var6 = 12345

#str 容器类型数据  / number类型数据 都可以
'''规律：基于原来的数据类型两边套上引号'''
res = str(var2)
res = str(var5)
res = str(var6)
# repr 以字符串的形式原型化输出数据
print(repr(res))

#list
'''
规律：
	如果是字符串，把里面的字符一个一个拿出来，作为列表的每一个元素
	如果是其他容器数据，只是基于原数据，把两边的符号换成[]，换成列表
	如果是字典，只是单纯的获取字典的健，不要那个值，组 成列表
'''
res = list(var1)
res = list(var3)
res = list(var4)
res = list(var5)
print(res)
# tuple
"""规律:如果是字符串,把里面的字符一个一个拿出来,作为元组的每一个元素
		如果是其他容器数据,只是基于原数据,把两边的符号换成() , 换成元组
		如果是字典,只是单纯的获取字典的键,不要那个值,组成元组.
"""
res = tuple(var1)
res = tuple(var2)
res = tuple(var4)
res = tuple(var5)
print(res)

# set
'''
规律：如果是字符串，把里面的字符一个一个拿出来，作为集合的每一个元素
	如果是其他容器数据，只是基于原数据，把两边的符号换成{}，换成集合
	如果是字典，只是单纯的获取字典的键，不要那个值，组成集合
	
	
	集合的特征，自动去重，无序
'''
res = set(var1)
res = set(var2)
res = set(var5)
print(res)

















