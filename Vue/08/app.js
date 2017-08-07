var app = new Vue({
  el: '#vue-app',
  data: {
    name: 'bonfy',
    age: 27,
    a: 0,
    b: 0
  },
  methods: {
    M_Add_A: function(){
      console.log('Method A exec');
      return this.age + this.a;
    },

    M_Add_B: function(){
      console.log('Method B exec');
      return this.age + this.b;
    }
  },
  computed: {
    P_Add_A: function(){
      console.log('Computed Prop A exec');
      return this.age + this.a;
    },

    P_Add_B: function(){
      console.log('Computed Prop B exec');
      return this.age + this.b;
    }
  }
})
