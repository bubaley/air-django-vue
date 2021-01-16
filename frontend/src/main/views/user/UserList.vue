<template>
    <v-col class="pa-0">
        <div class="mb-3 mt-2">Список пользователей</div>
        <router-link
            v-for="(el, index) in $user.list" :key="index"
            :to="{name: 'userItem', params: {userId: el.id}}">
            <v-row no-gutters align="center">
                <div>{{ el.id }}.</div>
                <div class="ml-3">{{ el.username }}</div>
            </v-row>
        </router-link>
    </v-col>
</template>

<script>
export default {
    name: 'UserList',
    data: () => ({}),
    methods: {},
    created() {
        this.$user.loadList()
    }
}
</script>

<style scoped>

</style>