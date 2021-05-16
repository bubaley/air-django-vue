<template>
    <v-app>
        <v-main v-if="!loading">
            <router-view></router-view>
        </v-main>
    </v-app>
</template>

<script>

export default {
    name: 'App',
    components: {

    },
    data: () => ({
        loading: true
    }),
    async created() {
        await this.$auth.me().catch(() => {})
        if (this.$auth.user)
            window.location.href = this.$route.query.path || this.$auth.success
        else
            this.loading = false
    }
}
</script>
