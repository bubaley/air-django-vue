<template>
    <v-app>
        <v-main v-if="!loading">
            <router-view></router-view>
        </v-main>
        <snackbar></snackbar>
    </v-app>
</template>

<script>

import Snackbar from "@/components/Snackbar";

export default {
    name: 'App',
    components: {
        Snackbar
    },
    data: () => ({
        loading: true
    }),
    async created() {
        await this.$auth.me()
        if (this.$auth.user)
            window.location.href = this.$route.query.path || this.$auth.success
        else
            this.loading = false
    }
}
</script>
