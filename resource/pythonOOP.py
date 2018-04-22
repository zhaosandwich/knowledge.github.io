#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

class ClassNameDemo(object) :
    #初始化
    def __init__(self, param1, param2):
        self.__param1 = param1
        self.__param2 = param2

    #数据封装
    def sumInputParamValues(self):
        return self.__param1 + self.__param2

print('类的实例与封装')
classInstance  = ClassNameDemo(90, 9)
print (classInstance.sumInputParamValues())
