import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from './views/Home.vue'
import NotFound from "@/components/NotFound";

const router = require('air-vue-model/router')

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home,
        meta: {
            auth: true
        },
        children: [
            ...Vue.prototype.$user.getRoutes()
        ]
    },
    {
        path: '*',
        component: NotFound
    }
]
export default router(Vue, VueRouter, routes)
