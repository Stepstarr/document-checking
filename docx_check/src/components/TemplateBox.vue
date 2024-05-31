<template>
    <div class="container">
        <div class="box">
            <div class="columns is-variable is-vcentered">
                <div class="column is-3 ">
                    <label class="label">当前模板:</label>
                </div>
                <div class="column has-text-left">
                    <p>{{ templateName }}</p>
                </div>
                <!-- <div class="column is-3 has-text-right">
                    <a>全部模板</a>
                </div> -->
            </div>
        </div>
        
        <div class="card">
            <header class="card-header">
                <p class="card-header-title">页面整体格式</p>
                <a class="card-header-icon" @click="toggleCardContent">
                    {{ isCloseP? '展开' : '收起' }}
                </a>
            </header>
            <div class="card-content" v-if="!isCloseP">
                <div class="columns is-variable is-vcentered">
                    <div class="column is-3 has-text-left">
                        <label class="label">页面大小</label>
                    </div>
                    <div class="column">
                        <input class="input" type="text" v-model="templateData.页面整体格式.页面大小" :readonly="!isEditable"/>
                    </div>
                </div>
                <div class="columns is-variable">
                    <div class="column is-3 has-text-left">
                        <lable class="label">页边距</lable>
                    </div>
                    <div class="column">
                        <div class="columns is-variable is-vcentered">
                            <div class="column is-one-third has-text-right">
                                <p>上:</p>
                            </div>
                            <div class="column is-centered">
                                <input class="input" type="text" v-model="templateData.页面整体格式.页边距.上" :class="{'is-danger': !isNumber && number.length > 0}" @input="validateInput" :readonly="!isEditable">
                            </div>
                            <div class="column has-text-left">
                                <p>mm</p>
                            </div>
                        </div>
                        <div class="columns is-variable is-vcentered">
                            <div class="column is-one-third has-text-right">
                                <p>下:</p>
                            </div>
                            <div class="column is-centered">
                                <input class="input" type="text" v-model="templateData.页面整体格式.页边距.下" :class="{'is-danger': !isNumber && number.length > 0}" @input="validateInput" :readonly="!isEditable">
                            </div>
                            <div class="column has-text-left">
                                <p>mm</p>
                            </div>
                        </div>
                        <div class="columns is-variable is-vcentered">
                            <div class="column is-one-third has-text-right">
                                <p>左:</p>
                            </div>
                            <div class="column is-centered">
                                <input class="input" type="text" v-model="templateData.页面整体格式.页边距.左" :class="{'is-danger': !isNumber && number.length > 0}" @input="validateInput" :readonly="!isEditable">
                            </div>
                            <div class="column has-text-left">
                                <p>mm</p>
                            </div>
                        </div>
                        <div class="columns is-variable is-vcentered">
                            <div class="column is-one-third has-text-right">
                                <p>右:</p>
                            </div>
                            <div class="column is-centered">
                                <input class="input" type="text" v-model="templateData.页面整体格式.页边距.右" :class="{'is-danger': !isNumber && number.length > 0}" @input="validateInput" :readonly="!isEditable">
                            </div>
                            <div class="column has-text-left">
                                <p>mm</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="columns is-variable">
                    <div class="column is-3 has-text-left">
                        <label class="label">页眉</label>
                    </div>
                    <div class="column">
                        <div class="columns is-variable is-vcentered">
                            <div class="column is-one-third has-text-right">
                                <p>字体:</p>
                            </div>
                            <div class="column is-6 ">
                                <div class="select is-fullwidth">
                                    <select v-model="templateData.页面整体格式.页眉.字体" :disabled="!isEditable">
                                        <option v-for="font in fontListC" :value="font">{{ font }}</option>
                                    </select>
                                </div>
                            </div>
                        </div>
                        <div class="columns is-variable is-vcentered">
                            <div class="column is-one-third has-text-right">
                                <p>英文字体:</p>
                            </div>
                            <div class="column is-6 ">
                                <div class="select is-fullwidth">
                                    <select v-model="templateData.页面整体格式.页眉.中文字体" :disabled="!isEditable">
                                        <option v-for="font in fontListE" :value="font">{{ font }}</option>
                                    </select>
                                </div>
                            </div>
                        </div>
                        <div class="columns is-variable is-vcentered">
                            <div class="column is-one-third has-text-right">
                                <p>字号:</p>
                            </div>
                            <div class="column is-6">
                                <div class="select is-fullwidth">
                                    <select v-model="templateData.页面整体格式.页眉.字号" :disabled="!isEditable">
                                        <option v-for="fontSize in fontSizeList" :value="fontSize">{{ fontSize }}</option>
                                    </select>
                                </div>
                            </div>
                        </div>
                        <div class="columns is-variable is-vcentered">
                            <div class="column is-one-third has-text-right">
                                <p>对齐方式:</p>
                            </div>
                            <div class="column is-6">
                                <div class="select is-fullwidth">
                                    <select v-model="templateData.页面整体格式.页眉.对齐方式" :disabled="!isEditable">
                                        <option v-for="align in alignmentsList" :value="align">{{ align }}</option>
                                    </select>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="card">
            <header class="card-header">
                <p class="card-header-title">目录设置</p>
            </header>
            <div class="card-content">
                <div class="columns is-variable ">
                    <div class="column is-3 has-text-left">
                        <label class="label">目录标题</label>
                    </div>
                    <div class="column">
                        <div class="columns is-variable is-vcentered">
                            <div class="column is-one-third has-text-right">
                                <p>中文字体:</p>
                            </div>
                            <div class="column is-6 ">
                                <div class="select is-fullwidth">
                                    <select v-model="templateData.目录.目录标题.中文字体" :disabled="!isEditable">
                                        <option v-for="font in fontListC" :value="font">{{ font }}</option>
                                    </select>
                                </div>
                            </div>
                        </div>
                        <div class="columns is-variable is-vcentered">
                            <div class="column is-one-third has-text-right">
                                <p>英文字体:</p>
                            </div>
                            <div class="column is-6 ">
                                <div class="select is-fullwidth">
                                    <select v-model="templateData.目录.目录标题.英文字体" :disabled="!isEditable">
                                        <option v-for="font in fontListE" :value="font">{{ font }}</option>
                                    </select>
                                </div>
                            </div>
                        </div>
                        <div class="columns is-variable is-vcentered">
                            <div class="column is-one-third has-text-right">
                                <p>字号:</p>
                            </div>
                            <div class="column is-6">
                                <div class="select is-fullwidth">
                                    <select v-model="templateData.目录.目录标题.字号" :disabled="!isEditable">
                                        <option v-for="fontSize in fontSizeList" :value="fontSize">{{ fontSize }}</option>
                                    </select>
                                </div>
                            </div>
                        </div>
                        <div class="columns is-variable is-vcentered">
                            <div class="column is-one-third has-text-right">
                                <p>对齐方式:</p>
                            </div>
                            <div class="column is-6">
                                <div class="select is-fullwidth">
                                    <select v-model="templateData.目录.目录标题.对齐方式" :disabled="!isEditable">
                                        <option v-for="align in alignmentsList" :value="align">{{ align }}</option>
                                    </select>
                                </div>
                            </div>
                        </div>
                        <div class="columns is-variable is-vcentered">
                            <div class="column is-one-third has-text-right">
                                <p>加粗:</p>
                            </div>
                            <div class="column is-6">
                                <div class="select is-fullwidth">
                                    <select v-model="templateData.目录.目录标题.加粗" :disabled="!isEditable">
                                        <option v-for="bold in boldList" :value="bold">{{ bold }}</option>
                                    </select>
                                </div>
                            </div>
                        </div>
                        <div class="columns is-variable is-vcentered">
                            <div class="column is-one-third has-text-right">
                                <p>斜体:</p>
                            </div>
                            <div class="column is-6">
                                <div class="select is-fullwidth">
                                    <select v-model="templateData.目录.目录标题.斜体" :disabled="!isEditable">
                                        <option v-for="italic in italicList" :value="italic">{{ italic }}</option>
                                    </select>
                                </div>
                            </div>
                        </div>
                        <div class="columns is-variable is-vcentered">
                            <div class="column is-one-third has-text-right">
                                <p>下划线:</p>
                            </div>
                            <div class="column is-6">
                                <div class="select is-fullwidth">
                                    <select v-model="templateData.目录.目录标题.下划线" :disabled="!isEditable">
                                        <option v-for="underline in underlineList" :value="underline">{{ underline }}</option>
                                    </select>
                                </div>
                            </div>
                        </div>
                        <div class="columns is-variable is-vcentered">
                            <div class="column is-one-third has-text-right">
                                <p>左缩进:</p>
                            </div>
                            <div class="column is-centered">
                                <input class="input" type="text" v-model="templateData.目录.目录标题.左缩进" :class="{'is-danger': !isNumber && number.length > 0}" @input="validateInput" :readonly="!isEditable">
                            </div>
                            <div class="column has-text-left">
                                <p>字符</p>
                            </div>
                        </div>
                        <div class="columns is-variable is-vcentered">
                            <div class="column is-one-third has-text-right">
                                <p>右缩进:</p>
                            </div>
                            <div class="column is-centered">
                                <input class="input" type="text" v-model="templateData.目录.目录标题.右缩进" :class="{'is-danger': !isNumber && number.length > 0}" @input="validateInput" :readonly="!isEditable">
                            </div>
                            <div class="column has-text-left">
                                <p>字符</p>
                            </div>
                        </div>
                        <div class="columns is-variable is-vcentered">
                            <div class="column is-one-third has-text-right">
                                <p>首行缩进:</p>
                            </div>
                            <div class="column is-centered">
                                <input class="input" type="text" v-model="templateData.目录.目录标题.首行缩进" :class="{'is-danger': !isNumber && number.length > 0}" @input="validateInput" :readonly="!isEditable">
                            </div>
                            <div class="column has-text-left">
                                <p>字符</p>
                            </div>
                        </div>
                        <div class="columns is-variable is-vcentered">
                            <div class="column is-one-third has-text-right">
                                <p>段前间距:</p>
                            </div>
                            <div class="column is-centered">
                                <input class="input" type="text" v-model="templateData.目录.目录标题.段前间距" :class="{'is-danger': !isNumber && number.length > 0}" @input="validateInput" :readonly="!isEditable">
                            </div>
                            <div class="column has-text-left">
                                <p>行</p>
                            </div>
                        </div>
                        <div class="columns is-variable is-vcentered">
                            <div class="column is-one-third has-text-right">
                                <p>段后间距:</p>
                            </div>
                            <div class="column is-centered">
                                <input class="input" type="text" v-model="templateData.目录.目录标题.段后间距" :class="{'is-danger': !isNumber && number.length > 0}" @input="validateInput" :readonly="!isEditable">
                            </div>
                            <div class="column has-text-left">
                                <p>行</p>
                            </div>
                        </div>
                        <div class="columns is-variable is-vcentered">
                            <div class="column is-one-third has-text-right">
                                <p>行距:</p>
                            </div>
                            <div class="column is-centered">
                                <input class="input" type="text" v-model="templateData.目录.目录标题.行距" :class="{'is-danger': !isNumber && number.length > 0}" @input="validateInput" :readonly="!isEditable">
                            </div>
                            <div class="column has-text-left">
                                <p>磅</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
export default {
  props: ['templateName', 'templateData', 'isEditable'],
  data() {
    return {
      number: 10,
    //   headercnFont: '宋体', 
    //   headerenFont: '',
    //   headerFontSize: '',
    //   headerAlign: '',
    //   pageSize:'',
    //   dircFont:'',
    //   direFont:'',
    //   dirFontSize:'',
    //   dirAlign:'',
    //   dirBold:'',
    //   dirItalic:'',
    //   dirUnderline:'',
    //   dirBps:'',
    //   dirAps:'',
    //   dirParaSpace:'',
    //   dirLeftIndent:'',
    //   dirRightIndent:'',
    //   dirfParaIndent:'',
      fontListC: ['宋体', '微软雅黑', '黑体', '仿宋', '楷体'],
      fontListE: ['Arial', 'Times New Roman', 'Arial Unicode MS'],
      fontSizeList: ['初号', '小初', '一号', '小一', '二号', '小二', '三号', '小三', '四号', '小四', '五号', '小五', '六号', '小六', '七号', '八号', '5', '5.5', '6.5', '7.5', '8', '9', '10', '10.5', '11', '12', '14', '16', '18', '20', '22', '24', '26', '28', '36', '48', '56', '72'],
      alignmentsList: ['左对齐', '居中', '右对齐', '两端对齐'],
      boldList: ['加粗', '不加粗'],
      italicList: ['斜体', '不斜体'],
      underlineList: ['下划线', '无下划线'],
      isCloseP: false,
      templateData: this.templateData,
    }
  },
  computed: {
    isNumber() {
        // 检查输入是否为数字
        return /^\d+$/.test(this.number);
    }
  },
  watch: {
    templateData(newValue) {
        if (newValue) {
            this.$emit('update-template-value', this.templateData);
        }
    }
  },
  methods: {
    validateInput() {
        if (!this.isNumber && this.number.length > 0) {
            this.number = this.number.replace(/[^0-9]/g, '');
        }
    },
    toggleCardContent() {
        this.isCloseP = !this.isCloseP;
    }
  },
}
</script>