#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example75
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/21 下午12:48

"""放松一下，算一道简单的题目"""
from com.python100.example.files.ExampleBase import *


class Example75(ExampleBase):
    def execute(self):
        sum = 0
        for i in range(1,37):
            sum+=i
            if i == 24:
                print(sum)
        print(sum)
