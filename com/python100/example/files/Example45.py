#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example45
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/19 下午10:35

"""统计 1 到 100 之和"""

from com.python100.example.files.ExampleBase import *

from functools import reduce
class Example45(ExampleBase):
    def execute(self):
        d = []
        for i in range(1, 101):
            d.append(i)
        sum = reduce(lambda x, y: x + y, d)
        print(sum)
