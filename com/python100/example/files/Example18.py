#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example18
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/17 下午10:50

"""求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
例如2+22+222+2222+22222(此时共有5个数相加)，
几个数相加由键盘控制。"""
from com.python100.example.files.ExampleBase import *


class Example18(ExampleBase):

    def execute(self):
        num = input('请输入要加的数字:')
        result = 0
        if self.isInt(num):
            r = self.inputCount()
            for i in range(1, r + 1):
                result = result + int(num * i)
                if i == r:
                    print('' + str(num * i), end='=')
                    print('' + str(result))
                else:
                    print('' + str(num * i), end='+')

        else:
            self.execute()

    def inputCount(self):
        count = input('请输入要加的次数：')
        if self.isInt(count) and int(count) > 0:
            return int(count)
        else:
           return  self.inputCount()

    def isInt(self, n):
        try:
            if isinstance(int(n), int):
                return True
            else:
                return False
        except:
            return False
