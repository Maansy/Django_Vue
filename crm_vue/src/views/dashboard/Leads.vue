<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-4 is-12">
                <h1 class="title">Leads</h1>
                <router-link to="/dashboard/lead/add">
                    Add lead
                </router-link>
            </div>
            <div class="column is-4 is-12">
                <table class="table is-fullwidth">
                    <thead>
                        <th>Company</th>
                        <th>Contact person</th>
                        <th>Status</th>
                        <th></th>
                    </thead>
                    <tbody>
                        <tr v-for="lead in leads" :key="lead.id">
                            <td>{{ lead.company }}</td>
                            <td>{{ lead.contact }}</td>
                            <td>{{ lead.status }}</td>
                            <td>
                                <router-link :to="{name: 'Lead', params:{id:lead.id}}">Details</router-link>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: "Leads",
    data() {
        return {
            leads: []
        }
    },
    mounted() {
        this.getLeads()
    },
    methods: {
        async getLeads() {
            this.$store.commit('setIsLoading', true)
            axios
                .get('/api/v1/leads')
                .then(response => {
                    this.leads = response.data
                    console.log(this.leads)
                })
                .catch(error => {
                    console.log(error)
                })
            this.$store.commit('setIsLoading', false)

        }
    }
}
</script>