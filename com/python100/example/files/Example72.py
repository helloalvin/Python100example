#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example72
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/21 下午12:34

"""创建一个链表"""
from com.python100.example.files.ExampleBase import *


class Example72(ExampleBase):
    result = []
    def execute(self):
        for i in range(0,6):
            s = input('请输入：')
            self.result.append(s)
        print(self.result)
