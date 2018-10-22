#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example49
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/19 下午11:14

"""使用lambda来创建匿名函数"""

from com.python100.example.files.ExampleBase import *


class Example49(ExampleBase):
    def execute(self):
        fun = lambda x, y, z: x * y * z
        print(fun(2, 3, 4))
