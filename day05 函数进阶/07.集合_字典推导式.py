# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/29 12:30
"""

#集合推导式
'''
案例:
	满足年龄在18到21,存款大于等于5000 小于等于5500的人,
	开卡格式为:尊贵VIP卡老x(姓氏),否则开卡格式为:抠脚大汉卡老x(姓氏)	
	把开卡的种类统计出来
'''
lst = [
	{"name":"王家辉","age":18,"money":10000},
	{"name":"王水机","age":19,"money":5100},
	{"name":"王鹏","age":20,"money":4800},
	{"name":"李站","age":21,"money":2000},
	{"name":"李小龙","age":180,"money":20}
]

'''
可哈希数据：不可变数据
	number(int float bool complex) str tuple
不可哈希数据：可变数据
	list set dict
	
如果是字典的键或者集合的值，数据类型必须可哈希
'''
"""
三目运算符：
	true if 条件表达式 else  False
如果条件表达式成立，执行True
如果条件表达式不成立，执行False
"""
#基本语法
setvar = set()
for i in lst:
	if 18<= i['age'] <= 21 and 5000 <= i['money'] <= 5500:
		strvar = "尊贵VIP卡老" + i['name'][0]
	else:
		strvar = "抠脚大汉卡老" + i['name'][0]
	setvar.add(strvar)

print(setvar)
# 集合推导式
lst = { "尊贵VIP卡老" + i['name'][0] if 18<= i['age'] <= 21 and 5000 <= i['money'] <= 5500 else "抠脚大汉卡老" + i['name'][0] for i in  lst }
print(lst)

"""
# 分解:
{
左手边:
"尊贵VIP卡老" + i['name'][0] if 18<=i['age']<=21 and 5000 <= i['money'] <= 5500 else "抠脚大汉卡老" + i['name'][0] 
右手边:
for i in lst
}	
"""

#字典推导式
'''
1. enumerate
enumerate(iterable, [start=0])
功能：枚举; 将索引号和iterable 中的值，一个一个拿出来配对组成元组放入迭代器中
参数：
	iterable; 可迭性数据，（常用：迭代器，容器类型数据，可迭代对象 range）
	start: 可以选择开始的索引号(默认从0开始索引)
返回值:
	迭代器
'''
from collections import Iterable, Iterator
lst = ['罗1峰',"李2海","银3","赖4"]
it = enumerate(lst)
#print(it) #<enumerate object at 0x000001FCB4D6B3A8>
#print(isinstance(it,Iterator))
#print(list(it))
'''
[里面可以是列表，元组，字符串]
(里面可以是列表，元组，字符串)
{里面是元组}
[('a',1),('b',"sdfsdfsdfsdfsd")]
(['a',1],('b',"sdfsdfsdfsdfsd"))
{('a',1),("b",909090909090909090900909)}

'''
# dict 强转迭代器变成字典

# {0: '罗1峰', 1: '李2海', 2: '银3', 3: '赖4'}
res = dict(it)
print(res)

#字典推导式的写法变成字典
it = enumerate(lst) # 重置迭代器
dic = {k:v for k,v in it} #k接受的是012..345 v接受的是列表中的值
print(dic)

it = enumerate(lst,start=10)
dic = {k:v for k, v in it}
print(dic)

#zip
'''
zip(iterable,......)
	功能：将多个iterable中的值，一个一个拿出来配对组成元组放入迭代器中
	iterable： 可迭代性数据(常用:迭代器，容器类型数据，可迭代对象 range)

返回值：
	迭代器

正常按照索引进行配对，放到元组中，如果找不到配对的选项，直接放弃
'''
lst1 = ["吴1","帅2","温3文"]
lst2 = ["夜光花","吴2橘","王3"]
lst3 = ["温1杰","刘2","陈3杰"]
it = zip(lst1,lst2,lst3)
print(it)
print(isinstance(it,Iterable))
print(list(it))

# dict强转迭代器变成字典
lst2 = ["夜光花","吴2橘","王3"]
lst3 = ["温1杰","刘1","陈2杰"]

it = zip(lst2,lst3)
res = dict(it)
print(res)

print('=========')
#字典推导式
dic = {k:v for k,v in zip(lst1,lst2)}
print(dic)


















