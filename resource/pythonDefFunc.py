#!/usr/bin/env python3
print('=========================无值返回=========================')
def returnNone(a, b):
	print('print ++++++')
print(returnNone(1,3))

print('=========================有值返回=========================')

def returnVal(a, b):
	print('has val return')
	return a
print(returnVal(4,5))

print('=========================空处理=========================')
def passFuc(a) :
    print('===pass====', 'a value:' ,a)
    pass
print(passFuc(2))