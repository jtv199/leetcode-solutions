from typing import List
from collections import defaultdict


class Solution:

    def twoliststodict (self, lista: List[int], listb: List[int]):
        dict = defaultdict(int)
        for i in lista:
            for j in listb:
                dict[i+j] += 1

        return dict

    def dictsToCount (self, a1,b1):
        count = 0
        a, b = dict(a1), dict(b1)
        print(a,b)
        for key,val in a.items():
            if -key in b:
                count += b[-key] * val

            pass

        return count



    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        dic = self.twoliststodict(A,B)
        dic2 = self.twoliststodict(C,D)
        count = self.dictsToCount(dic,dic2)
        return count


if __name__ == '__main__':
    A = [ 1, 2]
    B = [-2,-1]
    C = [-1, 2]
    D = [ 0, 2]
    ans = Solution()
    dic = ans.twoliststodict(A,B)
    dic2 = ans.twoliststodict(C,D)
    count = ans.dictsToCount(dic,dic2)

    print('hash of a* b',dic)
    print('hash of c* d',dic2)
    print('total count is ', count)
