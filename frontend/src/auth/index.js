import '../vendor/bootstrap'
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from '../plugins/vuetify'

Vue.config.productionTip = false
Vue.prototype.$auth = Vue.observable(require('../vendor/auth'))
Vue.prototype.$snackbar = Vue.observable(require('../vendor/snackbar'))
Vue.prototype.$rules = Vue.observable(require('air-vue-model/rules'))

new Vue({
    router,
    vuetify,
    render: h => h(App)
}).$mount('#app')
