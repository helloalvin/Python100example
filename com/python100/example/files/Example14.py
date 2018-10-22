#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example14
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/15 下午11:29

"""将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5"""
from com.python100.example.files.ExampleBase import *

class Example14(ExampleBase):
    result = []

    def execute(self):
        n = input('请输入一个整数：')
        if not isinstance(int(n), int):
            print('输入错误，请重新输入')
            self.execute()
            return
        self.result.clear()
        self.caculate(int(n))
        for pos in range(0,len(self.result)):
            if pos == len(self.result)-1:
               print(''+str(self.result[pos]))
            else:
               print('' + str(self.result[pos]),end='*')

    def caculate(self, n):
        for i in range(2, n + 1):
            isshuNumber = True
            for j in range(2, i):
                if (i % j) == 0:
                    isshuNumber = False
                    break
            if isshuNumber and n % i == 0:
                self.result.append(i)
                #print('n='+str(n)+',i='+str(i))
                if int(n / i) != 1:
                    self.caculate(int(n / i))
                    break
