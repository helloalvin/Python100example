#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example29
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/19 下午2:30

"""给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字"""

from com.python100.example.files.ExampleBase import *


class Example29(ExampleBase):
    def execute(self):
        number = input('请输入一个不多于5位数的正整数：')
        try:
            if isinstance(int(number), int):
                print('len:' + str(len(number)))
                print(number[::-1])
        except Exception as e:
            print(e)
            return self.execute()
