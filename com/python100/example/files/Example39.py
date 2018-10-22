#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example39
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/19 下午6:07

"""有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中"""

from com.python100.example.files.ExampleBase import *


class Example39(ExampleBase):
    datas = [9, 8, 7, 5, 4, 3, 2, 1]

    def execute(self):
        num = input('请输入一个数：')
        # 默认顺序由低到高排列
        order = False
        if num.isdigit():
            if self.datas[0] < self.datas[-1]:
                pass
            else:
                order = True
            for j in range(0, len(self.datas) - 1):
                if order:
                    if int(num) >= self.datas[j]:
                        self.datas.insert(j, int(num))
                        break
                else:
                    if int(num) <= self.datas[j]:
                        self.datas.insert(j, int(num))
                        break
            print(self.datas)
        else:
            print('输入数据格式异常')
