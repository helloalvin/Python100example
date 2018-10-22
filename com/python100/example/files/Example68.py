#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example68
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/20 下午10:41

"""有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数"""
from com.python100.example.files.ExampleBase import *


class Example68(ExampleBase):
    def execute(self):
        data = [11,22,33,44,55,66,77,88,99]
        m = 16
        temp = []
        for i in range(0,m):
            d = data.pop()
            data.insert(0,d)
        print(data)

