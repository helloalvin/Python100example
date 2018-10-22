#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example88
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/21 下午10:39

"""读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊"""
from com.python100.example.files.ExampleBase import *


class Example88(ExampleBase):
    def execute(self):
        for i in range(0, 7):
            num = input('请输入' + str(i) + '个整数:')
            if isinstance(int(num), int):
                print((int(num) * '*'))
            else:
                break
