#!/usr/bin/env python3
# -*- voding:utf-8 -*-
#判断大小
a = ['1','2','3']
for i in a:
	print('遍历a集合', i)
	
#dirt初始化
d = {}

d = {'姓':'zhao','名称':'shanwei'}

#dirt增加
d['GO'] = 'zhao' 
print(d['GO'])

#dirt删除
d.pop('姓')
#print(d['姓']) error

#dirt获取
d.get('姓')#ok
d.get('')
#d['姓']   #error，因为前面删除了

#dirt遍历
##对key遍历
for i in d:
	print('foreach key dirt')
	print(d.get(i))
##dirt对items遍历
for (k,v) in d.items():
	print('foreach dirt items')
	print('key:', k,'value:',v)
	
#set集合
#初始化
s = set([9])
print(s)
#添加
s.add(8)
print(s)
#删除
s.remove(9)
print(s)
#遍历
print('遍历Set')
s.add(10)
for k in s:
	print('遍历Set成员:',k)

	
