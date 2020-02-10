from typing import List
from collections import defaultdict

class Solution:
    def twoliststo2dlist (self, lista: List[int], listb: List[int]):
        grid = []
        for i in range(len(lista)):
            row = []
            for j in range(len(listb)):
                row.append(lista[i]+listb[j])
                print(f'adding {lista[i]} [ {i} ] with {listb[j]} [ {j} ] = {lista[i]+listb[j]}')
            grid.append(row)

        return grid

    def gridToHashtable (self, grid):
        hashtable = defaultdict(list)
        for i in range(len(grid)):
            for j in range(len(grid)):
                # make a tuple of the coordinates
                hashtable[grid[i][j]].append( (i,j))



        return hashtable

    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:

        return


if __name__ == '__main__':
    A = [ 1, 2]
    B = [-2,-1]
    C = [-1, 2]
    D = [ 0, 2]
    ans = Solution()
    grid = ans.twoliststo2dlist(A,B)
    hashtable = ans.gridToHashtable(grid)

    print('grid of A*B',grid)
    print('hastable built from grid', hashtable)
    print ('matching hashtables to ')
