import Vue from "vue";
import VueRouter from "vue-router";
import HomeView from "../views/HomeView.vue";
import BlogsView from "../views/Blogs/BlogsView.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/about",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
  },
  {
    path: "/blogs",
    name: "blogs",
    component: BlogsView,
  },
  {
    path: "/blogs/:post.id",
    name: "blog",
    // access the post.id parameter from the route
    props: true,
    component: () =>
      import(/* webpackChunkName: "blog" */ "../views/Blogs/BlogView.vue"),
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
