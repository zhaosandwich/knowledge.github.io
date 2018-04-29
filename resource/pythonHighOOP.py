#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Student(object):
     __slots__ =('name','age') # 用tuple定义允许绑定的属性名称,区分方法定义

s = Student()
s.name = 'Zhao'
s.age = 20
# s.address = 'maoming' #会报错，因为s没有在__slots__定义addres

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
if __name__ == '__main__':
    print ('okoko')
