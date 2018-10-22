#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example53
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/20 上午8:42

"""学习使用按位异或 ^ """
from com.python100.example.files.ExampleBase import *


class Example53(ExampleBase):
    def execute(self):
        a = 0b00101100
        b = 0b10000111
        print(str(bin(a^b)))

