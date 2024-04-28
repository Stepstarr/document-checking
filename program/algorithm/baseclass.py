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
    def __init__(self,index,parg):
        self.index = index
        self.parg = parg
        self.content = parg.Range.Text
        self.style = {"左缩进:": parg.LeftIndent,
                       "右缩进:":parg.RightIndent,
                       "首行缩进:":parg.FirstLineIndent,
                       "段前间距:":parg.SpaceBefore,
                       "段后间距:":parg.SpaceAfter,
                       "行距:":parg.LineSpacing,
                       "水平对齐方式:":parg.Alignment,
                       "字体": parg.Range.Font.Name,
                       "字体大小": parg.Range.Font.Size,
                       "加粗": parg.Range.Font.Bold,
                       "斜体": parg.Range.Font.Italic,
                       "下划线:": parg.Range.Font.Underline
                      }
        self.errors = {}
        self.correct_values = {}

    def check(self):
        correct_values = self.correct_values
        for attr, correct_value in correct_values.items():
            actual_value = self.style.get(attr)
            if actual_value != correct_value:
                if self.index not in self.errors:
                    self.errors[self.index] = [(actual_value, correct_value,f'属性 {attr} 错误: 当前值 {actual_value}，正确值应为 {correct_value}')]
                else:
                    self.errors[self.index].append((actual_value, correct_value,f'属性 {attr} 错误: 当前值 {actual_value}，正确值应为 {correct_value}'))
                yield f"data: 检测: 段落 {self.index} 属性 {attr} 错误: 当前值 {actual_value}，正确值应为 {correct_value}\n\n"

    # def modify(self, **kwargs):
    #     for key, value in kwargs.items():
    #         if hasattr(self, key):
    #             setattr(self, key, value)

    def add_com(self,path):
        comments = {key: '\n'.join(x[2] for x in value) for key, value in self.errors.items()}
        if len(comments)!=0:
            doc1 = Document(path)
            p = doc1.paragraphs[self.index]
            p.add_comment(comments[self.index], author='HFUT check')
            yield f'data: --------段落{self.index}批注完毕--------\n\n'
            doc1.save(path)

    # def __str__(self):
    #     return f"{self.__class__.__name__}"
