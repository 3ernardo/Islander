from random import randint

h = 3 # Map height
w = 4 # Map width
map = []
matrix = [[0 for x in range(w)] for y in range(h)]
lReference = 0

def randomizeMap(h, w):
    for lHCoord in range (h):
        for lWCoord in range (w):
            temp = randint(0, 1)
            matrix[lHCoord][lWCoord] = temp
            map.append([temp,lHCoord,lWCoord,0])

def printMap(map, h, w):
    pr = 0
    for x in range (h):
        for y in range (w):
            print (map[pr][0], end=' ')
            pr += 1
        print()

def coordFinder(hm, wm):
    if hm != 0:
        return (hm)*w+(wm)
    else:
        return wm


def groupLand(lReference):
    for lHCoord in range (h):
        for lWCoord in range (w):
            if matrix[lHCoord][lWCoord] == 1 and map[coordFinder(lHCoord, lWCoord)][3] == 0:
                lReference += 1
                map[coordFinder(lHCoord, lWCoord)][3] = lReference
                findNeighbor(lHCoord, lWCoord)



                print (matrix[lHCoord][lWCoord], map[coordFinder(lHCoord, lWCoord)])
            #    if map[x][1] == map[x][2]:
            #        print ('oi')

def findNeighbor(lHCoord, lWCoord):
    if lWCoord < w - 1:
        if matrix[lHCoord][lWCoord] == matrix[lHCoord][lWCoord + 1] and map[coordFinder(lHCoord, lWCoord+1)][3] == 0:
            print('found')
            map[coordFinder(lHCoord, lWCoord + 1)][3] = lReference
            #findNeighbor(lHCoord, lWCoord+1)
    if lHCoord < h - 1:
        if matrix[lHCoord][lWCoord] == matrix[lHCoord + 1][lWCoord] and map[coordFinder(lHCoord+1, lWCoord)][3] == 0:
            print('found')
            map[coordFinder(lHCoord + 1, lWCoord)][3] = lReference
            #findNeighbor(lHCoord+1, lWCoord)
    if lWCoord > 0:
        if matrix[lHCoord][lWCoord] == matrix[lHCoord][lWCoord - 1] and map[coordFinder(lHCoord, lWCoord-1)][3] == 0:
            print('found')
            map[coordFinder(lHCoord, lWCoord - 1)][3] = lReference
            #findNeighbor(lHCoord, lWCoord-1)
    if lHCoord > 0:
        if matrix[lHCoord][lWCoord] == matrix[lHCoord - 1][lWCoord] and map[coordFinder(lHCoord-1, lWCoord)][3] == 0:
            print('found')
            map[coordFinder(lHCoord - 1, lWCoord)][3] = lReference
            #findNeighbor(lHCoord-1, lWCoord)


def testPrint():
    print(map)
    print('=================')
    print(matrix)

def flood(carth, x, y):
    if carth[x][y] != 0:
        carth[x][y] = 2
        if x != 1: flood(carth, x - 1, y)
        if y != 1: flood(carth, x, y - 1)
        if x != len(carth)-1: flood(carth, x + 1, y)
        if y != len(carth[0])-1: flood(carth, x, y + 1)

randomizeMap(h, w)
printMap(map, h, w)
testPrint()
#groupLand(lReference)
flood(map, 0, 0)
testPrint()