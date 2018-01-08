# Python Beyond Basics (Lesson 1)

## package vs module

```python
>>> import urllib
>>> import urllib.request
>>> type(urllib)
<class 'module'>
>>> type(urllib.request)
<class 'module'>
>>> urllib.__path__
['/usr/local/Cellar/python3/3.6.4/Frameworks/Python.framework/Versions/3.6/lib/python3.6/urllib']

>>> urllib.request.__path__
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'urllib.request' has no attribute '__path__'
```

### Package is a module which can contain other modules

* Packages are generally directories (containing a special `__init__.py` file)
* the `__init__.py` file execute when package is imported
* packages can contain sub packages which themselves implement `__init__.py` file in directories
* Modules are generally files

### `sys.path` list directories Python search for modules

```python
>>> import sys
>>> sys.path
['', '/usr/local/Cellar/python3/3.6.4/Frameworks/Python.framework/Versions/3.6/lib/python36.zip', '/usr/local/Cellar/python3/3.6.4/Frameworks/Python.framework/Versions/3.6/lib/python3.6', '/usr/local/Cellar/python3/3.6.4/Frameworks/Python.framework/Versions/3.6/lib/python3.6/lib-dynload', '/usr/local/lib/python3.6/site-packages']
```

两种方法加入sys.path

方法一
```python
>>> import sys
>>> sys.path.append(dir_you_want_add)
```

方法二
```cmd
$ export PYTHONPATH=dir_you_want_add
```

#### Absolute import

imports use a full path to the module

```python
>>> from reader.reader import Reader
```

#### relative import

imports which use a relative path to modules **in the same package**

```python
>>> from .reader import Reader
```

#### __all__

list of attributes names imported via **`from module import *`**

#### namespace packages

> 主要用于大型项目 分割成小的

Defined in PEP420： packages split across several directories

* Name packages have no `__init__.py`
this avoid complex initialization ordering problems

1. Python scans all entries in sys.path
2. if a matching directory with `__init__.py` is found, a normal package is loaded
3. if foo.py is found, then it is loaded
4. Otherwise, all matching directory in sys.path are considered part of the namespace pachage

### Executuble directories

directories contain an entry point for Python execution

就是 加入 `__main__.py`

另外， zip, bz2 等都是可以执行的，只要打包的第一层目录里面有 `__main__.py`

```cmd
$ cd reader
$ zip -r ../reader.zip *
$ python3 reader.zip
```

### Python包结构建议

![Python代码结构建议](https://i.loli.net/2018/01/08/5a5304db6a018.png)

### 大型项目建议

![大型项目](https://i.loli.net/2018/01/08/5a53071b0544c.png)
