#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example93
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/22 上午9:24

"""时间函数举例3。"""
from com.python100.example.files.ExampleBase import *
import time

class Example93(ExampleBase):
    def execute(self):
        start = time.clock()
        for i in range(0,10000):
            print(i,end='')
        end = time.clock()
        print('')
        print('start='+str(start)+',end='+str(end)+':end-start:%.4f'%(end-start))

