<template>
    <v-row class="ma-0 fill-height" align="center">
        <v-col cols="10" md="4" offset-md="4" offset="1">
            <v-card class="pa-3">
                <div class="title font-weight-bold">Авторизация</div>
                <v-text-field dense hide-details outlined class="mt-5" label="Логин"
                              v-model="username"></v-text-field>
                <v-text-field @keyup.enter="login" dense hide-details outlined class="mt-5" label="Пароль"
                              type="password"
                              v-model="password"></v-text-field>
                <v-row align="center" class="pa-3 mt-2">
                    <v-btn :disabled="!username || !password" depressed class="text-none px-7" color="primary"
                           :loading="loading" @click="login">Войти
                    </v-btn>
                    <v-spacer></v-spacer>
                    <v-btn class="text-none" text @click="$router.push({'name': 'register'})">Регистрация</v-btn>
                </v-row>
            </v-card>
        </v-col>
    </v-row>
</template>

<script>

export default {
    name: "Login",
    data: () => ({
        username: '',
        password: '',
        loading: false,
    }),
    methods: {
        login() {
            this.loading = true
            this.$auth.login({
                username: this.username,
                password: this.password
            }).then(() => {
                this.loading = false
                window.location.href = this.$route.query.path || this.$auth.success
            }).catch(e => {
                this.loading = false
                this.$snackbar.fail('Неверные данные')
            })
        }
    },
    created() {

    }
}
</script>

<style scoped>

</style>