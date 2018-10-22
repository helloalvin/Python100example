#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example54
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/20 上午8:45

"""取一个整数a从右端开始的4〜7位。"""
from com.python100.example.files.ExampleBase import *


class Example54(ExampleBase):
    def execute(self):
        a = input('请输入一个整数：')
        try:
            if isinstance(int(a),int):
                print(str(bin((int(a)>>4)&0x0F)))
        except Exception as e:
            print(e)
            self.execute()

