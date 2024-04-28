# -*- coding: utf-8 -*-
# @Time    : 2024/4/16 15:22
# @Author  : Stepstar
# @FileName: Title.py
# @Software: PyCharm
from docx import Document
from win32com.client import constants
from flask import Flask, Response
from .baseclass import BaseClass
from flask import g
from format_config import title_format
import re
import time
class TitleClass(BaseClass):
    def __init__(self,index,parg,layer):
        super().__init__(index,parg)
        self.listnumber = parg.Range.ListFormat.ListString
        self.layer = layer
        if layer in title_format:
            self.correct_values = title_format[layer]

    def check(self):
        # 先从基类产生结果
        yield from super().check()
        right_number_dict = getattr(g, 'title_number',{})

        if self.index in right_number_dict:
            self.right_number = right_number_dict[self.index]
            value = self.right_number
            if str(self.parg.Range.ListFormat.ListString) == '':
                number, flag = self.get_number()
                if str(number) != str(value) + '  ':
                    clean_number = re.sub(r'\s+', '', str(number))
                    if clean_number == str(value):
                        if flag:
                            yield f"data: 检测: 段落 {self.index} 标题序号后无文本\n\n"
                            if self.index in self.errors:
                                self.errors[self.index].append((self.content,'序号后没有文本','标题序号后无文本,需检查'))
                                # time.sleep(10)
                            else:
                                self.errors[self.index]=[(self.content, '序号后没有文本','标题序号后无文本,需检查')]
                        else:
                            if self.index in self.errors:
                                self.errors[self.index].append((self.content, '标题缩进或空格错误','标题缩进或空格错误'))
                            else:
                                self.errors[self.index]=[(self.content, '标题缩进或空格错误','标题缩进或空格错误')]
                            yield f"data: 检测: 段落 {self.index} 标题缩进或空格错误\n\n"
                    else:
                        if self.index in self.errors:
                            self.errors[self.index].append((number,value,f'标题序号错误:当前值 {clean_number}，正确值应为 {str(value)}'))
                        else:
                            self.errors[self.index] = [(number, value,f'标题序号错误:当前值 {clean_number}，正确值应为 {str(value)}')]
                        yield f"data: 检测: 段落 {self.index} 标题序号错误:当前值 {clean_number}，正确值应为 {str(value)}\n\n"
            elif str(self.parg.Range.ListFormat.ListString) != str(value):
                yield f"data: 检测: 段落 {self.index} 标题序号错误:当前值 {self.parg.Range.ListFormat.ListString}，正确值应为 {str(value)}\n\n"
                if self.index in self.errors:
                    self.errors[self.index].append((self.parg.Range.ListFormat.ListString, str(value),f'标题序号错误:当前值 {self.parg.Range.ListFormat.ListString}，正确值应为 {str(value)}'))
                    # time.sleep(10)
                else:
                    self.errors[self.index] = [(self.parg.Range.ListFormat.ListString, str(value),f'标题序号错误:当前值 {self.parg.Range.ListFormat.ListString}，正确值应为 {str(value)}')]

            elif str(self.parg.Range.ListFormat.ListString) == str(value):
                space, flag = self.get_number() # 得到文本前的字符
                if flag:
                    yield f"data: 检测: 段落 {self.index}标题序号后无文本\n\n"
                    if self.index in self.errors:
                        self.errors[self.index].append((self.content, '序号后没有文本','标题序号后无文本,需检查'))
                        # time.sleep(10)
                    else:
                        self.errors[self.index] = [(self.content, '序号后没有文本','标题序号后无文本,需检查')]

                elif space != '  ':
                    yield f"data: 检测: 段落 {self.index}标题缩进或空格错误\n\n"
                    if self.index in self.errors:
                        self.errors[self.index].append((self.content,  '标题缩进或空格错误', '标题缩进或空格错误'))
                        # time.sleep(10)
                    else:
                        self.errors[self.index] = [(self.content,  '标题缩进或空格错误', '标题缩进或空格错误')]

        else:
            yield f'data: Error:段落{self.index}并未找到该标题正确的序号\n\n'

            '''
            包括以下几种情况
            Case1:手打标题序号，序号不在ListString里
            number:是第一个字母或文字前的字符串；flag:代表是否找到第一个字母或文字
                Case1.1:序号正确，缩进不对，即把字符串中空白符删去后相等
                    Case1.1.1 flag=True，即没找到第一个字母或文字，代表这一段只有序号,批注：'标题序号后面没有文本，需检查'
                    Case1.1.1 又有序号又有文字，批注：'标题缩进或空格错误'
                Case1.2:序号错误
            Case2:word中的自动标号，标号内容存在ListString里，ListString直接错误，则返回标题序号错误
            Case3:word中的自动标号，序号对了，检查空格         
            '''

    def get_number(self):
        match = re.search(r"[a-zA-Z\u4e00-\u9fff]", self.content)
        flag = False
        if match:  # 也就是数字后有文字
            return self.content[:match.start()], flag
        else:
            flag = True
            return self.content, flag  # TODO:报错方式待优化
        # 然后执行额外的检查
        # for attr, correct_value in additional_checks.items():
        #     actual_value = getattr(self.style, attr, None)
        #     if actual_value != correct_value:
        #         yield f"data: 新增属性 {attr} 错误: 当前值 {actual_value}，正确值应为 {correct_value}\n\n"
        #         time.sleep(1)  # 根据需要调整延迟




