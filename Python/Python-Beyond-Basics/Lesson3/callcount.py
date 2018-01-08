# coding: utf-8

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
