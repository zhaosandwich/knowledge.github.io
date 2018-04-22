#2.条件判断
##例子               
> 判断语句:执行缩进的两行print语句执行          
         
```angular2html
    a = ['1','2','3']
    if len(a) > 5:
        print('len bigger 5')
    elif len(a) > 4:
        print('len bigger 4') 
    else:
        print('less than 4')
```

#循环
- for循环         
```angular2html
    a = range(5)
    for b in a:
        print('circle show a member:', b)
```

- while循环
```angular2html
    a = 10
    while a > 0:
        if a % 2 == 0:
            print('打印偶数:', a)
        else:
            print('will be break,member:', a)
        a = a - 1
```
- break
```angular2html
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
```

- continute
```angular2html
    natureNumber = [2,4]
    for n in natureNumber:
        if n > 2:
            print('n:', n, 'will be continute')
            continue
        else:
            print('now number :', n)
        print('ok n=',n)
```








    


      
 

 