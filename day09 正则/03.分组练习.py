# ret=re.compile('-0\.\d+|-[1-9]\d*(\.\d+)?')
# c=ret.search('-1asdada-200')
# print(c.group())
# c1=ret.findall('-1asdada-200')
# print(c1)

import re

#findall 和 split遇上分组
ret = re.findall('-0\.\d+|-[1-9]\d*(\.\d+)?', '-lasdada-200')
print(ret)

ret = re.findall('www.baidu.com|www.google.com', 'www.baidu.com')
print(ret) #['www.baidu.com']

#优先匹配分组里的内容
ret = re.findall('www.(baidu|google).com', 'www.baidu.com')
print(ret) #['baidu']

#取消分组优先 (？：正则表达式 )
ret = re.findall('www.(?:baidu|google).com', 'www.baidu.com')
print(ret) #['www.baidu.com']

#split 遇到分组，会保留分组内被切掉的内容
ret = re.split('(\d+)','sam84abc30adb40')
print(ret) #['sam', '84', 'abc', '30', 'adb', '40', '']


#分组遇上search  如果search中有分组的话,通过group(n)就能够拿到group中的匹配的内容
ret = re.search('\d+(.\d+)(.\d+)(.\d+)?','1.2.3.4-2*(60+(-40.35/5)-(-4*3))')
print(ret.group())
print(ret.group(1)) #.2
print(ret.group(2)) #.3
print(ret.group(3)) #.3


ret=re.findall(r"\d+(?:\.\d+)?","1-2*(60+(-40.35/5)-(-4*3))")
print(ret) #['1', '2', '60', '40.35', '5', '4', '3']

ret = re.findall(r"\d+(?:\.\d+)|(\d+)","1-2*(60+(-40.35/5)-(-4*3))")
print(ret) #['1', '2', '60', '', '5', '4', '3']
ret.remove('')
print(ret)

#标签匹配
ret = re.findall('>(\w+)<', r'<a>wahaha</a>')
print(ret) #['wahaha']

ret = re.search(r'<(\w+)>(\w+)</(\w+)>',r'<a>wahaha</b>')
print(ret.group()) #<a>wahaha</b>
print(ret.group(1))
print(ret.group(2))

#分组命名
#<(?P<组名>正则表达式)>正则表达式</(?P=组名)>
	# (?P<name>正则表达式) 表示给分组起名字
	# (?P=name)表示使用这个分组,这里匹配到的内容应该和分组中的内容完全相同
ret = re.search('<(?P<name>\w+)>\w+</(?P=name)>', '<h1>hello</h1>')
print(ret.group('name')) #h1
print(ret.group()) #<h1>hello</h1>

#<(\w+)>\w+</\1>
# 通过索引使用分组
	 # \1 表示使用第一组,匹配到的内容必须和第一个组中的内容完全相同
ret = re.search(r'<(\w+)>\w+</\1>', '<h1>hello</h1>')
print(ret.group()) #<h1>hello</h1>

ret = re.search(r'<(?P<tag>\w+)>(?P<c>\w+)</(\w+)>',r'<a>wahaha</b>')
print(ret.group())
print(ret.group('tag'))
print(ret.group('c'))

# 正则指引---书推荐
# python语言为基础 来讲解正则表达式