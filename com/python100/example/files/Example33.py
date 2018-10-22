#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example33
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/19 下午4:03

"""按逗号分隔列表"""
from com.python100.example.files.ExampleBase import *


class Example33(ExampleBase):
    def execute(self):
        result = [1,2,3,4,5,6,7,8,9]
        print(','.join(str(L) for L in result))
        for L in result:
            print(str(L),end=',')
