<template>
  <main>
    <h1>Blog</h1>
    <p>Here are some of my thoughts:</p>
    <ul>
      <li v-for="post in posts" :key="post.id" post="post">
        <router-link :to="'/blogs/' + post.id">{{ post.title }}</router-link>
      </li>
    </ul>
  </main>
</template>

<script>
export default {
  props: {post: Object},
  data() {
    return {
      posts: [
        {
          id: 1,
          title: "My first blog post",
          content:
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec auctor, nisl eget ultricies ultricies, nisl nunc aliquet nisl, eget aliquet nunc nisl eget nunc. Donec auctor, nisl eget ultricies ultricies, nisl nunc aliquet nisl, eget aliquet nunc nisl eget nunc.",
        },
        {
          id: 2,
          title: "My second blog post",
          content:
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec auctor, nisl eget ultricies ultricies, nisl nunc aliquet nisl, eget aliquet nunc nisl eget nunc. Donec auctor, nisl eget ultricies ultricies, nisl nunc aliquet nisl, eget aliquet nunc nisl eget nunc.",
        },
        {
          id: 3,
          title: "My third blog post",
          content:
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec auctor, nisl eget ultricies ultricies, nisl nunc aliquet nisl, eget aliquet nunc nisl eget nunc. Donec auctor, nisl eget ultricies ultricies, nisl nunc aliquet nisl, eget aliquet nunc nisl eget nunc.",
        },
      ],
    };
  },
};
</script>

<style>
</style>