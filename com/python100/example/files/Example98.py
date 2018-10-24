#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example98
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/22 下午5:38

"""从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存。"""
from com.python100.example.files.ExampleBase import *


class Example98(ExampleBase):
    def execute(self):
        strs = input('请输入字符串:')
        fp = open('test', "w")
        fp.write(strs.upper())
        fp.close()
