#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: Example4
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/14 下午7:58

"""输入某年某月某日，判断这一天是这一年的第几天？"""
from com.python100.example.files.ExampleBase import *

class Example4(ExampleBase):
    def execute(self):
        date = input('请输入某年某月某日,（例如：20181014）：')
        #判断输入是否合法
        if len(date)!= 8:
            print('请输入正确格式')
            self.execute()
            return
        year_input = ''
        month_input = ''
        day_input = ''
        index = 0
        for c in date:
            if index < 4:
                year_input = year_input + c
            elif index < 6:
                month_input = month_input + c
            else:
                day_input = day_input + c
            index += 1
        year = int(year_input)
        month = int(month_input)
        day = int(day_input)

        leap = False

        if year % 400 == 0:
            leap = True
        elif year % 100 == 0:
            pass
        elif year % 4 == 0:
            leap = True

        month2day = 29 if leap else 28
        if leap :
            print('this year '+str(year) +' is leap year,month2day='+ str(month2day))
        else:
            print('this year ' + str(year) + ' is not leap year,month2day=' + str(month2day))

        days = [31,month2day,31,30,31,30,31,31,30,31,30]
        indexday = 0
        if month == 1:
            print('input date '+date+' is the '+str(day)+' day')
        else:
            for k in range(0,month-1):
                indexday = indexday + days[k]
            indexday+= day
            print('input date ' + date + ' is the ' + str(indexday) + ' day')