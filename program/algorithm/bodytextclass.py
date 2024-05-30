import re

from baseclass import BaseClass
from detection_method.title_identify import title_identify
import json

from utils import *


pattern1 = r'^[\da-z]\）' #匹配一级列项和二级列项的格式
pattern2 = r'^[\da-zA-Z]'#匹配一个数字或大小写英文字母
pattern3 = r'^\（[\da-zA-Z]\）'#匹配括号内有一个数字或大小写英文字母
#pattern4 = r'^[a-z]\）' #正确一级列项
pattern4 = r'^\s*\(?([a-zA-Z]+)\)?\s*'
#pattern5 = r'^\d\）' #正确二级列项
pattern5 = r'^\s*(?:\(\s*(\d+)\s*\)|\(\s*(\d+)|(\d+)\s*\))\s*$'


class bodytextclass(BaseClass):
    def __init__(self, doc, data):
        super().__init__(doc)
        self.paragraphs = doc.Paragraphs
        #获取目录中的开始和结束位置，从而判断正文从哪里开始
        self.start, self.end = self.get_start_end()
        self.true_values = data
        self.para_error_dict = None
        self.table_error_dict = None
        self.img_error_dict = None
        self.table_name_list = []
        self.img_name_list = []
        self.img_list = check_paragraphs_for_any_images(self.doc)
        pass



    def get_start_end(self):
        body_start = None
        body_end = len(self.paragraphs)
        # 检查文档中是否存在目录
        if self.doc.TablesOfContents.Count > 0:
            toc = self.doc.TablesOfContents(1)  # 获取第一个目录
            toc_end = toc.Range.End  # 获取目录结束位置

            paragraph_index = 1  # 初始化段落索引
            for i, para in enumerate(self.paragraphs, start=1):
                if para.Range.Start >= toc_end and body_start is None:
                    body_start = i
                if body_start is not None and (
                        para.Range.Text.strip().startswith("附录") or para.Range.Text.strip().startswith("参考文献")):
                    body_end = i
                    break

        return body_start, body_end



    def find_paragraph_index(self, target_paragraph):
        # 段落索引从1开始计数
        for i, paragraph in enumerate(self.paragraphs, start=1):
            if paragraph.Range.Start == target_paragraph.Range.Start and paragraph.Range.End == target_paragraph.Range.End:
                return i
        return None  # 如果找不到匹配的段落，返回 None

    def check_img(self):
        img_error_dict = {}
        para_start = self.paragraphs(self.start)
        para_end = self.paragraphs(self.end)
        img_start = para_start.Range.Start
        img_end = para_end.Range.End

        for i, img in enumerate(self.doc.InlineShapes, start=1):
            start = img.Range.Start
            end = img.Range.End
            if start >= img_start and end <= img_end:
                error_dict = check_one_img(img, self.true_values[0]["正文"]["图片"])
                # 检查图片标题
                # paragraph = img.Range.Paragraphs(1)
                # inline_shape = paragraph.Range.InlineShapes
                next_paragraph = img.Range.Next(1).Paragraphs(1)
                text = next_paragraph.Range.Text.strip()[:5]
                if text.startswith("图"):
                    self.table_name_list.append(self.find_paragraph_index(next_paragraph))
                    title_dict = check_one_img(img, self.true_values[0]["正文"]["图片标题"])
                    if len(title_dict) > 0:
                        error_dict["图片标题"] = title_dict
                else:
                    error_dict["图片标题"] = "图片没有标题"
                if len(error_dict) > 0:
                    img_error_dict[i] = error_dict


            else:
                continue
        return img_error_dict


    def check_img(self):
        def inspect_images(self):
            images = []

            # 获取嵌入图片
            for inline_shape in self.doc.InlineShapes:
                images.append({
                    'type': 'Inline',
                    'index': inline_shape.Range.Start,
                    'image': inline_shape
                })

            # 获取浮动图片
            # for shape in doc.Shapes:
            #     if shape.Type == win32.constants.msoLinkedPicture or shape.Type == win32.constants.msoPicture:
            #         if shape.Type == win32.constants.msoEmbeddedOLEObject or shape.Type == win32.constants.msoOLEControlObject:
            #             continue
            #         images.append({
            #             'type': 'Floating',
            #             'index': shape.Anchor.Information(win32.constants.wdFirstCharacterLineNumber),
            #             'image': shape
            #         })

            for shape in doc.Shapes:
                # 检查是否是链接图片或普通图片
                if shape.Type == 11 or shape.Type == 13:
                    # 确保不是嵌入的 OLE 对象或 OLE 控制对象
                    if not (
                            shape.Type == win32.constants.msoEmbeddedOLEObject or shape.Type == win32.constants.msoOLEControlObject):
                        # 获取图片所在的行号
                        line_number = shape.Anchor.Information(win32.constants.wdFirstCharacterLineNumber)
                        images.append({
                            'type': 'Floating',
                            'index': line_number,
                            'image': shape
                        })

            images_sorted = sorted(images, key=lambda x: x['index'])
            return images_sorted

        self.Images = inspect_images(self)
        img_error_dict = {}
        para_start = self.paragraphs(self.start)
        para_end = self.paragraphs(self.end)
        img_start = para_start.Range.Start
        img_end = para_end.Range.End
        img_index = 1#记录现在应该是表几
        img_index_char = 'a'

        for i, image in enumerate(self.Images, start=1):
            start = image['image'].Range.Start
            end = image['image'].Range.End
            if start >= img_start and end <= img_end:
                if image['type'] == 'Inline':#判断图片是否为嵌入图片
                    error_dict = {}
                    img = image['image']

                    #error_dict = check_one_img(img, self.true_values[0]["正文"]["图片"])
                    # 检查图片标题
                    paragraph = img.Range.Paragraphs(1)
                    # inline_shape = paragraph.Range.InlineShapes
                    #if paragraph.Alignment != win32.constants.wdAlignParagraphCenter:
                    if paragraph.Alignment != 1: #居中为1
                        error_dict['图片位置'] = '未居中放置'

                    next_paragraph = paragraph.Range.Next().Paragraphs(1)
                    text = next_paragraph.Range.Text.strip()
                    if text.startswith(img_index_char + '）'):#如果以字母）开头的情况
                        self.img_name_list.append(self.find_paragraph_index(next_paragraph))
                        title_dict = check_one_paragraph(next_paragraph, self.true_values[0]["正文"]["图标题"])
                        if len(title_dict) > 0:
                            error_dict['子图标题'] = title_dict
                        img_index_char = chr(ord(img_index_char) + 1)
                        next_next_paragraph = next_paragraph.Range.Next(1).Paragraphs()#获取子图标题的下一行，检查是否为图标题
                        text = next_next_paragraph.Range.Text.strip()
                        if text.startswith('图' + ' ' + str(img_index)):
                            img_index_char = 'a'
                            self.img_name_list.append(self.find_paragraph_index(next_next_paragraph))
                            title_dict = check_one_paragraph(next_next_paragraph, self.true_values[0]["正文"]["图标题"])
                            if len(title_dict) > 0:
                                error_dict['图标题'] = title_dict
                            img_index += 1


                    elif text.startswith('图' + ' ' + str(img_index)):
                        self.img_name_list.append(self.find_paragraph_index(next_paragraph))
                        title_dict = check_one_paragraph(next_paragraph, self.true_values[0]["正文"]["图标题"])
                        if len(title_dict) > 0:
                            error_dict["图标题"] = title_dict
                        img_index += 1
                    else:
                        error_dict["图片标题"] = "图片没有标题"
                        img_index += 1
                    if len(error_dict) > 0:
                        img_error_dict[i] = error_dict

                elif image['type'] == 'Floating':  # 判断图片是否为浮动图片
                    img_error_dict[i] = "图片未设置为嵌入型"
                    img_index += 1

            else:
                continue
        return img_error_dict



    #检查表格
    def check_table(self):
        table_error_dict = {}
        # 获取表格的开始和结束位置
        para_start = self.paragraphs(self.start)
        para_end = self.paragraphs(self.end)
        table_start = para_start.Range.Start
        table_end = para_end.Range.End
        table_indent = 1

        for table in self.doc.Tables:
            error_dict = {}
            start = table.Range.Start
            end = table.Range.End
            if start >= table_start and end <= table_end:

                error_dict = check_one_table(table, self.true_values[0]["正文"]["表格"], self.true_values[0]["正文"]["表格文字"])
                #因为表标题涉及到段落，因此写在类里进行检查，不单独写成一个函数

                #检查表格前的段落是不是标题
                prev_paragraph = table.Range.Previous(1).Paragraphs(1)# 获取表格的上一个段落
                text = prev_paragraph.Range.Text.strip()
                if text == "符号表":
                    continue
                if text.startswith("表" + ' ' + str(table_indent)):
                    table_indent += 1
                    self.table_name_list.append(self.find_paragraph_index(prev_paragraph))
                    title_dict = check_one_paragraph(prev_paragraph, self.true_values[0]["正文"]["表标题"])
                    if len(title_dict) > 0:
                        error_dict["表格标题"] = title_dict
                else:
                    error_dict["表格标题"] = {"错误": "表格前没有标题"}
                    table_indent += 1

                #检测表格跨页
                if len(check_tables_for_pagination(table)) != 0:
                    error_dict["表格跨页"] = {"错误": "未设置表格跨页"}
            #将表格错误信息添加到总错误列表中
                if len(error_dict) != 0:
                    table_error_dict[table_indent] = error_dict

            else:
                continue

        return table_error_dict


    def check_paragraph(self):
        para_error_dict = {}
        for i in range(self.start, self.end):
            if i in self.table_name_list or i in self.img_name_list or i in self.img_list:
                continue
            paragraph = self.paragraphs(i)
            flag, _ = title_identify(paragraph)
            if flag:#如果是标题，跳过当前段落
                continue
            if paragraph.Range.Tables.Count > 0:#如果段落中有表格，跳过当前段落
                continue

            #对于自动编号为空的情况，可能是正文，也可能是一二级列项
            if paragraph.Range.ListFormat.ListString == "":
                text = paragraph.Range.Text.strip()[:5]
                if re.match(pattern1, text): # 采用了列项的形式但没有采用自动编号

                    para_error_dict[i] = {"列项错误": "未设置自动编号"}
                elif re.match(pattern2, text) or re.match(pattern3, text): # 不规范的列项形式，同时没有采用自动编号
                    para_error_dict[i] = {"列项错误": "未设置自动编号，且列项形式不规范"}
                else: #普通的文本段落
                    error_dict = check_one_paragraph(paragraph, self.true_values[0]["正文"]["正文内容"])
                    if len(error_dict) != 0:
                        para_error_dict[i] = error_dict
            else:#采用了自动编号
                if re.match(pattern4, paragraph.Range.ListFormat.ListString):#一级列项
                    error_dict = check_one_paragraph(paragraph, self.true_values[0]["正文"]["一级列项"])
                    if len(error_dict) != 0:
                        para_error_dict[i] = error_dict
                elif re.match(pattern5, paragraph.Range.ListFormat.ListString):#二级列项
                    error_dict = check_one_paragraph(paragraph, self.true_values[0]["正文"]["二级列项"])
                    if len(error_dict) != 0:
                        para_error_dict[i] = error_dict
                else:
                    para_error_dict[i] = {"列项错误": "列项格式不规范"}
        return para_error_dict

    def check(self):
        self.img_error_dict = self.check_img()
        self.table_error_dict = self.check_table()
        self.para_error_dict = self.check_paragraph()
        print(self.img_error_dict)
        print(self.table_error_dict)
        print(self.para_error_dict)

    def add(self):
        for key, value in self.img_error_dict.items():
            image = self.Images[key -1]
            if image['type'] == "Inline":
                p_range = image['image'].Range
                conment_text = "图片" + str(key) + ":" + str(value)
            else:
                p_range = image['image'].Anchor
                conment_text = "图片" + str(key) + ":" + str(value)
            comment = p_range.Comments.Add(Range=p_range, Text=conment_text)
            comment.Author = "HFUT checker"
            self.doc.Save()



        for key, value in self.table_error_dict.items():
            table = self.doc.Tables(key)
            p_range = table.Range
            conment_text = "表格" + str(key) + ":" + str(value)
            comment = p_range.Comments.Add(Range=p_range, Text=conment_text)
            comment.Author = "HFUT checker"
            self.doc.Save()
        for key, value in self.para_error_dict.items():
            p_range = self.paragraphs(key).Range
            conment_text = "段落" + str(key) + ":" + str(value)
            comment = p_range.Comments.Add(Range=p_range, Text=conment_text)
            comment.Author = "HFUT checker"
            self.doc.Save()




if __name__ == '__main__':
    # with open('template_集团标准.json', 'r', encoding='utf-8') as f:
    #     data = json.load(f)
    #
    # word_app = win32.Dispatch('Word.Application')
    # doc = word_app.Documents.Open(r'C:\Users\jinxi\Desktop\word-detect\document-checking-main\program\algorithm\集团标准-航空发动机XX设计（公开）.docx')
    # bodytext_class = newbodytextclass(doc, data)
    # bodytext_class.check()
    # bodytext_class.add()

    with open('template_技术文件.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    word_app = win32.Dispatch('Word.Application')
    doc = word_app.Documents.Open(r'C:\Users\jinxi\Desktop\word-detect\document-checking-main\program\algorithm\技术文件模板-（公开）.doc')
    bodytext_class = bodytextclass(doc, data)
    bodytext_class.check()
    bodytext_class.add()