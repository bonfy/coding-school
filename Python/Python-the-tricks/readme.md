# Python The Tricks

## Patterns and Cleaner Python

* assert 是可以在生产环境 或者 运行时 禁用的

The biggest caveat with using asserts in Python is that assertions can
be globally disabled3 with the -O and -OO command line switches, as
well as the PYTHONOPTIMIZE environment variable in CPython.

* comma

list,dict 之类 最后可以加个逗号 [1,2,3,] == [1,2,3] 在 git diff 里面效果比较好

* with

```python
some_lock = threading.Lock()
# Harmful:
some_lock.acquire()
try:
    # Do something...
finally:
    some_lock.release()

# Better:
with some_lock:
    # Do something...
```


* `_` vs `__`

一个下划线 说明是 私有变量 但是还是可以访问的 a._val; 两个下划线访问不到 是 a.__val 是访问不到的，因为已经变成了 a._A__val 了，ugly 的设计，但是解决了问题

* String

Template String

```python
>>> from string import Template
>>> t = Template('Hey, $name!')
>>> t.substitute(name=name)
'Hey, Bob!'

>>> templ_string = 'Hey $name, there is a $error error!'
>>> Template(templ_string).substitute(
... name=name, error=hex(errno))

'Hey Bob, there is a 0xbadc0ffee error!'
```

Attack

```python
>>> SECRET = 'this-is-a-secret'
>>> class Error:
... def __init__(self):
... pass
>>> err = Error()
>>> user_input = '{error.__init__.__globals__[SECRET]}'
# Uh-oh...
>>> user_input.format(error=err)
'this-is-a-secret'


# How to solve
>>> user_input = '${error.__init__.__globals__[SECRET]}'
>>> Template(user_input).substitute(error=err)
ValueError:
"Invalid placeholder in string: line 1, col 1"
```

If your format strings are user-supplied, use Template
Strings to avoid security issues. Otherwise, use Literal
String Interpolation if you’re on Python 3.6+, and “New
Style” String Formatting if you’re not

## Python Functions

### Function First Class

```python
def yell(text):
    return text.upper() + '!'
>>> yell('hello')
'HELLO!'

>>> bark = yell
>>> bark('woof')
'WOOF!'

>>> del yell

>>> yell('hello?')
NameError: "name 'yell' is not defined"
>>> bark('hey')
'HEY!'

>>> bark.__name__
'yell'


# 高阶函数
>>> list(map(bark, ['hello', 'hey', 'hi']))
['HELLO!', 'HEY!', 'HI!']
```

就是 func 是堆上 分配空间，然后 bark 指针指向这个地方， 删除 yell 并没有gc 因为还有引用


Object is not function，but they can be made callable

```python

class Adder:
    def __init__(self, n):
        self.n = n
    def __call__(self, x):
        return self.n + x

>>> plus_3 = Adder(3)
>>> plus_3(4)
7
```

### Lambda



## Python Class

## Data Structure

## Loop and Iter

## Dictionary Tricks

## Pythonic
