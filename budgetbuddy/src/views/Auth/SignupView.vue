<template>
  <section class="signup-page p-3">
    <div class="gx-lg-5 align-items-center justify-content-center mb-5">
      <div class="mb-5 mb-lg-0">
        <div
          class="has-text-centered"
          style="color: #a3cd38; font-size: larger; font-weight: bolder"
        >
          Buddy Budget
        </div>
        <div class="py-3 px-5">
          <form @submit.prevent="Signup" class="card">
            <div class="has-text-centered">
              <div class="p-3 mb-5 fa fa-user title" style="font-size: larger">
                SIGN UP
              </div>
            </div>

            <!-- Email input -->
            <div class="columns">
              <div class="field">
                <label class="label">Email address</label>
                <input
                  type="email"
                  class="control"
                  placeholder="email"
                  v-model="email"
                />
              </div>
            </div>

            <div class="columns">
              <div class="field m-1">
                <label class="label">First Name</label>
                <input
                  type="text"
                  class="control"
                  placeholder="First Name"
                  v-model="firstName"
                />
              </div>

              <div class="field m-1">
                <label class="label">Last Name</label>
                <input
                  type="text"
                  class="control"
                  placeholder="last Name"
                  v-model="lastName"
                />
              </div>
            </div>
            <div class="columns">
              <!-- Password input -->
              <div class="field m-1">
                <label class="label">Password</label>
                <input
                  type="password"
                  id=""
                  class="control"
                  placeholder="Password"
                  v-model="password1"
                />
              </div>
              <div class="field m-1">
                <label class="label">Confirm Password</label>
                <input
                  type="password"
                  class="control"
                  placeholder="Confirm Password"
                  v-model="password2"
                />
              </div>
            </div>

            <div class="notification is-danger" v-if="errors.length">
              <p v-for="error in errors" :key="error">{{ error }}</p>
            </div>

            <!-- Checkbox -->
            <div class="mb-4">
              <label class="">
                <input
                  class="form-check-input mt-2 p-2"
                  type="checkbox"
                  required
                  unchecked
                />
                By signing up you agree to our
                <a href="#" class="">Terms of Service</a> and
                <a href="#" class="">Privacy Policy</a>. You also agree to
                receive occasional emails in the form of our newsletter.(You can
                unsubscribe at any moment.)
              </label>
            </div>
            <div class="">
              <!-- Submit button -->
              <button
                class="button is-block is-small mt-2 mb-4"
                style="
                  background-color: rgb(30, 60, 114, 0.8);
                  color: white;
                  width: 100%;
                  font-weight: 500;
                  height: 40px;
                "
              >
                CREATE ACCOUNT
              </button>
            </div>
            <div class="field has-text-centered mt-3 p-0">
              <label class="">
                Already have an account?
                <a href="/login" class="text-secondary"> Login </a>
              </label>
            </div>
          </form>
        </div>
      </div>
    </div>
  </section>
</template>
  <script>
import axios from "axios";
import { toast } from "bulma-toast";

export default {
  data() {
    return {
      firstName: "",
      lastName: "",
      email: "",
      phoneNumber: "",
      password1: "",
      password2: "",
      errors: [],
    };
  },
  methods: {
    Signup() {
      this.errors = [];

      if (this.firstName === "") {
        this.errors.push("First Name is required");
      }
      if (this.lastName === "") {
        this.errors.push("Last Name is required");
      }
      if (this.email === "") {
        this.errors.push("Email is required");
      }
      if (this.password1 === "") {
        this.errors.push("Password is required");
      }

      if (this.password1 !== this.password2) {
        this.errors.push("Passwords do not match");
      }

      if (!this.errors.length) {
        axios
          .post("/api/user-auth/users/", {
            first_name: this.firstName,
            last_name: this.lastName,
            email: this.email,
            phone_number: this.phoneNumber,
            password: this.password1,
          })
          .then((response) => {
            toast({
              message: "Account created successfully",
              type: "is-success",
              dismissable: true,
              duration: 2000,
              position: "bottom-right",
              animate: { in: "fadeIn", out: "fadeOut" },
            });

            this.$router.push("/login");
          })

          .catch((error) => {
            if (error.response) {
              toast({
                message: "error.response.data.messag",
                type: "error",
                dismissable: true,
                duration: 2000,
                position: "bottom-right",
              });
              for (const property in error.response.data) {
                this.errors.push(
                  `${property}: ${error.response.data[property]}`
                );
              }
              console.log(JSON.stringify(error.response.data));
            } else if (error.message) {
              this.errors.push("Something went wrong");
              console.log(JSON.stringify(error));
            }
          });
      }
    },
  },
  mounted() {
      document.title = "BuddyBudget | Sign Up";
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

.card {
  margin: auto auto;
  width: 50%;
}

.signup-page {
  background-color: rgb(30, 60, 114);
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>