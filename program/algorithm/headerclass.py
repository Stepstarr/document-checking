# -*- coding: utf-8 -*-
# @Time    : 2024/4/19 10:59
# @Author  : Stepstar
# @FileName: headerclass.py
# @Software: PyCharm
from .baseclass import BaseClass

class HeaderClass(BaseClass):
    def __init__(self,section_index,sec):
        self.index = section_index
        self.sec = sec
        self.content = sec.Range.Text
        self.errors = {}
    def check(self, correct_values):
        yield from super().check(correct_values)

