
from typing import List
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # [5,6,1,4,4,2,0,4,3,0,1]
        # where should i set my lowest number?
        # find the min
        # look after the min to find the next min
        # see if there are any numbers after that
        f,s,t = nums[0],None,None
        for i in range(len(nums)):
            n = nums[i]
            if n < f:
                f = n
                #  also gotta change s and t
            elif f< n and ( not t or n<t or n<s):
                s = n
            elif
