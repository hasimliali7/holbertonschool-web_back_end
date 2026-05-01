#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination module.
This module provides a Server class that handles dataset pagination
even when rows are deleted between requests.
"""
import csv
from typing import List, Dict, Optional


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initializes the Server instance with dataset placeholders.
        """
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Reads and caches the dataset from a CSV file.
        Returns:
            List[List]: The dataset excluding the header.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Creates and caches an indexed version of the dataset.
        Returns:
            Dict[int, List]: Dataset indexed by position.
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
        Retrieves a page of data starting from a specific index.
        This method is resilient to deletions in the underlying dataset.
        Args:
            index (int): The starting index for the page.
            page_size (int): The number of items to include in the page.
        Returns:
            Dict: A dictionary containing pagination metadata and data.
        """
        # Dataset-i götürürük
        data_indexed = self.indexed_dataset()
        
        # Validasiya: index mütləq daxil edilməli və limitdə olmalıdır
        assert isinstance(index, int) and 0 <= index < len(self.dataset())

        data = []
        current_index = index
        
        # page_size qədər mövcud datanı toplayırıq
        while len(data) < page_size and current_index < len(self.dataset()):
            item = data_indexed.get(current_index)
            if item is not None:
                data.append(item)
            current_index += 1

        # Nəticəni qaytarırıq
        return {
            'index': index,
            'next_index': current_index,
            'page_size': page_size,
            'data': data
        }
