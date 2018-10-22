#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example22
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/18 下午10:44

"""两个乒乓球队进行比赛，各出三人。
甲队为a,b,c三人，乙队为x,y,z三人。
已抽签决定比赛名单。有人向队员打听
比赛的名单。a说他不和x比，c说他不
和x,z比，请编程序找出三队赛手的名单"""
from com.python100.example.files.ExampleBase import *
import itertools

class Example22(ExampleBase):

    def execute(self):
        A = ['a', 'b', 'c']
        B = ['x', 'y', 'z']
        result1 = list(itertools.product(A, B))
        result2 = list(itertools.combinations(result1, 3))

        for i in range(0, len(result2)):
            value = result2[i]
            result3 = set()
            for k in range(0, len(value)):
                if ((value[k][0] == 'a') and value[k][1] == 'x') or (
                ((value[k][0] == 'c') and (value[k][1] == 'x') or (value[k][0] == 'c') and value[k][1] == 'z')):
                    pass
                else:
                    result3.add(value[k][0])
                result3.add(value[k][1])
            if len(result3) == len(A) + len(B):
                print(value)
