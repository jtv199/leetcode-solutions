"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    list
        1,4,9
        1, 3, 7
        2 , 4, 8
        2pow1,2pow2,2pow3
    insertion places
        powers of 2
        -1
        + how many there are before it
"""


class Solution:

    def connect(self, root: 'Node') -> 'Node':
        for i in root:
