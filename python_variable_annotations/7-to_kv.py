#!/usr/bin/env python3
"""Complex typing - to_kv"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple with a string and the square of a number"""
    return (k, float(v**2))
