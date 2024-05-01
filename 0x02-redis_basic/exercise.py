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
        data_key = str(uuid.uuid4())
        result = self._redis.set(data_key, data)
        if result:
            return data_key
        else:
            return None
