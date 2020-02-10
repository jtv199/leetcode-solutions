
from collections import defaultdict
import re

class Solution:
    slist,filterString, dic = None, None, None

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



    def longestSubstring(self, s: str, k: int) -> int:
        # convert into dict of occurances of charactors
        dic = self.strToDic(s)
        self.dic = dic

        # covert occurances into strings that are unfit
        filterString = self.dictToFilterString(dic, k)
        self.filterString = filterString

        # when its been split into lists
        if filterString == "":
            return len(s)
        slist = re.split(f"[{filterString}]",s)
        self.slist = slist
        return len(slist[0])

    # # TODO:
    # count occurance
    # split by things that occure less than k times
    # take the longest substring
if __name__ == '__main__':
    sol = Solution()
    input = "ababacbc"
    ans = sol.longestSubstring(input,3)
    print(f"ans is {ans}")
