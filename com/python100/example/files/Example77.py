#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example77
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/21 下午5:04

"""循环输出列表"""
from com.python100.example.files.ExampleBase import *


class Example77(ExampleBase):
    def execute(self):
        datas = ['1','2','3','4','5','6']
        for i in range(0,len(datas)):
            print(datas[i],end=',')


