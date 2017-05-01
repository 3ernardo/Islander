from itertools import groupby
from operator import itemgetter

def matrixReader(inputFile): # Reads the file and creates the matrix map.
    w, h = map(int, inputFile.readline().strip().split())
    matrix = [list(map(int, line.strip())) for line in inputFile]
    return matrix, h, w

def matrixAdvancedSweeper(matrix, h, w): # Swipes the matrix map after NEW land chunks and makes a tuple for each piece of land.
    islandCount = 1
    landCoordinates = []
    for y in range(h):
        for x in range(w):
            if matrix[y][x] == 1:
                islandCount += 1
                islandSorter(matrix, y, x, islandCount)
            if matrix[y][x] > 1:
                landCoordinates.append((matrix[y][x]-1, y, x)) # Creates a list of tuples with the number of the island, height position and width position.
    return sorted(landCoordinates, key=itemgetter(0, 1)) # Sorts the list of tuples (first) by number of the island and (second) by height position.
                
def islandSorter(m, h, w, c): # Recursive function to enumerate and hide any land attached to a chunk already swiped.
    if m[h][w] == 1:
        m[h][w] = c
        if w < len(m[0]) - 1: islandSorter(m, h, w + 1, c)
        if h < len(m) - 1: islandSorter(m, h + 1, w, c)
        if w > 0: islandSorter(m, h, w - 1, c)
        if h > 0: islandSorter(m, h - 1, w, c)

def coordinatePrinter(sortedCoordinates): # Prints the groups of coordinates that forms each island.
    for key, group in groupby(sortedCoordinates, lambda x: x[0]): # Creates groups using the first item of the tuples as key and traverses those returning each key and group.
        print('____________\n  Island %s\nCoordinates:' % (key))
        for tile in group:
            print(' x %s   y %s' % (tile[1], tile[2]))

with open('TestFile.txt') as inputFile: # Opens the defined file to execute the nested code and than closes it.
    coordinatePrinter(matrixAdvancedSweeper(*matrixReader(inputFile)))