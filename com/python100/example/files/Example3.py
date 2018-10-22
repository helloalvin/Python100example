#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example3
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/14 下午7:44

"""一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？"""
from com.python100.example.files.ExampleBase import *
import math
class Example3(ExampleBase):
    def execute(self):
        x = 0
        for x in range(-100,10000):
            if (math.sqrt(x+100) == int(math.sqrt(x+100))) and (math.sqrt(x+268) == int(math.sqrt(x+268))):
               print('x='+str(x))


