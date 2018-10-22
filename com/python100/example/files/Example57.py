#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example57
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/20 上午9:12

"""画图，学用line画直线"""
from com.python100.example.files.ExampleBase import *
from tkinter import *

class Example57(ExampleBase):
    def execute(self):
        canvas = Canvas(width=600, height=400, bg='yellow')
        canvas.pack(expand=YES, fill=BOTH)
        canvas.create_line(0, 0, 300, 200, fill='red')
        mainloop()
