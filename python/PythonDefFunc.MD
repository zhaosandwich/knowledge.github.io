#5.自定义函数        
## 格式
   def +函数名称+入参(入参不需要定义类型)+冒号+函数体,
   函数的返回值用return，否则返回None。区别如下
   ```angular2html
     def returnNone(a, b):
        print('print ++++++')
      print(returnNone(1,3))
      
      print('=========================分割线=========================')
      
      def returnVal(a, b):
        print('has val return')
        return a
       print(returnVal(4,5))
       
  结果:
  print ++++++
  None
  =========================分割线=========================
  has val return 4
```

##空处理
```angular2html
    对函数，如果没有任何的操作，可以使用pass
    def passFuc(a) :
        print('===pass====', 'a value:' ,a)
        pass
     print(passFuc(2))
     
 结果:
 ===pass==== a value: 2
 None
```

##返回值
- 单个值

- 多个值(Tuple)
```angularjs
    def move(x, y, step, angle=0):
        nx = x + step * math.cos(angle)
        ny = y - step * math.sin(angle)
        return nx, ny
```


