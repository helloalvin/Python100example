#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example100
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/22 下午5:38

"""两个列表转换为字典。"""
from com.python100.example.files.ExampleBase import *


class Example100(ExampleBase):
    def execute(self):
        data1 = ['A', 'B', 'C', 'D', 'E', 'F']
        data2 = [90, 80, 70, 60, 50, 40]
        l = len(data1)
        if l < len(data2):
            pass
        else:
            l = len(data2)
        d = dict()

        for i in range(0, l):
            d[data1[i]] = data2[i]

        print(d)
