#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example56
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/20 上午8:58

"""画图，学用circle画圆形"""
from com.python100.example.files.ExampleBase import *
from tkinter import *

class Example56(ExampleBase):
    def execute(self):
        canvas = Canvas(width=800, height=600, bg='yellow')
        canvas.pack(expand=YES, fill=BOTH)
        k = 1
        j = 1
        for i in range(0, 26):
            canvas.create_oval(310 - k, 250 - k, 310 + k, 250 + k, width=1)
            k += j
            j += 0.3
        mainloop()
