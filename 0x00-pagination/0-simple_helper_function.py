#!/usr/bin/env python3
"""Simple helper function"""


def index_range(page: int, page_size: int) -> tuple:
    """Return index range based on page and page_size"""
    end_index: int = page * page_size
    start_index: int = end_index - page_size
    result: tuple = (start_index, end_index)
    return result
