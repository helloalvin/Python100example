#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example76
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/21 下午12:51

"""编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n"""
from com.python100.example.files.ExampleBase import *


class Example76(ExampleBase):
    def execute(self):
        n = input('请输入n:')
        self.sum(int(n))

    def sum(self, n):
        sum = 0.0
        for i in range(1, int((n + 1) / 2)+1):
            if n % 2 == 0:
                sum += 1.0 /( 2 * i)
                #print('+'+str(1)+'/'+str(2*i),end='')
            else:
                sum = 1.0 / (2 * i - 1)
                #print('+' + str(1) + '/' + str(2 * i - 1),end='')
        print(sum)
