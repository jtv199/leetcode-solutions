from collections import defaultdict
'''
    todo
        process each strings into 2 arrays
        compare the sorted arrays
'''
def twins(a, b):
    # Write your code here
    stringArray = []
    for i in range(len(a)):
        firstString = strTo2Array( a[i])
        secondString = strTo2Array(b[i])

        if compareStrArray(firstString,secondString):
            stringArray.append('Yes')
        else:
            stringArray.append('No')

    return stringArray

def compareStrArray(a,b):
    for i in range(len(a)):
        if not sorted(a[i]) == sorted(b[i]):
            return False
    return True

def strTo2Array(s):
    evenOddArray = [[],[]]
    for i in range(len(s)):
        isOdd = i%2
        evenOddArray[isOdd].append(s[i])

    return evenOddArray

assert strTo2Array('abcd') == [['a','c'],['b','d']]
print(twins(["cdab","dcba","abcd"], ["abcd","abcd","abcdcd"]))
print(twins(["abbc","abbdd"],["abbc","ddbba"]))
