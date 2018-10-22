#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example87
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/21 下午10:31

"""回答结果（结构体变量传递）"""
from com.python100.example.files.ExampleBase import *


class Example87(ExampleBase):
    x = 0
    c = 0

    def execute(self):
        print(str(self.x) + ',' + str(self.c))
        self.fu()
        print(str(self.x) + ',' + str(self.c))

    def fu(self):
        self.x = 2
        self.c = 3
