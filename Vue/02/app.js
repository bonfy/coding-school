new Vue({
  // div id
  // 记得加 #
  el: '#app-vue',

  // 控制所有的Data
  data: {
    name: 'shawn',
    job: 'Ninja'
  },

  methods: {
    greet: () => {
      return 'Hello World';
    },
    // 参数
    greetTime: (time) => {
      return 'Hello world at ' + time;
    },

    // 调用 this ，不能用 =>
    greetData: function() {
      return 'Hello world at ' + this.job + ' ' +this.name;
    },

    // Arrow 方式怎么调用 data 呢？
    greetArrow: ()=> {
      return 'Hello world at ' // + data.job;
    }
  }
});
