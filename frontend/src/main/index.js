import './models'
import '../vendor/bootstrap'
import 'boxicons'
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from '../vendor/vuetify'
import '../vendor/vuesas'

Vue.config.productionTip = false

new Vue({
    router,
    store,
    vuetify,
    render: h => h(App)
}).$mount('#app')
