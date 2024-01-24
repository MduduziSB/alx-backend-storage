#!/usr/bin/env python3
"""
Obtains the HTML content of a particular URL
"""
import requests
import redis
from functools import wraps
import time


def cache_page(expiration_time):
    """
    Obtains the HTML content of a particular URL and returns it
    """
    def decorator(func):
        """
        Decorator method
        """
        @wraps(func)
        def wrapper(url, *args, **kwargs):
            """
            Wrapper method
            """
            # Use a unique key for each URL
            count_key = f"count:{url}"
            content_key = f"content:{url}"

            # Check if the content is already cached
            cached_content = cache.get(content_key)
            if cached_content:
                cache.incr(count_key)
                return cached_content.decode('utf-8')

            # If not cached, fetch the content and cache it
            content = func(url, *args, **kwargs)
            cache.setex(content_key, expiration_time, content)
            cache.incr(count_key)

            return content

        return wrapper
    return decorator


@cache_page(expiration_time=10)
def get_page(url: str) -> str:
    """
    Get_page method
    """
    response = requests.get(url)
    return response.text
