<template>
    <nav class="navbar is-dark">

        <div class="navbar-brand">
            <router-link to="/" class="navbar-item">
                <strong>CRM</strong>
            </router-link>
        </div>

        <div class="navbar-menu">
            <div class="navbar-end">
                <router-link to="/dashboard/leads" class="navbar-item">Leads</router-link>

                <div class="navbar-item">

                    <div class="buttons">
                        <template v-if="!$store.state.isAuthenticated">
                            <router-link to="/sign-up" class="button is-success">
                                <strong>Sign up</strong>
                            </router-link>

                            <router-link to="/log-in" class="button is-success">
                                <strong>Login</strong>
                            </router-link>
                        </template>

                        <template v-else>
                            <router-link to="/dashboard/myaccount" class="button is-info">My acoount</router-link>
                        </template>

                    </div>
                </div>
            </div>
        </div>

    </nav>
</template>

<script>
export default {
    name: 'Navbar'
}
</script>