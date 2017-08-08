# Vue 学习

打算学习 `Vue` 好久了，以前也断断续续学过几次，但是一直没怎么用到项目中,后来也学习了一阵子 `React`，但是现在的公司前端都用 `Vue`，所以打算再从头好好学一次


## 主页

`Vue` 的官方主页是 [https://vuejs.org/](https://vuejs.org/)

## 教程

这里主要使用的是 [The Net Ninja 的 VueJs教程](https://www.youtube.com/watch?v=5LYrN_cAJoA&index=1&list=PL4cUxeGkcC9gQcYgjhBoeQH7wiAyZNrYa)

### 列表：

> Simple Vue

* 01 - [Vue Instance](https://github.com/bonfy/coding-school/tree/master/Vue/01)
* 02 - [Data & Methods](https://github.com/bonfy/coding-school/tree/master/Vue/02)
* 03 - [Data Binding](https://github.com/bonfy/coding-school/tree/master/Vue/03)
* 04 - [Events](https://github.com/bonfy/coding-school/tree/master/Vue/04)
* 05 - [Event Modifier](https://github.com/bonfy/coding-school/tree/master/Vue/05)
* 06 - [Keyboard Event](https://github.com/bonfy/coding-school/tree/master/Vue/06)
* 07 - [2-Way Data Binding](https://github.com/bonfy/coding-school/tree/master/Vue/07)
* 08 - [Computed Properties](https://github.com/bonfy/coding-school/tree/master/Vue/08)
* 09 - [Dynamic CSS Classes](https://github.com/bonfy/coding-school/tree/master/Vue/09)
* 10 - [Conditionals](https://github.com/bonfy/coding-school/tree/master/Vue/10)
* 11 - [Looping v-for](https://github.com/bonfy/coding-school/tree/master/Vue/11)
* 12 - [A Simple Game](https://github.com/bonfy/coding-school/tree/master/Vue/12)
* 13 - [Multiple VUe Instance](https://github.com/bonfy/coding-school/tree/master/Vue/13)
* 14 - [Components](https://github.com/bonfy/coding-school/tree/master/Vue/14)
* 15 - [Refs](https://github.com/bonfy/coding-school/tree/master/Vue/15)

> Vue cli

* 16 - [vue-cli](https://github.com/bonfy/coding-school/tree/master/Vue/16)
* 17 - [vue File and Root Component](https://github.com/bonfy/coding-school/tree/master/Vue/17)
* 18 - [Nesting Components](https://github.com/bonfy/coding-school/tree/master/Vue/18)
* 19 - [CSS Scoped](https://github.com/bonfy/coding-school/tree/master/Vue/19)
* 20 - [Nesting Components Example](https://github.com/bonfy/coding-school/tree/master/Vue/20)

## Tips

### 计算属性 Computed Properties

如果用 methods 的话，整个页面重绘，而 computed 只有涉及到属性变换的 计算值才会 重新计算

另外 计算属性 已经和属性一样，所以不需要 `()`

### @click

理论上来说 @click="method()" 里面是一个函数，但是 其实 @click="method" 也是可以的，所以javascript还是比较随意的，个人感觉
