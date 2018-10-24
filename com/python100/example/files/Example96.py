#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example96
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/22 下午5:37

"""计算字符串中子串出现的次数。"""
from com.python100.example.files.ExampleBase import *


class Example96(ExampleBase):
    def execute(self):
        str1 = input('请输入一段内容：')
        str2 = input('请输入关键内容：')
        print('总共包含关键内容'+str(str1.count(str2))+'次')

