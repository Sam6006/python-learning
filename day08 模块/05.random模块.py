import random
#随机：在某个范围内取到每一个值的概率是相同的

#随机小数
print(random.random()) # 0-1之内的随机小数
print(random.uniform(1,5)) #任意范围之内的随机小数

#随机整数 *****
print(random.randint(1,5)) #[1,5] 包含5在内的范围内随机整数 只能给2个参数
print(random.randrange(1,2)) #[1,2] 不包含2在内的范围内随机整数
print(random.randrange(1,10,2)) #[1,10] 不包含10在内的范围内随机取奇数

#随机抽取
#随机抽取一个值
lst = [1,2,3,'aa',('wahaha', 'qqxing')]
ret = random.choice(lst)
print(ret)


# 自定义choice
def mychoice():
	length = len(lst)
	res = random.randrange(0,length)
	return lst[res]
print(mychoice())

#随机抽取多个值 [返回列表]
ret = random.sample(lst,2)
print(ret)

#打乱顺序 在原列表的基础上做乱序
lst = [1,2,3,'aa',('wahaha', 'qqxing')]
random.shuffle(lst)
print(lst)

