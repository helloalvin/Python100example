#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example92
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/22 上午9:20

"""时间函数举例2。"""
from com.python100.example.files.ExampleBase import *
import time


class Example92(ExampleBase):
    def execute(self):
        start = time.time()
        print('begin time:' + str(start))
        for i in range(0, 3000):
            print(i, end='')
        print('end time:' + str(time.time() - start))
