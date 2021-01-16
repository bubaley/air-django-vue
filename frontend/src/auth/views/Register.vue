<template>
    <v-row align="center" class="ma-0 fill-height">
        <v-col cols="10" md="4" offset-md="4" offset="1">
            <v-card>
                <v-alert text tile border="top" color="error" class="ma-0" v-if="errors.length > 0">
                    <v-row align="center" class="pa-0">
                        <div class="body-2" v-for="(el, index) in errors" :key="index">{{ el }}</div>
                    </v-row>
                </v-alert>
                <v-col class="pa-3">
                    <div class="title font-weight-bold">Регистрация</div>
                    <v-form
                        ref="form"
                        v-model="form"
                    >
                        <v-text-field ref="username" dense :rules="[$rules.required, $rules.login]" outlined
                                      class="mt-5"
                                      label="Логин"
                                      v-model="username"></v-text-field>
                        <v-text-field ref="email" type="email" :rules="[$rules.required, $rules.email]" dense outlined
                                      label="Почта"
                                      v-model="email"></v-text-field>
                        <v-text-field ref="password" :rules="[$rules.required, $rules.password, $rules.minLen(8)]"
                                      dense
                                      outlined
                                      label="Пароль" type="password"
                                      v-model="password"></v-text-field>
                        <v-text-field
                            outlined
                            dense
                            v-model="password_confirmation"
                            label="Подтвердите пароль"
                            type="password"
                            :rules="[$rules.required, $rules.match(password)]"
                        />
                        <v-row align="center" class="pa-3">
                            <v-btn :disabled="!form" depressed class="text-none" color="primary" :loading="loading"
                                   @click="register">
                                Регистрация
                            </v-btn>
                            <v-spacer></v-spacer>
                            <v-btn class="text-none" text @click="$router.push({'name': 'login'})">Войти</v-btn>
                        </v-row>
                    </v-form>
                </v-col>
            </v-card>
        </v-col>
    </v-row>
</template>

<script>

export default {
    name: "Register",
    data: () => ({
        username: '',
        password: '',
        password_confirmation: '',
        email: '',
        form: false,
        loading: false,
        errors: [],
    }),
    methods: {
        register() {
            this.loading = true
            this.$auth.register({
                username: this.username,
                password: this.password,
                email: this.email
            }).then(() => {
                this.loading = false
                window.location.href = this.$auth.success
                this.loading = false
            }).catch(e => {
            })
        }
    }
}
</script>

<style scoped>

</style>