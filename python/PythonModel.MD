#8.模块           
```angularjs
    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
    
    ' a test module '
    
    __author__ = 'Sandwich'
    
    import sys
    
    def test():
        args = sys.argv
        if len(args)==1:
            print('Hello, world!')
        elif len(args)==2:
            print('Hello, %s!' % args[1])
        else:
            print('Too many arguments!')
    
    def modelMethod() :
        print('okokokok')
    
    
    if __name__=='__main__':
        test()
        modelMethod()
```
##变量作用范围
    一般使用__name作为命名的规范
    
##外部包的引用
