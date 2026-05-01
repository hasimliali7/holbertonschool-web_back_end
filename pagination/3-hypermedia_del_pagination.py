#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""
import csv
from typing import List, Dict, Optional


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
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: Optional[int] = None,
                        page_size: int = 10) -> Dict:
        """
        Method that returns a dictionary with pagination data.
        The goals is to be resilient to deletions.
        """
        # Dataset-i götür
        dataset = self.indexed_dataset()

        # Validasiya: index mütləq tam ədəd olmalı və limitdə olmalıdır
        assert isinstance(index, int) and 0 <= index < len(self.dataset())

        data = []
        current_index = index

        # page_size qədər datanı toplayırıq
        while len(data) < page_size and current_index < len(self.dataset()):
            item = dataset.get(current_index)
            if item is not None:
                data.append(item)
            current_index += 1

        # Nəticəni tələb olunan açarlarla (keys) qaytarırıq
        return {
            'index': index,
            'next_index': current_index,
            'page_size': len(data),
            'data': data
        }
