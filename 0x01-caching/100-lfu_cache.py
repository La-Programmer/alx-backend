#!/usr/bin/env python3
"""LFUCache Implementation"""

from base_caching import BaseCaching
from typing import List
from typing import Union
from typing import Any


class LFUCache(BaseCaching):
    """LFUCache Class Implementation"""
    def __init__(self) -> None:
        """Initialize Class Instance"""
        self.freq_dict = {}
        super().__init__()

    def put(self, key: Union[str, int], item: Any) -> None:
        """Add an item to the cache"""
        if key and item:
            data: dict = self.cache_data
            freq_dict: dict = self.freq_dict
            keys_array: List[Union[str, int]] = list(data.keys())
            if len(data) >= self.MAX_ITEMS and key not in keys_array:
                min_freq: int = freq_dict[keys_array[0]]
                min_freq_key: Union[str, int] = keys_array[0]
                for freq_key, value in freq_dict.items():
                    if value < min_freq:
                        min_freq = value
                        min_freq_key = freq_key
                print("DISCARD: ", min_freq_key)
                del data[min_freq_key]
                del freq_dict[min_freq_key]
            data[key] = item
            if key in keys_array:
                freq_dict[key] += 1
            else:
                freq_dict[key] = 0

    def get(self, key: Union[str, int]) -> Any:
        """Get an item from the cache"""
        if key is None or key not in self.cache_data.keys():
            return None
        self.freq_dict[key] += 1
        # print("The next keys frequency", self.freq_dict[key])
        return self.cache_data[key]
