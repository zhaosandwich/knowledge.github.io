#!/usr/bin/env python3
# -*- voding:utf-8 -*-
#判断大小
sum = '0'
a = ['1','2','3']
for number in a:
	sum = sum + number
print('输出结果为:',sum)

#for循环

#range()循环
a = range(5)
for b in a:
	print('circle show a member:', b)
	
#while循环

a = 10
while a > 0:
	if a % 2 == 0:
		print('打印偶数:', a)
	else:
		print('will be break,member:', a)
	a = a - 1

#break

natureNumber = [2,4]
for number in natureNumber:
	if number > 3:
		break
	else:
		number = number + 1
		print('number increase one,number:' , number)
print('after circle')

for number in natureNumber:
	print('number:',number)

#continue
natureNumber = [2,4]
for n in natureNumber:
	if n > 2:
		print('n:', n, 'will be continute')
		continue
	else:
		print('now number :', n)
	print('ok n=',n)
