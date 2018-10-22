#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example90
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/22 上午8:59

"""列表使用实例。"""
from com.python100.example.files.ExampleBase import *


class Example90(ExampleBase):
    def execute(self):
        list = ['a','b','c','d','e','f']
        print('原始列表:'+str(list)+',长度：'+str(len(list)))
        list.append('元素')
        print('增加元素元素:' + str(list))
        list.pop(0)
        print('去掉第一个元素后:'+str(list))
        list.reverse()
        print('列表倒置后:'+str(list))
        print('元素的索引为:'+str(list.index('元素')))
        list.remove('元素')
        print('remove增加的元素后：'+str(list))

