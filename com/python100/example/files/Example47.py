#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example47
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/19 下午11:09

"""两个变量值互换。"""

from com.python100.example.files.ExampleBase import *


class Example47(ExampleBase):
    def execute(self):
        a = 1
        b = 2
        print('交换前a='+str(a)+',b='+str(b))
        a,b=b,a
        print('交换后a=' + str(a) + ',b=' + str(b))
