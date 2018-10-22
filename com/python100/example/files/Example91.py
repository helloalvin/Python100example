#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example91
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/22 上午9:06

"""时间函数举例1"""
from com.python100.example.files.ExampleBase import *
import time

class Example91(ExampleBase):
    def execute(self):
        print(time.ctime(time.time()))
        print(time.asctime(time.localtime(time.time())))
        print(time.asctime(time.gmtime(time.time())))
