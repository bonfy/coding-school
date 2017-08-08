<template>
  <div>
    <h1> List of Article</h1>
    <ul>
      <li v-for="item in articles">{{ item }}</li>
    </ul>
  </div>

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

<style scoped>
/*
  只对本vue component作用
  看源码 是加了id  <h1 id-xxx>
  style 里是  h1[id-xxx]
*/
  h1 {
    color: purple;
  }
</style>
