

def getLeft( index):
    return (index*2) +1

def getRight( index):
    return (index*2) +2

def maximum_path(node_values):
    return  recursivlyTraverse(0,node_values)

def recursivlyTraverse(index,list):

    if not list:
        return 0

    if index >= len(list):
        return 0

    currentIndex = index
    leftBranch = recursivlyTraverse(getLeft(index), list)
    thisNode = list[index]
    rightBranch = recursivlyTraverse(getRight(index), list)
    bestBranch = max([leftBranch,rightBranch])
    currentMax = thisNode + bestBranch

    return currentMax

def recursivlyTraverse2(index,list,count,countArray):
    if not list:
        return []

    if index>= len(list):
        return

    count += list[index]

    if getLeft(index) >= len(list) and getRight(index) >= len(list):
        countArray.append(count)
        return

    recursivlyTraverse2(getLeft(index),list,count,countArray)
    recursivlyTraverse2(getRight(index), list, count, countArray)









# testList = [i for i in range(11)]
# assert getRight(0) == 2
# assert getLeft(3) == 7
# assert recursivlyTraverse(0,testList) == 15
# assert recursivlyTraverse(0,[1,3,-1,3,1,5]) == 7
lastlist = []
testCases = [770, 964, -720, 5, -360, -54, -987, -54, 948, 33, 47, -557, -461, -509, 846, 963, 423, 75, 236, -19, -284, -702, -396, -890, 189, 330, -991, 717, -453, -59, 267, 795, 838, -967, 417, -473, 363, 548, 796, -182, 8, 602, 370, 577, -343, -112, -405, -191, 148, -970, -312, -576, -706, 133, -456, -497, 750, 567, 88, -580, -434, 378, 376, -905, 169, 819, 68, -322, 48, -980, -92, -427, -135, -932, -143, 826, 547, -46, 408, 309, 706, -358, 937, -248, -290, 958, -883, -980, 214, 960, -737, 328, -188, -100, 697, -945, -402, 994, -812, -379, -757, 426, 185, 159, 685, -544, -551, 845, 767, 274, -152, 982, -119, -174, 855, -465, -571, -108, 657, -368]
# testCases2 = [15,1,21,2,1,1,-1,0,0,10,12,0,0,0,0]
testCases3 = [1,0,1,2,-1,3,2,1,4,0,3]
testCases4 = [-1, 1, 4, 2, 1, 2, -2, 4, 0, 4, -1, -2, 2, 0, -3, 1, -4, -3, -1, -5]
print(recursivlyTraverse(0,testCases))


print(recursivlyTraverse2(0,testCases,0,lastlist))
print(lastlist)
print(max(lastlist))
# print(len(lastlist))
# print(len(testCases))


