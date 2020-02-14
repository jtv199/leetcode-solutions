from typing import List
import statistics


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # TODO:
        # find median
        # pivot it
        # then slice and dice

        median =statistics.median(nums)

        count = 0
        b = 0
        e = len(nums)
        bigger = []
        same = []
        smaller = []
        result = [None]*(e)

        for i in nums:
            if i > median:
                bigger.append(i)
            elif i == median:
                same.append(i)
            else:
                smaller.append(i)

        # pivoted = smaller+bigger
        print(f"median is {median}")
        print(smaller,bigger)

        #if length is even
        #bigger in the first odd slots and smaller in the last even slots
        if e % 2 == 0:
            for i in range(e-1,-1,-2):
                if not bigger:
                    break
                s = bigger.pop()
                result[i] = s

            for i in range(0,e,2):
                if not smaller:
                    break
                b = smaller.pop()
                result[i] = b
        else:
            for i in range(e,-1,-2):
                if not bigger:
                    break
                s = bigger.pop()
                result[i] = s

            for i in range(2,e,2):
                if not smaller:
                    break
                b = smaller.pop()
                result[i] = b

        for i in range(len(result)):
            if result[i] == None:
                result[i] = int(median)


        nums = result
        print(nums,result)

#         for i in range(half+1):
#             result.append(pivoted[i])
#             result.append(pivoted[i+half])
#             print(f"i is {i}")

#         print(result)
