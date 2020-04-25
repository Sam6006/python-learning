import random

# 抽奖 \ 彩票 \发红包 \验证码 \洗牌

#生成随机验证码
#4位数字的

#0-9
#基础版本
code = ''
for i in range(4):
	num = random.randint(0, 9)
	code += str(num)
print(code)

#函数版本
def rang_code(n= 4):
	code = ''
	for i in range(n):
		num = random.randint(0, 9)
		code += str(num)
	return code
print(rang_code())
print(rang_code(6))

#6位数字 + 字母
print(chr(97))
print(chr(122))

#基础版
code = ''
for i in range(6):
	rand_num = str(random.randint(0,9))
	rand_alph = chr(random.randint(97,122))  #小写字母
	rand_alph_upper = chr(random.randint(65,90)) #大写字母
	autom_code = random.choice([rand_num,rand_alph,rand_alph_upper])
	code += autom_code

print(code)


#函数版
def rand_code(n= 6):
	code = ''
	for i in range(n):
		rand_num = str(random.randint(0, 9))
		rand_alph = chr(random.randint(97, 122))  # 小写字母
		rand_alph_upper = chr(random.randint(65, 90))  # 大写字母
		autom_code = random.choice([rand_num, rand_alph, rand_alph_upper])
		code += autom_code
	return code

ret = rand_code()
print(ret)

#数字/数字+ 字母
def rand_code(n= 6, alph_flag= True):
	code = ''
	for i in range(n):
		rand_num = str(random.randint(0, 9))
		if alph_flag:
			rand_alph = chr(random.randint(97, 122))  # 小写字母
			rand_alph_upper = chr(random.randint(65, 90))  # 大写字母
			rand_num = random.choice([rand_num, rand_alph, rand_alph_upper])
		code += rand_num
	return code

ret = rand_code(alph_flag=False)
print(ret)