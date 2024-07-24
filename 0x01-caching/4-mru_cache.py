#!/usr/bin/env python3
"""MRUCache Implementation"""

from base_caching import BaseCaching
from typing import List
from typing import Any
from typing import Union
from datetime import datetime


class MRUCache(BaseCaching):
    """MRUCache Class Implementation"""
    def __init__(self) -> None:
        """Initialize class instance"""
        self.time_dict = {}
        super().__init__()

    def put(self, key: Union[str, int], item: Any) -> None:
        """Add an item to the cache"""
        if key and item:
            data: dict = self.cache_data
            time_dict: dict = self.time_dict
            if len(data) >= self.MAX_ITEMS and key not in data.keys():
                # print("If statement reached")
                keys_array = list(time_dict.keys())
                max_timestamp: datetime = time_dict[keys_array[0]]
                max_time_key: Union[str, int]
                for time_key, value in time_dict.items():
                    # print("For loop reached")
                    if value > max_timestamp:
                        max_timestamp = value
                        max_time_key = time_key
                # print("The maximum timestamp is: ", max_timestamp)
                # print("The key for the maximum timestamp is: ", max_time_key)
                print("DISCARD: ", max_time_key)
                del data[max_time_key]
                del time_dict[max_time_key]
            data[key] = item
            time_dict[key] = datetime.now()

    def get(self, key: Union[str, int]) -> Any:
        """Get an element from the cache"""
        if key is None or key not in self.cache_data.keys():
            return None
        self.time_dict[key] = datetime.now()
        return self.cache_data[key]
