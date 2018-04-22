print('abs(-90)=', abs(-90))
print('max(90,-100)=', max(90,-100))
a = int('90')
print('类型转换int,int(\'90\')=', a)
print('整数转16进制数', hex(9090))
print('布尔值bool(1)', bool('1'))

#自定义函数
print('-------compare number-------')
def compare (a, b) :
	if a > b:
		print(' a > b. a=%s,b=%s'%(a, b))
	else :
		print(' a <= b. a=%s,b=%s'%(a,b))

print('definition function, compare result:',compare(9, 10))
definition function, compare result: None



#默认参数
print('----------默认参数-----------')
def demoParamter(a, b, c='ok'):
	if c == 'ok':
		print('default parameter effect')
	else :
		print('input a={},b={},c={}'.format(a, b, c))
	return c

demoParamter('inputA', 'inputB', 'inputC')

demoParamter('inputA', 'inputB')






	
