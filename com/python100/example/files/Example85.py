#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example85
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/21 下午10:17

"""输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。"""
from com.python100.example.files.ExampleBase import *


class Example85(ExampleBase):
    def execute(self):
        print(float(str(('9'*8))))
        num = input('请输入一个奇数：')
        if isinstance(int(num), int):
            if int(num) % 2 == 1:
                count = 1
                while float('9' * count) % int(num) != 0:
                    count += 1
                print(str(count))
            else:
                self.execute()
        else:
            self.execute()
