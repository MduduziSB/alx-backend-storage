#!/usr/bin/env python3
"""
Redis module
"""
import uuid
import redis
from typing import Union, Callable, Optional, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Tracks call count of Cache methods
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        wrapper method
        """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    """
    call_history decorator to store the history of inputs and outputs
    """
    key_inputs = "{}:inputs".format(method.__qualname__)
    key_outputs = "{}:outputs".format(method.__qualname__)

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper method
        """
        self._redis.rpush(key_inputs, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(key_outputs, str(output))
        return output
    return wrapper


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

    @count_calls
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

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """
        Converts the data back to the desired format
        """
        value = self._redis.get(key)
        if value is not None and fn is not None:
            return fn(value)
        return value

    def get_str(self, data: bytes) -> str:
        """
        Converts data from bytes to string
        """
        return data.decode('utf-8')

    def get_int(self, data: bytes) -> int:
        """
        Converts data from bytes to integer
        """
        return int(data)
