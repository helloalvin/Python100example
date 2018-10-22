#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example78
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/21 下午5:08

"""找到年龄最大的人，并输出。请找出程序中有什么问题。"""
from com.python100.example.files.ExampleBase import *


class Example78(ExampleBase):
    def execute(self):
        dic = {"a": 18, "b": 13, "c": 54, "d": 40}
        m = "a"
        for key in dic.keys():
            if dic.get(key) < dic.get(m):
                pass
            else:
                m = key
        print(m + ',' + str(dic.get(m)))
