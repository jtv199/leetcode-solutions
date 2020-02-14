
from typing import List

class Solution:

    def listToDict( nums):
        dic = defaultdict(int)
        for i in nums:
            dic[i]+=1
        return dict(dic)


    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        dic = self.listToDict(nums1)
        for i in nums2:
            if dic[i] => 0 :
                result.append(i)
                dic[i] -= 1

        return result
