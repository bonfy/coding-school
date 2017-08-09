<template>
   <footer>
     <p>{{ copyright }}</p>
   </footer>
</template>

<script>
export default {

  data () {
    return {
      copyright: 'Copyright 2017 @BONFY'
    }
  },

  methods: {

  }
}
</script>

<style scoped>
footer {
  background: #222;
  padding: 6px;
}

p {
  color: lightblue;
  text-align: center;
}
</style>
