# name: 전현준
# student id: 2021105636
from typing import List

def binsearch(n: int, S: List[int], x: int) -> int:
    low, high = 0, n - 1
    location = -1

    while low <= high and location == -1:
        mid = (low + high) // 2
        if x == S[mid]:
            location = mid
        elif x < S[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return location