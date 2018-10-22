#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example11
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/15 下午6:10

"""古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，
小兔子长到第三个月后每个月又生一对兔子，
假如兔子都不死，问每个月的兔子总数为多少？"""
from com.python100.example.files.ExampleBase import *


class Example11(ExampleBase):
    def execute(self):
        f1 = 1
        f2 = 1
        for i in range(1, 22):
            print('%12ld %12ld' % (f1*2, f2*2),end='')
            f1 = f1 + f2
            f2 = f1 + f2
