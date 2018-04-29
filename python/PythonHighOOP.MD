#10.面向对象高级编程

##__slots__对属性进行限制

class Student(object):
    __slots__=('name','age') # 用tuple定义允许绑定的属性名称

##注解setter、getter
```
class InjectSetterAndGetter(object):
    @property
    def score(self):
        return self._name

    @score.setter
    def score(self, value):
        self._name = value

print ('注解方式设置值')
s = InjectSetterAndGetter()
s.score = 90
print (s.score)
```

##多重继承

