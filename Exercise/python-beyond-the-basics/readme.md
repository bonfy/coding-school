# Python Beyond the Basics

## 项目地址

[https://www.safaribooksonline.com/library/view/python-beyond-the/9781771373609/](https://www.safaribooksonline.com/library/view/python-beyond-the/9781771373609/)

## Excersize

1. MaxSizeList

```python
from assignments import MaxSizeList

a = MaxSizeList(1)
b = MaxSizeList(3)

a.push('hey')
a.push('hi')
a.push('let')
a.push('go')

b.push('hey')
b.push('hi')
b.push('let')
b.push('go')

print(a.get_list()) # ['go']
print(b.get_list()) # ['hi', 'let', 'go']
```

2.