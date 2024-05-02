#!/usr/bin/env python3
"""
In this tasks, we will implement a get_page function
(prototype: def get_page(url: str) -> str:).
The core of the function uses the requests module to obtain
the HTML content of a particular URL and returns it.
"""
import requests
import redis
import time


def get_page(url: str) -> str:
    """
    It tracks how many times a particular URL was accessed in
    the key "count:{url}" and cache the result with an expiration
    time of 10 seconds.
    """
    redis_instance = redis.Redis()

    cached_result = redis_instance.get(url)
    if cached_result:
        return (cached_result)

    response = requests.get(url)
    html = response.text

    redis_instance.setex(url, 10, html)

    return html


url = "http://slowwly.robertomurray.co.uk/delay/5000/url/http://www.google.com"
print(get_page(url))
