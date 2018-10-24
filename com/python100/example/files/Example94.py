#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example94
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/22 下午5:37

"""时间函数举例4,一个猜数游戏，判断一个人反应快慢。"""
from com.python100.example.files.ExampleBase import *
import random
import time

class Example94(ExampleBase):
    targetN = 0

    msg = '请输入（1-100）之间的一个整数:'

    def execute(self):
        self.targetN = int(100 * random.random())
        start = time.time()
        self.msg = '请输入（1-100）之间的一个整数:'
        while True:
            if self.guess() == True:
                break
        print('恭喜您，猜对啦~' + str(self.targetN))
        print('您总共耗时：' + str(time.time() - start))

    def guess(self):
        number = input(self.msg)
        try:
            if isinstance(int(number), int):
                if int(number) == self.targetN:
                    return True
                elif int(number) > self.targetN:
                    self.msg = '请输入比' + number + '小的一个整数:'
                    return False
                else:
                    self.msg = '请输入比' + number + '大的一个整数:'
                    return False
            else:
                return False
        except Exception as e:
            print(e)
            return False
