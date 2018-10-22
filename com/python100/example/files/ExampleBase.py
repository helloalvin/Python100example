#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Project: Python100example
#    File: ExampleBase
#  Author: liyaoyan
#   Email: helloalvin@163.com
#    Time: 2018/10/14 下午3:54

"""基类"""
import abc
from abc import *


class ExampleBase(metaclass=abc.ABCMeta):
    @abstractclassmethod
    def execute(self):
        pass
