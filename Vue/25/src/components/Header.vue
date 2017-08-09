<template>
  <header>
    <h1 @click="changeTitle()">{{ title }}</h1>
  </header>
</template>

<script>
import { bus } from '../main';

export default {
  props: {
      title: {
        type: String
      }
  },

  data () {
    return {

    }
  },

  methods: {
    changeTitle: function(){
      //this.$emit('changeTitle', 'Vue Totur Event');
      bus.$emit('titleChanged', 'Vue Bus Event');
      this.title = 'Vue Bus Event';
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
