<template>
  <div id="app">
    <app-header v-bind:title="title"></app-header>
    <app-article v-bind:ninjas="ninjas"></app-article>
    <app-footer v-bind:title="title"></app-footer>
  </div>
</template>

<script>
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'
import Article from './components/Article.vue'


export default {
  name: 'app',

  // 局部绑定，只能在这里调用
  components: {
    // 避免使用 html的 header
    // 加了 '-' 必须 引号，不然出错
    'app-header': Header,
    'app-article': Article,
    'app-footer': Footer
    // appheader: Header
  },

  data () {
    return {
      ninjas: [
          {name: 'Ryu', speciality: 'Vue Components', show: false},
          {name: 'Crystal', speciality: 'HTML Wizardry', show: false},
          {name: 'Hitoshi', speciality: 'Click Events', show: false},
          {name: 'Tango', speciality: 'Conditionals', show: false},
          {name: 'Kami', speciality: 'Webpack', show: false},
          {name: 'Yoshi', speciality: 'Data Diggin', show: false}
      ],

      title: 'Vuejs Tutor'
    }
  },
  methods: {

  },
  // lifecycle hooks
  beforeCreate(){
      alert('beforeCreate');
  },
  created(){
      alert('created');
  },
  beforeMount(){
      alert('beforeMount');
  },
  mounted(){
      alert('mounted');
  },
  beforeUpdate(){
      alert('beforeUpdate');
  },
  updated(){
      alert('updated');
  }
}
</script>

<style>

</style>
