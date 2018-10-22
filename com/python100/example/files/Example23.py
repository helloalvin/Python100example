#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example23
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/19 上午9:02

"""打印出如下图案（菱形）:
   *
  ***
 *****
*******
 *****
  ***
   *
   """
from com.python100.example.files.ExampleBase import *


class Example23(ExampleBase):
    def execute(self):
        lines = input('请输入要打印的行数：')
        try:
            if isinstance(int(lines), int):
                for i in range(0, int(lines)):
                    number = 0;
                    if i < int(lines) / 2:
                        number = 2 * i + 1
                    else:
                        number = 2 * (int(lines) - i - 1) + 1
                    print(int((int(lines) - number) / 2) * ' ' + number * '*' + int((int(lines) - number) / 2) * ' ')
        except:
            self.execute()
