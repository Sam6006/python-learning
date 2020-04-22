# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/15 11:43
"""
# format 字符串格式化的传参方式
'''
{}是format语法中的占位符
'''
#顺序传参
strvar = '{}向{}开了一枪，饮弹而亡'
strvar = strvar.format('alice','sam')
print(strvar)

#索引传参
strvar = '{1}给{0}一个大大的拥抱'
strvar = strvar.format('alex','nick')
print(strvar)

#关键字传参
strvar = "{shuile}给{wubo}一个飞吻"
strvar = strvar.format(wubo= '吴波', shuile = '帅乐')
print(strvar)

#容器类型数据（列表或元组）传参
strvar = '{0[1]}向{1[2]}抛了一个媚眼，神魂颠倒,鼻血直冒三万多尺'
res = strvar.format(["舒则会","郭一萌","刘璐"],("李祥海","孙兆强","无要诀"))
print(res)

#format当中如果是获取字典对应的值，不要加上引号
strvar = "{group2[qgqc]}向{group1[2]}抛了一个媚眼，神魂颠倒,鼻血直冒三万多尺"
res = strvar.format(group1=["邓良辉","刘志华","王文贤"],group2={"fhcm":"舒则会","byxh":"郭一萌","qgqc":"罗淞峰"})
print(res)