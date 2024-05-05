# -*- coding: utf-8 -*-
# @Time    : 2024/5/5 14:21
# @Author  : Stepstar
# @FileName: compare_attributes.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
# @Time    : 2024/5/2 19:57
# @Author  : Stepstar
# @FileName: compare_attributes.py
# @Software: PyCharm
def compare_attributes(index,parg,format_dict):
    '''
    这个函数是基本的属性值判断
    TODO：一个段落里，如果有不同的字体， parg.Range.Font.Name等返回的是第一个字体，也就是中间字体等什么的错误不会被识别出来，需补充这点,识别出段落中哪部分字体字号错误了
    并给出错误部分的range范围
    :param parg:段落
    :param format_dict:
    :return:
    '''
    style = {"左缩进:": parg.LeftIndent,
            "右缩进:": parg.RightIndent,
            "首行缩进:": parg.FirstLineIndent,
            "段前间距:": parg.SpaceBefore,
            "段后间距:": parg.SpaceAfter,
            "行距:": parg.LineSpacing,
            "水平对齐方式:": parg.Alignment,
            "字体": parg.Range.Font.Name,
            "字体大小": parg.Range.Font.Size,
            "加粗": parg.Range.Font.Bold,
            "斜体": parg.Range.Font.Italic,
            "下划线:": parg.Range.Font.Underline
                  }
    e = {'错误段落':index,
        '段落Range':None,
        '修改属性': {},
         '类型':'correct',
        '批注':''
        }
    flag = True
    correct_values = format_dict
    for attr, correct_value in correct_values.items():
        actual_value = style.get(attr)
        if actual_value != correct_value:
            flag = False
            e['修改属性'][attr] = correct_value
            e['批注'] += f"属性{attr}错误,当前值为{actual_value},正确值为{correct_value})"+'\n'
        if flag:
            return None
        return e