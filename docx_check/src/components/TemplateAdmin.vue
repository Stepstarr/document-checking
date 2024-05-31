<template>
    <div class="container">
      <section class="section">
        <div v-if="error" class="notification is-danger is-light">
          <button class="delete" @click="error=''"></button>
          {{error}}
        </div>
        
        <div class="field">
          <label class="label">上传模板：</label>
  
          <div class="field has-addons">
            <div class="control">
              <div class="file has-name">
                <label class="file-label">
                  <input class="file-input" type="file" accept=".docx" multiple @change="onFileChange">
                  <span class="file-cta">
                    <span class="file-icon">
                      <font-awesome-icon icon="upload" />
                    </span>
                    <span class="file-label">
                      模板
                    </span>
                  </span>
                  <span class="file-name">
                    <span v-if="files && files.length">
                      已上传 <strong>{{files.length}}</strong> 个模板
                    </span>
                    <span v-else>请选择模板...</span>
                  </span>
                </label>

                <div class="buttons ml-5">
                    <button class="button is-primary" :class="{'is-loading': checking}" @click="check" :disabled="!canCheck">加载模板</button>
                </div>
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
                {{f.name}}
              </li>
            </ol>
          </div>
  
        </div>
  
        <hr />
      </section>
    </div>
</template>
        
        

        
        
        
        
      
  
<script>
import axios from 'axios';

export default {
  name: 'Home',
  data () {
    return {
      files: [],
      error: '',
      fError: false,
      index: -1,
      messages: '',
      
      downloadUrl: null,
      downloadFiles: [],
      confirmMessage: false,
      isChecking: false,
      isCheckAll: false,
      isCommentAll: false,
      commentIndex: 0,
    }
  },
  computed: {
    canCheck () {
      return this.files.length
    },
    checking () {
      return this.isChecking
    },
    checkAll () {
      return this.isCheckAll && this.isCommentAll
    },
    correcting () {
      return
    },
    checkConfirm () {
      return this.confirmMessage
    }
  },
  watch: {
    config: function (val) {
      if (val) {
        this.loadConfig()
      }
    },
    index: function (val) {
      if (val >= 0) {
        this.checkOne()
      }
    },
  },
  // mounted() {
  //   this.initializeEventSource();
  // },
  methods: {
    onFileChange (e) {
      var files = e.target.files || e.dataTransfer.files;
      console.log(files[0])
      var validExtension = ['.docx'];
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
    clearError(){
      this.fError = false;
    },
    check () {
      if (!this.canCheck || this.checking) {
        return
      }
      // this.confirmMessage = true
      this.index = 0
      this.commentIndex = 0
      this.isCommentAll = false
      this.isChecking = true
    },
    
      
      // this.socket = new WebSocket('wss://your-websocket-server-url');

      // this.socket.onmessage = (event) => {
      //     // Append received message to data
      //     this.messages += `${event.data}\n`;
      // };

      // this.socket.onerror = (event) => {
      //     console.error('WebSocket error:', event);
      // };

      // this.socket.onclose = (event) => {
      //     console.log('WebSocket closed:', event);
      // };
    
    async checkOne () {
      
      if (this.index >= this.files.length) {
        this.isCheckAll = true
        this.index = -1
        return
      }
      // this.initializeEventSource()
      console.log('checkOne', this.index)
      console.log('checkOne start')
      console.log(this.index)
      // var replacements = {}
      // for (const r of this.replacements) {
      //   var name = r.name.trim()
      //   if (name) {
      //     replacements[name] = r.value
      //   }
      // }

      var file = this.files[this.index]
      console.log(file.name)
      // this.initializeEventSource(file.name)
      var vm = this
      const formData = new FormData();
      formData.append('file', file);
      try {
          const response = await axios.post('http://127.0.0.1:5000/upload', formData, {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
          });
          console.log(response.data)
          console.log(response.data.filepath)
          this.downloadUrl = response.data.filepath; // 假设后端返回的是处理后文件的URL
          this.initializeEventSource(this.downloadUrl)
          const commentDownloadUrl = response.data.addpath;// 带批注文件url
          const lastIndex = commentDownloadUrl.lastIndexOf('\\');
          const commentFilename = commentDownloadUrl.substring(lastIndex + 1);
          const newFile = {
              name: commentFilename, // 批注文件名
              url: commentDownloadUrl // 模拟文件下载链接
          };
          console.log("receiving documents")
          this.downloadFiles.push(newFile);
          console.log(this.downloadFiles[0].url)
          vm.index = vm.index + 1
          console.log(this.checking)
      } catch (error) {
          console.error('上传文件失败:', error);
      }
      // var reader = new FileReader();
      // reader.onload = function(e) {
      //   // binary data
      //   var content = e.target.result
      //   const zip = new PizZip(content);
      //   const doc = new Docxtemplater(zip, {
      //     paragraphLoop: true,
      //     linebreaks: true,
      //   });
      //   doc.render(replacements);
      //   const out = doc.getZip().generate({
      //     type: "blob",
      //     mimeType:
      //       "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
      //   });
      //   // Output the document using Data-URI
      //   saveAs(out, file.name);
      // vm.index = vm.index + 1
    },
    async downloadFile(url) {
      try {  
          const baseDownloadUrl = 'http://127.0.0.1:5000//download?downloadpath='
          var downloadUrl = baseDownloadUrl + url
          console.log(downloadUrl)
          // 调用后端下载接口  
          const response = await axios({  
            url: downloadUrl, // 后端提供的下载接口地址 
            method: 'get',  
            responseType: 'blob', // 告诉axios期望服务器返回的数据类型  
          }); 
    
          // 创建一个 Blob 对象，它表示一个不可变的原始数据块  
          const blob = new Blob([response.data], { type: response.headers['content-type'] });  
    
          // 创建一个链接指向blob对象  
          const fileUrl = window.URL.createObjectURL(blob);  
    
          // 创建一个a标签用于下载  
          const link = document.createElement('a');  
          link.href = fileUrl;
          const lastIndex = url.lastIndexOf('\\');
          const commentFilename = url.substring(lastIndex + 1);
          console.log(commentFilename)
          link.setAttribute('download', commentFilename); // 设置下载文件名  
          document.body.appendChild(link);  
          link.click(); // 模拟点击实现下载
    
          // 下载完成后移除链接和释放对象URL  
          window.URL.revokeObjectURL(fileUrl);  
          document.body.removeChild(link);  
          } catch (error) {  
            console.error('下载文件时发生错误:', error);  
          }  
    },
    
    isConfirmed(){
      this.confirmMessage = false
    },
    scrollToBottom() {  
      // 确保DOM更新后再进行滚动操作  
      this.$nextTick(() => {  
        const textarea = this.$refs.textarea;  
        textarea.scrollTop = textarea.scrollHeight;  
      });  
    },
  //   },
  // },
  // mounted () {
  //   if (this.config) {
  //     this.loadConfig()
  //   } else {
  //     var str = localStorage.getItem('replacements')
  //     if (str) {
  //       this.replacements = JSON.parse(str)
  //     }
  //   }
  },
}
</script>

<style scoped>
.my-url {
  word-break: break-all!important;
  white-space: normal;
}
</style>