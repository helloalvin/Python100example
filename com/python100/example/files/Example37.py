#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example37
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/19 下午5:07

"""对10个数进行排序"""

from com.python100.example.files.ExampleBase import *


class Example37(ExampleBase):
    datas = []

    def execute(self):
        num = input('请输入第' + str(len(self.datas) + 1) + '个数:')
        if num.isdigit():
            self.datas.append(int(num))
            if len(self.datas) == 10:
                print(sorted(self.datas))
            else:
                self.execute()
        else:
            self.execute()
