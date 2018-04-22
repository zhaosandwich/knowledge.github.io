#7.高阶函数           
将函数作为参数传入
map/reduce

- map           
入参是function、Iterable,返回Iterable

```angularjs
    #map
    print('map 用法')
    def functionMap(val):
    	return val * val
    
    L = map(functionMap, [1,2,3,4,5,6])
    from collections import Iterable
    print(isinstance(L,Iterable))
    
    for x in L:
    	print(x) 
    	
  map入参数时functionMap只需要传入函数名称即可，
  不用传参数:functionMap(val)
```

- reduce        
入参数function、Iterable,将结果累积，再与下一个序列做运算
```angularjs
    from functools import reduce
    print('reduce用法')
    def functionReduce(x, y):
    	return x + y
    
    print(reduce(functionReduce, [1,2,3,4,4,5]))
    #functionReduce函数的定义需要是2个入参，1个会报错
```

- filter        
用法与map类似，入参是function、Iterable,返回Iterable    
```angularjs
    print('filter用法')
    def functionFlier(val):
    	return val > 5;
    
    f = filter(functionFlier, range(0,10))
    for v in f:
    	print('遍历输出after filter result:', v)
```

- sorted        
```angularjs
    print('sorted用法')
    r = [1,2,3,4,5,6,7,8,9];
    r.append(-1)
    print(sorted(r))
```

- 匿名函数
```angularjs
    print('匿名函数用法')
    n = list(map(lambda x : x * x, [1,2,3,4,5,6,7,8,9]))
    for x in n:
    	print('遍历匿名函数结果', x)
    #lambda中的x指代参数，有限制就是只能有一个表达式 x * x 
```

- 装饰器           
```angularjs
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
```







