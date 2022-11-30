import { createApp } from 'vue'
import App from './App.vue'
import "vue-select/dist/vue-select.css";


import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css';
import router from './router'

createApp(App).use(router).mount('#app')
