new Vue({
  // div id
  // 记得加 #
  el: '#app-vue',

  // 控制所有的Data
  data: {
    name: 'shawn',
    food: 'apple'
  },

  methods: {
    readRef: function(){
      console.log(this.$refs);
      console.log(this.$refs.nameinput.value);

      this.food = this.$refs.nameinput.value;
    }
  }
});
