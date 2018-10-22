#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example40
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/19 下午6:39

"""将一个数组逆序输出"""

from com.python100.example.files.ExampleBase import *


class Example40(ExampleBase):
    datas = ['a','b','c','d','e','f','g']

    def execute(self):
        self.datas.reverse()
        print(self.datas)
