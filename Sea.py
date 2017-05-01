from itertools import groupby

def readMatrix(inputFile): # Reads the file and creates the matrix map.
    w, h = map(int, inputFile.readline().strip().split())
    sea = [list(map(int, line.strip())) for line in inputFile]
    return sea, h, w

def invertMatrix(sea):
    for y in range(h):
        for x in range(w):
            sea[y][x] = sea[y][x] * -1
    return sea

def swipeSeaCounter(sea, h, w): # Swipes the matrix map after NEW land chunks.
    counter = 0
    for y in range(h):
        for x in range(w):
            if sea[y][x] == -1:
                counter += 1
                islandFinderCounter(sea, y, x, counter)
    return sea, counter

def coordinates(sea):
    coordMap = []
    for y in range(h):
        for x in range(w):
            coordMap.append((sea[y][x], y, x))
    return coordMap

from operator import itemgetter

def organizeTuples(mapTuples):
    return sorted(mapTuples, key=itemgetter(0, 1))

def printIslands(sortedList):
    for key, group in groupby(sortedList, lambda x: x[0]):
        if key > 0:
            print('Island number %s:' %(key))
            for square in group:
                print('x:%s y:%s' %(square[1], square[2]))
            print()

def islandFinderCounter(sea, h, w, c): # Recursive function to hide any land attached to a chunk already swiped.
    if sea[h][w] == -1:
        sea[h][w] = c
        if w < len(sea[0]) - 1: islandFinderCounter(sea, h, w + 1, c)
        if h < len(sea) - 1: islandFinderCounter(sea, h + 1, w, c)
        if w > 0: islandFinderCounter(sea, h, w - 1, c)
        if h > 0: islandFinderCounter(sea, h - 1, w, c)

def mapPrinter(sea):
    for y in range(h):
        for x in range(w):
            print(sea[y][x], end=' ')
        print()

#mapPrinter(sea)
#print ('==================')
with open('testfile.txt') as inputFile:
    sea, h, w = readMatrix(inputFile)

    s, c = (swipeSeaCounter(invertMatrix(sea), h, w))
#mapPrinter(s)
#print ('==================')
#print(coordinates(s))
#print ('==================')
print(printIslands(organizeTuples(coordinates(s))))