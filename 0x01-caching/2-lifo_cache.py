#!/usr/bin/env python3
"""LIFO Cache Implementation"""

from base_caching import BaseCaching
from typing import List
from typing import Union
from typing import Any


class LIFOCache(BaseCaching):
    """LIFO Cache Class"""
    def __init__(self) -> None:
        """Initialize class instance"""
        super().__init__()

    def put(self, key: Union[str, int], item: Any) -> None:
        """Add item to the cache"""
        data: dict = self.cache_data
        if len(data) >= self.MAX_ITEMS and key not in data.keys():
            last_key: str | int = list(data.keys())[-1]
            del data[last_key]
            print(f'DISCARD: {last_key}')
        data[key] = item

    def get(self, key: Union[str, int]) -> Union[str, int]:
        """Get an item from the cache"""
        available_keys: List[str | int] = self.cache_data.keys()
        if key is None or key not in available_keys:
            return None
        return self.cache_data[key]
