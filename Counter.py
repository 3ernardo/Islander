def readMatrix(inputFile): # Reads the file and creates the matrix map.
    w, h = map(int, inputFile.readline().strip().split())
    sea = [list(map(int, line.strip())) for line in inputFile]
    return sea, h, w

def swipeSea(sea, h, w): # Swipes the matrix map after NEW land chunks.
    counter = 0
    for y in range(h):
        for x in range(w):
            if sea[y][x] == 1:
                counter += 1
                islandFinder(sea, y, x)
    return counter

def islandFinder(sea, h, w): # Recursive function to hide any land attached to a chunk already swiped.
    if sea[h][w] == 1:
        sea[h][w] = 0
        if w < len(sea[0]) - 1: islandFinder(sea, h, w + 1)
        if h < len(sea) - 1: islandFinder(sea, h + 1, w)
        if w > 0: islandFinder(sea, h, w - 1)
        if h > 0: islandFinder(sea, h - 1, w)

with open('testfile.txt') as inputFile:
    sea, h, w = readMatrix(inputFile)
    print(swipeSea(sea, h, w))