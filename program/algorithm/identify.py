# -*- coding: utf-8 -*-
# @Time    : 2024/4/19 10:55
# @Author  : Stepstar
# @FileName: identify.py
# @Software: PyCharm
from .titleclass import TitleClass
from .baseclass import BaseClass
from .referececlass import ReferenceClass
from flask import g
import re
import win32com.client as win32
from docx import Document
from win32com.client import constants
from .detection_method.title_identify import title_identify,title_
#from .detection_method.title_identify import

def create_object(index,parg):
    title_flag,title_layer = title_identify(parg)
    if title_flag:
        return TitleClass(index,parg,title_layer)
    # elif :
    #     return ReferenceClass(index,parg)
    else:
        return BaseClass(index,parg)


def article_object(parags):
    objects = [create_object(index,parg) for index,parg in enumerate(parags)]
   # yield 'object生成无问题'
    right_title_number = title_(objects)
    #yield 'title_number生成无问题'
    return objects,right_title_number



