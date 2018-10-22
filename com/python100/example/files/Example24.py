#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example24
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/19 下午12:07

"""有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。"""

from com.python100.example.files.ExampleBase import *


class Example24(ExampleBase):
    def execute(self):
        a = 2
        b = 1
        result = 0.0
        for i in range(1,21):
            result = result + a/b
            a,b = a+b,a
        print(result)

