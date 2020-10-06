'''
    todo
        parse list

        fill corners into grid
        then keep a list of artifacts found, and cap
        then see if all the artifacts have been found


'''
from collections import defaultdict

def start(n , artifacts, searched):
    if not artifacts or not searched:
        return [0,0]
    grid, artifactsDict = fillGrid(n,artifacts)
    result = findArtifacts(grid,searched,artifactsDict)
    return result



def locationsToCoords( locations):
    locationsList = locations.split()
    coords = [toCoords(loc) for loc in locationsList]
    return coords

def noOfWholeArtifacts(total: dict, found:dict):
    wholeArtifacts = 0
    for key,value in total.items():
        if found[key] == value:
            wholeArtifacts +=1
    return wholeArtifacts


def findArtifacts( grid, locations, artifactsDict):
    coords = locationsToCoords(locations)
    foundCount = defaultdict(int)
    totalFound = 0
    for coord in coords:
        tile = grid[coord[0]][coord[1]]
        if tile:
            totalFound+=1
            foundCount[tile] +=1

    wholeArtifacts = noOfWholeArtifacts(artifactsDict, foundCount)

    return [wholeArtifacts,totalFound]


def fillGrid ( n: int , artifactString):
    count = 0
    artifactsDict = defaultdict(int)
    grid = [[None for j in range(n)] for i in range(n)]
    occupiedTiles = parseToSquare(artifactString)

    #fill in count of artifacts and record times its done
    for artifact in occupiedTiles:
        count +=1
        for tile in artifact:
            artifactsDict[count] +=1
            grid[tile[0]][tile[1]] = count

    return grid , artifactsDict


def toSquare(topLeft, bottomRight):  # input (1,1) , (2,2)
    tiles = []
    for i in range(topLeft[0], bottomRight[0] +1 ):
        for j in range(topLeft[1], bottomRight[1] + 1):
            tiles.append((i, j))
    return tiles


def parseToSquare(artifactsInput: str):
    artifactsList = artifactsInput.split(', ')  # ['1A 1B','2C 2C']
    artifactsCorners = [coord.split() for coord in artifactsList]  # [['1A',1B'],['2C','2C']]

    occupiedTiles = []
    for artifacts in artifactsCorners:
        topLeft = toCoords(artifacts[0])
        bottemRight = toCoords(artifacts[1])
        occupiedTiles.append(toSquare(topLeft,bottemRight))

    return occupiedTiles

def toCoords(s):  # input looks like '1A'
    row, column = splitString(s)
    columnNo = toNumber(column)
    return (int(row)-1, toNumber(column)-1)


def toNumber(l):
    l = l.lower()
    result = ord(l) - 96
    return result


def splitString(s):
    s = s.lower()
    head = s.rstrip('abcdefghijklmnopqrstuvwxyz')
    tail = s[len(head):]

    return (head,tail)


# assert ('2', 'b') == splitString('2B')
# assert 2 == toNumber('b')
# assert sorted(toSquare((1, 1), (2, 2))) == sorted([(1, 1), (1, 2), (2, 1),(2, 2)])
# assert sorted(toSquare((1, 1), (2, 1))) == sorted([(1, 1), (2, 1)])
# assert (parseToSquare('1B 2C, 2D 4D')) == [[(1, 2), (1, 3), (2, 2), (2, 3)], [(2, 4), (3, 4), (4, 4)]]
# print(fillGrid(4,'1B 2C, 2D 4D'))
assert (start(3,'1A 1B, 2C 2C', '1B')) == [0, 1]
assert (start(4,'1B 2C, 2D 4D', '2B 2D 3D 4D 4A')) == [1, 4]
# tests
print(start(1,'1A 1A', '1A'))
print(start(1,'1A 1A', ''))
print(start(1,'', '1A'))
print(start(1,'', ''))