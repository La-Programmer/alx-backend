#!/usr/bin/env python3
"""Simple hypermedia implementation"""

import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """Return index range based on page and page_size"""
    end_index: int = page * page_size
    start_index: int = end_index - page_size
    result: tuple = (start_index, end_index)
    return result


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get values from csv file by within
        limits specified by the arguments
        """
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        self.dataset()
        page_range: tuple = index_range(page, page_size)
        result_array: List[List] = []
        if page_range[1] <= len(self.__dataset):
            for i in range(page_range[0], page_range[1]):
                result_array.append(self.__dataset[i])
        return result_array

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Return certain hypermedia values
        """
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        page_data: List[List] = self.get_page(page, page_size)
        dataset_length: int = len(self.__dataset)
        next_page = page + 1 if page + 1 <= dataset_length else None
        prev_page = page - 1 if page - 1 > 0 else None
        result_dict: dict = {
            'page_size': page_size,
            'page': page,
            'data': page_data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': math.ceil(dataset_length / page_size)
        }
        return result_dict
