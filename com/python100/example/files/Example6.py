#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example6
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/15 下午3:46

"""斐波那契数列:0、1、1、2、3、5、8、13、21、34...输出"""
from com.python100.example.files.ExampleBase import *


class Example6(ExampleBase):
    fbl=[]

    def execute(self):
        self.fbl.clear()
        i = 0
        for k in range(1, 100):
            self.outputFbn(i)
            i += 1
        print(self.fbl)

    def outputFbn(self, i):
        if i == 0:
            self.fbl.append(0)
        elif i == 1:
            self.fbl.append(1)
        elif i == 2:
            self.fbl.append(1)
        else:
            j = self.fbl[len(self.fbl) - 1:len(self.fbl) - 1 - 1:-1][0]
            k = self.fbl[len(self.fbl) - 1 - 1:len(self.fbl) - 1 - 1 - 1:-1][0]
            self.fbl.append((j + k))
