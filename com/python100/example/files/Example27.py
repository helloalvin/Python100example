#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example27
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/19 下午1:13

"""利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。"""
from com.python100.example.files.ExampleBase import *


class Example27(ExampleBase):
    def execute(self):
        self.out(['a','b','c','d','e','f'],5)

    def out(self,a=[],index=int):
        if index == -1:
            return
        else:
            print(a[index])
            self.out(a,index-1)



