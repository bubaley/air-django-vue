<template>
    <v-snackbar
            v-model="$snackbar.value"
            top
            style="top: 15px; right: 12px"
            right
            class="pa-0"
            :color="$snackbar.color"
            :timeout="1000"
    >
        {{ $snackbar.text }}
    </v-snackbar>
</template>

<script>
    export default {
        name: "Snackbar"
    }
</script>

<style scoped>

</style>