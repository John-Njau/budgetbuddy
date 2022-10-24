import axios from "axios";
import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    blog: {},
    blogs: [],
    token: " ",
    user: {},
    errors: [],
    isLoading: false,
    isAuthenticated: false,
    jwt: localStorage.getItem("token"),
    endpoints: {
      obtainSimpleJWToken: "http://127.0.0.1:8000/api/token/",
      refreshSimpleJWToken: "http://127.0.0.1:8000/api/token/refresh/",
    },
  },
  getters: {},
  mutations: {
    // initializeStore(state) {
    //   if (localStorage.getItem("token")) {
    //     state.token = localStorage.getItem("token");
    //     state.isAuthenticated = true;
    //   } else {
    //     state.token = " ";
    //     state.isAuthenticated = false;
    //   }
    // },
    // setting a loading bar
    setIsLoading(state, status) {
      state.isLoading = status;
    },
    setToken(state, newToken) {
      localStorage.setItem("token", newToken);
      state.jwt = newToken;
    },
    removeToken(state) {
      localStorage.removeItem("token");
      state.jwt = null;
    },
  },
  actions: {
    obtainToken(email, password) {
      const payload = {
        email: email,
        password: password,
      };

      axios
        .post(this.state.endpoints.obtainSimpleJWToken, payload)
        .then((response) => {
          this.commit("setToken", response.data.access);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    refreshToken() {
      const payload = {
        refresh: this.state.jwt,
      };

      axios
        .post(this.state.endpoints.refreshSimpleJWToken, payload)
        .then((response) => {
          this.commit("setToken", response.data.access);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    inspectToken() {
      const token = this.state.jwt; // get the token from the state
      if (token) {
        const decoded = jwt_decode(token); // decode the token
        const exp = decoded.exp; // get the expiration time
        const orig_iat = decoded.orig_iat; // get the issued at time
        if (
          exp - Date.now() / 1000 < 1800 &&
          Date.now() / 1000 - orig_iat < 628200
        ) {
          this.dispatch("refreshToken");
        } else if (
          exp - Date.now() / 1000 < 1800 &&
          Date.now() / 1000 - orig_iat > 628200
        ) {
          this.dispatch("logout");
        } else {
          console.log("Token is valid");
        }
      }
    },
  },
  modules: {},
});
