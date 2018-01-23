# Selection

## 查找

### document.getElementByClassName

注意 返回的是 LiveResult, 就是 你先 

```js
var items = document.getElementByClassName('selector')

console.log(items.length);
// 然后 后面比如 ul.append(element_with_selector_class)

// 这个长度就变掉了
console.log(items.length);

```

### document.querySelector

返回 第一个找到的元素

### document.querySelectorAll

* 返回 NodeList
* 返回的是 static result（就是 append后 除非重新查找，不然不变）

遍历 
```js
var items = document.querySelectorAll('#selector')

for(var i=0; i<items.length; i++){
    console.log(item[i].innerText);
}

var forEach = Array.prototype.forEach;
forEach.call(items, function(item){
    console.log(item.innerText);
});
```
