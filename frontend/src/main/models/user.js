const m = require('air-vue-model/model')()
m.name = 'user'
m.url = 'users'
m.routes = [
    {
        name: 'list',
        component: require('../views/user/UserList')
    },
    {
        name: 'item',
        component: require('../views/user/UserItem'),
        single: true
    }
]
module.exports = m