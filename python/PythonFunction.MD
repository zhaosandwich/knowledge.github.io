#4.函数
##help
对函数用法的解释            
````angular2html
    help(abs)：是对函数用法的解释说明
````

##abs                      
-  对数值取正数               
    abs(-67) = 69           
    abs(78) = 78
##max
-  对数值取最大值
    max(89, 1000)

##类型转换
 - 字符串转整数int                
 a = int('-90') = -90         
 - 字符串转float                
 a = float('0.1234') = 0.1234            
 - 整数转字符串str                               
 a= str(9090)  = ‘9090’          
 - 整数、字符串转bool                  
 boole wether = bool(1) = True      
 
 #自定义函数
 ##普通函数             
 > 定义函数名，参数列表（不需要类型），冒号，缩进语句，返回(可有、可无)
    
 ````angular2html
    #自定义函数
    print('-------compare number-------')
    def compare (a, b) :
    	if a > b:
    		print(' a > b. a=%s,b=%s'%(a, b))
    	else :
    		print(' a <= b. a=%s,b=%s'%(a,b))
    print('definition function, compare result:',compare(9, 10))
    #definition function, compare result: None
````

##默认参数
```angular2html
    print('----------默认参数-----------')
    def demoParamter(a, b, c='ok'):
        if c == 'ok':
            print('default parameter effect')
        else :
            print('input a={},b={},c={}'.format(a, b, c))
        return c
    
    demoParamter('inputA', 'inputB', 'inputC')
    
    demoParamter('inputA', 'inputB')
    
   注：定义的函数要在调用的前面，程序是顺序执行，定义与调用顺序不同会出现问题

```