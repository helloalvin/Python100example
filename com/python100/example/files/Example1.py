#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example_1
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/14 下午12:47

"""题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少"""

from com.python100.example.files.ExampleBase import *


class Example1(ExampleBase):
    results = []

    def execute(self):
        self.results.clear()
        for i in range(1, 5):
            for j in range(1, 5):
                if i == j:
                    continue
                for k in range(1, 5):
                    if j == k:
                        continue
                    if i == k:
                        continue
                    self.results.append(i * 100 + j * 10 + k)
        totalcout = 0
        #print('results:'+str(self.results))
        for r in self.results:
            totalcout = totalcout + 1
            print('第' + str(totalcout) + '个数是：' + str(r))