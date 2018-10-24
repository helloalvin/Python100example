#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example95
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/22 下午5:37

"""字符串日期转换为易读的日期格式"""
from com.python100.example.files.ExampleBase import *
from dateutil import parser

class Example95(ExampleBase):
    def execute(self):
        dt = parser.parse("Oct 24 2018 11:00AM")
        print(dt)

