"""
Compare time for linear and binary search with random number generator for the length of the list
"""

import random
import time

def linear_search(lst, value):
    """
    (list, object) -> int

    Return the index of the first occurrence of value in lst, or return
    -1 if value is not in lst.

    >>> linear_search([2, 5, 1, -3], 5)
    1
    >>> linear_search([2, 4, 2], 2)
    0
    >>> linear_search([2, 5, 1, -3], 4)
    -1
    >>> linear_search([], 5)
    -1
    """

    i = 0

    while i != len(lst) and lst[i] != value:
        i = i + 1

    if i == len(lst):
        return -1
    else:
        return i

def binary_search(lst, value):
    """
    (list, object) -> int

    Return the index of the first occurrence of value in lst, or return
    -1 if value is not in lst.

    Precondition: lst must be sorted from smallest to largest, otherwise
    the function's behaviour is undefined.

    >>> binary_search([2, 5, 7, 9, 11], 7)
    2
    >>> binary_search([2, 5, 7, 9, 11], 5)
    1
    >>> binary_search([2, 4, 6, 8, 10], 4)
    1
    >>> binary_search([2, 5, 7, 9, 11], 1)
    -1
    >>> binary_search([], 1)
    -1
    """

    # Mark the start and end of the still-unknown section of the list.
    low = 0
    high = len(lst) - 1

    # Keep going until the unknown section is empty.
    while low <= high:
        # Check the middle element.
        mid = (low + high) // 2
        if lst[mid] < value:
            low = mid + 1
        elif lst[mid] > value:
            high = mid - 1
        else:
            return mid

    return -1

def random_list(n):
    """
    (int) -> list

    Return a list of n random integers between 0 and n - 1.

    >>> random_list(5)
    [4, 1, 3, 2, 0]
    """

    lst = []
    for i in range(n):
        lst.append(random.randrange(n))
    return lst

def time_linear_search(n):
    """
    (int) -> float

    Return the number of seconds taken to run linear_search on a list of n
    random integers.
    """

    lst = random_list(n)
    start = time.time()
    linear_search(lst, -1)
    end = time.time()
    return end - start

def time_binary_search(n):
    