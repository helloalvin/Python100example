#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example67
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/20 下午10:20

"""输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组"""
from com.python100.example.files.ExampleBase import *


class Example67(ExampleBase):
    def execute(self):
        data = []
        for i in range(0, 6):
            k = input('请输入数字：')
            data.append(int(k))
        maxIndex = 0
        temp = data[0]
        for i in range(1, len(data) - 1):
            if temp < data[i]:
                temp = data[i]
                maxIndex = i
        data[0], data[maxIndex] = temp, data[0]
        minIndex = 0
        temp = data[0]
        for i in range(1, len(data) - 1):
            if temp > data[i]:
                temp = data[i]
                minIndex = i
        data[-1], data[minIndex] = temp, data[-1]
        print(data)
