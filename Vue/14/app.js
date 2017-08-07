// 注册

// 这样是 每次点击 只修改自己的
Vue.component('my-component', {
  template: '<div>A custom component! name is {{ name }} <button @click="changeName()">Change Component Name</button> </div>',
  data: function(){
    return {
      name: 'shawn-component'
    }
  },
  methods: {
     changeName: function(){
       this.name = 'marry-component'
     }
  }
})

// 这个是修改全局的，所以两边都变
obj = {
  name: 'your-component-shawn'
}

Vue.component('your-component', {
  template: '<div>A custom component! name is {{ name }} <button @click="changeName()">Change Component Name</button> </div>',
  data: function(){
    return obj;
  },
  methods: {
     changeName: function(){
       this.name = 'your-component-marry'
     }
  }
})



// 创建根实例
var one = new Vue({
  el: '#app-one',

  data: {
    name: 'shawn in one'
  }
})


// 创建根实例
var two = new Vue({
  el: '#app-two',

  data: {
    name: 'shawn in two'
  }
})
