<template>
  <main class="container">
    <div>
      <h3>All My Sources of Income</h3>
      <button class="button is-small" @click="addSource()">Add Source</button>
      <!-- plus icon -->
      <div class="income-form" v-if="isActive">
        <form action="" @submit.prevent="saveNewSource">
          <div class="field">
            <label class="label">Source Name</label>
            <div class="control">
              <input
                class="input"
                type="text"
                v-model="source_name"
                required
                placeholder="income source"
              />
            </div>
          </div>
          <div class="field">
            <label class="label">Amount</label>
            <div class="control">
              <input
                class="input"
                type="number"
                v-model="amount"
                required
                placeholder="Amount"
              />
            </div>
          </div>
          <div class="field">
            <label class="label">Start Date</label>
            <div class="control">
              <input class="input" type="Date" required v-model="start_date" />
            </div>
          </div>
          <div class="field">
            <label class="label">End Date</label>
            <div class="control">
              <input class="input" type="Date" required v-model="end_date" />
            </div>
          </div>
          <div class="field">
            <label class="label">Notes</label>
            <div class="control">
              <textarea
                class="textarea"
                required
                placeholder="Textarea"
                v-model="notes"
              ></textarea>
            </div>
          </div>
          <div class="field is-grouped">
            <div class="control">
              <button class="button is-small is-link">Save</button>
            </div>
            <div class="control">
              <button
                class="button is-small is-danger is-light"
                @click="clearInputs"
              >
                Clear
              </button>
            </div>
          </div>
        </form>
      </div>
    </div>
    <div>
      <h3>My Income</h3>
      <div class="table-container">
        <table class="table is-fullwidth is-striped">
          <thead>
            <tr>
              <th>Source Name</th>
              <th>Amount</th>
              <th>Start Date</th>
              <th>End Date</th>
              <th>Notes</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="source in sources" :key="source.id">
              <td>{{ source.source_name }}</td>
              <td>{{ source.amount }}</td>
              <td>{{ source.start_date }}</td>
              <td>{{ source.end_date }}</td>
              <td>{{ source.notes }}</td>
              <td>
                <button
                  class="button is-small is-link"
                  @click="editSource(source.id)"
                >
                  Edit
                </button>
                <button
                  class="button is-small is-danger"
                  @click="deleteSource(source.id)"
                >
                  Delete
                </button>
              </td>
            </tr>
            <!-- get Amount total -->
            <tr>
              <td>Total</td>
              <td>{{ total }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </main>
</template>

<script>
// use axios to make api calls
import axios from "axios";

export default {
  props: ["user", "source"],
  data() {
    return {
      source_name: "",
      amount: "",
      // frequency: "",
      start_date: "",
      end_date: "",
      notes: "",
      sources: [],
      total: 0,
      isActive: false,
    };
  },
  methods: {
    // toggle the form
    addSource() {
      this.isActive = !this.isActive;
      // toggle the form
      // this.$refs.incomeForm.classList.toggle("is-hidden");
    },

    saveNewSource() {
      axios
        .post("/api/income/", {
          source_name: this.source_name,
          amount: this.amount,
          frequency: this.frequency,
          start_date: this.start_date,
          end_date: this.end_date,
          notes: this.notes,
        })
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    getAllSources() {
      axios
        .get("/api/income/")
        .then((response) => {
          this.sources = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    // edit source
    editSource(id) {
      axios
        .patch(`/api/income/${id}/`)
        .then((response) => {
          this.sources = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    // delete source
    deleteSource(id) {
      axios
        .delete(`/api/income/${id}`)
        .then((response) => {
          this.sources = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    clearInputs() {
      this.source_name = "";
      this.amount = "";
      this.start_date = "";
      this.end_date = "";
      this.notes = "";
    },
  },

  mounted() {
    this.getAllSources();
    this.editSource();
    this.deleteSource();
  },

  computed: {
    calculateTotal() {
      let total = 0;
      this.sources.forEach((source) => {
        this.total += source.amount;

        console.log(source.amount);
      });
      // return this.total;
    },
  },
};
</script>

<style lang="scss">
form {
  //   display: flex;
  //   flex-direction: column;
  // flex-wrap: wrap;
  align-items: center;
  justify-content: center;
  margin: 16px auto;
  width: max-content;
  padding: 10px 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background: #f4f4f4;
}
</style>>
</style>