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
    isloading : false,
    isloggedin : false,
  },
  getters: {
  },
  mutations: {
  },
  actions: {
    
  },
  modules: {
  }
})
