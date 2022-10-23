<template>
  <!-- Section: Design Block -->
  <section class="login-page">
    <div class="gx-lg-5 align-items-center justify-content-center mb-5">
      <div class="mb-5 mb-lg-0">
        <div
          class="has-text-centered"
          style="color: #a3cd38; font-size: larger; font-weight: bolder"
        >
          Buddy Budget
        </div>
        <div class="py-3 px-5">
          <form @submit.prevent="SubmitForm">
            <div class="has-text-centered">
              <div class="fa fa-user"> Login</div>
            </div>
            <!-- Email input -->
            <div class="field">
              <label class="label"> Email</label>
              <input
                type="email"
                id="form3Example3"
                class="control"
                v-model="email"
                placeholder="email"
              />
            </div>

            <!-- Password input -->
            <div class="field">
              <label class="label">Password</label>

              <input
                type="password"
                class="control"
                v-model="password"
                placeholder="password"
              />
            </div>
            <div class="notification is-danger" v-if="errors.length">
              <p>{{ errors }}</p>
            </div>
            <!-- Submit button -->
            <div class="form form-group" id="login">
              <button
                class="btn btn-block btn-sm mt-3"
                style="
                  background-color: rgb(30, 60, 114);
                  color: #ffffff;
                  width: 100%;
                  height: 40px;
                "
              >
                LOG IN
              </button>
            </div>
            <div class="field mt-3 p-0">
              <label class="label">
                <a href="/reset-password" class="text-secondary">
                  Forgot your password?
                </a>
              </label>
            </div>
            <div class="field">
              <p class="">
                Don't have an account?
                <a href="/signup">Sign up</a>
              </p>
            </div>
          </form>
        </div>
      </div>
    </div>
  </section>
  <!-- Section: Design Block -->
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
    document.title = "Login";
  },

  methods: {
    async SubmitForm() {
      axios.defaults.headers.common["Authorization"] = "";

      localStorage.removeItem("token");

      const formData = {
        email: this.email,
        password: this.password,
      };

      await axios
        .post("http://127.0.0.1:8000/api/users/", formData)
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
  
  
  <style scoped lang='scss'>
input {
  border: 1px solid rgb(0, 0, 0, 0.4);
  border-radius: 5px;
  padding: 10px;
  margin-bottom: 10px;
}

.login-page {
  background-color: rgb(30, 60, 114);
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

@media only screen and (max-width: 991px) {
  #login-card {
    margin-top: 0;
  }
}
</style>