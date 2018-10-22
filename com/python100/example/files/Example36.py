#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example36
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/19 下午4:18

"""求100之内的素数。"""
from com.python100.example.files.ExampleBase import *


class Example36(ExampleBase):
    def execute(self):
        for i in range(2,101):
            f = True
            for j in range(2,int(i/2) +1):
                if i%j == 0:
                    f = False
                    break
            if f:
                print(i,end=',')

