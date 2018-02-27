# SICP 学习笔记

[Youtube地址](https://www.youtube.com/watch?v=iG6eVomFrhE&list=PLkEwH_Z2WOlppy8oUfrGwFVlOuKyo3RO_)

## 概念

### MOST-IMPORTANT  NAMING

* 编程 和 魔法一样， 如果你知道了 那个精灵的名字，你就能操控它
* 说明某件事的意义远比实现它难 （所以 关键的是 如何 抽象）
* 闭包 把一些东西组合在一起 而且 还可以用它们 继续组合成更复杂的组合 (闭包性质是组成大型系统的关键，而不仅仅是 pairs)
* procedure 和 data 的界限是模糊的， 定义一个 procedure 可以把它也看成 一个 object
* procedure is object， 也可以用来 Name (就是可以 用 function 来赋值)

### 语法糖

Sytactic Suger 方便输入的一种形式

```lisp
(define (square x) (* x x))

(define square (lambda (x) (* x x)))
```

两种表述是一样的，但是 上面的方法定义 是一种语法糖

### 递归定义

Recursive Defination

就是用自己 定义自己 （function）

### Block Structure

将 一些私有方法 定义在自己的块里 （good-enough） 每个Black-box 可能不一样的实现

### DATA Abstraction

数据抽象 -> Use(实际) 转化成 Representation (计算机/语言 内置方法)

通过假定的构造函数 和 选择函数 将数据对象 与它的表示 分割开来的 编程方法学

数据抽象是一种方法：

好处是 不必在构造的时候 去想怎么优化（因为 优化可以在完成抽象后 再任何一个抽象过程完成）

而 不抽象的话，一定要一开始就去思考好 哪里优化


### Closure

闭包 CONS 把一些东西组合在一起 而且 还可以用它们 继续组合成更复杂的组合

### 2维 -> N维

只要有 CONS (PAIR对) 就能推导表示 N 维 [1, ]-> [2, 3]

###　LIST

LIST 是 Lisp 表示序列数据的 一种约定(sequence of pairs)

[1,2,3,4]

```lisp
(cons 1 
    (cons 2
        (cons 3
            (cons 4 nil))))

// 简写 语法糖

(list 1 2 3 4)
```

## 经典

### SUM RECUSIVE

```lisp
(DEFINE (SUM TERM A NEXT B)
    (IF (> A B)
        0
        (+ (TERM A) 
           (SUM TERM 
                (NEXT A)
                NEXT
                B))))

// TERM 和 NEXT 都是函数 PROCEDURE
// TERM 是表示 是怎样的数 比如 a平方 立方 还是 a*(a+1)
// NEXT 表示STEP a+1 or a+6
```

### SUM ITERATIVE

```lisp
(DEFINE (SUM TERM a NEXT)
    (DEFINE (ITER j ANS)
        (IF (> j b)
            ANS
            (ITER (NEXT j)
                  (+ (TERM j) ANS))))
    (ITER a 0))
```


### CONS

定义 cons 为一个 procedure

```lisp
(define (cons a b)
    (lambda (pick)
        (cond ((= pick 1) a)
              ((= pick 2) b))))

(define (car x) (x 1))
(define (cdr x) (x 2))
```

## 高阶函数

### map

* p 是一个 function 或者之类的
* l 是一个 list

```lisp
(define (map p l)
    (if (null? l)
        nil
        (cons (p (car l) 
                 (map p (cdr l))))))
```

```
(define (scale-list s l)
    (map (lambda (item) (* item s))
         l))
```


### for-each

map 与 for-each的区别 : map 构建新的 list ，for-each 只是比如 打印 操作原来的 list，原来的list 不变

```lisp
(define (for-each proc list)
    (cond ((null? list) "done")
          (else (proc (car list))
                (for-each proc
                          (cdr list)))))
```