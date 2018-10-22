#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example62
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/20 下午10:10

"""查找字符串"""
from com.python100.example.files.ExampleBase import *


class Example62(ExampleBase):
    def execute(self):
        datas = 'askjdasjga;sd'
        key = 'jd'
        print(str(datas.find(key)))
