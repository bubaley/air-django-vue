import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from "@/auth/views/Login";
import Register from "@/auth/views/Register"

const router = require('air-vue-model/router')

const routes = [

    {
        path: '/login',
        name: 'login',
        component: Login,
    },
    {
        path: '/register',
        name: 'register',
        component: Register,
    },
]

export default router(Vue, VueRouter, routes)
