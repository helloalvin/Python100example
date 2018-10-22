#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example71
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/20 下午11:35

"""编写input()和output()函数输入，输出5个学生的数据记录"""
from com.python100.example.files.ExampleBase import *


class Example71(ExampleBase):
    result = []
    def execute(self):
        for i in range(0,3):
            self.inputInfo()
        self.outputInfo()

    def inputInfo(self):
        num = input('请输入学生学号:')
        name = input('请输入学生姓名：')
        score = []
        for i in range(1,4):
            s = input('请输入分数'+str(i)+':')
            score.append(s)
        self.result.append([num,name,score])

    def outputInfo(self):
        for i in range(0,3):
            print('学生'+str(i+1)+'的学号：'+self.result[i][0])
            print('学生'+str(i+1)+'的姓名：'+self.result[i][1])
            print('学生'+str(i+1)+'的分数：'+str(self.result[i][2]))

