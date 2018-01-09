# Python Beyond Basics (Lesson 5)

> Strings and Representations

## str() vs repr()

String Representations

__str__()  vs  __repr__()

```python
class Point2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def __repr__(self):
        return 'Point(x={}, y={})'.format(self.x, self.y)

>>> from point import Point2D
>>> p = Point2D(x=1, y=5)
>>> str(p)
'(1, 5)'
>>> repr(p)
'Point(x=1, y=5)'
```

### repr()

> repr() is for developers

* Exactness is more important than human-freindliness
* Suited for debugging
* Include identifing information
* Generally best for logging

should contain `more information than str()`

* pdb print command use repr()
* Always write a repr
* The default repr is not very helpful

### str()

> str() is for clients

produce a readable, human-friendly representation of an object

* By default str() simply calls repr()
* By default __format__() calls __str__()

## 总结

![总结](https://i.loli.net/2018/01/09/5a545aa134279.png)




