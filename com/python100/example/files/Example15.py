#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example15
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/15 下午11:35

"""利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示"""
from com.python100.example.files.ExampleBase import *


class Example15(ExampleBase):
    def execute(self):
        score = input('请输入学习成绩:')
        try:
            if isinstance(int(score), int):
                if int(score) >= 90:
                 print('A')
                elif int(score) >= 60:
                    print('B')
                else:
                    print('C')
            else:
                self.execute()
        except ValueError as e:
            print(e)
            self.execute()