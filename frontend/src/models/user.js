const m = require('air-vue-model/model')()
m.name = 'user'
m.url = 'users'
m.routes = [
    {
        name: 'list',
        component: require('../main/views/user/UserList')
    },
    {
        name: 'item',
        component: require('../main/views/user/UserItem'),
        single: true
    }
]
module.exports = m