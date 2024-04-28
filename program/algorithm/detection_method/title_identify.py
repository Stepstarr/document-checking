# -*- coding: utf-8 -*-
# @Time    : 2024/4/19 11:43
# @Author  : Stepstar
# @FileName: title_identify.py
# @Software: PyCharm
'''
判断一个段落是否为标题，并返回标题层级
'''
import re
def title_identify(parg):
    flag = False
    title_layer = None
    text = parg.Range.Text
    title_styles = ['标题 1', '标题 2', '标题 3', '标题 4', '标题 5']
    # Case 1:当样式为标题样式，则为该级别标题
    if str(parg.Style) in title_styles:
        return True,str(parg.Style)
        #title[str(parg.Style)].append(index + 1)  # index+1是为了提取Item，parags通过Item方法提取其中元素，索引从1开始
    # Case 2:当文字少于一定的文字且前面带有序号，则为x级别的标题(航发适用该方法，优先级1)
    elif bool(re.match(r'^\s*\d', text)):  # 如果以数字开头，这里\s怕手打缩进导致有空格，所以考虑了空格开头但第一个字符是数字
        match = re.search(r"[a-zA-Z\u4e00-\u9fff]", text)  # 提取出中英文前text
        if match:
            number = text[:match.start()]
            pattern = re.compile('\d+')
            # 有几个数字则为几层标题
            layers = len(re.findall(pattern, number))
            if layers >= 1:
                return True,title_styles[layers - 1]
                #title[title_styles[layers - 1]].append(index + 1)
        else:  # 没有中英文，只有序号
            pattern = re.compile('\d+')
            # 有几个数字则为几层标题
            layers = len(re.findall(pattern, text))
            if layers >= 1:
                return True, title_styles[layers - 1]
                #title[title_styles[layers - 1]].append(index + 1)
    elif parg.Range.ListFormat.ListString != '':  # 自动标号
        pattern = re.compile('\d+')
        layers = len(re.findall(pattern, parg.Range.ListFormat.ListString))
        if layers >= 1:
            return True, title_styles[layers - 1]
            #title[title_styles[layers - 1]].append(index + 1)
    return flag,title_layer
from bisect import bisect_left, bisect_right


def get_structure(title_n, n_1_index):
    '''
    是generate_hierarchical_numbers的一部分，采用了递归的写法，有了第n层的序号，n+1序号的得到
    例如已知二级标题是2.2，得到三级标题是2.2.x
    :param title_n: 第n层 {index：’x.x.x‘}
    :param n_1_index: 第n+1层的index
    :return: title_n_1 第n+1层的结构 {序号：’x.x.x.x‘}
    '''
    n_index = sorted(list(title_n))
    n_1_index = sorted(n_1_index)
    title_n_1 = {}
    for a in n_1_index:
        # 在n_index中找到比a小的最大数字的索引
        idx = bisect_left(n_index, a) - 1
        if idx >= 0:
            b = n_index[idx]  # 找到的n_index中的数字
            # 计算a在b下的正确相对排名
            left_rank = bisect_right(n_1_index, b)
            rank_in_A = bisect_left(n_1_index, a) - left_rank + 1
            title_n_1[a] = str(title_n[b]) + '.' + str(rank_in_A)
    return title_n_1

def generate_hierarchical_numbers(titles):
    '''
    这个函数是通过title_identify的结果，获得每个标题应当有的正确序号
    :param titles: title_identify的结果
    :return: 每个标题所在索引的正确序号，比如第3段是标题，那么返回包括3：‘x.x.x’ (第3段应当有的序号）
    '''
    titles = {key: value for key, value in titles.items() if value}
    result = []
    title_n = {}
    for t, v in titles.items():
        if t == '标题 1':
            for i in range(len(v)):
                title_n[v[i]] = i + 1
            result.append(title_n)
        else:
            title_n = get_structure(title_n, v)
            result.append(title_n)
    return {key: value for d in result for key, value in d.items()}

import re
def get_number(text):
    '''
    该函数是为了得到一段前面的序号相关字符，如'1.1.1  我是一个例子' 会返回 '1.1.1  '
    当没有文字的时候flag会是True,意味着这段只有序号相关字符缺乏文字
    :param text: 段落文本
    :return:
    '''
    match = re.search(r"[a-zA-Z\u4e00-\u9fff]", text)
    flag = False
    if match: #也就是数字后有文字
        return text[:match.start()],flag
    else:
        flag = True
        return text,flag #TODO:报错方式待优化

from ..titleclass import TitleClass
def collect_titles(objects):
    title_dict = {}
    for obj in objects:
        if isinstance(obj, TitleClass):
            if obj.layer not in title_dict:
                title_dict[obj.layer] = []
            title_dict[obj.layer].append(obj.index)
    return title_dict

def title_(objects):
    title_dict = collect_titles(objects)
    correct_title_number = generate_hierarchical_numbers(title_dict)
    return correct_title_number