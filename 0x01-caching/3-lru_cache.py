#!/usr/bin/env python3
"""LRU Cache Implementation"""

from base_caching import BaseCaching
from typing import List
from typing import Union
from typing import Any
from datetime import datetime


class LRUCache(BaseCaching):
    """"LRUCache Class Implementation"""
    def __init__(self) -> None:
        """Class Instance Initialization"""
        self.time_dict: dict = {}
        super().__init__()

    def put(self, key: Union[str, int], item: Any) -> None:
        """Add an element to the cache"""
        if key and item:
            data: dict = self.cache_data
            time_dict: dict = self.time_dict
            if len(data) >= self.MAX_ITEMS and key not in data.keys():
                # print("If statement reached")
                min_timestamp: datetime = datetime.now()
                min_time_key: Union[str, int]
                for time_key, value in time_dict.items():
                    # print("For loop reached")
                    if value < min_timestamp:
                        min_timestamp = value
                        min_time_key = time_key
                # print("The minimum timestamp is: ", min_timestamp)
                # print("The key for the minimum timestamp is: ", min_time_key)
                print("DISCARD: ", min_time_key)
                del data[min_time_key]
                del time_dict[min_time_key]
            data[key] = item
            time_dict[key] = datetime.now()

    def get(self, key: Union[str, int]) -> Any:
        """Get an element from the cache"""
        if key is None or key not in self.cache_data.keys():
            return None
        self.time_dict[key] = datetime.now()
        return self.cache_data[key]
