from StringSort import listToDict, dictToSelectorString

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # TODO: hash everything
        # if hash value = 1 put that into a string
        # then
        dic = listToDict(s)
        selectorString = dictToSelectorString(dic,(lambda c : c == 1) )

        for i in range(len(s)):
            if s[i] in selectorString:
                return i

        return -1
