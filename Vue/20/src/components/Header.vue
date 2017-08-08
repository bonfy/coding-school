<template>
  <header>
    <h1>{{ title }}</h1>
  </header>
</template>

<script>
export default {

  data () {
    return {
      title: 'Vue Tutor'
    }
  },

  methods: {

  }
}
</script>

<style scoped>
header {
  background: lightblue;
  padding: 10px;
}

h1 {
  color: #222;
  text-align: center;
}
</style>
