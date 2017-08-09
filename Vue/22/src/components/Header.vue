<template>
  <header>
    <h1 @click="changeTitle()">{{ title }}</h1>
  </header>
</template>

<script>
export default {
  props: {
      title: {
        required: true,
        type: String
      }
  },

  data () {
    return {

    }
  },

  methods: {
    changeTitle: function(){
      this.title = 'title changed';
    }
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
