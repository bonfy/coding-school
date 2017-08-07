<template>
  <div id="app">
    <h1>{{ title }}</h1>

    <p>{{ greet() }}</p>
  </div>
</template>

<script>
export default {
  name: 'app',
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
