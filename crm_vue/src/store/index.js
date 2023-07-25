import { createStore } from 'vuex'

export default createStore({
  state: {
    isLoading: false, //here we put init values and these values are mutabel
    isAuthenticated: false,
    token: ''
  },
  getters: {
  },
  mutations: { // here i can change these values
    // here we can put functions that change the state
    initializeStore(state) {
      if (localStorage.getItem('token')) {
        state.token = localStorage.getItem('token')
        state.isAuthenticated = true
      } else {
        state.token = ''
        state.isAuthenticated = false
      }
    },
    setIsLoading(state, status) {
      state.isLoading = status
    },
    setToken(state, token) {
      state.token = token
      state.isAuthenticated = true
    },
    removeToken(state){
      state.token = ''
      state.isAuthenticated = false
    },
  },
  actions: {
  },
  modules: {
  }
})
