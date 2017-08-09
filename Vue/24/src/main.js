import Vue from 'vue'
import App from './App.vue'

// 全局申明
// import Article from './Article.vue'

// Vue.component('art', Article);

// 全局申明 Event Bus
export const bus = new Vue()

new Vue({
  el: '#app',
  render: h => h(App)
})
