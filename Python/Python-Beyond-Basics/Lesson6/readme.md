# Python Beyond Basics (Lesson 6)

> Numeric and Scalar Types

## Numeric Type

```python
>>> import sys
>>> sys.float_info
sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)
>>> sys.int_info
sys.int_info(bits_per_digit=30, sizeof_digit=4)
```

```python
>>> 0.8-0.7
0.10000000000000009
```

## decimal

module: `decimal` contains class: `Decimal`

```python
>>> import decimal
>>> decimal.getcontext()
Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, capitals=1, clamp=0, flags=[], traps=[InvalidOperation, DivisionByZero, Overflow])

>>> from decimal import Decimal
>>> Decimal('0.8') - Decimal('0.7')
Decimal('0.1')
>>> Decimal(0.8) - Decimal(0.7)
Decimal('0.1000000000000000888178419700')

# decimal 里面传值一般用 '', 然后下面这个可以避免输入 float 数字
>>> decimal.getcontext().traps[decimal.FloatOperation] = True
>>> Decimal(0.8) - Decimal(0.7)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
decimal.FloatOperation: [<class 'decimal.FloatOperation'>]
>>> Decimal('0.8') > 0.7
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
decimal.FloatOperation: [<class 'decimal.FloatOperation'>]

>>> a = Decimal(3)
>>> b = Decimal('3.0')
>>> a==b
True
>>> a
Decimal('3')
>>> b
Decimal('3.0')
```

![decimal减法](https://i.loli.net/2018/01/09/5a546d697d155.png)


```python
>>> -7 % 3
2
>>> Decimal(-7) % Decimal(3)
Decimal('-1')

>>> -7 // 3
-3
>>> Decimal(-7) // Decimal(3)
Decimal('-2')
```

### int(x, base)

base 2 to 36
* bin: base=2
* oct: base=8
* hex: base=16

```python
>>> 0b101010
42
>>> 0o52
42
>>> 0x2a
42
>>> bin(42)
'0b101010'
>>> oct(42)
'0o52'
>>> hex(42)
'0x2a'
>>> int('2a', base=16)
42
```

## datetime

![datetime](https://i.loli.net/2018/01/09/5a5476e663c00.png)

```python
>>> import datetime
>>> d = datetime.date.today()
>>> d.year
2018
>>> d.month
1
>>> d.day
9
>>> d.weekday()
1
>>> d.isoweekday()
2
>>> d.isoformat()
'2018-01-09'
>>> d.strftime('%A %d %B %Y')
'Tuesday 09 January 2018'
>>> 'The date is {:%A %d %B %Y}'.format(d)
'The date is Tuesday 09 January 2018'
>>> '{d.year}-{d.month}-{d.day} {d:%A}'.format(d=d)
'2018-1-9 Tuesday'

>>> datetime.datetime.now()
datetime.datetime(2018, 1, 9, 16, 19, 4, 376020)
>>> datetime.datetime.today()
datetime.datetime(2018, 1, 9, 16, 19, 8, 127307)
>>> datetime.datetime.utcnow()
datetime.datetime(2018, 1, 9, 8, 19, 13, 630906)
>>> t = datetime.datetime.now()
>>> t
datetime.datetime(2018, 1, 9, 16, 21, 15, 98362)
>>> t.isoformat()
'2018-01-09T16:21:15.098362'
>>> datetime.datetime.now() + datetime.timedelta(weeks=1) * 3
datetime.datetime(2018, 1, 30, 16, 24, 25, 515850)
```