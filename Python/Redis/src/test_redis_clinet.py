# coding: utf-8


import json

from .redis_client import RedisClient


class TestRedisClient:

    r = RedisClient()

    def test_set_get(self):

        assert self.r.get('no_key')
        # Value
        assert self.r.set('test_h', 'hello')
        v = self.r.get('test_h')
        assert v == 'hello'

        # Dict
        d = dict(a=1)
        assert self.r.set('test_dict', d)
        v = self.r.get('test_dict')
        assert type(v) is str
        assert json.loads(v) == d

        # Dict set None to key
        d = dict(a=None)

    def test_flush(self):

        self.r.set('test_1', 1)
        self.r.set('test_2', 2)
        self.r.set('test_3', 3)
        self.r.set('test_4', 4)

        self.r.set('ntest_1', 5)

        assert self.r.get('test_1') == '1'
        assert self.r.get('ntest_1') == '5'

        self.r.flush('test_')

        assert self.r.get('test_1') is None
        assert self.r.get('ntest_1') == '5'

    def test_flush_all(self):
        self.r.flushall()
        lst = self.r.keys()
        assert len(lst) == 0
