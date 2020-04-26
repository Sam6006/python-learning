# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/2 22:52
@Auth ： Sam
@File ：05.字符串str.py
@IDE ：PyCharm
"""
# ### 字符串类型  用引号引起来的就是字符串
"""
转义字符：语法 \ 来进行转义
	把有意义的字符变得无意义
	把无意义的字符变得有意义
	
\n 换行
\r\n 换行
\r 把\r后面的字符串直接拉到当前行的行首
\t 缩进（水平制表符) 一般一个\t 是4个空格的间隔
"""
# 1.单引号
strvar = '我爱你亲爱的菇凉,见到你我就心慌'
print(strvar)
print(type(strvar))

# 2.双引号
strvar = "黑夜给了我黑色的眼睛,但我却用它翻白眼"
strvar = "黑夜给了我黑色的眼睛,\n但我却用它翻白眼"
strvar = "黑夜给了我黑色的\n眼睛,\r但我却用它翻白眼"
strvar = "黑夜给了我黑色的\r\n眼睛,\t但我却用它翻白眼"
strvar = "黑夜给了我黑色的'眼睛',但我却用它翻白眼"
# \ 除了可以把无意义的字符变得有意义,也可以吧有意义的字符变得无意义.
strvar = "黑夜给了我黑色的\"眼睛\",但我却用它翻白眼"
print(strvar)
print(type(strvar))

# 3.三引号 可以支持跨行操作
strvar = """轻轻的我走了,正如我轻轻的来
我轻轻的挥一挥手,不带走一片云彩
"""
strvar = '''轻轻的我走了,正如我轻轻的来
我轻轻的挥一挥手,不带走一片云彩
'''
print(strvar)

# 4 元字符串r + "字符串“ 让转义字符失效
strvar = r"asdfasdf\tsdfsd\n3242"
print(strvar)

#5.字符串的格式化
"""
%d 整型占位符
%f 浮点型占位符
%s 字符串占位符
语法：
"字符串" %（值1，值2 。。）
"""

# %d
strvar = "树则会买了%d个面膜"   %    (10)
print(strvar)

#%2d 默认数字居右
strvar = "alex买了%2d个布加迪威龙" % (7)
print(strvar)
# %-2d默认数字居左
strvar = strvar = "alex买了%-2d个布加迪威龙" % (7)
print(strvar)

# %f 小数点部分自动保存6位小数
strvar = "黄花昨天开工资了,发了%f元" % (9.989)
print(strvar)
# %.2f 小数点保留二位 存在四舍五入
strvar = "黄花昨天开工资了,发了%.2f元" % (9.989)
print(strvar)

#%s 字符串占位符
strvar = "%s" %("好看的皮囊千篇一律,有趣的灵魂300多斤")
print(strvar)

#综合案例
strvar = "%s开工资了,发了%.2f元,昨天晚上买了%d个娃娃,心情%s" % ("小明",99.1234,2,"感觉身体被掏空")
print(strvar)

