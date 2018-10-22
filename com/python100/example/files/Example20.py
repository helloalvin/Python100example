#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example20
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/17 下午11:14

"""一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？"""

from com.python100.example.files.ExampleBase import *


class Example20(ExampleBase):
    def execute(self):
        distance = 0
        H = 100
        for i in range(1, 11):
            if i == 1:
                distance = distance + H
            else:
                distance = distance + H
                H = H / 2
        print('distance:' + str(distance) + ',第10次反弹：' + str(H / 2))
