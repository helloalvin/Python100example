#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example17
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/17 下午10:36

"""输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数"""
from com.python100.example.files.ExampleBase import *

class Example17(ExampleBase):
    def execute(self):
        ss = input('请输入一行字符:')
        char = 0
        space = 0
        number = 0
        other = 0

        for s in ss:
           # s.isalpha()
            if s == ' ':
                space+=1
            elif (s >= 'a' and s<= 'z') or   (s >= 'A' and s<= 'Z') or('\u4e00' <= s <= '\u9fff'):
                char+=1
            elif s>='0' and s<='9' :
                number+=1
            else:
                other+=1
        print('字母='+str(char)+',空格='+str(space)+',数字='+str(number)+',其它='+str(other))