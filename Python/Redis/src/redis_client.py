# coding: utf-8

import redis
import json


# 可以直接从 project 的 config 引入
REDIS_CONFIG = {
    'host': '127.0.0.1',
    'port': 6379,
    'db': 0
}


class RedisClient:
    """
    Redis_Client:

    封装 Redis Client

    >>> rc = Redis_Client()
    >>> rc.set('test', 'hello')
    >>> rc.get('test')

    直接调用 redis_client
    >>> rc.redis_client.setex('test_expire_in_5_sec', 'hello', 5)
    """
    def __init__(self):

        pool = redis.ConnectionPool(**REDIS_CONFIG)
        self.redis_client = redis.Redis(connection_pool=pool)
        # pipeline :  buffering multiple commands
        #             to the server in a single request
        # 详情见 https://pypi.python.org/pypi/redis
        self.pipe = self.redis_client.pipeline()

    def set(self, key, value):
        """
        Set Key

        if value is dict, json.dumps(dict)

        :param key type:   str
        :param value type: object
        :return type:      boolean
        """
        if type(value) is dict:
            value = json.dumps(value)
        return self.redis_client.set(key, value)

    def get(self, key):
        """
        Get Key

        :param key type:   str
        :return type:      str
        """
        v = self.redis_client.get(key)
        if not v:
            return None
        return v.decode()

    def keys(self, prefix=''):
        pattern = prefix + '*'
        return self.redis_client.keys(pattern)

    def flush(self, prefix):
        """
        清空特定 pattern 的keys
        """
        keys = self.keys(prefix)
        self.redis_client.delete(*keys)

    def flushall(self):
        """
        清空所有 Redis 键值
        """
        return self.redis_client.flushall()
