#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example74
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/21 下午12:43

"""列表排序及连接"""
from com.python100.example.files.ExampleBase import *


class Example74(ExampleBase):
    def execute(self):
        a = [3,5,1,2]
        b = ['a','b','c','d','e']
        print(a)
        a.sort()
        print('sorted:'+str(a))
        a.extend(b)
        print('a+b:'+str(a))

