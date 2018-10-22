#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example79
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/21 下午5:15

"""字符串排序。"""
from com.python100.example.files.ExampleBase import *


class Example79(ExampleBase):
    def execute(self):
        s1 = 'hasdaffasdf'
        s2 = 'haaafasdfff'
        s3 = 'abcdeeee'

        ss = []
        ss.append(s1)
        ss.append(s2)
        ss.append(s3)
        print(sorted(ss))
