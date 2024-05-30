import win32com.client as win32


#获取段落格式
def get_format(paragraph):
    para_format = paragraph.Range.ParagraphFormat
    # 段落格式
    format_values = {
        "对齐方式": para_format.Alignment,
        "段前间距": para_format.SpaceBefore,
        "段后间距": para_format.SpaceAfter,
        "行距": para_format.LineSpacing,
        "首行缩进": para_format.FirstLineIndent,
        "左缩进": para_format.LeftIndent,
        "右缩进": para_format.RightIndent
    }
    return format_values

#获取字体格式
#遍历段落中的每个字符的字体格式
def get_font(char):

    font = char.Font
    # 字体格式
    font_values = {
        "字体": font.Name,
        "字号": font.Size,
        "加粗": font.Bold,
        "斜体": font.Italic,
        "下划线": font.Underline
    }
    return font_values


#对一个段落的格式和字体进行检测
def check_one_paragraph(paragraph, true_values):
    para_error_dict = {}
    # 对段落格式进行检查
    format_values = get_format(paragraph)
    for key, value in format_values.items():
        if format_values[key] != true_values[key]:
            para_error_dict[key] = "错误, 这里为{}， 正确值应为{}".format(format_values[key], true_values[key])
    # 对字体格式进行检查
    char_set = set()
    for char in paragraph.Range.Characters:
        font_values = get_font(char)
        for key, value in font_values.items():
           if key == "字体":
               if not (font_values[key] == true_values["中文字体"] or font_values[key] == true_values["英文字体"]):
                   char_set.add(font_values[key])
                   para_error_dict[key] = "错误, 这里为{}， 正确值为{}或{}".format(char_set, true_values["中文字体"], true_values["英文字体"])
           else:
              if font_values[key] != true_values[key]:
                  para_error_dict[key] = "错误，这里为{}， 正确值为{}".format(font_values[key], true_values[key])
    return para_error_dict


#获取边框信息
# def get_border_info(table):
#     border_info = {}
#     borders = {
#         'Top': win32.constants.wdBorderTop,
#         'Bottom': win32.constants.wdBorderBottom,
#         'Left': win32.constants.wdBorderLeft,
#         'Right': win32.constants.wdBorderRight,
#         #'InsideHorizontal': win32.constants.wdBorderHorizontal,
#         #'InsideVertical': win32.constants.wdBorderVertical
#     }
#     for name, border_id in borders.items():
#         border = table.Borders(border_id)
#         border_info[name] = {
#             "外框线宽": border.LineWidth,
#             "外框可见": border.Visible
#         }
#     alignment = table.Range.ParagraphFormat.Alignment
#     border_info["对齐方式"] = alignment
#     return border_info

# wdBorderBottom	-3	底边框线。
# wdBorderDiagonalDown	-7	方向从左上角开始的斜向边框线。
# wdBorderDiagonalUp	-8	方向从左下角开始的斜向边框线。
# wdBorderHorizontal	-5	横向框线。
# wdBorderLeft	-2	左侧框线。
# wdBorderRight	-4	右侧框线。
# wdBorderTop	-1	上框线。
# wdBorderVertical	-6	纵向框线。

def get_border_info(table):
    border_info = {}
    borders = {
        'Top': -1,
        'Bottom': -3,
        'Left': -2,
        'Right': -4,
        #'InsideHorizontal': win32.constants.wdBorderHorizontal,
        #'InsideVertical': win32.constants.wdBorderVertical
    }
    for name, border_id in borders.items():
        border = table.Borders(border_id)
        border_info[name] = {
            "外框线宽": border.LineWidth,
            "外框可见": border.Visible
        }
    alignment = table.Range.ParagraphFormat.Alignment
    border_info["对齐方式"] = alignment
    return border_info

#获取单元格内信息
def get_cell_info(cell):
    cell_value = {
       # "对齐方式": cell.Range.ParagraphFormat.Alignment,
        "字体名称": cell.Range.Font.Name,
        "字号": cell.Range.Font.Size,
        #"行距": cell.Range.ParagraphFormat.LineSpacing,
        #"首行缩进": cell.Range.ParagraphFormat.FirstLineIndent,
        #"段前间距": cell.Range.ParagraphFormat.SpaceBefore,
        #"段后间距": cell.Range.ParagraphFormat.SpaceAfter,
    }
    return cell_value

#检查一个表格
# def check_one_table(table, true_values):
#     error_dict = {}
#     # 对表格边框进行检查
#     border_info = get_border_info(table)
#     for key, value in border_info.items():
#         if (border_info[key]["线型"] != true_values["线型"] or border_info[key]["线宽"] != true_values["线宽"] or border_info[key]["颜色"] != true_values["颜色"]
#                 or border_info[key]["可见性"] != true_values["可见性"]):
#             error_dict[key] = "错误"
#     # 对表格内容进行检查
#     if table.Rows.Count == 0 or table.Columns.Count == 0:
#         error_dict["内容"] = "空表格"
#         return error_dict
#     for row_index in range(1, table.Rows.Count + 1):
#         for column_index in range(1, table.Columns.Count + 1):
#             # 首先检查这个单元格是否存在，避免合并单元格导致的错误
#             try:
#                 # 尝试访问单元格，如果单元格不存在，会引发异常
#                 cell = table.Cell(row_index, column_index)
#             except:
#                 # 如果单元格不存在，则跳过后续操作
#                 continue
#             cell_value = get_cell_info(cell)
#             for key, value in cell_value.items():
#                 if key == "字体名称:":
#                     if cell_value[key] != true_values["中文字体"] and cell_value[key] != true_values["英文字体"]:
#                         error_dict[key] = "错误"
#                 else:
#                     if cell_value[key] != true_values[key]:
#                         error_dict[key] = "错误"
#     return error_dict
def check_one_table(table, true_values1, true_values2):
    error_dict = {}
    # 对表格边框进行检查
    border_info = get_border_info(table)
    for key, value in border_info.items():
        if key in ['Top', 'Bottom', 'Left', 'Right']:#检查外部边框
            border_line = "外框线"
            for k1, v1 in value.items():
                if border_info[key][k1] != true_values1[k1]:
                    if key in error_dict:
                        error_dict[key].append(f"{k1}错误,{k1}为{v1}，应为{true_values1[k1]}")
                    else:
                        error_dict[key] = [f"{k1}错误,{k1}为{v1}，应为{true_values1[k1]}"]
        # elif key in ['InsideHorizontal', 'InsideVertical']:
        #     border_line = "内框线"
        #     for k1, v1 in value.items():
        #         if border_info[key][k1] != true_values[border_line][k1]:
        #             if key in error_dict:
        #                 error_dict[key].append(f"{k1}错误,{k1}为{v1}，应为{true_values[border_line][k1]}")
        #             else:
        #                 error_dict[key] = [f"{k1}错误,{k1}为{v1}，应为{true_values[border_line][k1]}"]
        else:
            if border_info[key] != true_values1[key]:
                error_dict[key] = f"{key}错误，{key}为{border_info[key]}，应为{true_values1[key]}"


    # 对表格内容进行检查
    if table.Rows.Count == 0 or table.Columns.Count == 0:
        error_dict["内容"] = "空表格"
        return error_dict
    cell_dict = {}
    for row_index in range(1, table.Rows.Count + 1):
        for column_index in range(1, table.Columns.Count + 1):
            # 首先检查这个单元格是否存在，避免合并单元格导致的错误
            try:
                # 尝试访问单元格，如果单元格不存在，会引发异常
                cell = table.Cell(row_index, column_index)
            except:
                # 如果单元格不存在，则跳过后续操作
                continue
            cell_value = get_cell_info(cell)
            for key, value in cell_value.items():
                if key == "字体名称":
                    if not (cell_value[key] == true_values2["中文字体"] or cell_value[key] == true_values2["英文字体"]):
                        if (row_index, column_index)  in cell_dict:
                            cell_dict[(row_index, column_index)].append(f'{key}错误，这里为{cell_value[key]}，正确应为'
                                                                        f'{true_values2["中文字体"]}或{true_values2["英文字体"]}"')
                        else:
                            cell_dict[(row_index, column_index)] = [f'{key}错误，这里为{cell_value[key]}，正确应为'
                                                                        f'{true_values2["中文字体"]}或{true_values2["英文字体"]}"']
                else:
                    if cell_value[key] != true_values2[key]:
                        if (row_index, column_index)  in cell_dict:
                            cell_dict[(row_index, column_index)].append(f'{key}错误,这里为{cell_value[key]}，正确应为{true_values2[key]}')
                        else:
                            cell_dict[(row_index, column_index)] = [f'{key}错误,这里为{cell_value[key]}，正确应为{true_values2[key]}']
    if len(cell_dict) > 0:
        error_dict["单元格"] = cell_dict

    return error_dict

#检查表格跨页
def check_tables_for_pagination(table):
    # 获取表格开始页
    first_cell = table.Cell(1, 1)
    #start_page = first_cell.Range.Information(win32.constants.wdActiveEndAdjustedPageNumber)
    start_page = first_cell.Range.Information(1)
    # 获取表格结束页
    last_row = table.Rows.Count
    last_col = table.Columns.Count
    last_cell = table.Cell(last_row, last_col)
    #end_page = last_cell.Range.Information(win32.constants.wdActiveEndAdjustedPageNumber)
    end_page = last_cell.Range.Information(1)
    #如果表格跨页
    if start_page != end_page:
        if table.Rows.Count > 0:  # 确保表格至少有一行
            heading_format = table.Rows(1).HeadingFormat  # 检查第一行是否设置为在新页顶部重复显示
            if heading_format:
                return {}
            else:
                return {"表格跨页": "未设置表格跨页"}

    else:
        return {}


#检查段落中有没有图片，输出图片所在段落的索引
def check_paragraphs_for_any_images(doc):
    img_list = []
    for i, paragraph in enumerate(doc.Paragraphs, start=1):
        inline_images = len(paragraph.Range.InlineShapes)
        has_floating_images = any(
            shape.Anchor.Information(win32.constants.wdFirstCharacterLineNumber) == paragraph.Range.Start
            for shape in doc.Shapes if shape.Type in [11, 13]
        )
        # has_floating_images = any(
        #     shape.Anchor.Information(win32.constants.wdFirstCharacterLineNumber) == paragraph.Range.Start
        #     for shape in doc.Shapes if shape.Type in [win32.constants.msoLinkedPicture, win32.constants.msoPicture]
        # )
        if inline_images > 0 or has_floating_images:
            img_list.append(i)
    return img_list


