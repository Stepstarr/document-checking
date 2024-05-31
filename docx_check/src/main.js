import { createApp } from 'vue'
import App from './App.vue'
import hw from './components/HelloWorld.vue'
import header from './components/Header.vue'
import 'bulma/css/bulma.css'
import fChecker from './components/FormatChecker.vue'
import { library } from '@fortawesome/fontawesome-svg-core';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { faUpload } from '@fortawesome/free-solid-svg-icons';
import fTemplate from './components/FormatTemplate.vue'
import tAdmin from './components/TemplateAdmin.vue'
import login from './components/Login.vue'
import register from './components/Register.vue'
import sRegister from './components/SuperRegister.vue'
import Buefy from 'buefy';
import 'buefy/dist/buefy.css';
import templateBox from './components/TemplateBox.vue'
import docTemplate from './components/DocTemplate.vue'

library.add(faUpload);
const app = createApp(App)
app.component('my-hw', hw)
app.component('my-header', header)
app.component('my-fChecker', fChecker)
app.component('font-awesome-icon', FontAwesomeIcon)
app.component('my-fTemplate', fTemplate)
app.component('my-tAdmin', tAdmin)
app.component('my-login', login)
app.component('my-register', register)
app.component('my-sRegister', sRegister)
app.component('my-templateBox', templateBox)
app.component('my-docTemplate', docTemplate)

app.mount('#app')
app.use(Buefy);