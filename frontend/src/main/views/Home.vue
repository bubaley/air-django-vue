<template>
    <v-main>
        <v-app-bar app>
            <div>Application</div>
            <v-spacer></v-spacer>
            <v-btn small :to="{name: 'userList'}">Пользователи</v-btn>
            <v-btn small class="ml-3" @click="logout">Выйти</v-btn>
        </v-app-bar>
        <v-container>
            <router-view></router-view>
        </v-container>
    </v-main>
</template>

<script>
export default {
    name: 'Home',
    data: () => ({}),
    methods: {
        logout() {
            this.$auth.logout()
            window.location.href = '/login'
        }
    }
}
</script>

<style scoped>

</style>