#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example13
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/15 下午11:15

"""打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，
其各位数字立方和等于该数本身。
例如：153是一个"水仙花数"，
因为153=1的三次方＋5的三次方＋3的三次方"""
from com.python100.example.files.ExampleBase import *
import math

class Example13(ExampleBase):
    def execute(self):
        for i in range(100, 1000):
            b = int(i / 100)
            s = int((i % 100) / 10)
            g = int((i % 100) % 10)
            if (math.pow(b, 3) + math.pow(s, 3) + math.pow(g, 3)) == i:
                print(i, end=', ')
