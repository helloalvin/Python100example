#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example82
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/21 下午8:02

"""八进制转换为十进制"""
from com.python100.example.files.ExampleBase import *
import math

class Example82(ExampleBase):
    def execute(self):
        print(ord('4'))
        num = input('请输入一个八进制数：')
        sum = 0
        index = 0
        for i in num[::-1]:
            sum = sum + int(i)*math.pow(8,index)
            index+=1
        print(str(sum))

