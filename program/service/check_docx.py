# -*- coding: utf-8 -*-
# @Time    : 2024/4/19 9:52
# @Author  : Stepstar
# @FileName: check_docx.py
# @Software: PyCharm
from flask import Blueprint, send_from_directory,g,request,current_app
import os
from flask import Flask, Response, send_from_directory
from flask import Response, stream_with_context
from algorithm.baseclass import BaseClass
import win32com.client as win32
import time
import pythoncom
from format_config import reference_format
from algorithm.identify import article_object
check_bp = Blueprint('check_bp', __name__)

@check_bp.route('/check',methods=['GET'])
def compare():
    # 从查询参数中获取文件路径
    path = request.args.get('filepath', '')
    if not path:
        return "No file path provided", 400
    dir_path, filename = os.path.split(path)
    base_filename, extension = os.path.splitext(filename)
    new_filename = base_filename + '_addcomment' + extension # 添加字符串 'add' 到文件基本名，保持扩展名不变
    # 重建完整的新路径
    add_path = os.path.join(dir_path, new_filename)
    # path = r'D:\pycharm\pythonProject\标准化检测\test_file\航发标题层级测试.docx'
    pythoncom.CoInitialize()
    doc_app = win32.Dispatch("Kwps.Application")
    # doc_app = win32.gencache.EnsureDispatch('Word.Application')

    doc_app.Visible = 1  # 设置应用程序可见
    doc = doc_app.Documents.Open(path, ReadOnly=True)  # 打开文档
    time.sleep(2)
    parags = doc.Paragraphs
    def generate():
        yield 'data: --------正在检测文档对象--------\n\n'
        a_objects, right_title_number = article_object(parags)
        g.aobjects = a_objects
        g.title_number = right_title_number
        yield 'data: --------对象识别完毕--------\n\n'
        for obj in a_objects:
            for message in obj.check():
                yield message.encode('utf-8')
            for message in obj.add_com(add_path):
                yield message.encode('utf-8')
        yield 'data: --------该文档修改完毕--------\n\n'
        doc_app.Quit()
    return Response(stream_with_context(generate()), mimetype='text/event-stream')

