#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example84
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/21 下午10:11

"""连接字符串。"""
from com.python100.example.files.ExampleBase import *


class Example84(ExampleBase):
    def execute(self):
        data = ['a', 'b', 'c', 'd', 'e', 'f']
        print(' '.join(data))
