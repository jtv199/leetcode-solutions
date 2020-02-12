from typing import List
from itertools import chain

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        flatten_list = list(chain.from_iterable(matrix))
        flatten_list.sort()
        return flatten_list[k-1]
