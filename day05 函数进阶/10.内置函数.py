# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/29 21:23
"""
# ### 内置函数
# abs    绝对值函数
res = abs(-90)
res = abs(-99.7)
print(res)

#round 四舍五入（n.5 n为偶数则舍去，n.5为奇数，则进一！）奇进偶不进
res = round(3.67)
res = round(3.89)
res = round(4.5)
res = round(5.5)
print(res)

#sum 计算一个序列得和
tup = (1,34,34,23,42,34,2,342,43,2,34)
print(sum(tup))
# max    获取一个序列里边的最大值
lst  = [2,4,23,423,42,43,23,4,234,2,34,234,999]
print(max(lst))
lst2 = sorted(lst)
print(lst2)

# 最大值
print(lst2[-1])
# 最小值
print(lst2[0])

# min    获取一个序列里边的最小值 key = 自定义函数
lst  = [2,4,23,423,42,43,23,4,234,2,34,234,999]
res = min(lst)
print(res)

print("<=====>")

"""
('罗1风', 80)
('银2', 81)
('舒3会', 18)
('郭4萌', 90)
"""
lst = [("罗1风",82),("银2",81),("舒3会",18),("郭4萌",90)]
def func(n):
	return n[1] % 10
"""
	0  ("郭4萌",90)
	1  ("银2",81)
	2  ("罗1风",82)
	8  ("舒3会",18)
"""

res = min(lst, key=func)
print(res)

#pow 计算某个数值的x次方
'''
第三次参数是可选项，如果存在，那么前两个数平方之后再和第三个数取余
'''
res = pow(2,3)
print(res)

res = pow(2,3,3)  # 8 % 3
res = pow(2,3,4)
res = pow(2,3,5)
print(res)

#range 产生指定范围数据的可迭代对象
for i in range(5):
	print(i)

for i in range(3,7):
	print(i)

print('====')
for i in range(9,0,-2):
	print(i)

#bin 将10进制数据转化为二进制
print(bin(6))

#oct 将10进制数据转化为八进制
print(oct(9))

#hex 将10 进制数据转化为16进制
print(hex(16))

#chr 将ASCII编码转换为字符
print(chr(97))

#ord 将字符转换为ASCII 编码
print(ord('A'))

#eval 将字符串当作python代码执行
strvar = 'print(1234)'
res = eval(strvar)
#print(res) # eval返回值没有意义,直接执行即可

strvar = 'wangwen = "宇宙最帅的人啊"'
# eval(strvar) error eval 执行部分字符串时,比如声明变量,是不允许的

#exec 将字符串当作python 代码执行（功能更强大）
strvar = 'wangwen = "宇宙最帅的人啊"'
exec(strvar)
print(wangwen)
strvar = """
for i in range(10):
	print(i)
"""
exec(strvar)

#repr 不转义字符输出字符串(原型化输出)
strvar = '老男孩老师来到深圳校区视察工作\n每个员工表现的非常积极'
res = repr(strvar)
print(res)
# input  接受输入字符串,程序会添加阻塞
#res = input("先森,你妈贵姓?")
#print(res)

#hash 生成哈希值
strvar1 = "保定爱迪生,狄龙,专门早无用发明"
strvar2 = "保定爱迪生,狄龙,专门早无用发明"
print(hash(strvar1))
print(hash(strvar2))



































