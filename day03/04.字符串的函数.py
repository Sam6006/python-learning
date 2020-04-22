# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/15 12:12
"""
#字符串.函数()
#capitalize 字符串首字母大写
strvar = 'i love you baby'
print(strvar.capitalize())

#title 每个单词的首字母大写  非字母隔开的单词
strvar = 'i hate you bigbrother'
res = strvar.title()
print(res)

#upper 将所有字母变成大写
strvar = "you love me"
res = strvar.upper()
print(res)

#lower 将所有字母变成小写
strvar = "I MISS YOU"
res = strvar.lower()
print(res)

#swapcase 大小写互换
strvar = 'to BE or Not to be'
res = strvar.swapcase()
print(res)

#count 统计字符串中某个元素的数量
res = "是生是死,的确是一个问题".count("是")
print(res)

#find 查找某个字符串第一次出现的索引位置
'''find('字符串',[开始索引，结束索引]) 结束索引的最大值取不到'''
strvar = "Oh father this is my favorite girls"
res = strvar.find('father')
print(res)
res = strvar.find("s",3)
print(res) # 13
# 14~17的这个索引区间找s这个字符的索引号,最大值是取不到的;
res = strvar.find("s",14,18)
print(res)

#如果找不到直接返回-1，表达没有
res = strvar.find('你')
print(res)
#index 与find 功能相同， find 找不到返回-1，而index找不到数据直接报错
#res = strvar.index('你') ValueError: substring not found
#print(res)

#startswith 判断是否以某个字符或字符串开头
"""endswith,startswith(字符串,[开始索引,结束索引]) 结束索引最大值取不到"""
strvar = "Oh father this is my favorite girls"
res = strvar.startswith('Oh')
print(res)

res = strvar.startswith('father',3)
res = strvar.startswith('father',4)
print(res)

#endswith 判断是否以某个字符或字符串结尾
res = strvar.endswith('girls')
print(res)

#split 按某个字符将字符串分割成列表（默认字符是空格）
strvar = 'you can you up no can no bb'
res = strvar.split()
print(res)

strvar = 'you,can,you,up,no,can,no,bb'
res = strvar.split(',')
print(res)
#可以选择分隔的次数
res = strvar.split(',',4)
print(res)

# rsplit 从右向左分隔
res = strvar.rsplit(",")
print(res)
# 一样可以选择分隔的次数
res = strvar.rsplit(",",4)
print(res)

#join 按某字符将列表拼接成字符串（容器类型都可以）
lst = ['you', 'can', 'you', 'up', 'no', 'can', 'no', 'bb']
res = '-'.join(lst)
print(res)

#replace 替换字符串（可选择替换的次数）默认替换所有
strvar = "可爱的小狼狗喜欢吃肉,有没有,有没有,还有没有"
# replace(替换谁，替换成什么，[替换几次])
res = strvar.replace('有没有', '真没有')
print(res)

res = strvar.replace("有没有","真没有",2)
print(res)

#isalnum 判断字符串是否是由数字，字母，汉字组成
strvar= "2342sdfsd你好&*&*"
strvar= "2342sdfsd你好"
res = strvar.isalnum()
print(res)

#isdigit 检测字符串数是数字组成，接受二进制字节流
'''
二进制字节流，传输数据，存储数据
字符串： 一个一个字符组成
字节流：一个一个字节组成
1byte = 8bit
1B = 8b

语法格式：b'字符串'

注意点：
b开头的二制字节流，里面的字符编码只能是ascii编码
encode
decode
用来转换中文变成二进制的字节流，中文前面加b是错误的

strvar = b"1234454" # 二进制字节流
# strvar = b"你好上" error

'''
#isdecimal 检测字符串是否以数字组成， 必须是纯数字
strvar = '12334'
res = strvar.isdecimal()
print(res)

#len 计算容器类型数据长度
strvar = "阳光洒在手指间"
res = len(strvar)
print(res)

#center 填充字符串，原字符串居中（默认填充空格）
strvar = 'alic'
#10是一共的长度，原字符串长度+ 填充字符=10
#center(长度,[要填充的字符，默认不写填充空格])
res = strvar.center(10)
res = strvar.center(10,"%")
print(res)

#strip 默认去掉首尾两边的空白符
"""网站注册的时,在存在数据库之前,先处理两边的空白符"""
strvar = "           							刘德华     "
res = strvar.strip()
print(res)

strvar = "@王战"
res = strvar.strip("@")
print(res)


