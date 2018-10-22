#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example7
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/15 下午4:57

"""将一个列表的数据复制到另一个列表中"""
from com.python100.example.files.ExampleBase import *


class Example7(ExampleBase):
    def execute(self):
        list1=[1,2,3,4,5,6,7,8,9]
        list2= None
        print('list1='+str(list1)+',list2='+str(list2))
        list2 = list1[:]
        print('After copy,list1=' + str(list1) + ',list2=' + str(list2))

