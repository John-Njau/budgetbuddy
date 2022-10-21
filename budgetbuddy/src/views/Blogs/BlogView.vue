<template>
  <main>
    <div class="blog">
        {{post}}
      <h1>{{ post.title }}</h1>
      <p>{{ post.content }}</p>
    </div>
    <div>
      <h3>Blog view</h3>
    </div>
  </main>
</template>

<script>
export default {
  data() {
    return {};
  },
  props: { post: Object },
};
</script>

<style>
</style>