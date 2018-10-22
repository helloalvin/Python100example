#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example66
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/20 下午10:15

"""输入3个数a,b,c，按大小顺序输出。"""
from com.python100.example.files.ExampleBase import *


class Example66(ExampleBase):
    def execute(self):
        data = []
        for i in range(0,3):
            k = input('输入一个数字：')
            data.append(int(k))
        print(sorted(data))

