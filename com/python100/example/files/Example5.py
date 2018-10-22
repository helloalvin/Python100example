#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example5
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/15 下午2:09

"""输入三个整数x,y,z，请把这三个数由小到大输出"""
from com.python100.example.files.ExampleBase import *
class Example5(ExampleBase):
    def execute(self):
        cout = 1
        inputs = []
        for i in range(1, 4):
            print('请输入第' + str(cout) + '个整数：')
            inputs.append(input())
            cout += 1
        inputs.sort()
        for value in inputs:
            print('从小到大输出：' + str(value))
