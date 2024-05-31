const marginTypes = [
  {name: '上', component: 'SectionNumber', unit: 'mm'},
  {name: '下', component: 'SectionNumber', unit: 'mm'},
  {name: '左', component: 'SectionNumber', unit: 'mm'},
  {name: '右', component: 'SectionNumber', unit: 'mm'},
]

const chineseFonts = [
  {label: '宋体', value: '宋体'},
  {label: '微软雅黑', value: '微软雅黑'},
  {label: '黑体', value: '黑体'},
  {label: '仿宋', value: '仿宋'},
  {label: '楷体', value: '楷体'},
]

const englishFonts = [
  {label: 'Arial', value: 'Arial'},
  {label: 'Times New Roman', value: 'Times New Roman'},
  {label: 'Arial Unicode MS', value: 'Arial Unicode MS'},
]

const fontSizes = [
  {label: '初号', value: '初号'},
  {label: '小初', value: '小初'},
  {label: '一号', value: '一号'},
  {label: '小一', value: '小一'},
  {label: '二号', value: '二号'},
  {label: '小二', value: '小二'},
  {label: '三号', value: '三号'},
  {label: '小三', value: '小三'},
  {label: '四号', value: '四号'},
  {label: '小四', value: '小四'},
  {label: '五号', value: '五号'},
  {label: '小五', value: '小五'},
  {label: '六号', value: '六号'},
  {label: '小六', value: '小六'},
  {label: '七号', value: '七号'},
  {label: '八号', value: '八号'},
  {label: '5', value: '5'},
  {label: '5.5', value: '5.5'},
  {label: '6.5', value: '6.5'},
  {label: '7.5', value: '7.5'},
  {label: '8', value: '8'},
  {label: '9', value: '9'},
  {label: '10', value: '10'},
  {label: '10.5', value: '10.5'},
  {label: '11', value: '11'},
  {label: '12', value: '12'},
  {label: '14', value: '14'},
  {label: '16', value: '16'},
  {label: '18', value: '18'},
  {label: '20', value: '20'},
  {label: '22', value: '22'},
  {label: '24', value: '24'},
  {label: '26', value: '26'},
  {label: '28', value: '28'},
  {label: '36', value: '36'},
  {label: '48', value: '48'},
  {label: '56', value: '56'},
  {label: '72', value: '72'},
]

const alignments = [
  {label: '左对齐', value: 0},
  {label: '居中', value: 1},
  {label: '右对齐', value: 2},
  {label: '两端对齐', value: 3},
]

const fontTypes = [
  {name: '字体', component: 'SectionSelect', options: chineseFonts},
  {name: '英文字体', component: 'SectionSelect', options: englishFonts},
  {name: '字号', component: 'SectionSelect', options: fontSizes},
  {name: '对齐方式', component: 'SectionSelect', options: alignments},
]

const styleTypes = [
  {name: '字体', component: 'SectionSelect', options: chineseFonts},
  {name: '英文字体', component: 'SectionSelect', options: englishFonts},
  {name: '字号', component: 'SectionSelect', options: fontSizes},
  {name: '对齐方式', component: 'SectionSelect', options: alignments},
  {name: '加粗', component: 'SectionSelect', options: [{label: '加粗', value: 1}, {label: '不加粗', value: 0}]},
  {name: '斜体', component: 'SectionSelect', options: [{label: '斜体', value: 1}, {label: '不斜体', value: 0}]},
  {name: '下划线', component: 'SectionSelect', options: [{label: '下划线', value: 1}, {label: '无下划线', value: 0}]},
  {name: '左缩进', component: 'SectionNumber', unit: '字符'},
  {name: '右缩进', component: 'SectionNumber', unit: '字符'},
  {name: '首行缩进', component: 'SectionNumber', unit: '字符'},
  {name: '段前间距', component: 'SectionNumber', unit: '行'},
  {name: '段后间距', component: 'SectionNumber', unit: '行'},
  {name: '行距', component: 'SectionNumber', unit: '磅'},
]

const pageNumTypes = [
  {name: '字体', component: 'SectionSelect', options: englishFonts},
  {name: '字号', component: 'SectionSelect', options: fontSizes},
  {name: '页码形式', component: 'SectionSelect', options: [{label: 'Ⅰ,Ⅱ,Ⅲ,...', value: 'Ⅰ,Ⅱ,Ⅲ,...'}, {label: '1,2,3,...', value: '1,2,3,...'}]},
  {name: '对齐方式', component: 'SectionSelect', options: alignments},
]

const formTypes = [
  {name: '外框线宽', component: 'SectionNumber', unit: '磅'},
  {name: '外框可见', component: 'SectionSelect', options: [{label: '可见', value: true}, {label: '不可见', value: false}]},
  {name: '对齐方式', component: 'SectionsSelect', options: [{label: '左对齐', value: 0}, {label: '居中', value: 1}, {label: '右对齐', value: 2}]},
]

const formTextTypes = [
  {name: '中文字体', component: 'SectionSelect', options: chineseFonts},
  {name: '英文字体', component: 'SectionSelect', options: englishFonts},
  {name: '字号', component: 'SectionSelect', options: fontSizes},
]


const pageLayoutSections = [
  {name: '页面大小', component: 'CardText'},
  {name: '页边距', component: 'Section', modelTypes: marginTypes},
  {name: '页眉', component: 'Section', modelTypes: fontTypes},
]

const indexSections = [
  {name: '目录标题', component: 'Section', modelTypes: styleTypes},
  {name: '一级目录', component: 'Section', modelTypes: styleTypes},
  {name: '二级目录', component: 'Section', modelTypes: styleTypes},
  {name: '三级目录', component: 'Section', modelTypes: styleTypes},
  {name: '页码', component: 'Section', modelTypes: pageNumTypes},
]

const prefaceSections = [
  {name: '前言标题', component: 'Section', modelTypes: styleTypes},
  {name: '前言正文', component: 'Section', modelTypes: styleTypes},
  {name: '页码', component: 'Section', modelTypes: pageNumTypes},
]

const textSections = [
  {name: '标题1', component: 'Section', modelTypes: styleTypes},
  {name: '标题2', component: 'Section', modelTypes: styleTypes},
  {name: '标题3', component: 'Section', modelTypes: styleTypes},
  {name: '正文内容', component: 'Section', modelTypes: styleTypes},
  {name: '一级列项', component: 'Section', modelTypes: styleTypes},
  {name: '二级列项', component: 'Section', modelTypes: styleTypes},
  {name: '图标题', component: 'Section', modelTypes: styleTypes},
  {name: '表标题', component: 'Section', modelTypes: styleTypes},
  {name: '表格', component: 'Section', modelTypes: formTypes},
  {name: '表格文字', component: 'Section', modelTypes: formTextTypes},
  {name: '页码', component: 'Section', modelTypes: pageNumTypes},
]

export const modelConfig = [
  {name: '页面整体格式', sections: pageLayoutSections},
  {name: '封面', sections: []},
  {name: '目录', sections: indexSections},
  {name: '前言', sections: prefaceSections},
  {name: '正文', sections: textSections},
  {name: '附录', sections: []},
  {name: '参考文献', sections: []},
]


