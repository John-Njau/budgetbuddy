<template>
    <section>
      <div class="reset-page card  mb-3 mb-lg-0">
        <form @submit.prevent="SetNewPassword" class="p-4 mb-3">
          <div class="has-text-centered">
            <div class="fa fa-key"> Reset Password</div>
          </div>
          <div class="has-text-centered m-4">
            <p>
             Enter your new pasword. Password MUST not be same to earlier used passwords.
            </p>
          </div>
          <!-- Email input -->
          <div class="field mb-4">
            <label class="label text-white" for="form3Example3">
              Email
              <input
                type="email"
                class="form-control"
                v-model="email"
                placeholder="xyz@gmail.com"
              />
            </label>
          </div>
          <div class="">
              <!-- Password input -->
              <div class="field m-1">
                <label class="label">Password <input
                  type="password"
                  id=""
                  class="control"
                  placeholder="Password"
                  v-model="password1"
                /></label>
                
              </div>
              <div class="field m-1">
                <label class="label">Confirm Password <input
                  type="password"
                  class="control"
                  placeholder="Confirm Password"
                  v-model="password2"
                /></label>
                
              </div>
            </div>
          <!-- Submit button -->
          <div class="field mb-4 form-group has-text-centered">
            <button
              class="button is-sm outline-2 has-text-white"
              style="background-color: rgb(30, 60, 114; height: 40px; font-weight: 500;">
              SAVE PASSWORD
            </button>
          </div>
         
        </form>
      </div>
    </section>
  </template>
  <script>
  import axios from "axios";
  
  export default {
    data() {
      return {
        email: "",
        password: "",
        errors: [],
      };
    },
    mounted() {
      document.title = "BuddyBudget | Password Reset";
    },
  
    methods: {
      async SetNewPassword() {
        axios.defaults.headers.common["Authorization"] = "";
  
        localStorage.removeItem("token");
  
        const formData = {
          email: this.email,
          password: this.password,
        };
  
        await axios
          .post("/api/v1/token/login/", formData)
          .then((response) => {
            const token = response.data.auth_token;
  
            this.$store.commit("setToken", token);
  
            axios.defaults.headers.common["Authorization"] = "Token" + token;
  
            localStorage.setItem("token", token);
  
            const toPath = this.$route.query.to || "/";
  
            this.$router.push(toPath);
          })
  
          .catch((error) => {
            if (error.response) {
              for (const property in error.response.data) {
                this.errors.push(`${property}: ${error.response.data[property]}`);
              }
            } else {
              this.errors.push(error.message);
  
              console.log(JSON.stringify(error));
            }
          });
      },
    },
  };
  </script>
  
  
  <style scoped>
  input {
    border: 1px solid rgb(0, 0, 0, 0.4);
    border-radius: 5px;
    padding: 10px;
    margin-bottom: 10px;
  }
  .reset-page {
    background-color: rgb(30, 60, 114);
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  </style>