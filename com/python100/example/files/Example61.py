#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example61
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/20 上午9:34

"""打印出杨辉三角形（要求打印出10行如下图）"""
from com.python100.example.files.ExampleBase import *


class Example61(ExampleBase):
    def execute(self):
        data = []
        for i in range(0, 10):
            d = []
            if i == 0:
                d.append(1)
                data.append(d)
            elif i == 1:
                d.append(1)
                d.append(1)
                data.append(d)
            else:
                for j in range(0, i + 1):
                    if j == 0:
                        d.append(1)
                    elif j == i:
                        d.append(1)
                    else:
                        d.append(data[i - 1][j - 1] + data[i - 1][j])
                data.append(d)
        print(data, end='\n')
