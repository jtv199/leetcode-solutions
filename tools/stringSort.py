from typing import List
from collections import defaultdict


def listToDict( nums):
    dic = defaultdict(int)
    for i in nums:
        dic[i]+=1
    return dict(dic)

def dictToSelectorString( dic , selector) -> str:
    result = []
    for k,v in dic.items():
        if selector(v) :
            result.append(k)
    return ''.join(str(e) for e in result)
