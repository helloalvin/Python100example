#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example31
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/19 下午2:59

"""输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母"""

from com.python100.example.files.ExampleBase import *


class Example31(ExampleBase):
    WEEK=[('MON','星期一'),('TUS','星期二'),('WEN','星期三'),('THR','星期四'),('FRI','星期五'),('SAT','星期六'),('SUN','星期日')]
    cache=''
    def execute(self):
        day = input('请输入星期几的第' + str(len(self.cache) + 1) + '一个字母：')
        try:
            if str.isalpha(day):
                self.cache = self.cache + day.upper()
                result = []
                for DAY in self.WEEK:
                    if str(DAY[0]).startswith(str.upper(self.cache)):
                        result.append(DAY)
                if len(result) > 1:
                    self.execute()
                elif len(result) == 1:
                    print('' + str(result[0][1]))
                else:
                    self.cache = ''
                    self.execute()
            else:
                raise Exception('请输入字母')

        except Exception as e:
            print(e)
            self.execute()
