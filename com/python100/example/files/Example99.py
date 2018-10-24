#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example99
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/22 下午5:38

"""有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。"""
from com.python100.example.files.ExampleBase import *


class Example99(ExampleBase):
    def execute(self):
        fp1 = open('testfile/A', 'r')
        result1 = fp1.read()
        fp1.close()
        fp2 = open('testfile/B', 'r')
        result2 = fp2.read()
        fp2.close()
        result = result1 + result2
        result = ''.join(sorted(result))
        fp = open('testfile/C', 'w')
        fp.write(result)
        fp.close()
        print('处理完毕，请查看testfile/C文件！')
