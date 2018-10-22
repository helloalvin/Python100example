#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example44
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/19 下午7:16

"""两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵"""

from com.python100.example.files.ExampleBase import *

class Example44(ExampleBase):
    m1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    m2 = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]
    m3 = []

    def execute(self):
        for i in range(0, 3):
            m = []
            for j in range(0, 3):
                m.append(self.m1[i][j] + self.m2[i][j])
            self.m3.append(m)
        print(self.m3)
