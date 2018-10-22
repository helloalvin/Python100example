#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example83
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/21 下午8:14

"""求0—7所能组成的奇数个数"""
from com.python100.example.files.ExampleBase import *
import itertools

class Example83(ExampleBase):
    def execute(self):
        result = []
        key = [0,1,2,3,4,5,6,7]

        for i in range(1,9):
            for j in itertools.permutations(key,i):
                if  j[0]==0 or j[-1]==0 or j[-1]==2 or j[-1]==4 or j[-1]==6:
                    #print(j)
                    continue
                result.append(j)
        print(str(len(result)))

