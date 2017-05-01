def matrixReader(inputFile): # Reads the file and creates the matrix map.
    w, h = map(int, inputFile.readline().strip().split())
    matrix = [list(map(int, line.strip())) for line in inputFile]
    return matrix, h, w

def matrixSweeper(matrix, h, w): # Swipes the matrix map after NEW land chunks.
    counter = 0
    for y in range(h):
        for x in range(w):
            if matrix[y][x] == 1:
                counter += 1
                islandFinder(matrix, y, x)
    return counter

def islandFinder(matrix, h, w): # Recursive function to hide any land attached to a chunk already swiped.
    if matrix[h][w] == 1:
        matrix[h][w] = 0
        if w < len(matrix[0]) - 1: islandFinder(matrix, h, w + 1)
        if h < len(matrix) - 1: islandFinder(matrix, h + 1, w)
        if w > 0: islandFinder(matrix, h, w - 1)
        if h > 0: islandFinder(matrix, h - 1, w)

with open('TestFile.txt') as inputFile:
    print(matrixSweeper(*matrixReader(inputFile)))