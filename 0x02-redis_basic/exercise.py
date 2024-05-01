#!/usr/bin/env python3
"""
This module consists of the following:
 - Cache class
 - store method
"""
import redis
import uuid
from typing import Union


class Cache:
    """
    This class consist of the __init__ method that sores an instance
    of the Redis client as a private variable named _redis and flush
    the instance using flushdb
    """
    def __init__(self):
        """
        Initialization dunder method
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        It generates a random key, stores the input data in Redis
        using the random key.

        Return: the random key generated
        """
        data_key = str(uuid.uuid4())
        result = self._redis.set(data_key, data)
        if result:
            return data_key
        else:
            return None

    def get(self, key: str, fn=None):
        """
        A method that takes a key string arg and an optional
        Callable argument named fn
        """
        result = self._redis.get(key)

        if fn is None:
            return (result)
        else:
            result = fn(result)
        return (result)

    def get_str(self, data):
        """
        This callable is used to convert the data back to string
        """
        decoded_data = data.decode("utf-8")
        return (eval(decoded_data))

    def get_int(self, data):
        """
        This callable is used to convert the data back to integer
        format.
        """
        decoded_data = data.decode("utf-8")
        return (eval(decoded_data))
