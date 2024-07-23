#!/usr/bin/env python3
"""FIFO Cache Implementation"""

from base_caching import BaseCaching
from typing import List
from typing import Union
from typing import Any


class FIFOCache(BaseCaching):
    """FIFOCache Class Implementation"""
    def __init__(self) -> None:
        """Initialize class instance"""
        super().__init__()

    def put(self, key: Union[str, int], item: Any) -> None:
        """Add an item to the cache"""
        data: dict = self.cache_data
        if len(data) >= self.MAX_ITEMS and key not in data.keys():
            first_key: str | int = list(self.cache_data.keys())[0]
            del self.cache_data[first_key]
            print(f'DISCARD: {first_key}')
        self.cache_data[key] = item

    def get(self, key: Union[str, int]) -> Union[str, int]:
        """Get an item from the cache"""
        available_keys: List[str | int] = self.cache_data.keys()
        if key is None or key not in available_keys:
            return None
        return self.cache_data[key]
