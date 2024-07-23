#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List
from typing import Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Get hypermedia for indexed dataset
        """
        assert index > 0 and index < len(self.__dataset)
        indexed_dataset: Dict[int, List] = self.indexed_dataset()
        indexed_dataset_keys: List[int] = list(indexed_dataset.keys())
        next_index: int = indexed_dataset_keys[index + page_size]
        start_index: int = index - index % page_size
        end_index: int = start_index + page_size
        actual_page: List[List] = [
            indexed_dataset[
                indexed_dataset_keys[i]
            ] for i in range(start_index, end_index)
        ]
        result_dict: dict = {
            'index': index,
            'data': actual_page,
            'page_size': page_size,
            'next_index': next_index
        }
        return result_dict
