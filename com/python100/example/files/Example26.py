#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example26
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/19 下午1:04

"""利用递归方法求5!。"""

from com.python100.example.files.ExampleBase import *


class Example26(ExampleBase):
    def execute(self):
        print(self.fac(5))

    def fac(self, n):
        if n > 1:
            return n * self.fac(n - 1)
        else:
            return 1
