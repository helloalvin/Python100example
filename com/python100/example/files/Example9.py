#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example9
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/15 下午5:51

"""暂停一秒输出。"""
from com.python100.example.files.ExampleBase import *
import time

class Example9(ExampleBase):
    def execute(self):
        for i in range(1,4):
            time.sleep(1)
            print(str(i)+'  ',)

