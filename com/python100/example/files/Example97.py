#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example97
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/22 下午5:37

"""从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止"""
from com.python100.example.files.ExampleBase import *
from sys import stdout

class Example97(ExampleBase):
    def execute(self):
        filename = input('请输入文件名:\n')
        fp = open(filename, "w")
        ch = input('输入字符串:\n')
        while ch != '#':
            fp.write(ch)
            #stdout.write(ch)
            ch = input('')
        fp.close()
