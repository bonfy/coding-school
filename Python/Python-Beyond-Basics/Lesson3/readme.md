# Python Beyond Basics (Lesson 3)

> Closures and Decorators

## Local Function

函数里面的函数

```python
def sort_by_last_letter(strings):
    def last_letter(s):
        return s[-1]
    print(last_letter) # 多次调用的话 地址是不一样的，运行时创建
    return sorted(strings, key=last_letter)
```

### LEGB Rule

local, enclosing, global, built-in


### Benefits

* Useful for specialized, one-off functions
* Aid code organization and readablity
* Similar to lambda, but more general
    * May contain mutliple expressions
    * May contain statements


## Returning functions

```python
>>> def outer():
...     def inner():
...         print('inner')
...     return inner
...
>>> i = outer()
>>> i()
inner
```

> Python 特性: first-class Functions
> Functions can be treated like any other object

## Closures

```python
>>> def outer():
...     x = 5
...     def inner(y):
...         return x + y
...     return inner
...
>>> i = outer()
>>> i(3)   # 注意要传参数
8
```
> Closures
> Maintain references to objects from earlier scope

```python
>>> def enclosing():
...     x = 'closed over'
...     def local_func():
...         print(x)
...     return local_func
...
>>> lf = enclosing()
>>> lf()
closed over
>>> lf.__closure__
(<cell at 0x104708168: str object at 0x104718e30>,) # 闭包保存了参数 x
```

### Function Factory

> Function that returns new, specialized functions

```python
>>> def raise_to(exp):
...     def raise_to_exp(x):
...         return pow(x, exp)
...     return raise_to_exp
...
>>> square = raise_to(2)
>>> square
<function raise_to.<locals>.raise_to_exp at 0x1047201e0>
>>> square.__closure__
(<cell at 0x104708348: int object at 0x1043b2a90>,)
>>> square(4)
16
>>> cube = raise_to(3)
>>> cube(4)
64
```

### LEGB does not apply when making new bindings

```python
>>> message = 'global'
>>> def enclosing():
...     message = 'enclosing'
...     def local():
            # global message  # change global
            # nonlocal message # change enclosing
...         message = 'local'
...     print(message)
...     local()
...     print(message)
...
>>> print('global massage:', message)
global massage: global
>>> enclosing()
enclosing
enclosing
>>> print('global massage:', message)
global massage: global

```

### global key-word

> introduce names from global namespace into the local namespace

### nonlocal key-world

> introduce names from the enclosing namespace into the local namespace

you get a `SyntaxError` if the name does not exist

## Decorators

> Modify or enhance functions without changing their defination

> Implemented as callables that take and return other callables

* Replace, enhance, or modify existing functions
* Does not change the original function defination
* Calling code does not need to change
* Decorator mechanism uses the modified function's original name

What can be decorators

* function
* class
```python
class CallCount:

    def __init__(self, f):
        self._f = f
        self._count = 0

    def __call__(self, *args, **kwargs):
        self._count += 1
        return self._f(*args, **kwargs)

@CallCount
def hello(name):
    print('Hello, {}'.format(name))

>>> from callcount import hello
>>> hello('bonfy')
Hello, bonfy
>>> hello('rene')
Hello, rene
>>> hello._count
2
```
* Instance(class instance)

```python
class Trace:

    def __init__(self):
        self.enabled = True
    
    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print('Calling {}'.format(f))
            return f(*args, **kwargs)
        return wrap

tracer = Trace()

@tracer
def hello(name):
    print('Hello {}'.format(name))

>>> from tracer import tracer, hello
>>> hello('bonfy')
Calling <function hello at 0x104720598>
Hello bonfy
>>> hello('rene')
Calling <function hello at 0x104720598>
Hello rene
>>> tracer.enabled=False
>>> hello('jack')
Hello jack
```


### 使用 functools.wraps

> functools.wraps properly update metadata on wrapped functions

非常重要，不然会丢失 __doc__, __name__ 等属性 metadata

![丢失 __name__](https://i.loli.net/2018/01/08/5a53334c4008a.png)

```python
import functools

def check_non_negative(index):
    """ check index non negative """
    def validator(f):
        @functools.wraps(f)
        def wrap(*args):
            if args[index] < 0:
                raise ValueError('Argument {} must be non-negative'.format(index))
            return f(*args)
        return wrap

    return validator

@check_non_negative(1)
def create_list(value, size):
    """ create list """
    return [value] * size


>>> from createlist import create_list
>>> help(create_list)

>>> create_list('a',3)
['a', 'a', 'a']
>>> create_list('a',-1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/kai.chen/bonfy/Github/coding-school/Python/Python-Beyond-Basics/Lesson3/createlist.py", line 11, in wrap
    raise ValueError('Argument {} must be non-negative'.format(index))
ValueError: Argument 1 must be non-negative
```

![logger](https://i.loli.net/2018/01/08/5a5337f6943fa.png)
