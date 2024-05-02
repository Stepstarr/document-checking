# -*- coding: utf-8 -*-
# @Time    : 2024/5/2 16:22
# @Author  : Stepstar
# @FileName: Add_comment.py
# @Software: PyCharm
'''
这是一个加批注的示例，可以通过这个来检测
'''
import win32com.client as win32
doc_app = win32.Dispatch("Kwps.Application")
doc =doc_app.Documents.Open(r'D:\Mo\项目\航发-标准化检测\4-28航发文件\测试.doc')
p = doc.Paragraphs(2).Range # 表示第二段的range
range_to_comment = doc.Range(Start=p.Start+2, End=p.Start + 5)  #以range的index为最小单位,选中第二段的第二个字符到第四个字符
# 添加批注
comment_text = "这里是更新后的批注内容"
comment = range_to_comment.Comments.Add(Range=range_to_comment, Text=comment_text)
comment.Author = "HFUT checker"
# 保存并关闭文档
doc.Save()
doc.Close()

# 关闭 Word 应用程序
doc_app.Quit()