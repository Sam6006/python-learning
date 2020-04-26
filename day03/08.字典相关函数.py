# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/22 12:58
"""
#字典相关函数
# 1.增
dictvar = {}
dictvar["fhzm"] = "舒11"
dictvar["byxh"] = "郭22"
dictvar["qgqc"] = "罗33"
dictvar["cyly"] = "银33"
dictvar["ttyl"] = "刘33"
print(dictvar)

#fromkeys() 使用一组键和默认值创建字典（返回新字典）
lst = ['a','b','c']
dit = {}.fromkeys(lst,None)
print(dit)

# fromkeys 不推荐使用,三个键所指向的是同一个列表;
dictvar = {}.fromkeys(lst,[1,2,3])
print(dictvar)
dictvar["a"].append(4)
print(dictvar)

# 2.删
dictvar = {'fhzm': '舒11', 'byxh': '郭一1', 'qgqc': '罗11', 'cyly': '银11', 'ttyl': '刘11'}
# 2.1 pop()       通过键去删除键值对 (若没有该键可设置默认值,预防报错)
res = dictvar.pop('cyly')
print(res)
print(dictvar)
# 当删除一个不存在的键时,直接报错,
# res = dictvar.pop("xboyww") error
# 为了预防报错,可以设置默认值
res = dictvar.pop("xboyww","设置默认值,该神秘男子不存在")
print(res)
print(dictvar)

# popitem（）删除最后一个键值对
dictvar = {'fhzm': '舒11', 'byxh': '郭一1', 'qgqc': '罗11', 'cyly': '银11', 'ttyl': '刘11'}
res = dictvar.popitem()
print(res)
print(dictvar)

# 2.3 clear()  清空字典
dictvar.clear()
print(dictvar)

# 3.改
#update() 批量更新(有该键就更新,没该键就添加)
dictvar = {"鼓上骚":"石阡","母夜叉":"杜十娘","浪里白条":"张顺","花和尚":"录制山","入云龙":"公孙上","黑旋风":"李奎"}
# 更新方式1 (推荐)
dictvar.update(  {"神秘男孩":"王文","闭月羞花":"郭一萌","倾国倾城":"罗送风","入云龙":"公孙胜"}   )
print(dictvar)

# 更新方式1
dictvar.update( zhiduoxing="吴用",jishiyu = "宋江" )
print(dictvar)

# 4.查
#get()    通过键获取值(若没有该键可设置默认值,预防报错) 最大的好处在没有该键的时候不报错
dictvar = {"鼓上骚":"石阡","母夜叉":"杜十娘","浪里白条":"张顺","花和尚":"录制山","入云龙":"公孙上","黑旋风":"李奎"}
res = dictvar.get("母夜叉123")
print(res) # None
# 设置默认值
res = dictvar.get("母夜叉123","该母老虎没有")
print(res)

#其他
#keys()将字典的键组成新的可迭代对象
dictvar = {"鼓上骚":"石阡","母夜叉":"杜十娘","浪里白条":"张顺","花和尚":"录制山","入云龙":"公孙上","黑旋风":"李奎"}
res1 = dictvar.keys()
print(res1)
#values() 将字典中的值组成新的可迭代对象
res2 = dictvar.values()
print(res2)

#items()  将字典的键值对凑成一个个元组,组成新的可迭代对象
res3 = dictvar.items()
print(res3)

for i in res3:
	print(i)


