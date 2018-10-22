#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example50
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/19 下午11:14

"""输出一个随机数。"""

from com.python100.example.files.ExampleBase import *
import random

class Example50(ExampleBase):
    def execute(self):
        print(random.random())
