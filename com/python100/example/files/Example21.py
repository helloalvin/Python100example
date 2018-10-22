#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example21
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/18 下午10:31

"""猴子吃桃问题：猴子第一天摘下若干个桃子，
当即吃了一半，还不瘾，又多吃了一个第二天早
上又将剩下的桃子吃掉一半，又多吃了一个。
以后每天早上都吃了前一天剩下的一半零一个。
到第10天早上想再吃时，见只剩下一个桃子了。
求第一天共摘了多少"""
from com.python100.example.files.ExampleBase import *


class Example21(ExampleBase):
    def execute(self):
        total = 0
        for i in range(1, 11):
            if i == 1:
                total = total + 1
            else:
                total = 2 * (total + 1)
        print('total:' + str(total))
