#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example46
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/19 下午10:44

"""求输入数字的平方，如果平方运算后小于 50 则退出"""

from com.python100.example.files.ExampleBase import *
import math

class Example46(ExampleBase):
    def execute(self):
        num = input('请输入一个数字：')
        try:
            if isinstance(float(num), float) or isinstance(int(num), int):
                result = math.pow(float(num), 2)
                if result < 50:
                    exit(0)
                else:
                    print(result)
            else:
                self.execute()
        except Exception as e:
            print(e)
            self.execute()

