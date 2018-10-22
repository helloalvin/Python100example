#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example8
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/15 下午5:18

"""输出 9*9 乘法口诀表"""
from com.python100.example.files.ExampleBase import *


class Example8(ExampleBase):
    def execute(self):
        for i in range(1, 10):
            for j in range(1, i + 1):
              print(str(j) + '*' + str(i) + '=' + str(i * j) + '  ',end='' if i!=j else '\n')
