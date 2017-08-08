<template>
  <ul>
    <li v-for="item in articles">{{ item }}</li>
  </ul>
</template>

<script>
export default {
  data () {
    return {
      articles: ['art1', 'art2', 'art3']
    }
  }
}
</script>
