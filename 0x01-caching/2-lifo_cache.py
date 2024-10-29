#!/usr/bin/env python3
"""
LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache class """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """ Add an item to the cache """
        if key is not None and item is not None:
            if (len(self.cache_data) >= BaseCaching.MAX_ITEMS
                    and key not in self.cache_data):
                del self.cache_data[self.last_key]
                print("DISCARD:", self.last_key)
            self.cache_data[key] = item
            self.last_key = key

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)