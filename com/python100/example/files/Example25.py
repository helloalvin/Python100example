#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example25
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/19 下午12:22

"""求1+2!+3!+...+20!的和"""
from com.python100.example.files.ExampleBase import *
from functools import reduce
import math


class Example25(ExampleBase):
    def execute(self):
        sum = 0
        for i in range(1,21):
            sum = sum + math.factorial(i)
        print(sum)

    def factorial(self,n):
        return reduce(lambda x,y:x*y,range(1,n+1))
