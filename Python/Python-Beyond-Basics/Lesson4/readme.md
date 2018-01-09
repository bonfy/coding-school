# Python Beyond Basics (Lesson 4)

> Property and Class Methods

## Class Attributes

```python
class ShippingContainer:

    next_serial = 1

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        # 这里要设置 class 属性，不然不能全局控制
        self.serial = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1

>>> from shipping import *
>>> c1 = ShippingContainer('aws', 'clothes')
>>> c1.serial
1
>>> c2 = ShippingContainer('qcloud', 'hats')
>>> c2.serial
2
```

## Static Method

```python
class ShippingContainer:

    next_serial = 1

    @staticmethod
    def _get_serial():
        serial = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return serial

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer._get_serial()

```

## Class Method

如果需要 访问 Class 里面的 Class Attr 倾向于用 classmethod,虽然其实和 Static Method 差不多

```python
class ShippingContainer:

    next_serial = 1

    @classmethod
    def _get_serial(cls):
        serial = cls.next_serial
        cls.next_serial += 1
        return serial

    # Class Method 的一种常用方法
    # Create Named structure
    @classmethod
    def create_empty(cls, owner_code):
        return cls(owner_code, contents=None)

    @classmethod
    def create_with_items(cls, owner_code, *items):
        return cls(owner_code, contents=list(items))

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer._get_serial()

```

## Class Method vs Static Method

![classmethod vs staticmethod](https://i.loli.net/2018/01/09/5a542a94300b4.png)


## Static Method vs Inheritence

StaticMethod 在 子类可以被重写

但是 一定在 `__init__()` 或者 其他父类调用的时候用的是 self.method 而不是 class.method

## Class Method vs Inheritence


## @property

## @property 的继承

这个是难点，虽然也能够做到继承，但是尤其是 property setter 容易出些问题

> All Probelems in Computer Science Can Be Solved By Another Level of Indirection

### Template method

就是比如定一个  `_set_value()` 的 Method， 然后再 property 的 setter 的设置 _set_value(), 然后 子类重写 `_set_value()` method 就可以了


## 总结

![总结](https://i.loli.net/2018/01/09/5a544c47e34ee.png)
