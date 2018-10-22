#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example10
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/15 下午5:59

"""暂停一秒输出，并格式化当前时间"""
from com.python100.example.files.ExampleBase import *
import time


class Example10(ExampleBase):
    def execute(self):
        print('wait for 1 second to output current time:')
        time.sleep(1)
        print(time.strftime("%Y-%m-%d %H-%M-%S",time.localtime(time.time())))


