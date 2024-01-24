#!/usr/bin/env python3
"""
Obtains the HTML content of a particular URL
"""
import redis
import requests
from functools import wraps
from typing import Callable


def cache_page(fn: Callable) -> Callable:
    """
    get_page method decorator
    """
    @wraps(method)
    def wrapper(url: str) -> str:
        """
        wrapper method
        """
        client = redis.Redis()
        client.incr(f'count:{url}')
        cached = client.get(f'result:{url}')
        if cached:
            return cached.decode('utf-8')

        res = method(url)
        client.set(f'{url}', 0)
        client.setex(f'result:{url}', 10, res)
        return res
    return wrapper


@cache_page
def get_page(url: str) -> str:
    """
    get_page method
    """
    response = requests.get(url)
    return response.text
