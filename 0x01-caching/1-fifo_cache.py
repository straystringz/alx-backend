#!/usr/bin/python3
"""
Module 1-fifo_cache.py_
"""
from base_caching import BaseCaching
from collections import deque


class FIFOCache(BaseCaching):
    """
    Overrides put() nad_ self()
    from parent
    """

    def __init__(self):
        """initialize_"""
        super().__init__()
        self.queue = deque([])

    def put(self, key, item):
        """Add an_ item in the cache
        """
        if key and item:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS\
                    and key not in self.queue:
                del_key = self.queue.popleft()
                del self.cache_data[del_key]
                print("DISCARD: {}".format(del_key))
            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """Get an_ item by key
        """
        value = self.cache_data.get(key)
        return value
