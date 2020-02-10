from typing import List
from collections import defaultdict

class Solution:
    def listToDict(self, nums):
        dic = defaultdict(int)
        for i in nums:
            dic[i]+=1
        return dict(dic)

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = self.listToDict(nums)
        sortedDic = sorted(dic, key=dic.get, reverse=True)

        return sortedDic[:k]

if __name__ == '__main__':
    sol = Solution()
    ans = sol.topKFrequent([1,1,1,2,2,3,4,4,4],2)

    print(f'ans is {ans}')
