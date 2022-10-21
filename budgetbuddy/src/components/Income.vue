<template>
  <main class="container">
    <div>
      <h3>All My Sources of Income</h3>
      <button class="button is-small">Add Source</button>
      <!-- plus icon -->
      <div class="source-form">
        <form action="" @submit.prevent="AddNewSource">
          <div class="field">
            <label class="label">Source Name</label>
            <div class="control">
              <input
                class="input"
                type="text"
                v-model="source_name"
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
                placeholder="Amount"
              />
            </div>
          </div>
          <div class="field">
            <label class="label">Frequency</label>
            <div class="control">
              <div class="select">
                <select v-model="frequency">
                  <option>Monthly</option>
                  <option>Bi-Weekly</option>
                  <option>Weekly</option>
                  <option>Yearly</option>
                </select>
              </div>
            </div>
          </div>
          <div class="field">
            <label class="label">Start Date</label>
            <div class="control">
              <input
                class="input"
                type="Date"
                placeholder="Text input"
                v-model="start_date"
              />
            </div>
          </div>
          <div class="field">
            <label class="label">End Date</label>
            <div class="control">
              <input
                class="input"
                type="Date"
                placeholder="Text input"
                v-model="end_date"
              />
            </div>
          </div>
          <div class="field">
            <label class="label">Notes</label>
            <div class="control">
              <textarea
                class="textarea"
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
              <button class="button is-small is-danger is-light">Clear</button>
            </div>
          </div>
        </form>
      </div>
    </div>
    <div>
        <h3>My Sources of Income</h3>
        <div class="table-container">
            <table class="table is-fullwidth is-striped">
                <thead>
                    <tr>
                        <th>Source Name</th>
                        <th>Amount</th>
                        <th>Frequency</th>
                        <th>Start Date</th>
                        <th>End Date</th>
                        <th>Notes</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="source in sources" :key="source.id">
                        <td>{{source.source_name}}</td>
                        <td>{{source.amount}}</td>
                        <td>{{source.frequency}}</td>
                        <td>{{source.start_date}}</td>
                        <td>{{source.end_date}}</td>
                        <td>{{source.notes}}</td>
                        <td>
                            <button class="button is-small is-link">Edit</button>
                            <button class="button is-small is-danger">Delete</button>
                        </td>
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
    data() {
        return {
            source_name: "",
            amount: "",
            frequency: "",
            start_date: "",
            end_date: "",
            notes: "",
        
        }
    },
    methods: {
        AddNewSource() {
            axios.post("http://127.0.0.1:8000/api/income/income/", {
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
        getAllSources(){
            axios.get("http://127.0.0.1:8000/api/income/income")
            .then((response) => {
                console.log(response);
            })
            .catch((error) => {
                console.log(error);
            });
        }
        
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