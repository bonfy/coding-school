# Python Beyond Basics (Lesson 2)

> Beyond basic functions

## Class Callable

### def __call__(self)

```python
import socket

class Resolver:

    def __init__(self):
        self._cache = {}

    def __call__(self, host):
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
        return self._cache[host]
```

```python
>>> from resolver import Resolver
>>> resolver = Resolver()
>>> resolver('dapaimian.com')

# Resolver class
# resolver object and can be called
```

## lambda vs function

![lambda vs function](https://i.loli.net/2018/01/08/5a5310bc50fb7.png)


## built-in callable function

```python
>>> callable(list)
True
>>> callable(list.append)
True
>>> is_odd = lambda num : num % 2 == 1
>>> callable(is_odd)
True
>>> callable("this is not callable")
False
```

## args and kwargs

```python
>>> def trace(f, *args, **kwargs):
...     print('args = ', args)
...     print('kwargs = ', kwargs)
...     result = f(*args, **kwargs)
...     print('reuslt = ', result)
...     return result
...
>>> int('ff', base=16)
255
>>> trace(int, 'ff', base=16)
args =  ('ff',)
kwargs =  {'base': 16}
reuslt =  255
255
```

## python 矩阵转置

```python
>>> monday = [1, 2 ,3 ,4 ,5 ,6 ,7]
>>> tuesday = [2, 3 ,4 ,5 ,6 ,7 ,8]
>>> wednesday = [3, 4, 5, 6 ,7 , 8, 9]
>>> daily = [monday, tuesday, wednesday]
>>> daily
[[1, 2, 3, 4, 5, 6, 7], [2, 3, 4, 5, 6, 7, 8], [3, 4, 5, 6, 7, 8, 9]]
>>> for item in zip(*daily):
...     print(item)
...
(1, 2, 3)
(2, 3, 4)
(3, 4, 5)
(4, 5, 6)
(5, 6, 7)
(6, 7, 8)
(7, 8, 9)

>>> transposed = list(zip(*daily))
```