#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example30
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/19 下午2:49

"""一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。"""
from com.python100.example.files.ExampleBase import *


class Example30(ExampleBase):
    def execute(self):
        number = input('请输入一个5位数：')
        try:
            if isinstance(int(number), int):
                if len(number) == 5:
                    if number[0] == number[-1] and number[1] == number[-2]:
                        print(number + '是回文数')
                    else:
                        print(number + '不是回文数')
                else:
                    raise Exception('请输入五位长度')
        except Exception as e:
            print(e)
            self.execute()
