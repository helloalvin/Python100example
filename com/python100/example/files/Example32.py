#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example32
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/19 下午3:46

"""按相反的顺序输出列表的值"""
from com.python100.example.files.ExampleBase import *


class Example32(ExampleBase):
    def execute(self):
        result = [1,2,3,4,5,6,7,8,9]
        print(result[::-1])

