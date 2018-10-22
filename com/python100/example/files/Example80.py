#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example80
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/21 下午5:19

"""海滩上有一堆桃子，五只猴子来分。
第一只猴子把这堆桃子平均分为五份，
多了一个，这只猴子把多的一个扔入海中，
拿走了一份。第二只猴子把剩下的桃子又平均
分成五份，又多了一个，它同样把多的一个扔入
海中，拿走了一份，第三、第四、第五只猴子都
是这样做的，问海滩上原来最少有多少个桃子？"""
from com.python100.example.files.ExampleBase import *


class Example80(ExampleBase):
    def execute(self):
        n = 6  # 假设第五次分之前有6个桃子
        result = []
        while True:
            result.clear()
            temp = n
            v = True
            for i in range(0, 5):
                if (temp - 1) % 5 == 0:
                    result.append(temp)
                    temp = temp - 1 - (temp - 1) / 5
                else:
                    v = False
                    break
            if v:
                break
            n += 1
        print(result)
