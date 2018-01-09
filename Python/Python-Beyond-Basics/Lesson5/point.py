# coding: utf-8

class Point2D:

    def __init__(self, x, y, *args, **kwargs):
        self.x = x
        self.y = y
        print('args:', args)
        print('kwargs:', kwargs)

    @classmethod
    def create_point_with_dict(cls, dct):
        _keys_noneed = set('args', 'self', 'kwargs')
        _keys_must_have = set(cls.__init__.__code__.co_varnames) - _keys_noneed
        
        _keys_dct = set(dct.keys())
        _keys_zero = _keys_must_have - _keys_dct

        for k in _keys_zero:
            dct[k] = 0

        return cls(**dct)

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def __repr__(self):
        return 'Point(x={}, y={})'.format(self.x, self.y)