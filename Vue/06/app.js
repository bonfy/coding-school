var app = new Vue({
  el: '#vue-app',
  data: {
    name: 'bonfy',
    age: 29
  },
  methods: {
    logName: function(event){
      console.log('log name');
    },
    logAge: function(event){
      console.log('log age');
    },
    logPlace: (event)=>{
      console.log('log place');
    }
  }
})
