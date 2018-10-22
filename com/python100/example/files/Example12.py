#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example12
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/15 下午6:20

"""判断101-200之间有多少个素数，并输出所有素数"""
from com.python100.example.files.ExampleBase import *


class Example12(ExampleBase):
    def execute(self):
        total = 0
        for i in range(101, 200):
            isshuNumber = True
            for j in range(2, i):
                if (i % j) == 0:
                    isshuNumber = False
                    break
            if isshuNumber:
                total += 1
                print('  ' + str(i), end=',')
        print('total count = '+str(total))