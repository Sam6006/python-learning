# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/8 16:07
@Auth ： Sam
@File ：14.for 循环.py
@IDE ：PyCharm
"""
# for 循环
'''循环 遍历 迭代 这三个名词都是获取每个数据的意思'''
'''
	for 循环专门用来遍历数据
	而while循环遍历数据有局限性，无法遍历无序容器数据
	while一般用于复杂的逻辑操作

语法：
	可迭代对象   容器类型数据，range对象，迭代器
	for i in 可迭代对象
		code..		
'''
"""
# while 遍历数据的局限性
lst = [1,2,3,4]
lst = {1,2,3,4}
i = 0 
while i<len(lst):
	res = lst[i]
	print(res)
	i+=1
"""

# 遍历集合
container = {"树则会","郭一萌","银燕","刘璐","罗淞峰"}
# 遍历列表
container = ["树则会","郭一萌","银燕","刘璐","罗淞峰"]
# 遍历元组
container = ("树则会","郭一萌","银燕","刘璐","罗淞峰")

for i in container:
	print(i)
# 遍历字符串
'''
container = "我爱你,美丽的祖国,我歌颂党的伟大,积极响应党的号召"
for i in container:
	print(i)
'''
# 遍历字典 在遍历字典的时,默认遍历键
container = {"wzh":"老哥~稳","mjk":"奄奄一息",'zzh':"梦游神国","dlh":"九九有神"}
for i in container:
	print(i)

# 遍历等长的二级容器
listvar = [("王健林", "王思聪", "王美丽"), ["马云", "马化腾", "马冬梅"], ("王宝强", "马蓉", "宋小宝")]


#变量的解包
a, b = [1,2]
print(a,b)
a,b,c =(7,8,9)
print(a,b,c)
a,b = 7,8
print(a,b)

for i in listvar:
	"""
	('王健林', '王思聪', '王美丽')
	['马云', '马化腾', '马冬梅']
	('王宝强', '马蓉', '宋小宝')
	"""
	print(i)

for a,b,c in listvar:
	print(a,b,c)

# 遍历等长的二级容器
listvar = [("王健林","王思聪","王美丽"),["马云","马化腾"],("王宝强",)]

for i in listvar:
	for j in i:
		print(j)

# range对象
"""
range(start,end,step)
start 开始值
end   结束值 (最大值取不到,取到之前的那个值)
step  步长
"""
# 1.range中只有一个值
for i in range(10):
	print(i)

# 2. range中有二个值
for i in range(1,9):
	print(i)

# 3. range中有三个值 正向值
for i in range(1,15,3):
	# 1 4 7 10 13
	print(i)

print("<=============>")
# 3. range中有三个值 逆向值
for i in range(15,0,-3):
	# 1 4 7 10 13
	print(i)










