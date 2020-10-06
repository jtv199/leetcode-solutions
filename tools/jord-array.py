def solve(arr):
    index = 0

    total = [arr[index]]
    index += 1

    level = 0
    while index + level < len(arr):
        current = []

        # Furtherest left path
        current.append(total[0] + arr[index])
        index += 1

        # Find the maxs
        for i in range(level):
            current.append(max(arr[index], arr[index+1]) + total[i+1])
            index += 1

        # Furtherest right path
        current.append(arr[index] + total[-1])
        index += 1

        total = current
        level += 1

    return(max(total))



testCases = [770, 964, -720, 5, -360, -54, -987, -54, 948, 33, 47, -557, -461, -509, 846, 963, 423, 75, 236, -19, -284, -702, -396, -890, 189, 330, -991, 717, -453, -59, 267, 795, 838, -967, 417, -473, 363, 548, 796, -182, 8, 602, 370, 577, -343, -112, -405, -191, 148, -970, -312, -576, -706, 133, -456, -497, 750, 567, 88, -580, -434, 378, 376, -905, 169, 819, 68, -322, 48, -980, -92, -427, -135, -932, -143, 826, 547, -46, 408, 309, 706, -358, 937, -248, -290, 958, -883, -980, 214, 960, -737, 328, -188, -100, 697, -945, -402, 994, -812, -379, -757, 426, 185, 159, 685, -544, -551, 845, 767, 274, -152, 982, -119, -174, 855, -465, -571, -108, 657, -368]
testcase2 = [15,1,21,2,1,1,-1,0,0,10,12,0,0,0,0]
testCases3 = [1,0,1,2,-1,3,2,1,3,0,3]
testCases4 = [1,2,1,2,1,1,-1,0,0,10,12,0,0,0,0]

# print(len(testCases4))
print(solve(testCases))