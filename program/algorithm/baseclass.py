# -*- coding: utf-8 -*-
# @Time    : 2024/4/17 15:50
# @Author  : Stepstar
# @FileName: baseclass.py
# @Software: PyCharm
import time
from docx import Document
from win32com.client import constants
from flask import Flask, Response,g

#TODO :1.中英文字体判别
class BaseClass:
    def __init__(self,doc):
        self.pargs = doc.Paragraphs
        self.index =[]
        self.doc = doc

        self.paragraphs = doc.Paragraphs

        self.errors = []
        self.correct_values = {}
    '''
    index:在win32com里对应的段落号，for index,p in enumerate(doc.Paragraphs)里对应的段落号
    通过index锁定位置
    有时候存在表、公式等index不一定指一段，后续对index可改进（有问题一起交流\n

    errors:[] ,主要记录错误点
    键为属性，值为包含当前值和正确值的列表。后续可改进，目标为：仅通过error可以定位位置，并且知道如何改
    correct_values存了正确的格式，这个的格式以及键值暂时自己设定，并写注释，后续统一接入
    '''
    def check(self):
        pass


    # def __str__(self):
    #     return f"{self.__class__.__name__}"
