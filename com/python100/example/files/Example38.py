#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example38
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/19 下午5:23

"""求一个3*3矩阵主对角线元素之和"""
from com.python100.example.files.ExampleBase import *


class Example38(ExampleBase):
    datas = []

    def execute(self):
        self.datas.clear()
        for i in range(0, 3):
            data = []
            for j in range(0, 3):
                num = input('请输入第' + str((3 * i) + j + 1) + '个数：')
                if num.isdigit():
                    data.append(int(num))
                else:
                    print('输入数据格式异常，请重新执行')
                    exit(-1)
            self.datas.append(data)
        sum = 0
        for k in range(0, 3):
            sum = sum + self.datas[k][k]
        print(sum)
