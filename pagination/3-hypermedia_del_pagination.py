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
        """Initializes the server instance.
        """
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset retrieval.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Retrieves a page of data from a deletion-resilient dataset.
        """
        # Dataset-i götür
        indexed_data = self.indexed_dataset()
        
        # Validasiya
        assert index is not None and 0 <= index < len(self.dataset())

        data = []
        current_index = index
        
        # Nümunə testdəki (3-main.py) məntiqə görə:
        # Biz page_size qədər data tapana qədər indeksləri gəzirik.
        while len(data) < page_size and current_index < len(self.dataset()):
            item = indexed_data.get(current_index)
            if item is not None:
                data.append(item)
            current_index += 1

        # Nəticə lüğəti
        return {
            'index': index,
            'data': data,
            'page_size': page_size,
            'next_index': current_index
        }
