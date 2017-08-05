var app = new Vue({
  el: '#vue-app',
  data: {
    name: 'bonfy',
    age: 29
  },
  methods: {
    add: function(num) {
      this.age += num;
    },
    sub: function(num) {
      this.age -= num;
    },

    click: ()=>{
      alert('prevent open link here');
    }
  }
})
