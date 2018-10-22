#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example48
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/19 下午11:12

"""数字比较"""

from com.python100.example.files.ExampleBase import *

class Example48(ExampleBase):
    def execute(self):
        num1 = input('请输入第1个数：')
        num2 = input('请输入第2个数：')
        try:
            if isinstance(float(num1), float) and isinstance(float(num2), float):
                if float(num1) < float(num2):
                    print(str(num1) + '<' + str(num2))
                elif float(num1) == float(num2):
                    print(str(num1) + '==' + str(num2))
                else:
                    print(str(num1) + '>' + str(num2))
            else:
                self.execute()
        except Exception as e:
            print(e)
            self.execute()
