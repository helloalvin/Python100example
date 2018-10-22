#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example70
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/20 下午10:50

"""写一个函数，求一个字符串的长度，在main函数中输入字符串，并输出其长度。"""
from com.python100.example.files.ExampleBase import *


class Example70(ExampleBase):
    def execute(self):
        s = input('请输入字符串：')
        print(str(len(s)))

