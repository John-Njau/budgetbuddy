<template>
  <main class="homeview">
  <HomeComp/>
  <IncomeComp/>
  </main>
</template>

<script>
// @ is an alias to /src
import HomeComp from '@/components/Home.vue'
import IncomeComp from '@/components/Income.vue'

export default {
  name: 'HomeView',
  components: {
    HomeComp,
    IncomeComp
  }
}
</script>
