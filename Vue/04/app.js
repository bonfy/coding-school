new Vue({
  // div id
  // 记得加 #
  el: '#app-vue',

  // 控制所有的Data
  data: {
    name: 'shawn',
    age: 27,
    x: 0,
    y: 0
  },

  // methods
  methods: {
    add: function(num){
      if (this.age + num > 100) {
        alert("can not older than 100");
      }else{
        this.age += num;
      }
    },
    sub: function(num){
      if (this.age - num < 1) {
        alert("can not smaller than 1");
      }else{
        this.age -= num;
      }
    },
    moveXY: function(event){
        this.x = event.offsetX;
        this.y = event.offsetY;
    }
  }
});
