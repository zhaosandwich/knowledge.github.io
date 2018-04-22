#6.高级特性
##切片            
L = ['0','1','2','3','4','5','6','7','8','9','10']
- 遍历
```
    for x in range(len(L)):
        print('遍历L数字', L[x])
```         
       
- 顺序切片

```
    print('顺序切片,前面3个')
    K = L[0:3]
    for x in range(len(K)):
    	print(K[x])
```

- 倒序切片倒序切片(L[beginIndex : endIndex])        

```angularjs
    D = L[-2: ]
    for x in range(len(D)):
        print('遍历后面2个参数',D[x])
```

- 间隔切片(F[beginIndex : endIndex : 间隔])   
```angularjs
    F = L[0 : 8 : 2]
    for index in range(len(F)):
    	print('分割取切片', F[index])
    #result = 0,2,4,6,包含了第一个
```  

##迭代
- List和Tuple的迭代
```angularjs
    #List迭代
    for x in L:
    	print('paramer:', x)
    	 
    mapVal = {'a': 1, 'b': 2, 'c': 3}
    
    #Map迭代
    for key in mapVal:
    	print('key:', key)
    	print('val:',mapVal.get(key))
    
    #下标enumerate迭代	
    for index,val in enumerate (L):
    	print('index=', index,'val:', val)
    	
    #二元数组的迭代
    for x,y in {(1,2),(3,4),(5,6),(7,8)}:
    	print('二元数组迭代,顺序无序的,x=',x,'y=',y)
```

- 判断是否可以迭代(先引入collections包)
```angularjs
    from collections import Iterable
    print(isinstance(L,Iterable))
    print(isinstance('asbcd',Iterable))
```

##列表生成式         
用于生成List结构

- range()
```angularjs
    #遍历List
    ListVal = list(range(0,10))
    for val in ListVal:
        print('遍历生成的List结构',val)
```

- for循环
```angularjs
    List = []
    for val in range(0,11):
    	List.append(val)
    print(List)
```

- for中带有for
```angularjs
    # for中包含for
    loop = [x * x for x in range(0,10)]
    print('for中包含for',loop)
```

##生成器           
一边生成一边计算

- 对比生成器与List

L = [1,2,3,4,5]
G = (1,2,3,4,5)

- 定义            
A. G = (1,2,3,4,5)
B. 函数中包含yield
```angularjs
    def fib(max) :
        n,a,b = 0,0,1
        while n < max:
            yield b
            a, b = b, a + b
            n = n + 1
        return 'done'
```
生成器执行时，遇到yield就返回，下次执行从上次跳出的地方继续执行。
另外返回的也是一个生成器

## 迭代器
- for 循环的Iterable : str、list、set、tuple、dict、generator




