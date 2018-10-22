#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example55
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/20 上午8:56

"""学习使用按位取反~"""
from com.python100.example.files.ExampleBase import *


class Example55(ExampleBase):
    def execute(self):
        a = 3
        print(str(bin(~a)))

