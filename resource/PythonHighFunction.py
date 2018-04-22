# --------------------map用法--------------------
# print('map 用法')
# def functionMap(val):
# 	return val * val

# L = map(functionMap, [1,2,3,4,5,6])
# from collections import Iterable
# print(isinstance(L,Iterable))

# for x in L:
# 	print(x)

#--------------------reduce用法--------------------
# from functools import reduce
# print('reduce用法')
# def functionReduce(x, y):
# 	return x + y

# print(reduce(functionReduce, [1,2,3,4,4,5]))

#--------------------filter用法--------------------
# print('filter用法')
# def functionFlier(val):
# 	return val > 5;

# f = filter(functionFlier, range(0,10))
# for v in f:
# 	print('遍历输出after filter result:', v)

#--------------------sorted用法--------------------
# print('sorted用法')
# r = [1,2,3,4,5,6,7,8,9];
# r.append(-1)
# print(sorted(r))

#--------------------匿名函数用法--------------------
# print('匿名函数用法')
# n = list(map(lambda x : x * x, [1,2,3,4,5,6,7,8,9]))
# for x in n:
# 	print('遍历匿名函数结果', x)


#--------------------装饰器用法--------------------

def log(func):
	def wrapper(*args, **kw):
		print('call  %s():' % func.__name__)
		return func(*args, **kw)
	return wrapper

@log
def now():
	print('20180301')
	return 'now time'

print(now())
#@log放到了now的上方，相当于执行了now = log(now)