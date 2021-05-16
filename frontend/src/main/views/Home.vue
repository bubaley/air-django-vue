<template>
    <v-main>
        <v-app-bar app>
            <div>Application</div>
            <v-spacer></v-spacer>
            <vs-button :to="{name: 'userList'}">Пользователи</vs-button>
            <vs-button @click="logout" class="px-1">
                <i class="bx bx-exit mr-2 mt-1"></i>
                <div class="font-weight-medium">Выйти</div>
                <!--                <box-icon size="sm" name='exit'></box-icon>-->
                <!--                Выйти-->
            </vs-button>
        </v-app-bar>
        <v-container>
            <vs-card>
                <template slot="title">
                    <h3>Pot with a plant</h3>
                </template>
                <template slot="img">
                    <img
                        src="https://interactive-examples.mdn.mozilla.net/media/cc0-images/grapefruit-slice-332-332.jpg"
                        alt="">
                    <!--                    <v-img-->
                    <!--                        src="https://interactive-examples.mdn.mozilla.net/media/cc0-images/grapefruit-slice-332-332.jpg"></v-img>-->
                </template>
                <template slot="text">
                    <p>
                        Lorem ipsum dolor sit amet consectetur, adipisicing elit.
                    </p>
                </template>
                <template #interactions>
                    <vs-button danger icon>
                        <i class='bx bx-heart'></i>
                    </vs-button>
                    <vs-button class="btn-chat" shadow primary>
                        <i class='bx bx-chat'></i>
                        <span class="span">
          54
        </span>
                    </vs-button>
                </template>
                <template slot="buttons">
                    <v-row no-gutters align="center" class="pb-2 px-1">
                        <vs-button danger>
                            <i class="fas fa-users"></i>
                            <i class="fas fa-users"></i>
                            asdas
                            <i class='bx bx-heart'></i>
                            dsfjhgsdhjf
                        </vs-button>
                    </v-row>
                </template>
            </vs-card>
            <router-view></router-view>
        </v-container>
    </v-main>
</template>

<script>
export default {
    name: 'Home',
    data: () => ({
        kek: null
    }),
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