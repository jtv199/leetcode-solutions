
from collections import defaultdict
import re

class Solution:
    slist,filterString, dic, largestString = None, None, None, None

    def strToDic(self, s):
        dic = defaultdict(int)
        for i in s:
            dic[i]+=1
        return dict(dic)

    def dictToFilterString(self, dic , num) -> str:
        result = []
        for k,v in dic.items():
            if v < num:
                result.append(k)
        return ''.join(str(e) for e in result)



    def strToList(self, s: str, k: int):
        # convert into dict of occurances of charactors
        dic = self.strToDic(s)
        self.dic = dic

        # covert occurances into strings that are unfit
        filterString = self.dictToFilterString(dic, k)
        self.filterString = filterString

        # when its been split into lists
        if filterString == "":
            # return len(s)
            return [s]
        slist = re.split(f"[{filterString}]",s)
        self.slist = slist
        # return len(slist[0])
        return slist

    def BFSToNum (self, list, k):
        #gives unsorted str list, returns number after recursivly iterating it
        print(list)

        filt = [x for x in list if len(x)>=k]
        filt.sort(key = len, reverse = True)
        if filt == []:
            return 0
        if filt[0] == self.largestString:
            return len(filt[0])



        self.largestString = filt[0]
        filt = filt + self.strToList(filt.pop(0),k)

        return self.BFSToNum(filt,k)

    def longestSubstring (self,l,k):
        a = self.strToList(l,k)
        return self.BFSToNum(a,k)







    # # TODO:
    # count occurance
    # split by things that occure less than k times
    # pop the longest substring
    # run str to list through it again
    #   pop it, append the result and sort
    # how do i know its right
    #   when it gives the same list
    # it either returns to empty list or
if __name__ == '__main__':
    testCases = [
                  ("ababacbc",3),
                  ("abababc",3),
                  ("abababc",2),
                  ("abababc",3),
                  ]
    ansArray = []

    for input, num in testCases:
        sol = Solution()
        ans = sol.longestSubstring(input,num)
        print(f"{input} , {num} is {ans}")
        ansArray.append(sol)

    # sol = Solution()
    # ans = sol.strToList(input,3)
    # print(f"ans is {ans}")
