#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example81
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/21 下午7:42

"""809*??=800*??+9*?? 其中??代表的两位数,
 809*??为四位数，8*??的结果为两位数，9*??的
 结果为3位数。求??代表的两位数，及809*??后的结果。"""
from com.python100.example.files.ExampleBase import *
import math


class Example81(ExampleBase):
    def execute(self):
        for ii in range(10, 100):
            if 4 == self.calL(809 * ii) and self.calL(8 * ii) == 2 and self.calL(9 * ii) == 3:
                print(ii)
                print(809 * ii)

    """判断一个数字是1-4中的几位数"""
    def calL(self, num):
        temp = 1
        for i in range(4, 0, -1):
            temp = i
            if int(num / math.pow(10, i - 1)) > 0:
                break
        return temp
