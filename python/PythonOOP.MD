#9.面向对象编程

##类       
    * class   
    * className(首字母大写) 
    * 类继承自那个类,默认是object
    eg：
        class  ClassNameDemo(object) :
            pass

##实例      
    class ClassNameDemo(object) :
        def __init__(sellf, param1,param2) :
            self.param1 = param1
            self.param2 = param2
            
     cl  = ClassNameDemo(1, 2);
     print(cl)
     
     说明:				
     * 实例方法名称固定__init__
     * 实例__init__的参数，第一个必须是self
     * 类中存在__init__,则类的创建必须有参数，且第一个参数不传值
     * 类内的方法，参数第一个必须是self
     *  初始化方法在外部也可以调用
  
##封装			
    通过类，向外提供方法，方法对内调用方法，实现数据、方法的
    封装
    
##访问限制 					 
    变量声明作为私有，则需要将变量的前缀加双下划线
    __name				
    *这种情况是不允许外部的方法对变量进行访问。注:区分前后双下划线的情况__name__(t特殊变量)
    *外部修改__param私有参数的问题
      eg: bart.__name = 'New Name' # 设置__name变量,并没有设置内部的私有变量，
     而是声明了一个变量
    
    
