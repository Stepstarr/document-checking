# -*- coding: utf-8 -*-
# @Time    : 2024/5/4 20:50
# @Author  : Stepstar
# @FileName: regex_expression.py
# @Software: PyCharm
import re

import re

def t_letter_column_item(text):
    """
    用于标题类字母列项获取
    :param text:
    :return:
    """
    # 正则表达式解释：
    # ^\s* : 行开始，可以有任意数量的空白
    # \(?\s* : 可选的左圆括号，后跟任意数量的空白
    # ([a-zA-Z]+) : 一个或多个字母，捕获这些字母
    # \s*\)? : 字母后可以有任意数量的空白，后跟一个可选的右圆括号
    # \s* : 任意数量的空白
    pattern = r'^\s*\(?([a-zA-Z]+)\)?\s*'
    match = re.match(pattern, text)
    if match:
        return match.group(0),match.group(1)  # 返回匹配到的字母项
    return None

import re

def t_number_column_item(text):
    """
    用于标题类数字列项获取，要求数字前后至少有一个 '(' 或 ')'。
    :param text: 输入的文本
    :return: 返回匹配到的整个表达式及数字
    """
    # 正则表达式解释：
    # ^\s* : 行开始，可以有任意数量的空白
    # (?: : 非捕获组，用于逻辑分组
    # \(\s*(\d+)\s*\) : 数字两侧都有圆括号
    # |
    # \(\s*(\d+) : 左圆括号后跟任意数量的空白和数字
    # |
    # (\d+)\s*\) : 数字后跟任意数量的空白和一个右圆括号
    # )
    # \s* : 任意数量的空白
    pattern = r'^\s*(?:\(\s*(\d+)\s*\)|\(\s*(\d+)|(\d+)\s*\))\s*$'
    match = re.match(pattern, text)
    if match:
        # 如果找到匹配项，确定哪一个组是数字
        num_group = match.lastindex  # 使用lastindex找到最后一次成功匹配的分组
        return match.group(0), match.group(num_group)
    return None


def get_text_pre(text):
    """
    用于标题类文本前所有内容提取
    :param text:
    :return:
    """
    # 文字前所有内容
    match = re.search(r"[a-zA-Z\u4e00-\u9fff]", text)
    flag = False
    if match:  # 也就是数字后有文字
        return text[:match.start()], flag
    else:
        flag = True
        return text, flag