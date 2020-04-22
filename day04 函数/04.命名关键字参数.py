# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/24 21:56
"""
#命名关键字参数
'''
1. def func(a,b,*,参数1，参数2） 在*后面定义的参数就是命名关键字参数
2. def func(*args,参数，**kwargs) 夹在普通收集参数和关键字收集参数之间的是命名关键字参数
如果命名关键参数，必须使用关键字实参进行调用赋值
'''
#方法1
def func(a,b,*,c,d):
	print(a,b)
	print(c,d)
func(1,2,c=3,d=4)

#方法2
def func(*args,c,**kwargs):
	print(args)
	print(c)
	print(kwargs)

func(1,2,34,5,a=1,b=2,c=3)

#方法3
def func(a,b,*,c=3):
	print(a,b)
	print(c)

#func(1,2)
func(1,2,c=22)
# 区别于默认形参
def func(a,b,c=3):
	print(a,b)
	print(c)
# 三种方式皆可
func(1,2)
func(1,2,c=22)
func(1,2,22)

# * 和 ** 的魔术用法
'''
	在函数的定义处：* ** 相当于打包操作 （一个是元组，一个是字典）
	在函数的调用处：* ** 相当于解包操作 （把里面的元素一个一个拿出来，当成实参调用赋值）
'''
#*
def func(a,b,c):
	print(a,b,c)

lst = [1,2,3]
func(*lst) #相当于func(1,2,3) 把列表里面的每个元素都单独拿出来当成参数进行函数调用

#**
def func(a,*,b,c,d):
	print(a)
	print(b,c,d)

dictvar = {'b':2,'c':3,'d':4}
func(1,**dictvar) #相当于func(1,b=2,c=3,d=4) 把字典里面的每个键值对，都拿出来，变成键=值的形式,进行关键字实参赋值操作

#扩展
#函数的定义处
def func(a,b,*,c,d):
	print(a,b)
	print(c,d)

lst = [1,2]
dictvar = {'c':3,'d':4}
#函数的调用处
func(*lst,**dictvar)

'''
在字典的前面加上一个*号，默认只传递键
一个*号 后面可以跟str list tuple set dict 常用的一般就是list
二个** 后面可以跟dict 把 键值对变成键=值的形式进行函数调用
'''
def func(a,b):
	print(a,b)

dictvar = {'c':3,'d':4}
func(*'pa')

'''
函数的定义处：参数的定义有顺序
普通形参 -> 默认形参 -> 普通收集参数 -> 命名关键字参数 -> 关键字收集参数

def func(*args,**kwargs):  这样的形式定义函数，可以接收到所有种类的参数
	pass

'''
# 参数练习:
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

#(一)
# f1(1, 2) # a=1,b=2,c=0,args=(),kw={}
# f1(1, 2, c=3) #a=1,b=2,c=3,args=(),kw={}
# f1(1, 2, 3, 'a', 'b') # a=1,b=2,c=3,args=(a,b),kw={}
# f1(1, 2, 3, 'a', 'b', x=99)#a=1,b=2,c=3,args=(a,b),kw={x:99}
# f2(1, 2, d=99, ext=None)#a=1,b=2,c=0,d=99,kw={ext:None}

#(二)
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
# f1(1,2,3,4,d=99,x="#")
f1(*args, **kw) #a=1,b=2,c=3,args=(4,),kw={'d':99,x:'#'}

#(三)
myargs = (1, 2, 3)
mykw = {'d': 88, 'x': '#'}
f2(*myargs, **mykw) #a=1,b=2,c=3,d=88,kw={x:'#'}


#(四) a b 普通形参  c 默认形参 *args 普通收集参数 d 命名关键字参数 kw 关键字收集参数
def f1(a, b, c=0, *args,d,**kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
    print(d)

f1(1,2,3, 'a', 'b',d=67, x=99,y=77) #a=1,b=2,c=3,d=67,args=(a,b),kw={,x:99,y:77}

















