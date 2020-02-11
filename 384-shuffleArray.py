import random
from typing import List
import copy


class Solution:
    original = None

    def __init__(self, nums: List[int]):
        self.original = nums



    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.original


    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        nl = copy.deepcopy(self.original)
        random.shuffle(nl)



        return nl



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
if __name__ == '__main__':
    sol = Solution([1,2,3,4,5])
    shuf1 = sol.shuffle()
    reset = sol.reset()
    shuf2 = sol.shuffle()
    print(shuf1,reset,shuf2)
