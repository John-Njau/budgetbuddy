import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    blog : {},
    blogs : [],
    token : " ",
    user : {},
    errors : [],
    isLoading : false,
    isAuthenticated : false,
  },
  getters: {
  },
  mutations: {
    initializeStore(state){
      if(localStorage.getItem('token')){
        state.token = localStorage.getItem('token')
        state.isAuthenticated = true
      }else{
        state.token = " "
        state.isAuthenticated = false
      }
    },
     // setting a loading bar
     setIsLoading(state, status) {
      state.isLoading = status;
    },
    setToken(state, token) {
      state.token = token;
      state.isAuthenticated = true;
    },
    removeToken(state) {
      state.token = '';
      state.isAuthenticated = false;
    },
   
  },
  actions: {
    
  },
  modules: {
  }
})
