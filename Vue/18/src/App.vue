<template>
  <div id="app">
    <h1>{{ title }}</h1>

    <p>{{ greet() }}</p>

    <art></art>
  </div>
</template>

<script>
import Article from './Article.vue'
export default {
  name: 'app',

  // 局部绑定，只能在这里调用
  components: {
    art: Article
  },

  data () {
    return {
      title: 'Hello from Vue component'
    }
  },
  methods: {
    greet: function(){
      return 'Hello world from vue methods';
    }
  }
}
</script>
