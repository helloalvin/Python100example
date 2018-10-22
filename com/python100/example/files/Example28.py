#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example28
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/19 下午2:05

"""有5个人坐在一起，问第五个人多少岁？
他说比第4个人大2岁。问第4个人岁数，
他说比第3个人大2岁。问第三个人，
又说比第2人大两岁。问第2个人，
说比第一个人大两岁。最后问第一个人，
他说是10岁。请问第五个人多大？"""
from com.python100.example.files.ExampleBase import *


class Example28(ExampleBase):
    def execute(self):
        print(self.age(5))

    def age(self, index=int):
        if index == 1:
            return 10
        else:
            return self.age(index - 1) + 2
