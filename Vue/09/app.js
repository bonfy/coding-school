new Vue({
  // div id
  // 记得加 #
  el: '#app-vue',

  // 控制所有的Data
  data: {
    name: 'shawn',
    available: false,
    nearby: false
  },

  computed: {
    computedClass: function(){
      return {
        available: this.available,
        nearby: this.nearby
      }
    }
  }
});
