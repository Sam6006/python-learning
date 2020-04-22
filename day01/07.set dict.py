# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/2 23:19
@Auth ： Sam
@File ：07.set dict.py
@IDE ：PyCharm
"""

# 集合 set (集合是用来做交叉并补操作的)
"""自动去重，无序"""

#定义一个空集合
#setvar = {} 这个dict 字典类型
# print(setvar,type(setvar))

setvar = set()
print(setvar,type(setvar))

setvar = {"刘德华","张学友","郭富城","王文"}
print( setvar   ,   type(setvar)   )
setvar = {"刘德华","张学友","郭富城","王文","王文"}
print(setvar)


# 集合能够获取值么? 不行
# res = setvar[0] error

# 集合能够修改值么? 不行
# setvar[0] = 199   error

# setvar = {1,2,"a",(1,2,3,{"a":1}) }
# print(setvar)

#字典

'''python 3.6版本之前无序
python 3.6版本之后有序（表面上有序，本质上无序)

键值对存储的数据，有序
语法: {键1:值1 , 键2:值2 , 键3:值3 }
'''

# 定义一个空字典
dictvar = {}
print(dictvar, type(dictvar))

dictvar = {"top":"夏侯惇" , "middle":"亚瑟","bottom":"鲁班七号","jungle":"刘备","support":"蔡文姬"}

# 通过键获取字典中的值
res = dictvar["top"]
print(res)

# 修改字典的中的值
dictvar["bottom"]="孙尚香"
print(dictvar)

#字典中的键和集合中的值有要求，需要可哈希数据
"""
可哈希数据：（不可变数据)  Number(int,float,bool, complex), str, tuple
可哈希数据可以作为字典的键和集合的值，剩下的都不可以

不可哈希数据:(可变数据) list dict set

字典中的键 推荐使用按照变量命名的字符串去声明最为理想;
"""

dictvar = {5:1 , 3.78:12 , True:90 , 6+8j:"abc" , "你好":99,(1,2,3):1122}
print(dictvar)
