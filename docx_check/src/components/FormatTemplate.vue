<template>
  <div class="container">
      <section class="section">
          <div v-if="error" class="notification is-danger is-light">
              <button class="delete" @click="error=''"></button>
              {{error}}
          </div>
          <div v-if="message" class="notification is-primary is-light">
              <button class="delete" @click="message=''"></button>
              {{message}}
          </div>
          <div class="field">
              <div class="columns is-variable is-vcentered">
                  <div class="column is-3 has-text-left">
                      <label class="label">模板库:</label>
                  </div>
                  <div class="column" >
                      <div class="file has-name is-right">
                          <label class="file-label">
                              <input class="file-input" type="file" accept=".docx, .doc" multiple @change="onFileChange" ref="fileInput">
                              <span class="file-cta">
                                  <span class="file-icon">
                                      <font-awesome-icon icon="upload" />
                                  </span>
                                  <span class="file-label">
                                      添加模板
                                  </span>
                              </span>
                              <span class="file-name">
                                  <span v-if="files && files.length">
                                      已上传 <strong>{{files.length}}</strong> 个模板
                                  </span>
                                  <span v-else>请选择模板...</span>
                              </span>
                          </label>
                      </div>
                  </div>
              </div>
              <div v-if="fError" class="notification is-danger">
                  <button class="delete" @click="clearError"></button>
                      文档格式错误，只允许上传.docx文档
              </div> 
              
              <div class="control pl-5">
                  <ol>
                      <li v-for="(f, i) in files" :key="'f-'+i">
                          <div class="columns is-variable is-vcentered">
                              <div class="column">
                                  {{f.name}}
                              </div>
                              <div class="column is-2">
                                <button class="delete" @click="removeFile(i)"></button>
                              </div>
                              <div class="column is-4 has-text-right">
                                  <button class="button is-primary" @click="parseTemplate(i)" :loading="parseLoading">
                                      解析模板
                                  </button>
                              </div>
                          </div>
                      </li>
                  </ol>
              </div>
              
              <div class="template-cards" ref="templateCards">
                  <my-docTemplate :templateName="fileName" :templateData="jsonData[0]" :isEditable="isTemplateEditable" v-if="isShowTemplate" @update-template-value="updateTValue($event)"/>
                  
                  <div class="control" v-if="isShowTemplates">
                      <ul>
                          <div class="box">
                              <li v-for="(fname, index) in fileNames" :key="index">
                                  <div class="columns is-variable is-vcentered">
                                      <div class="column is-two-thirds">
                                          <p :class="{ 'has-text-weight-bold': showTemplateName === fname }">{{ index+1 }}.{{ fname }}</p>
                                      </div>
                                      <div class="column has-text-right">
                                          <button class="button is-link is-outlined mb-1" @click="applyTemplate(fname)">应用模板</button>
                                          <button class="button is-link is-outlined" @click="checkTemplate(fname)">查看模板</button>
                                      </div>
                                  </div>
                                  
                                  <hr />
                              </li>
                          </div>
                      </ul>
                  </div>
              </div>
              
              <div class="columns is-variable is-vcentered">
                  <div class="column">
                      <div class="buttons is-right mt-5" v-if="isSaveTemplate">
                          <button class="button is-success" @click="saveTemplate">保存模板</button>
                          <button class="button is-danger" @click="cancelTemplate">取消加载</button>
                      </div>
                      <div class="buttons is-right mt-5" v-if="isViewTemplate">
                          <button class="button is-success" @click="correctTemplate">修改模板</button>
                          <button class="button is-danger" @click="returnTemplates">返回模板库</button>
                      </div>
                      <div class="buttons is-right mt-5" v-if="isEditTemplate">
                          <button class="button is-success" @click="editTemplate">保存模板</button>
                          <button class="button is-danger" @click="returnTemplate">取消</button>
                      </div>
                  </div>
              </div>
          </div>
      
      </section>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Home',
  props: ['applyTemplate'],
  data () {
    return {
        files: [],
        fError: false,
        fileName: '',
        jsonData: '',
        isTemplateEditable: false,
        isShowTemplate: false,
        isShowTemplates: true,
        fileNames: [],
        showTemplateName: this.applyTemplate,
        isSaveTemplate: false,
        isViewTemplate: false,
        isEditTemplate: false,
        message: '',
        error: '',
        parseLoading: false,
    }
  },
  computed: {
    
  },
  watch: {
    isShowTemplates(newValue) {
        if (newValue) {
            this.templatesNames();
        }
    },
  },
  methods: {
    onFileChange (e) {
      var files = e.target.files || e.dataTransfer.files;
      console.log(files[0])
      var validExtension = ['.docx', '.doc'];
      var isValid = true;
      for (const file of files) {  
          if (!validExtension.some(ext => file.name.endsWith(ext))) {  
              isValid = false;  
              break; 
          }
      } 
      if (!isValid){
          this.fError = true;
          this.files = [];
          return;
      }
      if (!files.length)
        return;
      this.fError = false;
      this.files = files;
    },
    clearError() {
      this.fError = false;
    },
    async parseTemplate(index) {
      const fileData = this.files[index];
      this.parseLoading = true;
      if (!fileData) return;
      const formData = new FormData();
      formData.append('file', fileData);
      this.message = "";
      this.error = "";
      try {
        const response = await axios.post('http://127.0.0.1:5000/get-template', formData, {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
        });
        this.fileName = response.data.filename;
        this.jsonData = response.data.filedata;
        this.isShowTemplate = true;
        this.isTemplateEditable = true;
        this.isSaveTemplate = true;
        this.isViewTemplate = false;
        this.parseLoading = false;
        this.isShowTemplates = false;
        this.isEditTemplate = false;
        this.adjustHeight();
        this.message = "模板文件解析成功";
        var vm = this;
        setTimeout(function() {
          vm.message = "";
        }, 5000);
      } catch (error) {
        console.error('Error parsing template:', error);
        this.error = "模板文件解析失败";
        var vm = this;
        setTimeout(function() {
          vm.error = "";
        }, 5000);
      }
    },
    updateTValue(newValue) {
        this.jsonData[0] = newValue;
    },
    async saveTemplate() {
        axios.post('http://127.0.0.1:5000/save-template', {
            fileName: this.fileName,
            jsonData: this.jsonData,
        })
        .then(response => {
            console.log('File saved successfully:', response.data.filename);
            this.isTemplateEditable = false;
            this.isShowTemplate = false;
            this.isShowTemplates = true;
            this.isSaveTemplate = false;
            this.isViewTemplate = false;
            this.isEditTemplate = false;
            this.adjustHeight();
            this.message = "模板文件保存成功";
            var vm = this;
            setTimeout(function() {
              vm.message = "";
            }, 5000);
        })
        .catch(error => {
            console.error('Error saving file:', error);
            this.error = "模板文件保存失败";
            var vm = this;
            setTimeout(function() {
              vm.error = "";
            }, 5000);
        });
    },
    async cancelTemplate() {
        axios.post('http://127.0.0.1:5000/delete-template', {
        fileName: this.fileName
      })
      .then(response => {
        console.log('File deleted successfully:', response.data);
        this.isTemplateEditable = false;
        this.isShowTemplate = false;
        this.isShowTemplates = true;
        this.isSaveTemplate = false;
        this.isViewTemplate = false;
      })
      .catch(error => {
        console.error('Error deleting file:', error);
      });
    },
    async templatesNames() {
      try {
        const response = await axios.get('http://127.0.0.1:5000/get-templates'); // 假设后端 API 地址为 /api/files
        console.log(response.data.filenames)
        this.fileNames = response.data.filenames;
      } catch (error) {
        console.error('Error fetching file names:', error);
        this.error = "模板库读取错误"
      } 
    },
    correctTemplate() {
        this.isTemplateEditable = true;
        this.isViewTemplate = false;
        this.isEditTemplate = true;
        this.message = "";
        this.error = "";
    },
    adjustHeight() {
      this.$nextTick(() => {
        const templateCards = this.$refs.templateCards;
        const windowHeight = window.innerHeight;
        const buttonHeight = this.$el.querySelector('button').offsetHeight;
        const margin = 200; // Adjust for any additional margins or padding
        const newHeight = windowHeight - buttonHeight - margin;
        templateCards.style.height = `${newHeight}px`;
      });
    },
    applyTemplate(fileName) {
        this.showTemplateName = fileName;
        this.$emit('update-value', this.showTemplateName);
    },
    async checkTemplate(fileName) {
        const baseUrl = "http://127.0.0.1:5000/check-template?filename=";
        const sendUrl = baseUrl + fileName;
        try {
            const response = await axios.get(sendUrl); // 假设后端 API 地址为 /api/files
            console.log(response.data.filename)
            this.fileName = response.data.filename;
            this.jsonData = response.data.filedata;
            this.isShowTemplates = false;
            this.isShowTemplate = true;
            this.adjustHeight();
            this.isSaveTemplate = false;
            this.isViewTemplate = true;
        } catch (error) {
            console.error('Error fetching file names:', error);
            this.error = "模板加载发生错误";
        }
    },
    returnTemplates() {
        this.isTemplateEditable = false;
        this.isShowTemplate = false;
        this.isShowTemplates = true;
        this.isSaveTemplate = false;
        this.isViewTemplate = false;
        this.isEditTemplate = false;
    },
    returnTemplate() {
      this.isTemplateEditable = false;
      this.isShowTemplate = true;
      this.isEditTemplate = false;
      this.isViewTemplate = true;
      this.isSaveTemplate = false;
    },
    removeFile(index) {
      const dataTransfer = new DataTransfer();
      var vm = this;
      Array.from(vm.files).forEach((file, idx) => {
        if (index !== idx) {
          dataTransfer.items.add(file);
        }
      });
      vm.files = dataTransfer.files;
      this.$refs.fileInput.value = '';
    },
    async editTemplate() {
      axios.post('http://127.0.0.1:5000/save-template', {
            fileName: this.fileName,
            jsonData: this.jsonData,
        })
        .then(response => {
            console.log('File saved successfully:', response.data.filename);
            this.isTemplateEditable = false;
            this.isShowTemplate = true;
            this.isSaveTemplate = false;
            this.isViewTemplate = true;
            this.isEditTemplate = false;
            this.adjustHeight();
            this.message = "模板文件保存成功";
            var vm = this;
            setTimeout(function() {
              vm.message = "";
            }, 5000);
        })
        .catch(error => {
            console.error('Error saving file:', error);
            this.error = "模板文件保存失败";
            var vm = this;
            setTimeout(function() {
              vm.error = "";
            }, 5000);
        });
    },
  },
  mounted() {
    this.adjustHeight();
    window.addEventListener('resize', this.adjustHeight);
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.adjustHeight);
  },
  created() {
    if (this.isShowTemplates) {
      this.templatesNames();
    }
  }
}
</script>
<style>
.template-cards {
  overflow-y: auto; /* 允许垂直滚动 */
  overflow-x: hidden; /* 防止水平滚动，除非需要 */
  border: 1px solid #ffffff;
  padding: 1em;
  margin-top: 1em;
}
</style>