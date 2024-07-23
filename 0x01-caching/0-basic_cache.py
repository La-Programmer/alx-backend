#!/usr/bin/env python3
"""Basic Cache Implementation"""
from base_caching import BaseCaching
from typing import Any
from typing import List


class BasicCache(BaseCaching):
    """Basic Cache Class"""
    def __init__(self) -> None:
        """Instance initialization"""
        super().__init__()

    def put(self, key, item) -> None:
        """Add an item to the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key) -> Any:
        """Retrieve an item from the cache"""
        available_keys: List[str | int] = self.cache_data.keys()
        if key is None or key not in available_keys:
            return None
        return self.cache_data[key]
