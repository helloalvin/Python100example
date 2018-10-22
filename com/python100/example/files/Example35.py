#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example35
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/19 下午4:14

"""文本颜色设置"""
from com.python100.example.files.ExampleBase import *

class Example35(ExampleBase):
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    def execute(self):
        print(self.OKGREEN+'OKGREEN'+self.ENDC)

