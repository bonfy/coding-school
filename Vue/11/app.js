new Vue({
  // div id
  // 记得加 #
  el: '#app-vue',

  // 控制所有的Data
  data: {
    name: 'shawn',
    stringlist: ['AAA', 'BBB', 'CCC', 'DDD'],
    objectlist: [
      {name: 'first-person', age: 34},
      {name: 'second-person', age: 32},
      {name: 'third-person', age: 35}
    ]
  }
});
