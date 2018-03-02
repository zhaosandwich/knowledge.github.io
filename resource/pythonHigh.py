#高级特性
L = ['0','1','2','3','4','5','6','7','8','9','10']


# #遍历
# for x in range(len(L)):
# 	print('遍历L数字', L[x])

# #顺序切片
# print('顺序切片,前面3个')
# K = L[0:3]
# for x in range(len(K)):
# 	print(K[x])

# 倒序切片(L[beginIndex : endIndex])
# D = L[-2: ]
# for x in range(len(D)):
# 	print('遍历后面2个参数',D[x])


#分割取切片(F[beginIndex : endIndex : 间隔])
# F = L[0 : 8 : 2]
# for index in range(len(F)):
# 	print('分割取切片', F[index])
#	# result = 0,2,4,6,包含了第一个


#-------------迭代--------------

# for x in L:
# 	print('List迭代')
#     print('paramer:', x)

# mapVal = {'a': 1, 'b': 2, 'c': 3}

# for key in mapVal:
# 	print('map迭代')
# 	print('key:', key)
# 	print('val:',mapVal.get(key))

# #下标迭代
# for index,val in enumerate (L):
# 	print('index=', index,'val:', val)

# #二元数组迭代
# for x,y in {(1,2),(3,4),(5,6),(7,8)}:
# 	print('二元数组迭代,顺序无序的,x=',x,'y=',y)

# #判断是否可迭代
# from collections import Iterable
# print(isinstance(L,Iterable))
# print(isinstance('asbcd',Iterable))

# --------------列表生成式---------------
# #range生成
# val = list(range(0,10))

# #遍历List
# List = []
# for val in range(0,10):
# 	List.append(val)
# print(List)

# for中包含for
# loop = [x * x for x in range(0,10)]
# print('for中包含for',loop)

#生成器(对比数组是[1,2,3,4,5,6])

# 定义
G = (1,2,3,4,5,6)
from collections import Iterable
print(isinstance(G, Iterable))
for mumber in G:
	print('mumber:', mumber)


	









	
