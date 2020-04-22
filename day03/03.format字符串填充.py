# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/15 11:55
"""

# format 字符串填充
#format的填充符号的使用(^ ><)
"""
^ 原字符串居中
> 原字符串居右
< 原字符串居左

语法：
{who:*>10}
* 要填充的字符
> 原字符串居右
10 原字符个数+要填充的个数 = 长度10
"""
strvar = "{who:*^10}在长春长生公司{something:!<10},感觉{feel:>>8}"
res = strvar.format(who='李祖庆',something='扎疫苗',feel='爽歪歪')
print(res)

#进制转换等特殊符号的使用(:d :f :s :,)
'''
:d 整数占位符
:f 浮点数占位符
:s 字符占位符
:, 金钱占位符
'''

#:d
strvar = 'alex买了{:d}个棒棒糖'
res = strvar.format(3)
print(res)

#:2d 占用2位 默认原字符居右
strvar = 'alex买了{:2d}个棒棒糖'
res = strvar.format(3)
print(res)

#:^3d 占用3位，原字符居中
strvar = 'alex买了{:^3d}个棒棒糖'
res = strvar.format(3)
print(res)

#:f 浮点型占位符
strvar = '买一斤西红柿的价格是{:f}'
res = strvar.format(3.6)
print(res)

#:.2f 小数点后保留二位
strvar = '买一斤西红柿的价格是{:.2f}'
res = strvar.format(3.6)
print(res)

#:s 字符串占位符 format 不能默认强转，只能是填充什么样式的格式，就写什么样的数据
strvar = '{:s}'
res = strvar.format('你好啊，大妹子')
#res = strvar.format(3.567) ValueError: Unknown format code 's' for object of type 'float'
print(res)

#如果是%号用法 默认会进行强制转换，强转，但是format格式化时不会执行
strvar = "%s" % (3.14334)
print(strvar)

#:,金钱占位符
strvar = '{:,}'
res = strvar.format(12345678910)
print(res)

# 综合案例
strvar = "黄花买了{:d}个布加迪威龙,价格{:.1f},心情{:s}"
res = strvar.format(3,9.9,"好极了")
print(res)