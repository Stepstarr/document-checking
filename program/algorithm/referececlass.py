# -*- coding: utf-8 -*-
# @Time    : 2024/4/19 14:43
# @Author  : Stepstar
# @FileName: referececlass.py
# @Software: PyCharm
from .baseclass import BaseClass
from format_config import reference_format
class ReferenceClass(BaseClass):
    def __init__(self,index,parg):
        super().__init__(index, parg)
        self.correct_values = reference_format

