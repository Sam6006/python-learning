# ### json
import json

"""
json 可以序列化数据， 转化成一个字符串
json 格式的数据，可以让所有的编程语言都能识别
有数据类型的限制： bool float int list tuple dict str None
"""
#第一组：dumps 和loads 用来序列化或反序列化字符串
'''
ensure_ascii = True 是否显示中文， 设置ensure_ascii = False 显示
sort_keys = True 对字典的键按照ascii 进行排序
'''
#序列化数据， 转化成一个字符串
# .......得到一个字符串的结果 过程就叫序列化
# 字典 / 列表 / 数字 /对象 -序列化->字符串
# 为什么要序列化
    # 1.要把内容写入文件 序列化
    # 2.网络传输数据     序列化
dic = {'name': 'abc', 'age': 18, 'sex': 'man', 'family': ["爸爸","妈妈","姐姐","妹妹"]}
res = json.dumps(dic, ensure_ascii=False, sort_keys=True)
print(res, type(res))

#反序列化，转换成字典   # 字符串-反序列化->字典 / 列表 / 数字 /对象
dic = json.loads(res)
print(dic, type(dic))

#第二组: dump 和 load 用来对数据进行存储
dic = {"name":"abc","age":58,"sex":"man","family":["爸爸","妈妈","姐姐","妹妹"]}
with open("cesi03.json", "w", encoding="utf-8") as fp:
	json.dump(dic, fp, ensure_ascii=False)

with open("cesi03.json", "r", encoding="utf-8") as fp:
	dic = json.load(fp)

print(dic, type(dic)) #<class 'dict'>

# json 和 pickle 两个模块的区别?
#json 用法特征
"""
json 可以连续dump 但是不能连续load
load 只可以load 一次，它是一次性把所有的数据作为一个整体来进行转化
可以使用loads 来进行解决
"""
dic1 = {'a':1,"b":2}
dic2 = {"c":3,"d":4}

with open('ceshi04.json', 'w', encoding='utf-8') as f:
	json.dump(dic1, f)
	f.write('\n')
	json.dump(dic2, f)
	f.write('\n')
#error 只能load 一次， 是一次性把所有数据转化
'''
with open("ceshi04.json",mode="r",encoding="utf-8") as fp:
	res = json.load(fp)
	print(res)
'''
# 想dump多个数据进入文件,用dumps
# dic = {'abc':(1,2,3)}
# lst = ['aaa',123,'bbb',12.456]
# with open('json_demo','w') as f:
#     str_lst = json.dumps(lst)
#     str_dic = json.dumps(dic)
#     f.write(str_lst+'\n')
#     f.write(str_dic+'\n')

# with open('json_demo') as f:
#     for line in f:
#         ret = json.loads(line)
#         print(ret)

#解决方法
with open("ceshi04.json",mode="r",encoding="utf-8") as fp:
	for line in fp:
		res = json.loads(line)
		print(res)

# pickle 用法特征:
'''
pickle 可以连续dump， 也可以连续load
'''
import pickle
dic1 = {'a':1,"b":2}
dic2 = {"c":3,"d":4}

with open("ceshi05.pkl",mode="wb") as fp:
	pickle.dump(dic1, fp)
	pickle.dump(dic2, fp)

with open("ceshi05.pkl",mode="rb") as fp:
	try:
		while True:
			dic = pickle.load(fp)
			print(dic)
	except:
		pass

print(333)

# 文件对象是迭代器么? 是的!
from collections import Iterator
print(isinstance(fp,Iterator))

"""
try ... except ...
把有问题的代码直接卸载try这个代码块当中,
如果出现异常,直接走except这个代码块,防止报错终止程序.
try:
	print(wangwendashuaiguo)	
except:
	pass
"""

#总结
"""
#json 和 pickle 两个模块的区别
	1. json 序列化之后的数据类型是str 所有编程语言都识别
	但是仅限于 int float bool str list tuple dict None
	json 不能连续load 只能一次性拿出所有数据
	# set不能被dump/dumps
	# json的其他参数,是为了用户看的更方便,但是会相对浪费存储空间
	
	2. pickle 序列化之后的数据类型是bytes,
	所有数据类型都可以转化， 便仅限于python之间的存储传输
	pickle 可以连续load 多套数据放到同一个文件中
"""






