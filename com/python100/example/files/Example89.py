#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example89
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/21 下午10:54

"""某个公司采用公用电话传递数据，数据
是四位的整数，在传递过程中是加密的，加
密规则如下：每位数字都加上5,然后用和除
以10的余数代替该数字，再将第一位和第四
位交换，第二位和第三位交换。"""
from com.python100.example.files.ExampleBase import *


class Example89(ExampleBase):
    def execute(self):
        num = input('请输入四位整数：')
        if isinstance(int(num),int) and len(num) == 4:
            temp = []
            for i in num:
                temp.append(str((int(i)+5)%10))
            temp[0],temp[len(temp)-1]=temp[len(temp)-1],temp[0]
            temp[1],temp[2]=temp[2],temp[1]
            print(''.join(temp))
        else:
            self.execute()

