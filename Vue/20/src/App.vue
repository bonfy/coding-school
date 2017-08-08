<template>
  <div id="app">
    <app-header></app-header>
    <app-article></app-article>
    <app-footer></app-footer>
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
    }
  },
  methods: {

  }
}
</script>

<style>

</style>
