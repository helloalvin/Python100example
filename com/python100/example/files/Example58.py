#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example58
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/20 上午9:17

"""画图，学用rectangle画方形。"""
from com.python100.example.files.ExampleBase import *
from tkinter import *

class Example58(ExampleBase):
    def execute(self):
        canvas = Canvas(width=600, height=400, bg='yellow')
        canvas.create_rectangle(100,100,300,300,fill='RED')
        canvas.pack()
        mainloop()

