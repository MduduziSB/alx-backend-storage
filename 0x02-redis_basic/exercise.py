#!/usr/bin/env python3
"""
Redis module
"""
import uuid
import redis
from typing import Union


class Cache:
    """
    Cache class definition
    """
    def __init__(self):
        """
        Constructor / initialization method
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        The method should generate a random key (e.g. using uuid),
        store the input data in Redis using the random key and return the key.

        Args:
        - data (Union[str, bytes, int, float])

        Return:
        - returns a string (key)
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
