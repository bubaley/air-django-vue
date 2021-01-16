<template>
    <v-col class="pa-0">
        <v-row no-gutters align="center">
            <div>{{ $user.item.id }}.</div>
            <div class="ml-3">{{ $user.item.username }}</div>
        </v-row>
    </v-col>
</template>

<script>
export default {
    name: 'UserItem',
    data: () => ({}),
    methods: {}
}
</script>

<style scoped>

</style>