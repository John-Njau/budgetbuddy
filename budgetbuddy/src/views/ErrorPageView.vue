<template>
  <section class="error-page">
    <h2>404</h2>
    <p>Page not found</p>
    <button>
      <router-link to="/" class="button">Home</router-link>
    </button>
  </section>
</template>

<script>
export default {};
</script>

<style>
.error-page {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
  width: 100vw;
  background-color: #2b387d;
}
</style>