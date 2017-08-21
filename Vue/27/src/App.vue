<template>
    <div>
      <!-- keep alive 保持状态，不然切换的时候 输入的值就丢了 -->
      <keep-alive>
            <component v-bind:is="component"></component>
      </keep-alive>
      <button v-on:click="component = 'form-one'">Show form one</button>
      <button v-on:click="component = 'form-two'">Show form two</button>
    </div>
</template>

<script>

import formOne from './components/formOne.vue'
import formTwo from './components/formTwo.vue'

export default {
    components: {
        'form-one': formOne,
        'form-two': formTwo
    },
    data () {
      return {
          component: 'form-one'
      }
    },
    methods: {
        handleSubmit: function(){
            alert('thanks for submitting');
        }
    }
}
</script>

<style>
body{
    margin: 0;
    font-family: 'Nunito SemiBold';
}
</style>
