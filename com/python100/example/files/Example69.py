#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example69
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/20 下午10:49

"""有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。"""
from com.python100.example.files.ExampleBase import *


class Example69(ExampleBase):
    def execute(self):
        data = []
        for i in range(1, 10):
            data.append(i)
        print(data)
        num = 0
        while (len(data) != 1):
            if num == 3:
                num = 0
                data.pop(0)
            else:
                num = num + 1
                value = data.pop(0)
                data.append(value)
        print(data)
